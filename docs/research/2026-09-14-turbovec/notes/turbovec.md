# turbovec and TurboQuant — checked at the source on 2026-09-14

## Access and confidence

- **Read in full, first-hand:** the `RyanCodrai/turbovec` repository on its
  default branch — `README.md`, `LICENSE`, `Cargo.toml`, `CHANGELOG.md`
  (226 KB), `docs/api.md`, `benchmarks/download_data.py`, the benchmark
  scripts `benchmarks/suite/speed_d1536_{2,4}bit_x86_st.py`,
  `recall_d1536_4bit.py` and `compression.py`, and the result files
  `benchmarks/results/{compression,recall_d1536_2bit,recall_d1536_4bit,recall_glove_2bit}.json`
  (raw files; `github.com` HTML gives this session a 403 by `curl` but is
  readable through the fetch tool, and the repository metadata came from
  GitHub's search API); the author's GitHub profile; the `README.md`,
  `ann/RESULTS.md`, `accuracy/RESULTS.md` and `efficiency/RESULTS.md` of
  `VectorDB-NTU/rabitq-turboquant-comparison`; the FAISS wiki page on
  FastScan; PyPI's JSON API for `turbovec`, `turboquant-py` and
  `faiss-cpu`.
- **Run here:** `turbovec` 1.0.0 and `faiss-cpu` 1.15.0 on a four-core
  x86 container with AVX-512 VNNI, against two real embedding sets from a
  public mirror — [`turbovec-run.md`](turbovec-run.md).
- **Not obtained — blocked by this session's egress policy (403 at the
  proxy), not by the sites:** `arxiv.org` (the TurboQuant paper, the NTU
  comparison paper, the TurboVec case-study paper), `research.google`,
  `huggingface.co`, `news.ycombinator.com`, `medium.com`, `dev.to`,
  `elastic.co`, `qdrant.tech`, `milvus.io`, `crates.io`, `docs.rs`,
  `iclr.cc`, `wikipedia.org`, `nlp.stanford.edu`, `ann-benchmarks.com`.
  What is taken from them — the paper's abstract and authors, the Google
  blog's date and KV-cache claims, the market episode, the Elastic and
  Qdrant positions, the Milvus interview, the case-study paper's numbers —
  comes from search-result snippets corroborated across several results.
  Marked *(search)* below; lower confidence than the rest.

## What turbovec is, in its own words

`RyanCodrai/turbovec` (read): "turbovec is a Rust vector index with Python
bindings, built on Google Research's TurboQuant algorithm — a data-oblivious
quantizer with near-optimal distortion and no separate training phase."
The headline: "A 10 million document corpus takes 31 GB of RAM as float32.
turbovec fits it in 4 GB - and searches it faster than FAISS."

