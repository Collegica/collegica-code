The notes behind Sixteen Times Smaller: the repository, API and changelog read at the source, the RaBitQ authors' reproduction, and turbovec run against FAISS on two real embedding sets on four CPU cores.

# Research Reports

* [Sixteen times smaller — plan and research](turbovec-report.md) - What was verified and against what, the decisions behind the article — the method before the library, the dispute sourced from both sides, a rerank column in every table — and the traps hit.

# Research Notes

* [turbovec against FAISS on four CPU cores — the run](turbovec-run.md) - turbovec 1.0.0 and faiss-cpu 1.15.0 on GloVe-100 and DBpedia/OpenAI-1536, 100K vectors each — index bytes, build time, search latency at one and four threads, recall with and without a float32 rerank, and the kernel-level allowlist against a post-filter.
* [turbovec and TurboQuant — checked at the source on 2026-09-14](turbovec.md) - The library in its own words — API, file format, 1.0 guarantees, its benchmark numbers and how they were produced; the TurboQuant method step by step; the RaBitQ authors' reproduction and the Elastic and Qdrant positions; the other paper called TurboVec; which pages could not be fetched.
