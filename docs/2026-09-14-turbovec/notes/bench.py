"""turbovec vs FAISS on two real embedding sets, on a CPU-only box.

Usage: THREADS=1 python bench.py   (RAYON_NUM_THREADS is read by turbovec at import)
Datasets (ann-benchmarks HDF5, angular): glove-100 and dbpedia-openai-100k (ada-002, d=1536).
Everything is normalised, so inner product == cosine. Ground truth is recomputed exactly
with a float32 brute-force pass on the subset actually indexed.
"""
import os, sys, time, json
THREADS = int(os.environ.get("THREADS", "1"))
os.environ["RAYON_NUM_THREADS"] = str(THREADS)
import numpy as np, h5py, faiss
from turbovec import TurboQuantIndex, IdMapIndex
faiss.omp_set_num_threads(THREADS)

N_BASE, N_Q, K, SEED = 100_000, 1_000, 64, 42
KS = [1, 2, 4, 8, 16, 32, 64]
REPS = 5
out = {"threads": THREADS, "cpus": os.cpu_count(), "datasets": {}}

def med_ms(fn, n):
    ts = []
    for _ in range(REPS):
        t0 = time.perf_counter(); fn(); ts.append((time.perf_counter() - t0) / n * 1000)
    return round(sorted(ts)[REPS // 2], 4)

def load(path, pad_to=None):
    with h5py.File(path) as h:
        base = np.asarray(h["train"], dtype=np.float32); q = np.asarray(h["test"], dtype=np.float32)
    rng = np.random.RandomState(SEED)
    base = base[rng.permutation(len(base))[:N_BASE]]; q = q[:N_Q]
    base /= np.linalg.norm(base, axis=1, keepdims=True); q /= np.linalg.norm(q, axis=1, keepdims=True)
    return np.ascontiguousarray(base), np.ascontiguousarray(q)

def recalls(true_ids, pred):  # true_ids: (nq, 10) exact top-10; pred: (nq, >=64)
    r = {f"r1@{k}": round(float(np.mean([true_ids[i, 0] in pred[i, :k] for i in range(len(pred))])), 4) for k in KS}
    r["r10@10"] = round(float(np.mean([len(set(true_ids[i, :10]) & set(pred[i, :10])) / 10 for i in range(len(pred))])), 4)
    return r

def faiss_bytes(ix):
    return int(faiss.serialize_index(ix).nbytes)

def rerank(base, q, pred, top):  # exact rescoring of the top `top` candidates
    outp = np.empty((len(q), top), dtype=np.int64)
    for i in range(len(q)):
        c = pred[i, :top]; s = base[c] @ q[i]; outp[i] = c[np.argsort(-s)]
    return outp

def run(name, path, pad):
    base, q = load(path)
    d = base.shape[1]; res = {"n": len(base), "nq": len(q), "dim": d, "methods": {}}
    print(f"\n=== {name}: n={len(base)} d={d} nq={len(q)} threads={THREADS}", flush=True)
    # exact ground truth, float32 flat
    flat = faiss.IndexFlatIP(d); flat.add(base)
    t0 = time.perf_counter(); _, gt = flat.search(q, 10); gt_ms = (time.perf_counter() - t0) / len(q) * 1000
    res["methods"]["flat_f32"] = {"bytes": faiss_bytes(flat), "build_s": 0.0, "search_ms": med_ms(lambda: flat.search(q, K), len(q)), **recalls(gt, flat.search(q, K)[1])}
    print(" flat", res["methods"]["flat_f32"], flush=True)

    # turbovec: zero-pad to a multiple of 8 if needed (inner products unchanged)
    dt = d if d % 8 == 0 else d + (8 - d % 8)
    if dt != d:
        bt = np.zeros((len(base), dt), np.float32); bt[:, :d] = base; qt = np.zeros((len(q), dt), np.float32); qt[:, :d] = q
    else:
        bt, qt = base, q
    res["turbovec_dim"] = dt
    for bits in (2, 3, 4):
        for calib in (False, True):
            if bits == 3 and calib: continue
            tag = f"tq{'+' if calib else ''}_{bits}bit"
            ix = TurboQuantIndex(dim=dt, bit_width=bits)
            t0 = time.perf_counter()
            if calib:
                rng = np.random.RandomState(SEED); ix.calibrate(bt[rng.choice(len(bt), 1024, replace=False)])
            ix.add(bt); ix.prepare(); build = time.perf_counter() - t0
            ix.search(qt[:1], k=K)
            _, pred = ix.search(qt, k=K); pred = np.asarray(pred)
            m = {"bytes": len(ix.to_bytes()), "build_s": round(build, 3), "search_ms": med_ms(lambda: ix.search(qt, k=K), len(q)), **recalls(gt, pred)}
            rr = rerank(base, q, pred, 64); m["rerank64_r1@1"] = recalls(gt, rr)["r1@1"]; m["rerank64_r10@10"] = recalls(gt, rr)["r10@10"]
            res["methods"][tag] = m; print(" ", tag, m, flush=True)

    # FAISS baselines at matched bit rates
    cfgs = []
    if d % 2 == 0: cfgs.append(("faiss_pq8_m=d/2 (4-bit rate)", lambda: faiss.IndexPQ(d, d // 2, 8, faiss.METRIC_INNER_PRODUCT)))
    if d % 4 == 0: cfgs.append(("faiss_pq8_m=d/4 (2-bit rate)", lambda: faiss.IndexPQ(d, d // 4, 8, faiss.METRIC_INNER_PRODUCT)))
    cfgs.append(("faiss_pqfastscan_m=d (4-bit rate)", lambda: faiss.IndexPQFastScan(d, d, 4, faiss.METRIC_INNER_PRODUCT)))
    if d % 2 == 0: cfgs.append(("faiss_pqfastscan_m=d/2 (2-bit rate)", lambda: faiss.IndexPQFastScan(d, d // 2, 4, faiss.METRIC_INNER_PRODUCT)))
    cfgs.append(("faiss_sq8", lambda: faiss.IndexScalarQuantizer(d, faiss.ScalarQuantizer.QT_8bit, faiss.METRIC_INNER_PRODUCT)))
    cfgs.append(("faiss_sq4", lambda: faiss.IndexScalarQuantizer(d, faiss.ScalarQuantizer.QT_4bit, faiss.METRIC_INNER_PRODUCT)))
    cfgs.append(("faiss_hnsw32_f32", lambda: faiss.IndexHNSWFlat(d, 32, faiss.METRIC_INNER_PRODUCT)))
    for tag, mk in cfgs:
        ix = mk(); t0 = time.perf_counter(); ix.train(base); ix.add(base); build = time.perf_counter() - t0
        if "hnsw" in tag: ix.hnsw.efSearch = 128
        ix.search(q[:1], K); _, pred = ix.search(q, K)
        m = {"bytes": faiss_bytes(ix), "build_s": round(build, 3), "search_ms": med_ms(lambda: ix.search(q, K), len(q)), **recalls(gt, pred)}
        if "pq" in tag: rr = rerank(base, q, pred, 64); m["rerank64_r1@1"] = recalls(gt, rr)["r1@1"]; m["rerank64_r10@10"] = recalls(gt, rr)["r10@10"]
        res["methods"][tag] = m; print(" ", tag, m, flush=True)

    # filtered search: 1% allowlist, IdMapIndex kernel filter vs over-fetch-and-post-filter
    rng = np.random.RandomState(SEED); allowed = np.sort(rng.choice(len(base), len(base) // 100, replace=False)).astype(np.uint64)
    sub = faiss.IndexFlatIP(d); sub.add(base[allowed.astype(np.int64)]); _, gsub = sub.search(q, 10); gt_f = allowed[gsub]
    im = IdMapIndex(dim=dt, bit_width=4); im.add_with_ids(bt, np.arange(len(bt), dtype=np.uint64)); im.prepare()
    _, pf = im.search(qt, k=10, allowlist=allowed); pf = np.asarray(pf)
    _, pall = im.search(qt, k=1000); pall = np.asarray(pall); aset = set(allowed.tolist())
    post = [[x for x in row if x in aset][:10] for row in pall]
    r_kernel = float(np.mean([len(set(gt_f[i]) & set(pf[i])) / 10 for i in range(len(q))]))
    r_post = float(np.mean([len(set(gt_f[i]) & set(post[i])) / 10 for i in range(len(q))]))
    res["filter_1pct"] = {"allowlist_r10@10": round(r_kernel, 4), "allowlist_ms": med_ms(lambda: im.search(qt, k=10, allowlist=allowed), len(q)),
                          "postfilter_top1000_r10@10": round(r_post, 4), "postfilter_ms": med_ms(lambda: im.search(qt, k=1000), len(q))}
    print("  filter", res["filter_1pct"], flush=True)
    out["datasets"][name] = res

run("glove-100", "data/glove-100-angular.hdf5", True)
run("dbpedia-openai-1536", "data/dbpedia-100k-openai-ada002-angular.hdf5", False)
json.dump(out, open(f"results_t{THREADS}.json", "w"), indent=1)
print(json.dumps(out, indent=1))