Five bullets carry the pitch: **online ingest** ("Add vectors, they're
indexed — no train step, no parameter tuning, no rebuilds as the corpus
grows"); **fast SIMD search** ("Hand-written kernels — NEON SDOT/SMMLA on
ARM, AVX-512 VNNI and `vpermb` on x86, with AVX2 and scalar fallbacks —
beat FAISS IndexPQFastScan in every measured config, averaging 3.4× at
4-bit and 23% at 2-bit"); **incremental saves** (`sync(path)` "persists
just what changed since the last sync — one fsync per call, crash-safe at
any byte"); **filter at search time** (an id allowlist or slot bitmask
"honoured directly" by the kernel, "no over-fetching, no recall hit on
selective filters"); **pure local** ("No managed service, no data leaving
your machine or VPC").

Two index types: `TurboQuantIndex` (positional slots, O(1) `swap_remove`)
and `IdMapIndex` (stable `uint64` external ids, `remove(id)` in O(1),
`allowlist=` on search). `bit_width ∈ {2, 3, 4}`; `dim` "must be a positive
multiple of 8 and ≤ 16384", or inferred from the first add. Inputs must be
contiguous float32 — "other dtypes are rejected rather than silently
converted." Files: `.tv` / `.tvim`, format v7 as of 1.0.0, one fsync and
an atomic rename; `to_bytes()` / `from_bytes()` for caches and database
columns; pickle and copy supported.

**Framework integrations**, each a drop-in for the framework's own
in-memory store: LangChain (`InMemoryVectorStore`), LlamaIndex
(`SimpleVectorStore`), Haystack (`InMemoryDocumentStore`), Agno
(`LanceDb`) — via `pip install turbovec[langchain]` and so on.

**Rust:** `cargo add turbovec`; the same two types; `from_parts` for
embedders that keep the payload in their own storage. All x86_64 builds
target `x86-64-v2`; AVX2 and AVX-512 kernels are selected at runtime.

### The project's facts

| | |
|---|---|
| Repository | `RyanCodrai/turbovec`, created 2026-03-26 (GitHub API), last push 2026-09-13 |
| Stars / forks | 17,083 / 1,466 on 2026-09-14 (GitHub API) |
| Language | Rust; Python bindings via maturin |
| Licence | MIT, "Copyright (c) 2026 Ryan Codrai" |
| Author | GitHub profile bio: "Member of Technical Staff at Anthropic"; pinned repos turbovec, gemma-emotional-probes, sourced |
| PyPI | `turbovec` 1.0.0, uploaded 2026-08-18; `requires_python >= 3.9`; `numpy >= 1.20`; extras `agno`, `haystack`, `langchain`, `llama-index` |
| Wheels | `cp39-abi3` for macOS arm64, manylinux x86_64 and aarch64, Windows amd64 (from 0.4.3) |
| Releases | 0.1.0 on 2026-04-13; 0.4.x–0.8.0 through May–June; 1.0.0 on 2026-08-18 — nineteen PyPI releases in five months |
| Rust crate | also `turbovec`; drifted to 0.9.0 before both surfaces went to 1.0.0 together |
| Summary field | "Fast vector quantization with 2-4 bit compression and SIMD search" |

What 1.0.0 committed to, per the changelog: "the on-disk format: v7 is
what turbovec reads and writes, and a file written by this release will be
readable by later ones." Pre-v7 files are refused and a `turbovec::convert`
tool moves v5/v6 files forward; files before v5 "predate the rotation
change that altered every encoded byte and can only be rebuilt from the
source vectors." The 1.0 notes also list long-lived bugs fixed: a delete
that "could stall for seconds behind concurrent searches", a load that
"allocated from a file's apparent length rather than its declared
contents", an aarch64 search that "got slower the moment an index crossed
32768 vectors".

## How it works, step by step (README, "How it works")

1. **Normalize.** Store each vector's length as one float; keep the unit
   direction.
2. **Random rotation.** "Multiply all vectors by the same random orthogonal
   matrix. After rotation, each coordinate independently follows a Beta
   distribution that converges to Gaussian N(0, 1/d) in high dimensions.
   This holds for any input data."
3. **Per-coordinate calibration (TQ+), optional.** "TQ+ fits two scalars
   per coordinate — a shift and a scale — mapping each coordinate's
   empirical quantiles onto the codebook's outermost centroids." One
   `index.calibrate(sample)` call with "~1024 rows" of a random,
   representative sample, before adding. "An index you never calibrate is
   plain TurboQuant." The API doc: "worth roughly +2.5 points of R@10 on
   average, and up to ~8.7 on the most anisotropic data measured"; and the
   warning that "a sorted or clustered prefix of the same size fits
   quantiles that are shifted and far too narrow, and actively destroys
   recall."
4. **Lloyd-Max scalar quantization.** "Since the distribution is known, we
   can precompute the optimal way to bucket each coordinate. For 2-bit,
   that's 4 buckets; for 4-bit, 16 buckets… These are computed once from
   the math, not from the data."
5. **Bit-pack.** "A 1536-dim vector goes from 6,144 bytes (FP32) to 384
   bytes (2-bit). That's 16x compression." At 3 bits "a byte holds only two
   codes rather than 8/3", so the payload is about a third larger than the
   bit count implies.
6. **Length-renormalized scoring.** "Scalar quantization systematically
   underestimates inner products… We compute one scalar per vector at
   encode time… and store `||v|| / ⟨u, x̂⟩` alongside each compressed
   vector," turning "the inner-product estimator from downward-biased into
   unbiased at zero search-time cost." The README's references credit this
   step to **RaBitQ** (SIGMOD 2024): "the source of the per-vector
   length-renormalization correction adapted in step 5."

**Search:** "we rotate the query once into the same domain and score
directly against the codebook values," with nibble-split lookup tables on
AVX-512BW / AVX2 / NEON and a scalar fallback. The README states the
Lloyd-Max codebook "achieves distortion within a factor of 2.7x of the
information-theoretic lower bound."

The scan is exhaustive: every stored vector is scored on every query.
There is no graph, no inverted file, no clustering — which is why there is
no training and why cost is linear in the corpus. A search-result summary
put it as "TurboVec implements flat quantized search (exhaustive search
over compressed vectors), not HNSW" *(search)*; the README never claims
otherwise, and the FAISS comparators it picks (`IndexPQ`, `IndexPQFastScan`)
are flat too.

