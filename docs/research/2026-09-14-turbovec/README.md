# Sixteen times smaller — plan and research

Plan and notes for the AI article on **turbovec**, Ryan Codrai's Rust vector
index built on Google Research's TurboQuant quantizer: what the method does
(rotate, then round each coordinate), what the library adds (online
ingest, incremental saves, kernel-level filtering, framework drop-ins),
what it costs in recall, who says RaBitQ got there first, and how it
compares with FAISS on a machine with four CPU cores and no GPU. Started
2026-09-14, four weeks after turbovec 1.0.0.

Audience: someone building retrieval for a local or private RAG system —
the reader of "An Agent on Your Own Machine" and "A Voice in the Room" —
who has heard that TurboQuant "fits 10 million documents in 4 GB" and
wants to know what that sentence leaves out.

## What was verified, and how

| Claim | Checked against |
|---|---|
| What turbovec is, its API, its file format, its 1.0 guarantees, its own benchmark numbers and how they were produced | The repository's `README.md`, `docs/api.md`, `CHANGELOG.md`, benchmark scripts and result JSONs, read in full from the raw default branch — [`notes/turbovec.md`](notes/turbovec.md) |
| Versions, dates, wheels, dependencies, licence | PyPI's JSON API; the `LICENSE` file; GitHub's search API for stars, forks and creation date |
| Compression, recall, build time and search speed against FAISS on real embeddings, on this machine | `turbovec` 1.0.0 and `faiss-cpu` 1.15.0 installed here on Python 3.12 and run on GloVe-100 and DBpedia/OpenAI-1536 (100K vectors each, from a public mirror of the ann-benchmarks files) — [`notes/turbovec-run.md`](notes/turbovec-run.md), script [`notes/bench.py`](notes/bench.py) |
| The RaBitQ authors' reproduction and its findings | `VectorDB-NTU/rabitq-turboquant-comparison` README and result notes, read in full |
| The TurboQuant paper's abstract and authors, the Google blog, the memory-stock episode, Gao's Medium statement, the Elastic and Qdrant positions, the Milvus interview, the Snowflake case-study paper | Search-result snippets — `arxiv.org`, `research.google`, `medium.com`, `dev.to`, `elastic.co`, `qdrant.tech`, `milvus.io` and `news.ycombinator.com` were blocked by this session's egress policy. Marked *(search)* in the notes; lower confidence |

Not verified: the paper's proofs; any GPU or ARM number (the README's
speed cells are the author's, on Axion and Sapphire Rapids); anything at
10 million vectors — the run here is 100K per dataset, and the "31 GB →
4 GB" line is arithmetic the article checks rather than a run it repeats.

## Decisions

1. **The method before the library.** Rotate-then-round is one idea and
   fits in six steps; the library's features make sense only after it.
2. **Run it against the real competitor, on real embeddings.** FAISS PQ at
   matched bit rates, FAISS FastScan (the README's speed baseline), scalar
   quantization at 8 and 4 bits, an HNSW graph for context, and exact
   float32 as ground truth — on a low-dimensional word-vector set (the
   regime the README calls harder) and on 1536-dimensional OpenAI
   embeddings (the regime the pitch is written for).
3. **Give the dispute its own section, sourced.** The RaBitQ authors'
   reproduction is public code with a README; their claims are quoted from
   it, the TurboQuant side from its abstract, and turbovec's own README —
   which credits RaBitQ for its unbiasing step — sits between them.
4. **Say what turbovec is not.** A flat scan: linear in the corpus, no
   graph, no clustering. At 100K that is a feature; at 100M it is the
   design question.
5. **Rerank, because everyone does.** Every table carries a
   "rerank top-64 with float32" column, since that is how a compressed
   index is used in practice and it changes the recall story.
6. **Date everything.** Nineteen PyPI releases in five months; a 1.0 four
   weeks old.
7. **No hero yet.** Generated (`hero.md`); the CDN was blocked; the article
   ships without a banner until the file is added — same as the previous
   three.

## Traps hit

- `github.com` HTML returns 403 through this proxy for `curl`, and GitHub's
  MCP tools are scoped to this repository only; raw files and the search
  API were the two doors that opened. Stars, forks and the creation date
  came from the search API.
- turbovec requires `dim` to be a multiple of 8. GloVe-100 is not; the run
  zero-pads to 104, which leaves every inner product unchanged and costs
  four per cent of the code bytes. FAISS took 100 as is.
- The DBpedia HDF5 stores float64; turbovec rejects anything but float32
  rather than converting, so cast first.
- The grep-then-tee pipeline that captured the benchmark log buffered
  everything until exit; check for the results file, not the log, when a
  run seems silent.
- The scratchpad from the three previous articles held 16 GB of finished
  environments; they had to go before a 1.7 GB dataset would fit.