## The project's own numbers (README and result JSONs, read)

**Compression** (`compression.json`, 100K vectors): GloVe d=200 — 76.3 MB
fp32 → 5.1 MB at 2-bit (14.8×), 9.9 MB at 4-bit (7.7×). OpenAI d=1536 —
585.9 MB → 37.0 MB (15.8×) / 73.6 MB (8.0×). OpenAI d=3072 — 1171.9 MB →
73.6 MB (15.9×) / 146.9 MB (8.0×).

**Recall** against FAISS `IndexPQ` with 256-entry codebooks (nbits=8) and
sub-quantizer counts matched to the bit rate (m = d/2 at 4-bit, d/4 at
2-bit), 100K vectors, recall@1@k:

| Cell | TQ | TQ+ | FAISS PQ | at k |
|---|---|---|---|---|
| OpenAI 1536, 2-bit | 0.888 | 0.901 | 0.872 | 1 |
| OpenAI 1536, 4-bit | 0.967 | 0.959 | 0.966 | 1 |
| GloVe 200, 2-bit | 0.550 | 0.572 | 0.564 | 1 |
| GloVe 200, 2-bit | 0.909 | 0.923 | 0.925 | 8 |

All three reach ≥ 0.997 by k=4 on the OpenAI sets. The README's gloss: on
OpenAI d=1536 and d=3072 "TQ+ beats FAISS at R@1 on three of four cells
(by 0.9–2.9 points; d=1536 4-bit trails by 0.7)"; GloVe "is the harder
regime — at low dim the asymptotic Beta assumption is looser", where FAISS
keeps "a slim edge at 2-bit from k≈8".

**Speed** against `IndexPQFastScan` (nbits=4, m matched — m=d at 4-bit),
100K vectors, 1K queries, k=64, median of five runs, on two 8-vCPU cloud
machines: ARM (Google Axion) "3.5× at 4-bit (3.4–3.7×) and 26% at 2-bit
(22–29%)"; x86 (Sapphire Rapids) "3.4× at 4-bit (3.2–3.5×) and 20% at
2-bit (5–32%)". Insertion: a single `add()` "lands in 6.3–19.7 µs" versus
"7.6–13.9× faster than a FAISS single add"; removal by id "0.44–1.22 µs"
versus FAISS `remove_ids` on an `IndexIDMap` at "0.19–1.02 s per single
remove at 100K" because FAISS repacks codes.

**A note the README makes itself:** the FAISS `IndexPQ` baseline "is a
stronger baseline than the custom u8-LUT PQ in the TurboQuant paper", and
the project "reproduce[s] the paper's TurboQuant numbers on OpenAI d=1536 /
d=3072".

## TurboQuant, the algorithm *(search — arXiv and Google blog blocked)*

*TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate*,
arXiv 2504.19874 (April 2025), Amir Zandieh, Majid Daliri, Majid Hadian,
Vahab Mirrokni (Google Research, with KAIST and NYU); ICLR 2026. Abstract,
via snippets: data-oblivious algorithms that "achieve near-optimal
distortion rates (within a small constant factor) across all bit-widths
and dimensions", by "randomly rotating input vectors, inducing a
concentrated Beta distribution on coordinates, and leveraging the
near-independence property of distinct coordinates in high dimensions to
simply apply optimal scalar quantizers per each coordinate"; and, because
"MSE-optimal quantizers introduce bias in inner product estimation", a
two-stage variant: "an MSE quantizer followed by a 1-bit Quantized JL (QJL)
transform on the residual, resulting in an unbiased inner product
quantizer." Two named sub-algorithms: **PolarQuant** and **QJL**. Results
claimed: KV-cache "quality neutrality with 3.5 bits per channel and
marginal quality degradation with 2.5 bits"; in nearest-neighbour search
"outperforms existing product quantization techniques in recall while
reducing indexing time to virtually zero."

Google Research blog, 24 March 2026 (Zandieh and Mirrokni): KV-cache memory
cut "6x without accuracy loss", 4-bit attention "up to 8x faster than
32-bit" on H100, tested on Gemma and Mistral with LongBench, Needle In A
Haystack and ZeroSCROLLS. The market reaction two days later: Micron fell
about 14% in 48 hours, Samsung and SK Hynix 5–6% — the "TurboQuant
selloff" of 26 March 2026 (CNBC, Benzinga). The turbovec repository was
created on 26 March 2026.

Note the difference between the paper's unbiasing step (QJL, a one-bit
residual sketch) and turbovec's (a per-vector scale factor, credited to
RaBitQ). turbovec implements the rotation-plus-Lloyd-Max core of
TurboQuant, and borrows the correction from the method TurboQuant is
accused of under-citing.

## The dispute *(search — Medium, dev.to, Milvus blocked; NTU repository read)*

**RaBitQ** (Gao and Long, SIGMOD 2024; submitted October 2023, arXiv May
2024): quantize a D-dimensional vector to D bits after a random rotation
(a Johnson–Lindenstrauss transform), with a proven error bound matching
the Alon–Klartag lower bound; extended later to multi-bit. Adopted in
Milvus 2.6 (`IVF_RABITQ`), Elasticsearch and Lucene as BBQ ("Better Binary
Quantization"), FAISS, VectorChord, CockroachDB, turbopuffer and others
(snippets of the Milvus interview and Gao's post).

**Jianyang Gao's statement** (Medium, March 2026), three problems: the
TurboQuant arXiv and ICLR versions "described RaBitQ as grid-based PQ
while omitting the core random rotation step in RaBitQ"; an ICLR reviewer
asked for a fuller comparison and the final version instead moved the
RaBitQ discussion "into the appendix"; and "in January 2025… the second
author of TurboQuant, Majid Daliri, proactively contacted them and asked
for help debugging his own Python version translated from their RaBitQ C++
implementation."

**The NTU comparison** (`VectorDB-NTU/rabitq-turboquant-comparison`, read;
paper arXiv 2604.19528, April 2026; Gao, Gou, Xu, Shi, Yang, Li, Wong,
Long): "In quantization accuracy, RaBitQ_prod matches or outperforms
TurboQuant_prod across all tested bit widths." "In nearest neighbor search,
RaBitQ consistently achieves higher recall than both TurboQuant variants
across all datasets and bit widths." "TurboQuant_mse consistently achieves
higher recall than TurboQuant_prod, even though the latter is the variant
designed for inner-product estimation." On efficiency: RaBitQ on GPU is
1.2–1.8× faster than TurboQuant on the same A100, and the quantization
times in the TurboQuant paper "could not be reproduced from the released
implementation under the stated hardware configuration" — TurboQuant's
released code ran "up to approximately two orders of magnitude slower".
On the paper's RaBitQ timings: "According to our private correspondence
with the TurboQuant authors, their experiments evaluated RaBitQ on a
single-core CPU with multi-threading disabled, while evaluating TurboQuant
on an A100 GPU." On KV cache: "the two methods have comparable downstream
accuracy, with no consistent winner." Their datasets are the same three
the turbovec README uses (GloVe-200, OpenAI 1536, OpenAI 3072).

**Elastic** (Elasticsearch Labs, 5 May 2026 *(search)*): "Optimized Scalar
Quantization (OSQ) (the algorithm behind Better Binary Quantization (BBQ))
beats TurboQuant where production systems care most: throughput, ranking
accuracy, and storage efficiency"; "On Apple M2 Max, OSQ's symmetric
kernels are 10-40x faster, and on shifted embeddings its 1-bit document
encoding beats TurboQuant at 4 bits on ranking accuracy"; conceding
"TurboQuant still wins on raw reconstruction MSE, but that advantage comes
mostly from the Hadamard rotation".

**Qdrant** (1.18, 11 May 2026 *(search)*): shipped TurboQuant as "an
extended version of the algorithm with borrowed RaBitQ ideas", offering
"similar recall to Scalar Quantization (SQ), using 2x less memory", and
1-bit TurboQuant with "better recall" than binary quantization "at
equivalent storage budgets, albeit at a lower speed"; the usual pattern is
search the compressed vectors, then "rescore the candidates against the
full-precision originals on disk."

## The other "TurboVec" *(search)*

arXiv 2607.16973 (18 July 2026), Navnit Shukla, Kamal Pandey, Omshankar
Tiwari, *TurboVec: A Case Study in Cost-Efficient Private Retrieval for
Enterprise RAG via Codebook-Oblivious Quantization*: a deployment of the
library on Snowpark Container Services — "11ms median query latency at
100K vectors versus approximately 707ms for a warehouse brute-force scan";
"TurboQuant 4-bit outperforms trained FAISS Product Quantization at the
same memory budget by 8.5-8.9 percentage points in Recall@5"; the
allowlist filter "maintains 0.86–0.93 Recall@10 across 10–1000 tenant
workloads versus 0.09–0.19 for a simple over-fetch post-filter baseline";
and an argument that trained codebooks "may expose corpus statistics"
across tenants, which a data-oblivious quantizer does not. A user's case
study, not the author's paper.

## Other implementations, for the record

`turboquant-py` 0.1.0 on PyPI (2026-03-27, `msilverblatt/turboquant-py`):
"Python implementation of the TurboQuant and QJL vector quantization
algorithms" — the community reference the turbovec README compares against
at d=384. `hackimov/turboquant-kv`, `OnlyTerp/turboquant`,
`yashkc2025/turboquant` *(search)*: PyTorch KV-cache implementations.
`kostadis/turbovecdb` *(search)*: a database built on the crate. FAISS's
own FastScan (wiki, read): 4-bit PQ codes "packed in batches of bbs=32"
with lookup tables held in SIMD registers — the layout turbovec's x86
kernel "adapts", per its README.

## Licences

| Piece | Licence |
|---|---|
| turbovec (code, Rust crate, Python wheel) | MIT |
| TurboQuant (algorithm) | a published method; Google's own KV-cache code not examined |
| RaBitQ-Library | not read here; the NTU repository states its own licence in-tree |
| faiss-cpu | MIT (PyPI) |
| ann-benchmarks datasets used in the run | GloVe (Stanford, public domain licence per the GloVe project); DBpedia-OpenAI embeddings (public mirror; original Hugging Face dataset terms not read) |
