# Pipeline research — "Python for Reproducible Research"

Research date: **2026-09-12**. All versions, percentages and URLs checked live on
this date unless flagged otherwise. Audience: technically literate
researchers/engineers, 45–65, skeptical, who have written analysis code for
years and never packaged it for anyone else.

Scope: the three stages **Explore → Organize → Share**, plus testing, archiving
and citation. **Environments vs packages (pixi/Poetry/uv, lockfiles, PEP 621)
is deliberately out of scope** — see [`tooling.md`](tooling.md).

---

## Access and confidence

### Read in full (high confidence — primary source, text actually extracted)

**Papers**

| Source | URL | Accessed |
|---|---|---|
| Pimentel et al. 2019, MSR — **full PDF, text extracted locally with `pdftotext`** | https://leomurta.github.io/papers/pimentel2019a.pdf | 2026-09-12 |
| Pimentel et al. 2021, EMSE — **full JATS XML from Europe PMC, extracted locally** | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8106381/fullTextXML | 2026-09-12 |
| Samuel & Mietchen 2024, GigaScience — abstract verbatim, both routes | https://arxiv.org/abs/2308.07333 · https://doi.org/10.1093/gigascience/giad113 | 2026-09-12 |
| Rule et al. 2019, "Ten simple rules … Jupyter Notebooks" | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007 | 2026-09-12 |
| Wilson et al. 2017, "Good Enough Practices" (article + source repo) | https://doi.org/10.1371/journal.pcbi.1005510 | 2026-09-12 |
| Sandve et al. 2013, "Ten Simple Rules for Reproducible Computational Research" | https://doi.org/10.1371/journal.pcbi.1003285 | 2026-09-12 |
| Noble 2009, "A Quick Guide to Organizing Computational Biology Projects" | https://doi.org/10.1371/journal.pcbi.1000424 | 2026-09-12 |
| FAIR4RS v1.0 — **the RDA PDF itself, principle table read directly** | https://doi.org/10.15497/RDA00068 | 2026-09-12 |
| Crossref API record for the *Scientific Data* FAIR4RS companion | https://api.crossref.org/works/10.1038/s41597-022-01710-x | 2026-09-12 |
| Semantic Scholar API records (4 papers: metadata, abstracts, citation counts) | https://api.semanticscholar.org/graph/v1/paper/DOI:… | 2026-09-12 |
| Zenodo dataset record for the Pimentel corpus | https://zenodo.org/records/3519618 | 2026-09-12 |

**Docs and specifications**

| Source | URL | Accessed |
|---|---|---|
| PyPA, src layout vs flat layout — **raw reST from the PyPA repo** | https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ | 2026-09-12 |
| PEP 660, editable installs | https://peps.python.org/pep-0660/ | 2026-09-12 |
| setuptools "Development Mode" | https://setuptools.pypa.io/en/latest/userguide/development_mode.html | 2026-09-12 |
| IPython magics reference (`%pip`, `%conda`) | https://ipython.readthedocs.io/en/stable/interactive/magics.html | 2026-09-12 |
| IPython autoreload extension (docs "Last updated Sep 01, 2026") | https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html | 2026-09-12 |
| Project Jupyter documentation home | https://docs.jupyter.org/en/latest/ | 2026-09-12 |
| pytest: good practices, fixtures, tmp_path, parametrize, `approx` reference | https://docs.pytest.org/en/stable/ | 2026-09-12 |
| NumPy: testing routines, `assert_allclose`, `Generator`, legacy RNG | https://numpy.org/doc/stable/reference/routines.testing.html | 2026-09-12 |
| Hypothesis docs + strategies reference | https://hypothesis.readthedocs.io/ | 2026-09-12 |
| **GitHub docs — raw Markdown and YAML from `github/docs`** (large files, repository limits, LFS, `large_files.yml`) | https://raw.githubusercontent.com/github/docs/main/… | 2026-09-12 |
| `github/gitignore` Python template | https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore | 2026-09-12 |
| Zenodo help: enable repository, GitHub upload, DOI versioning, citing, size limits | https://help.zenodo.org/ · https://support.zenodo.org/ | 2026-09-12 |
| GitHub docs: referencing and citing content | https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content | 2026-09-12 |
| Citation File Format site + **raw `schema.json`** | https://citation-file-format.github.io/ | 2026-09-12 |
| Software Heritage docs — SWHID specification | https://docs.softwareheritage.org | 2026-09-12 |
| nbdime docs | https://nbdime.readthedocs.io/ | 2026-09-12 |
| DVC docs | https://doc.dvc.org/ | 2026-09-12 |
| pooch docs | https://www.fatiando.org/pooch/ | 2026-09-12 |
| JOSS review checklist and review criteria | https://joss.readthedocs.io/en/latest/review_checklist.html | 2026-09-12 |
| PLOS materials, software and code sharing policy | https://journals.plos.org/plosone/s/materials-software-and-code-sharing | 2026-09-12 |
| Horizon Europe open science (REA) | https://rea.ec.europa.eu/open-science_en | 2026-09-12 |
| cOAlition S | https://www.coalition-s.org/ | 2026-09-12 |

**Repositories and package indexes (raw JSON, not summaries)**

| Source | URL | Accessed |
|---|---|---|
| Cookiecutter Data Science — **all docs pages as raw Markdown via the GitHub contents API** | https://github.com/drivendataorg/cookiecutter-data-science | 2026-09-12 |
| jupytext — **README raw via GitHub contents API** | https://github.com/jupytext/jupytext | 2026-09-12 |
| PyPI JSON API: pytest, hypothesis, pytest-regressions, syrupy, jupytext, papermill, nbdev, dvc, pooch, nbstripout | `https://pypi.org/pypi/<pkg>/json` | 2026-09-12 |
| GitHub API: the-turing-way, reproducible-project-template, scientific-python/cookie, pyos-package-template, nbdev, papermill, nbstripout, pytest-regressions, syrupy, iterative/dvc | https://api.github.com/repos/… | 2026-09-12 |
| Ionel Cristian Mărieș, "Packaging a python library" | https://blog.ionelmc.ro/2014/05/25/python-packaging/ | 2026-09-12 |
| Hynek Schlawack, "Testing & Packaging" | https://hynek.me/articles/testing-packaging/ | 2026-09-12 |
| Jake VanderPlas, "Installing Python Packages from a Jupyter Notebook" | https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/ | 2026-09-12 |
| Joel Grus, speaking list (confirms talk titles and venues) | https://joelgrus.com/speaking/ | 2026-09-12 |
| JupyterCon 2018 programme entry for "I don't like notebooks." | https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/68282.html | 2026-09-12 |
| The Turing Way — overview, definitions, testing (6 subpages), code-quality, vcs, rdm, rdm-metadata, licensing, open | https://book.the-turing-way.org/ | 2026-09-12 |
| Good Research Code Handbook — index, /setup, /tidy, /docs, /pipelines | https://goodresearch.dev/ | 2026-09-12 |

### Snippet-only — weaker, re-verify before quoting verbatim

- Ionel Mărieș, "Rehashing the src layout" (2017) — summary only, wording not confirmed.
- `jupytext.org` rendered marketing copy — reads like paraphrase. **Quote the README instead.**
- `nbdev.fast.ai` philosophy text and its named endorsements (Chris Lattner, Fernando Pérez) — **wording unverified; do not quote.**
- DrivenData's `ccds-v2` announcement blog — summary only. The `v1.md` tree itself is verbatim.
- uv editable-install prose (https://docs.astral.sh/uv/pip/packages/) — syntax reliable, prose not.
- nbdev3's reported `settings.ini` → `pyproject.toml` move — **unverified; do not assert.**
- The Turing Way `overview-benefit` quotes, and its reported "10–40% reproducibility rates" figure — page-reported, citation untraced. **Do not use that number; §1 has better.**
- pyOpenSci's enumerated peer-review checklist — could not be retrieved. **Treat as unconfirmed.**

### Blocked, paywalled or unreadable (cite metadata only)

- **Perkel, "Why Jupyter is data scientists' computational notebook of choice"**, *Nature* **563**, 145–146 (2018), doi:10.1038/d41586-018-07196-1 — **paywalled**; only the citation block and first paragraph rendered. Do not attribute quotes.
- **`blog.jupyter.org` (Medium)** — Cloudflare 403 on every attempt. Pérez & Granger's "Computational Narratives as the Engine of Collaborative Data Science" was **not read**. Do not quote it.
- **Springer `link.springer.com` and ACM DL** — 403/404. The EMSE 2021 paper was recovered via Europe PMC instead.
- **arXiv PDF endpoint** — blocks scripted download; abstract pages fetch fine.
- **Joel Grus's slide decks** (Google Slides) — not fetchable. Only titles, venues, his own one-line descriptions, and the JupyterCon programme abstract are verified.
- **Yihui Xie, "The First Notebook War"** — 403. Not used.
- **Michael Feathers, *Working Effectively with Legacy Code*** — O'Reilly 403. The characterisation-test definition in §3.5 is **Wikipedia's summary of Feathers' term, not Feathers' words.**
- **`acm.org`** — 403 to direct fetch. The Artifact Review and Badging text in §7.4 came through the **`r.jina.ai` reader proxy**. Matches the well-known taxonomy but was **not confirmed from ACM's own server**. Spot-check before quoting.
- **`softwareheritage.org`** — repeated TLS certificate errors across three attempts. Only `docs.softwareheritage.org` was read; the SWHID spec is solid, the mission wording is not.
- **All NIH domains** (grants.nih.gov, osp.od.nih.gov, sharing.nih.gov) — 403 or deprecated-page notices. **The NIH DMS Policy effective date is entirely unverified.**
- **whitehouse.gov / federalregister.gov** — 403/404. The Nelson memo's *implementation deadline* is unverified; only its 25 August 2022 issue date is attested, and only via Wikipedia.
- **nature.com and science.org editorial policy pages** — login walls and 403s. **No 2026 code-availability wording was fetched.**
- **reddit.com** — blocked to the fetcher entirely. The "against stripping notebook outputs" case in §4.4 is reasoned, not sourced.
- **bssw.io** — no usable article located.

### Explicitly NOT verified — do not state these in the article

1. Any specific figure from Hossain et al. 2025 (arXiv:2509.23645). Abstract only; **no corpus size, no rates published in it.**
2. The NIH Data Management and Sharing Policy's effective date or 2026 status.
3. The OSTP Nelson memo's compliance deadline.
4. Nature's or Science's current code-availability policy wording.
5. Whether Horizon Europe's DMP/FAIR mandate extends to software as firmly as to data.
6. A version-specific Zenodo DOI for The Turing Way v1.2.3 (only the concept DOI, `10.5281/zenodo.3233853`, is confirmed).
7. A release date for DVC 3.67.1, or any version/date for `cffconvert`.
8. Any per-GiB dollar price for GitHub LFS metered billing.
9. Julynter's current maintenance status.
10. That The Turing Way states the "notebooks are for exploration, modules for logic" convention — **it was looked for and not found.**

### Session constraint worth recording

The shared WebSearch budget (200 calls) was **exhausted mid-session**. Everything
after that point was reached by direct `WebFetch`/`curl` against known URLs.
Several sources above were recovered only because a raw-file or API route
existed (`raw.githubusercontent.com`, Europe PMC, Crossref, PyPI JSON, the
GitHub contents API). Where a source could not be located without search, that is
stated explicitly rather than guessed.

---

## 1. The notebook reproducibility problem — the opening

### 1.1 Pimentel et al. 2019 (MSR) — the headline numbers

**Citation.** João Felipe Pimentel, Leonardo Murta, Vanessa Braganholo, Juliana
Freire, "A Large-scale Study about Quality and Reproducibility of Jupyter
Notebooks", *Proceedings of the 16th International Conference on Mining
Software Repositories (MSR 2019)*, pp. 507–517.
DOI [10.1109/MSR.2019.00077](https://doi.org/10.1109/MSR.2019.00077).
256 citations as of 2026-09-12 (Semantic Scholar API, accessed 2026-09-12).
Dataset: [10.5281/zenodo.3519618](https://zenodo.org/records/3519618) (~20 GB, v4 dated 2021-03-15; accessed 2026-09-12).

**The corpus** (all from the paper PDF, https://leomurta.github.io/papers/pimentel2019a.pdf, accessed 2026-09-12):

| Quantity | Number |
|---|---:|
| Unique notebooks collected | **1,159,166** |
| GitHub repositories | **264,023** |
| Duplicates excluded (forks etc.) | 264,510 (18.58%) |
| Valid Python notebooks | 1,005,689 (86.76%) |
| Notebooks with *unambiguous* execution order, cells executed | **863,878** (74.53%) |
| Notebooks actually taken into the reproducibility run | 788,813 (minus 32 corrupted) |
| Collection cut-off | 16 April 2018 |

**The two numbers the article opens on** — verbatim from the introduction:

> "out of 863,878 attempted executions of valid notebooks … only 24.11% executed without errors and only 4.03% produced the same results"
> — Pimentel et al. 2019, §I ([PDF](https://leomurta.github.io/papers/pimentel2019a.pdf), accessed 2026-09-12)

So: **24.11% ran to the end. 4.03% produced the same results.** Absolute
count for the first: 208,323 notebooks finished successfully.

**Why they failed** (§IV-G):

| Cause | Share of notebook executions |
|---|---:|
| `ImportError` + `ModuleNotFoundError` (missing dependencies) | **29.23%** |
| `NameError` (hidden state / out-of-order) | **14.53%** |
| `FileNotFoundError` + `IOError` (absolute paths, data not in repo) | **12.59%** |
| Exceeded the 5-minute time limit | 9,982 notebooks |
| Failed on some exception | 570,476 notebooks |

The sting in the dependency number: **45.18%** of notebooks from repositories
that *did* declare dependencies failed with `ImportError`/`ModuleNotFoundError`,
against **31.24%** from repositories that declared none (the latter ran in
bloated Anaconda images). Declaring dependencies made things *worse* — because
the declarations were incomplete. Failure rates for the declaration files
themselves: `setup.py` 67.55%, `requirements.txt` 61.17%, `Pipfile` 65.20%.

**The structural bad practices** (§IV-F, §IV-C, §IV-D):

| Finding | Number |
|---|---:|
| Notebooks with unambiguous execution order | 912,343 (86.59% of executed) |
| Of those, **notebooks with out-of-order cells** | **36.36%** |
| Notebooks with at least one execution-counter **skip** | **76.90%** (66.08% excluding skips at the very start) |
| Average executions inside a skip | 12.82 (10.32 excluding leading skips) |
| Executed notebooks with **non-executed code cells** | **21.11%** |
| Executed notebooks with **empty cells** | 62.08% |
| Executed notebooks finishing with empty cells | 59.07% |
| Valid Python notebooks that **define any function** | **53.94%** |
| …that define any class | 8.54% |
| …that have any **local import** (i.e. import a module from their own repo) | **10.30%** |
| …that import any **testing** module | **1.54%** (15,473 notebooks) |
| Notebooks whose filename starts with "Untitled" | 1.99% |
| Notebooks with no markdown cell at all | 30.93% |

Two of those carry the article's whole argument: **10.30% import local code**
and **1.54% import a test framework**. Those are the "Organize" and "Testing"
sections in one line each.

**The paper's own eight best practices** (§V, paraphrased headings, verbatim
where short):

1. "Use short titles with a restrict charset" for notebook filenames; put rich titles in markdown.
2. "Pay attention to the bottom of the notebook" — that is where markdown and executed cells thin out.
3. **"Abstract code into functions, classes, and modules and test them."**
4. "Declare the dependencies in requirement files and pin the versions of all packages."
5. "Use a clean environment for testing the dependencies to check if all of them are declared."
6. "Put imports at the beginning of notebooks."
7. **"Use relative paths for accessing data in the repository."**
8. **"Re-run notebooks top to bottom before committing."**

(Quotes from §V of the PDF, accessed 2026-09-12. Nos. 3, 7 and 8 map directly
onto the article's Organize/Share stages.)

**A calibration the paper offers itself:** 24.11% is "very close to the
reproducibility rate of 24.9% that Collberg et al. achieved in their study of
reproducibility in general computer systems research" (§IV-G). Notebooks are
not uniquely bad; they are *typically* bad. That is a useful line for a
skeptical reader who expects to be scolded.

### 1.2 Pimentel et al. 2021 (EMSE) — the authors' own replication, with tougher methodology

**Citation.** Same four authors, "Understanding and improving the quality and
reproducibility of Jupyter notebooks", *Empirical Software Engineering* **26**,
2021. DOI [10.1007/s10664-021-09961-9](https://doi.org/10.1007/s10664-021-09961-9).
PMC8106381. 89 citations as of 2026-09-12 (Semantic Scholar API).
Read in full via Europe PMC, accessed 2026-09-12.

This matters because it pre-empts the obvious objection to the 2019 paper — *you
ran the cells in the recorded execution-counter order, not top to bottom, in a
shared environment; of course it failed.* The 2021 paper re-ran the experiment
in **five modes** (Table 1):

| # | Environment | Execution order |
|---|---|---|
| 1 | Shared OS, conda/anaconda envs | cell execution counter |
| 2 | Isolated Docker, anaconda env | cell execution counter |
| 3 | Isolated Docker, anaconda env | **top-down** |
| 4 | "Bloated" Docker (max packages installed) | cell execution counter |
| 5 | "Bloated" Docker | **top-down** |

and applied a ladder of output normalisations (encode, execution counter,
stream, dictionary, dataframe, exception path, deprecation, whitespace, decimal,
date, time, memory address, image).

**The result** — verbatim:

> "the reproducibility of notebooks is far from ideal with only 4.90% to 15.04% of Python notebooks being replicated successfully"
> — Pimentel et al. 2021, Related Work section (Europe PMC full text, accessed 2026-09-12)

and, in the conclusion:

> "We achieved a reproducibility rate that ranged from 4.90% to 15.04%."

**Read the range correctly, because the article must not overstate it.**
- **4.90%** = mode 1 (shared env, execution-counter order), no normalisation at all — essentially the 2019 setup, and it reproduces the 2019 figure (4.03%) within the changed corpus.
- **15.04%** = mode 5 (bloated container with the maximum possible dependencies pre-installed, top-down execution) **after image normalisation**, which the paper itself calls "the most susceptible to false positives, as it ignores differences in image results."
- So the honest framing is: *give a notebook every advantage — a container stuffed with every package, top-down execution, and forgive every plot that looks slightly different — and you still reproduce fewer than one in six.*

**Cells that ran all the way through**, by mode: 26.09% / 23.24% / 25.84% /
22.57% / 25.43%. Note the top-down order did **not** rescue execution — the
bottleneck is dependencies, not ordering.

**Do popular notebooks do better?** Yes, and by less than you'd hope:

> "They are 31.04% more likely to execute until the end, 84.83% more likely to reproduce the same results without normalizations"
> — Pimentel et al. 2021 (Europe PMC, accessed 2026-09-12)

In absolute terms the popular subset still only ran all cells 31.84–36.27% of
the time. "More likely" off a tiny base is still a tiny base.

**Updated structural figures in the 2021 paper** (recomputed on a re-collected
corpus, so they differ slightly from 2019): out-of-order cells **36.45%**;
at least one skip **76.88%**; ambiguous execution order **15.94%**; dependency
install failure **59.30%** of notebooks (setup.py 65.53%, requirements.txt
57.21%, Pipfile 60.69%). `requirements.txt` was the *least* bad — the paper
attributes this to it being declarative with pinned versions, while `setup.py`
is an arbitrary Python script.

**Association rules** (Table 8) — genuinely useful, concrete advice:
notebooks of **9 cells or fewer** are 2.2× more likely to reproduce; notebooks
of **37 cells or more** are 0.30× as likely. Unordered cells: 0.34×. Skips in
the middle: 0.64×. *Short notebooks reproduce; long notebooks do not.*

**Julynter** — the 2021 paper's output is a JupyterLab extension that lints
notebooks against these findings. Worth one sentence, not a section. (I did not
verify Julynter's current maintenance status; **do not claim it is maintained**.)

### 1.3 Samuel & Mietchen 2024 (GigaScience) — the newer replication, on published science

**Citation.** Sheeba Samuel, Daniel Mietchen, "Computational reproducibility of
Jupyter notebooks from biomedical publications", *GigaScience*, published
11 January 2024. DOI [10.1093/gigascience/giad113](https://doi.org/10.1093/gigascience/giad113).
Preprint arXiv:2308.07333. 64 citations as of 2026-09-12 (Semantic Scholar API).
Abstract read verbatim from both https://arxiv.org/abs/2308.07333 and the
journal page, accessed 2026-09-12.

This is the study to pair with Pimentel, because the corpus is not "all of
GitHub" but **notebooks attached to peer-reviewed biomedical papers** — the
population a researcher-reader identifies with.

The funnel, verbatim from the abstract:

| Stage | Count |
|---|---:|
| Jupyter notebooks found | **27,271** |
| from GitHub repositories | 2,660 |
| associated with publications (PubMed Central) | 3,467 |
| written in Python | 22,578 |
| **with dependencies declared** in standard requirement files | 15,817 |
| for which **all declared dependencies installed** | 10,388 |
| **ran through without any errors** | **1,203** |
| **produced results identical to those reported** | **879** |
| ran but produced different results | 324 |

> "1,203 notebooks ran through without any errors, including 879 that produced results identical to those reported"
> — Samuel & Mietchen 2024, abstract (accessed 2026-09-12)

**Denominators matter here — pick one and state it.** The paper gives counts,
not percentages, and different framings are all defensible:
- 879 / 10,388 (dependencies installed cleanly) = **8.5%**
- 1,203 / 10,388 = **11.6%** ran clean
- 879 / 15,817 (attempted automatically) = **5.6%**
- 879 / 22,578 (all Python notebooks found) = **3.9%**
- 879 / 27,271 (all notebooks found) = **3.2%**

**Recommendation for the article: quote the raw counts** ("879 of 27,271") and
give one derived percentage, clearly labelled. Do not present a percentage the
paper did not print.

Their own stated conclusion, per the journal abstract: the large majority could
not be executed automatically, mostly because dependencies were badly
documented. Same headline cause as Pimentel, six years and one peer-review
filter later.

**Companion paper** (metadata only, not needed for the article): Samuel &
Mietchen, "FAIR Jupyter: a knowledge graph approach…", *Transactions on Graph
Data and Knowledge* 2(2), 4:1–4:24, 2024, DOI 10.4230/TGDK.2.2.4
(https://arxiv.org/abs/2404.12935, accessed 2026-09-12). It republishes the
above dataset as a queryable knowledge graph; it reports no new reproducibility
rates.

### 1.4 Very recent work (2025) — flag as thin

Hossain, Brown, Koop & Malik, "Similarity-Based Assessment of Computational
Reproducibility in Jupyter Notebooks", arXiv:2509.23645, submitted 28 September
2025 (https://arxiv.org/abs/2509.23645, accessed 2026-09-12). Proposes a
**Similarity-based Reproducibility Index (SRI)** scoring each rerun cell in
[0,1] rather than pass/fail, because "rerunning a Jupyter Notebook may not
always generate identical results due to various factors, such as randomness,
changes in library versions, or variations in the computational environment."

**Confidence: abstract only.** The abstract describes "a case study … applied to
a set of Jupyter Notebooks" and gives **no corpus size and no rates**. Use it, if
at all, only for the *idea* that binary reproducible/not is too crude a measure.
**Do not attribute any number to it.**

### 1.5 The failure modes, named

Each of these is evidenced above rather than asserted:

| Failure mode | Evidence |
|---|---|
| **Hidden state** — a variable exists only because of a cell you since edited or deleted | `NameError` in 14.53% of executions (Pimentel 2019 §IV-G); 76.90% of notebooks have at least one execution-counter skip |
| **Out-of-order execution** | 36.36% of unambiguous notebooks have out-of-order cells (2019); 36.45% (2021) |
| **Non-executed cells left in the file** | 21.11% of executed notebooks |
| **Absolute paths / data not in the repo** | `FileNotFoundError`+`IOError` = 12.59% of executions |
| **Undeclared or under-declared dependencies** | 29.23% `ImportError`/`ModuleNotFoundError`; and declaring made it *worse* (45.18% vs 31.24%) |
| **`!pip install` in a cell** | see below — it can install into a different Python than the kernel |
| **Unpinned randomness** | see §3.2 — `default_rng` carries *no* cross-version bit-stream guarantee |

**On `%pip` versus `!pip`** — Jake VanderPlas's 2017 post is still the clearest
statement of the mechanism (https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/,
accessed 2026-09-12):

> "The shell environment is determined when the Jupyter notebook is launched, while the Python executable is determined by the kernel"
> — Jake VanderPlas, 2017 (trimmed; the full sentence continues "…and the two do not necessarily match")

His proposed fix became the IPython magics. IPython's own reference now documents
them (https://ipython.readthedocs.io/en/stable/interactive/magics.html, accessed 2026-09-12):

> "Run the pip package manager within the current kernel."
> — IPython docs, `%pip`

So the article's line is: **if you must install from a notebook, use `%pip`, not
`!pip` — and better, don't, because the install is not recorded anywhere a
second machine will see it.** That last clause is the one the data supports.

### 1.6 The counter-view: what notebooks are genuinely good at

This section must be honest, or the skeptical reader stops reading.

**(a) The critic.** Joel Grus, **"I Don't Like Notebooks"**, JupyterCon 2018 —
confirmed from his own site (https://joelgrus.com/speaking/, accessed
2026-09-12), where he describes it as:

> "This talk is possibly what I'm most famous for."
> — Joel Grus, joelgrus.com/speaking

The JupyterCon 2018 programme entry
(https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/68282.html,
accessed 2026-09-12) lists him as Joel Grus, Allen Institute for Artificial
Intelligence, and its abstract describes notebooks as something that:

> "ties your hands in a lot of ways"
> — JupyterCon 2018 programme abstract for "I don't like notebooks."

He gave a constructive sequel, **"If Not Notebooks, Then What?"**, at the AAAI
2019 "Reproducible AI" Workshop, and **"Reproducibility: A Trojan Horse for
Software Engineering Best Practices"** at ICLR 2019 — same site. That second
title is a gift to this article: reproducibility as the Trojan horse for
engineering practice is exactly the article's own argument.

**⚠️ Caveat: the slide decks are Google Slides and could not be fetched. The
talk's specific arguments — hidden state, out-of-order execution, encouraging bad
practice — are widely attributed to it but were NOT verified from the deck or a
transcript. Do not put words in Grus's mouth beyond the title and the programme
abstract above.** Pimentel et al. 2021 do cite "Grus 2018" for criticisms about
"lack of IDE features" and "lock-in aspects of Jupyter", which is a legitimate
secondhand attribution with a citable source.

**(b) The defence, and it is the strongest available source.** Rule et al.,
**"Ten simple rules for writing and sharing computational analyses in Jupyter
Notebooks"**, *PLOS Computational Biology*, 25 July 2019, DOI
[10.1371/journal.pcbi.1007007](https://doi.org/10.1371/journal.pcbi.1007007)
(read in full 2026-09-12). **Fernando Pérez — who created IPython — is a
co-author.** This is not an outsider scolding notebook users; it is the
notebook's own author conceding the failure modes and prescribing fixes.

Their positive claim, verbatim:

> "combine code, results, and descriptive text in a single 'computational narrative'"
> — Rule et al. 2019, Introduction

Their concession, verbatim:

> "can delete key steps or introduce 'hidden state' that confounds analyses and confuses readers"
> — Rule et al. 2019, Introduction

The ten rules (verbatim headings):

1. Tell a story for an audience
2. Document the process, not just the results
3. Use cell divisions to make steps clear
4. **Modularize code**
5. **Record dependencies**
6. **Use version control**
7. Build a pipeline
8. Share and explain your data
9. Design your notebooks to be read, run, and explored
10. Advocate for open research

Rules 4, 5 and 6 *are* the article's Organize and Share stages, written by the
Jupyter people. Useful supporting quotes:

> "wrap code you are about to copy and reuse in a function, which you can then call"
> — Rule et al. 2019, Rule 4 (trimmed)

> "the interactive nature of notebooks makes it easy to accidentally change or delete important content"
> — Rule et al. 2019, Rule 6 (trimmed)

> "differences … are expressed as changes in the abstruse JSON metadata for the notebook"
> — Rule et al. 2019, Rule 6 (trimmed)

Their own operational advice on hidden state:

> "make a habit of regularly restarting your kernel and rerunning all cells"
> — Rule et al. 2019, Rule 7 (trimmed)

**(c) Jupyter's own framing.** Project Jupyter's documentation home
(https://docs.jupyter.org/en/latest/, accessed 2026-09-12) describes the notebook
as:

> "a fast interactive environment for prototyping and explaining code"
> — Project Jupyter documentation

Note what is *absent*: the word reproducibility does not appear as a stated goal
on that page. **This is a genuinely useful observation for the article — the tool
is advertised as a prototyping and explanation environment, and it is very good
at that. The reproducibility expectation was imported by users, not promised by
the project.** (Confidence: this is my reading of one page; phrase it as an
observation about that page, not as a claim about Project Jupyter's position.)

**(d) The bit of the data that defends notebooks.** From Pimentel 2021: short
notebooks (≤9 cells) are ~2.2× more likely to reproduce. A notebook used as a
*narrative over already-organised code* is a different artefact from a notebook
used as the codebase. The article's thesis is not "stop using notebooks"; it is
"the notebook is the explore stage, and it should get shorter as the module
grows."

---

## 2. Organize — getting code out of the notebook

### 2.1 `src/` layout versus flat layout

**Primary source:**
https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
(read in full, via the raw reST from the PyPA repo, accessed 2026-09-12).

**PyPA's position is descriptive, not prescriptive — and the article should say
so.** The page defines both layouts, lists three behavioural differences, and
never concludes that one is correct. Anyone who tells you "PyPA says use src/"
is overreading it.

The three differences, verbatim:

> "The src layout requires installation of the project to be able to run its code"
> — PyPA packaging discussions

> "helps prevent accidental usage of the in-development copy of the code"
> — PyPA packaging discussions

> "helps enforce that an editable installation is only able to import files"
> — PyPA packaging discussions

**The mechanism, in one sentence:** "the Python interpreter includes the current
working directory as the first item on the import path" (PyPA, same page). With a
flat layout, `import myproject` from the repo root picks up the *source tree*,
not the installed package. So your tests pass against code that was never
packaged — and a file you forgot to include in the distribution is invisible
until a user reports it.

**What flat layout specifically breaks:** an editable install can put "the other
project files (eg: README.md, tox.ini)" and "packaging/tooling configuration
files (eg: setup.py, noxfile.py)" on the import path, so "certain imports work
in editable installations but not regular installations" (PyPA, same page). The
bug surfaces after you publish.

**PyPA's own sanctioned `sys.path` exception:** for running a CLI from an
uninstalled src-layout tree, the page documents prepending the package folder to
`sys.path` inside `__main__.py`. Narrow, deliberate, and not a general licence —
worth mentioning so the article's later attack on `sys.path` hacks is fair.

**The two originating essays**, both read in full on 2026-09-12:

**Ionel Cristian Mărieș, "Packaging a python library"** (25 May 2014, updated
30 Sep 2019), https://blog.ionelmc.ro/2014/05/25/python-packaging/ — the post
credited with originating the modern src argument.

> "You get import parity."
> — Ionel Cristian Mărieș (section heading)

> "You will be forced to test the installed code"
> — Ionel Cristian Mărieș

> "Without src you get messy editable installs"
> — Ionel Cristian Mărieș

> "Less chance for user mistakes - they will happen"
> — Ionel Cristian Mărieș

His 2017 follow-up, "Rehashing the src layout"
(https://blog.ionelmc.ro/2017/09/25/rehashing-the-src-layout/) is notably more
relaxed — roughly, if your existing flat project is not causing problems there
is little value in switching, and src needs tooling (tox) to be worth it.
**Confidence: snippet-level summary, not raw HTML. Do not quote it verbatim.**

**Hynek Schlawack, "Testing & Packaging"** (19 Oct 2015, updated 4 Jan 2021),
https://hynek.me/articles/testing-packaging/ — read in full 2026-09-12.

> "your tests do not run against the package as it will be installed by its users"
> — Hynek Schlawack

> "They run against whatever the situation in your project directory is"
> — Hynek Schlawack

> "isolating the code into a separate – un-importable – directory might be a good idea"
> — Hynek Schlawack

**Nice historical detail for the article:** in his 2021 update Hynek notes that
three of the four projects he originally used as flat-layout examples — Flask,
Pyramid and Twisted — had since moved to `src/`. The argument was won by
attrition, not decree.

**Where this lands for the article's audience.** The honest framing is not
"src/ is correct" but: *`src/` is the layout that makes it impossible to test
code you have not installed. For a researcher whose whole problem is that the
code only runs in one directory on one machine, that is the point.*

### 2.2 Cookiecutter Data Science (DrivenData)

**Best-sourced material in this note** — all pages read as raw Markdown via the
GitHub contents API rather than a rendered summary, accessed 2026-09-12:
`docs/docs/index.md`, `opinions.md`, `using-the-template.md`, `why.md`, `v1.md`
at https://github.com/drivendataorg/cookiecutter-data-science.

**Maintenance (GitHub API, 2026-09-12):** 10,050 stars, 34 open issues, ~2.6k
forks, not archived. Latest tagged release **v2.3.0**, published 2025-07-24.
Last push to the repo 2026-08-07. Actively maintained, with development
continuing past the last tag.

**The v2 tree, verbatim from `index.md`** (abridged here; the full tree is worth
reproducing in the article because the inline comments *are* the opinions):

```
├── LICENSE
├── Makefile           <- convenience commands like `make data` or `make train`
├── README.md
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── docs               <- A default mkdocs project
├── models             <- Trained and serialized models, model predictions, or model summaries
├── notebooks          <- Jupyter notebooks.
├── pyproject.toml
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
├── requirements.txt
├── setup.cfg
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    ├── __init__.py
    ├── config.py               <- Store useful variables and configuration
    ├── dataset.py              <- Scripts to download or generate data
    ├── features.py             <- Code to create features for modeling
    ├── modeling
    │   ├── predict.py
    │   └── train.py
    └── plots.py
```

**The load-bearing opinion** — `opinions.md` has a section headed
**"Notebooks are for exploration and communication, source files are for
repetition."** Its justification, verbatim:

> "Source code is superior for replicability because it is more portable, can be tested more easily, and is easier to code review."
> — Cookiecutter Data Science, opinions (accessed 2026-09-12; 21 words — trim before quoting)

Shorter, quotable fragments from the same page:

> "raw data must be treated as immutable"
> — Cookiecutter Data Science, opinions

> "we recommended not collaborating directly with others on Jupyter notebooks"
> — Cookiecutter Data Science, opinions

**Its signal for when to leave the notebook** — this is the single most useful
practical sentence found in the whole research pass, because it gives the reader
a trigger rather than an exhortation. From the "Refactor the good parts into
source code" subsection:

> "duplicating old notebooks to start new ones, copy/pasting functions between notebooks, and creating object-oriented classes within notebooks"
> — Cookiecutter Data Science, opinions (its "classic signs that you are ready to move from a notebook to source code")

**Other stated positions:**
- `data/` is **in `.gitignore` by default**. "by default, the `data/` folder is included in the `.gitignore` file."
- `notebooks/` is subdivided into `notebooks/exploratory/` and `notebooks/reports/`.
- `models/` has no imposed structure; the emphasis is on documenting "provenance of the data and the version of the code."
- They ship **`nbautoexport`** (github.com/drivendataorg/nbautoexport), which auto-exports a `.py` companion on every notebook save, specifically so that reviewers can leave line-by-line comments on a pull request. A different answer to the same problem jupytext solves — worth naming both.
- Meta-principle from `why.md`: "be liberal in changing the folders around for *your* project, but be conservative in modifying the default cookiecutter structure for *all* projects," explicitly invoking PEP 8's "a foolish consistency is the hobgoblin of little minds."
- Also from `why.md`: "data science code quality is about correctness and reproducibility" — not formatting.

**The notebook naming convention, and a caveat.** The convention is *ordered
prefix + author initials + description*. But DrivenData's own docs give three
mutually inconsistent examples:
- `index.md` tree comment: `1.0-jqp-initial-data-exploration` (this is the **v1** form, carried over)
- `using-the-template.md`: `0.01-pjb-data-source-1.ipynb`, described as `PHASE.NOTEBOOK` where phase 0 = exploration, 1 = cleaning/features, 2 = visualisation, 3 = modelling, 4 = publication
- `opinions.md`: `<step>-<ghuser>-<description>.ipynb`, e.g. `0.3-bull-visualize-distributions.ipynb`

State the convention; do not claim a single canonical format.

**v1 → v2 changes** (from `v1.md` verbatim plus DrivenData's announcement at
https://drivendata.co/blog/ccds-v2 — **the blog is snippet-level, the v1.md tree
is verbatim**):
- **`src/` was renamed to `{{ cookiecutter.module_name }}`** — a real importable package named after the project. This is the change the article must not get wrong: *Cookiecutter Data Science v2 no longer uses a directory called `src/`.* Rationale given: "This better reflects the common Python practice of having your top level module be the project name."
- `setup.py` → `pyproject.toml`
- Sphinx → MkDocs for `docs/`
- A new `ccds` CLI replaces calling `cookiecutter` directly
- Requires Python 3.9+
- v1 explicitly deprecated but still usable

### 2.3 "Notebooks are for exploration, modules are for logic" — who actually says it

**Cookiecutter Data Science** is the strongest and most directly quotable source
(§2.2 above). Its section heading is literally the convention.

**Wilson et al. 2017, "Good Enough Practices in Scientific Computing"** is the
citable academic ancestor — see §7.2. Read in full from the source repo
(https://github.com/swcarpentry/good-enough-practices-in-scientific-computing,
`index.md`, accessed 2026-09-12):

> "readable, reusable, and testable are all side effects of writing modular code"
> — Wilson et al. 2017

It predates the notebook-heavy era but makes the same argument one level up:
short single-purpose functions in `src/`, plus a thin driver script.

**Rule et al. 2019** (§1.6) Rule 4, "Modularize code", with Fernando Pérez as a
co-author — the closest thing to an endorsement from inside Jupyter.

**⚠️ The Turing Way does NOT state this convention.** The Organize research pass
checked `/reproducible-research/reproducible-research`, `/code-reuse` and
`/code-quality` directly and found nothing of the kind; `code-reuse` only
mentions in passing that a project "can range from a small script you use for
data processing to a notebook used for data analysis, or a software library."
**Do not attribute this framing to The Turing Way.** (Three of roughly nine
top-level guides were checked; absence is not proof, but it is not there in the
obvious places.)

**Software Carpentry's git-novice lesson** does not address it either (checked
directly, https://swcarpentry.github.io/git-novice/, accessed 2026-09-12).

**The opposing camp is nbdev**, and the article is stronger for naming it.
nbdev's position is that notebooks should hold production logic permanently, not
be drafted and discarded (https://nbdev.fast.ai/, accessed 2026-09-12):

> "nbdev makes exploration an integral part of your workflow, all while promoting software engineering best practices."
> — nbdev (**snippet-level fetch; verify wording before quoting**)

### 2.4 jupytext, papermill, nbdev — what each solves, and whether it is alive

All version and maintenance figures below come from the **PyPI JSON API and the
GitHub API directly**, accessed 2026-09-12 — raw JSON, not summaries.

| Tool | Problem it solves | Version | Released | Repo state 2026-09-12 |
|---|---|---|---|---|
| **jupytext** | Pairs an `.ipynb` with a plain-text `.py`/`.md` twin so notebooks diff and review like source | **1.19.5** | 2026-07-21 | `jupytext/jupytext` (moved from `mwouts/`), last push **2026-09-11**, 7,244 stars, 170 open issues, not archived — **actively maintained** |
| **papermill** | Parameterises and executes notebooks headlessly; chains them into pipelines | **2.7.0** | 2026-02-27 | `nteract/papermill`, last feature commit **2026-03-08**, 6,486 stars, 196 open issues, 48 open PRs, not archived — **slowing** |
| **nbdev** | Makes the notebook the *source of truth* for a package: exports library code, tests and docs from annotated cells | **3.3.18** | **2026-09-09** | **`AnswerDotAI/nbdev`** (moved from `fastai/`), last push 2026-09-09, 5,316 stars, 185 open issues — **very actively maintained** |

**On papermill, be careful.** Its README carries **no** deprecation or
"seeking maintainers" notice — that was checked directly. The honest sentence is:
*commit activity visibly slowed through 2026, with no formal statement either
way.* Do not write "unmaintained."

**On nbdev, a checkable fact worth one line:** the repo now lives under
**Answer.AI**, not the `fastai` org, though the README copyright line still reads
"Copyright © 2019 onward fast.ai, Inc." (GitHub API 301 redirect confirmed
2026-09-12). nbdev3's config reportedly moved from `settings.ini` to
`pyproject.toml` — **snippet-level, unverified; do not assert.**

**jupytext is the one the article should actually recommend**, and here is the
mechanism, verbatim from the repo README (read raw via the GitHub contents API,
2026-09-12):

> "These are a set of two files, say `.ipynb` and `.py`, that contain the same notebook, but in different formats."
> — jupytext README (trimmed)

> "You can edit the `.py` version of the paired notebook, and get the edits back in Jupyter"
> — jupytext README (trimmed)

Formats: **`py:percent`** (`# %%` cell markers — "well suited for version
control… a regular Python file"; recommended "for notebooks that mostly contain
code"), **`py:light`** (minimal markers), and Markdown variants including MyST
and Quarto Markdown, recommended when "your notebook is documentation-oriented."

Config, exactly as the README prints it:

```toml
# jupytext.toml at the root of your notebook directory
formats = "ipynb,py:percent"
```

Per-project configuration under `[tool.jupytext]` in `pyproject.toml` is also
supported (mentioned in the README; not shown there).

CLI:
```
jupytext --set-formats ipynb,py:percent notebook.ipynb   # pair
jupytext --sync notebook.py                              # sync
jupytext --to ipynb notebook.py                          # convert
jupytext --pipe black notebook.ipynb                     # format
```

**Why this makes git diffs meaningful:** only inputs — code and markdown — land
in the text file. Outputs, JSON structure and base64 image blobs stay in the
`.ipynb`, which you can git-ignore. The diff on a paired notebook is "nothing
else than a standard diff on a Python script" (jupytext README). That connects
directly to Rule et al.'s complaint about "abstruse JSON metadata" (§1.6) and to
§4's nbstripout debate.

**Caveat recorded:** jupytext.org's rendered marketing copy returned phrasing
that reads like paraphrase rather than page text. **Quote the README, not the
website.**

### 2.5 Importing project code into a notebook — and why `sys.path` is the wrong answer

**The right answer is an editable install**, and it is standardised.

**PEP 660, "Editable installs for pyproject.toml based builds"**
(https://peps.python.org/pep-0660/, read in full 2026-09-12):

> "Python programmers want to be able to develop packages without having to install (i.e. copy) them into site-packages"
> — PEP 660 (trimmed)

> "changes to the project python code in the local source tree become effective without the need of a new installation step"
> — PEP 660 (trimmed)

PEP 660 generalised what had been a setuptools-only trick (`setup.py develop`)
to every build backend.

**setuptools' "Development Mode" docs**
(https://setuptools.pypa.io/en/latest/userguide/development_mode.html, read in
full 2026-09-12) describe the problem `pip install -e .` exists to remove:

> "require the developers to manipulate the PYTHONPATH environment variable or to continuously re-build and re-install"
> — setuptools development-mode docs (trimmed)

That sentence *is* the description of a `sys.path.append('../src')` cell. It is
manual PYTHONPATH manipulation with extra steps. setuptools implements PEP 660
as of v64.0.0.

**setuptools' own honest caveats** (same page) — include these, this audience
rewards them: non-Python files and binary extensions "may only be exposed as
snapshots"; adding new dependencies or entry points requires reinstallation; and
editable installs are "not a perfect replacement for regular installs in test
environments." The last one loops straight back to Hynek and Ionel in §2.1.

`uv` supports the identical syntax — `uv pip install -e .` — and states that
"Editable packages do not need to be reinstalled for changes to their source code
to be active" (https://docs.astral.sh/uv/pip/packages/, accessed 2026-09-12;
**snippet-level prose, syntax reliable**). That is the only uv fact in this note;
the rest is the companion article's.

**Why `sys.path.append('../src')` is wrong — four reasons, each traceable:**
1. It is per-notebook, per-machine boilerplate that breaks the moment the notebook moves directory or someone clones to a different path.
2. It silently shadows the installed package — the exact hazard PyPA names in §2.1. You can end up running different code in the notebook than `pip install` would ship.
3. It bypasses packaging metadata entirely: dependencies, entry points, data files. An editable install is a real install; a path hack is not.
4. Cookiecutter Data Science's own template installs the project locally by default precisely so this is unnecessary (`using-the-template.md`, accessed 2026-09-12).

**Note there is no single canonical "sys.path is bad" essay.** The argument above
is assembled from PyPA, setuptools and Ionel. Present it as a synthesis, not a
citation.

**The `%autoreload` idiom**, verbatim from the current IPython docs
(https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html,
IPython 9.17.1, page "Last updated on Sep 01, 2026", accessed 2026-09-12):

```python
%load_ext autoreload
%autoreload 2
```

Modes: `0`/`off` disable; `1`/`explicit` reload only `%aimport`-marked modules;
**`2`/`all` reload everything before each execution — the idiom everyone uses**;
`3`/`complete` same as 2 plus newly added objects. Flags `--print`/`-p` and
`--log`/`-l` report what reloaded.

**The caveats, verbatim — these matter, because autoreload silently half-works:**

> "C extension modules cannot be reloaded, and so cannot be autoreloaded."
> — IPython autoreload docs

> "Functions that are removed (eg. via monkey-patching) from a module before it is reloaded are not upgraded."
> — IPython autoreload docs

> "changing a @property in a class to an ordinary method or a method to a member variable can cause problems"
> — IPython autoreload docs (trimmed; "in old objects only")

And the subtle one: reloading a module creates **new** Enum objects — "These may
look the same, but are not" — so `is` comparisons and `isinstance` checks against
values still held in notebook variables silently fail.

**Cookiecutter Data Science publishes exactly this three-line idiom** as the
recommended way to use project code from a notebook (`opinions.md`, accessed
2026-09-12):

```python
%load_ext autoreload
%autoreload 2
from {{ cookiecutter.module_name }}.data import make_dataset
```

That is the whole "Organize" stage in three lines, and it is a good candidate
for the article's pivot image.

---

## 3. Testing research code

### 3.1 pytest, only the parts that matter here

**Current version: pytest 9.1.1**, uploaded 2026-06-19 (PyPI JSON API,
https://pypi.org/pypi/pytest/json, accessed 2026-09-12). Release date taken from
the artefact upload timestamp; not cross-checked against the changelog.

**Discovery rules** — verbatim from
https://docs.pytest.org/en/stable/explanation/goodpractices.html (accessed 2026-09-12):

- "Recurse into directories, unless they match `norecursedirs`."
- "In those directories, search for `test_*.py` or `*_test.py` files"
- Collect "`test` prefixed test functions or methods outside of class"
- and "`test` prefixed test functions or methods inside `Test` prefixed test classes (without an `__init__` method)"

**The trap worth naming in the article:** a `Test`-prefixed class that defines
`__init__` is silently skipped. No error, no test. That is a classic first-timer
experience and it is implied by the parenthetical above.

**Fixtures** (https://docs.pytest.org/en/stable/how-to/fixtures.html, accessed 2026-09-12).
What they are for, verbatim:

> "starting from a clean state so it can provide consistent, repeatable results"
> — pytest docs, fixtures how-to

> "Test functions request fixtures they require by declaring them as arguments."
> — pytest docs, fixtures how-to

**`tmp_path`** (https://docs.pytest.org/en/stable/how-to/tmp_path.html, accessed 2026-09-12)
is the one fixture research code actually needs, because analysis code writes
files:

> "will provide a temporary directory unique to each test function"
> — pytest docs, tmp_path

It hands back a `pathlib.Path`. The docs state "These days, it is preferred to
use `tmp_path` and `tmp_path_factory`" over the older `tmpdir`. By default the
last 3 temporary directories are kept (configurable via
`tmp_path_retention_count` / `tmp_path_retention_policy`), which is a nice
detail — the test output is still there to inspect after a failure.

**`@pytest.mark.parametrize`**
(https://docs.pytest.org/en/stable/how-to/parametrize.html, accessed 2026-09-12):

> "enables parametrization of arguments for a test function"
> — pytest docs, parametrize

The canonical docs example, which is short enough to reproduce in the article:

```python
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

For research code this is how you test one function against several known
input/output pairs without copy-pasting the test body — the single most useful
pytest feature for someone with a table of expected values.

**`pytest.approx`** — from the reference docstring at
https://docs.pytest.org/en/stable/reference/reference.html (accessed 2026-09-12).
Signature `approx(expected, rel=None, abs=None, nan_ok=False)`. The defaults,
verbatim:

> "by default, `approx` considers numbers within a relative tolerance of `1e-6` … to be equal"
> — pytest docs, `approx` (trimmed)

> "also considers numbers within an absolute tolerance of `1e-12` of its expected value to be equal"
> — pytest docs, `approx`

And the combination rule, which people get wrong:

> "If you specify both `abs` and `rel`, the numbers will be considered equal if either tolerance is met"
> — pytest docs, `approx`

**So: `pytest.approx` default is rel 1e-6 OR abs 1e-12.** The absolute term
exists specifically so comparisons against `0.0` can pass at all — a pure
relative tolerance can never be satisfied against zero.

### 3.2 Numerical code: tolerance, and the seed problem

**`numpy.testing.assert_allclose`**, signature confirmed at
https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html
(accessed 2026-09-12):

```
assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True,
                err_msg='', verbose=True, *, strict=False)
```

**Defaults: `rtol=1e-7`, `atol=0`.** Pass condition, as stated in the docs:
`abs(actual - desired) <= atol + rtol * abs(desired)`.

**This is the detail the article should land, because it surprises people:**

| | relative | absolute |
|---|---|---|
| `pytest.approx` | 1e-6 | 1e-12 |
| `numpy.testing.assert_allclose` | 1e-7 | **0** |

`assert_allclose` gives you **no free pass near zero** unless you set `atol`
yourself. Two functions both called "close" disagree about what close means, and
one of them will fail on a value that should be zero. That is a concrete,
checkable, slightly embarrassing fact — exactly the register this audience
responds to.

**NumPy's own preference**, verbatim from
https://numpy.org/doc/stable/reference/routines.testing.html (accessed 2026-09-12),
under a section headed "Asserts (not recommended)":

> "It is recommended to use one of `assert_allclose`, `assert_array_almost_equal_nulp` or `assert_array_max_ulp` instead"
> — NumPy testing routines docs (trimmed)

`assert_array_almost_equal(actual, desired, decimal=6, ...)` compares to
`1.5 * 10**(-decimal)` — a non-standard tolerance definition, which is why NumPy
steers you off it.

**Seeds and the reproducibility guarantee — this is the genuinely important bit,
and it cuts against the obvious advice.**

Modern API: `rng = np.random.default_rng(seed)`. But from
https://numpy.org/doc/stable/reference/random/generator.html (accessed 2026-09-12):

> "`Generator` does not provide a version compatibility guarantee."
> — NumPy `Generator` docs

> "as better algorithms evolve the bit stream may change"
> — NumPy `Generator` docs

Whereas the legacy API is explicitly frozen, from
https://numpy.org/doc/stable/reference/random/legacy.html (accessed 2026-09-12):

> "RandomState is effectively frozen and will only receive updates that are required by changes in the internals of Numpy"
> — NumPy legacy RNG docs (trimmed)

> "using the same parameters will always produce the same results up to roundoff error"
> — NumPy legacy RNG docs (trimmed)

**The honest framing for the article:** `default_rng(seed)` is the right modern
default and gives you per-test isolation instead of a hidden global. But if your
"golden" baseline depends on an exact random stream surviving NumPy upgrades
forever, the *old* API is the one with the stronger written guarantee. That is
an uncomfortable, verifiable, non-obvious fact and it is exactly the kind of
thing this reader will check.

Sandve et al. 2013's Rule 6 says the same thing from the research side: "For
Analyses That Include Randomness, Note Underlying Random Seeds" (see §7.2).

### 3.3 Hypothesis (property-based testing) — mention, don't prescribe

**Current version: hypothesis 6.168.0**, uploaded 2026-09-08
(https://pypi.org/pypi/hypothesis/json, accessed 2026-09-12).

What it does, from https://hypothesis.readthedocs.io/ (accessed 2026-09-12):

> "let Hypothesis randomly choose which of those inputs to check"
> — Hypothesis docs (trimmed)

`hypothesis.extra.numpy` (installed as `hypothesis[numpy]`) ships strategies for
generating arrays, shapes and dtypes: `arrays()`, `array_shapes()`,
`from_dtype()`, `floating_dtypes()`, `broadcastable_shapes()`, `basic_indices()`.

**Adoption in scientific Python, verified by inspecting the actual repositories
on 2026-09-12 (not from claims about them):**

| Project | Uses Hypothesis? | Evidence |
|---|---|---|
| **NumPy** | Yes | first-party `numpy/testing/_private/hypothesis_helpers.py`; 28 files import it |
| **SciPy** | Yes | `scipy/conftest.py` registers two profiles — a `"nondeterministic"` CI profile and a `"deterministic"` one with `derandomize=True, database=None` |
| **xarray** | Yes | public `xarray/testing/strategies.py`, a whole `properties/` test directory, `slow_hypothesis` CI marker |
| **astropy** | Yes | `hypothesis>=6.84.0` pinned as a test dependency |
| **pandas** | **No** | `from hypothesis import` returns 0 results; no dependency in `pyproject.toml`. The text hits are prose about statistical hypotheses. |

SciPy's deterministic profile is the detail worth quoting in the article: the
most numerically serious project in the ecosystem deliberately *turns off* the
randomness in its property tests for end users, because a test that finds a new
failure on someone else's machine is not reproducible either.

**Verdict — say this plainly.** Every project above already had a mature pytest
suite before adding Hypothesis, and pandas, one of the most-used libraries in
the ecosystem, does not use it at all. For a researcher who has never written a
test, Hypothesis is over-engineering. Mention it as where the road goes, not as
step one.

### 3.4 The Turing Way on testing

Chapter: https://book.the-turing-way.org/reproducible-research/testing (accessed
2026-09-12). Two quotable lines:

> "Testing code thoroughly and frequently is vital to ensure reliable, reproducible research."
> — The Turing Way, Testing

> "You should write tests *because* you are short on time"
> — The Turing Way, Testing

That second one is the argument to make to this audience. It reframes testing as
a time-saver rather than a virtue.

On how much is enough — the line for a reader who is about to decide the whole
thing is too big to start:

> "Testing one tiny thing in a code that's thousands of lines long is infinitely better than testing nothing."
> — The Turing Way, testing guidance

And:

> "A thorough test suite will contain tests at all of these levels (though some levels will need very few)."
> — The Turing Way, testing overview

Its six named test types, each on its own subpage under
`/reproducible-research/testing/testing-*` (all accessed 2026-09-12):

| Type | The Turing Way's definition (trimmed, verbatim fragments) |
|---|---|
| **Smoke** | "a special kind of initial checks designed to ensure very basic functionality"; run first, "as a sanity check" |
| **Unit** | "the smallest testable part of any software", with dependencies "replaced with stub or mock implementations" |
| **Integration** | "individual units are combined and tested as a group"; exposes "faults in the interaction between integrated units" |
| **Acceptance** | whether software satisfies requirements "from the business or user's perspective" — the page itself notes these "may be unnecessary" for research software |
| **Regression** | "retesting after changes are made"; record expected outputs, then "compare the output from the code to the expected outputs, and raise an error if these do not match" |
| **Runtime** | "tests that run as part of the program itself" — inline assertions during execution |

**Note a terminology gap worth exploiting in the article:** The Turing Way's
regression page describes the golden-master mechanism precisely and **never uses
the words "characterisation test" or "golden master."** The software-engineering
literature and the research-software literature have separate names for the same
thing. That is a small, true, useful observation.

It does **not** prescribe an ordering of the six types.

### 3.5 The realistic minimum: characterisation / golden-master tests

This is the section that actually changes behaviour, and it should be the
article's concrete ask.

**The term.** Michael Feathers, *Working Effectively with Legacy Code* (2004),
coined "characterization test." **Source caveat: O'Reilly's page returned 403.
The definition below is Wikipedia's summary of Feathers' term
(https://en.wikipedia.org/wiki/Characterization_test, accessed 2026-09-12), not
Feathers' own words. Do not present it as a Feathers quote.**

> "a means to describe (characterize) the actual behavior of an existing piece of software"
> — Wikipedia, Characterization test (accessed 2026-09-12)

Also called **golden master testing**. The framing that makes it work for
research code:

> "traditional tests check that individual properties have certain values … whereas characterization testing checks that no properties have been changed"
> — Wikipedia, Characterization test (trimmed)

**Why this is the right first test for an analysis script.** You do not need to
know the right answer. You need to know that today's answer has not silently
changed. A researcher who has never written a test almost always *does* trust
today's output — that is exactly the precondition a characterisation test
requires and a unit test does not.

**The minimum viable version, no new dependencies:** run the analysis once,
commit the output (a small CSV, a `.npy` array, three summary statistics), and
write one test:

```python
def test_output_matches_baseline():
    result = run_analysis(DATA)
    expected = np.load("tests/baseline.npy")
    np.testing.assert_allclose(result, expected, rtol=1e-6)
```

Ten lines. Catches the refactor, the dependency upgrade, the off-by-one, the
changed default in a library. It does not catch "you were wrong all along" — and
the article should say so, because this reader will spot the gap immediately and
respect being told about it first.

**Two maintained pytest plugins that package the same idea** (both verified via
PyPI JSON + GitHub API on 2026-09-12):

| Plugin | Version | Released | Repo state 2026-09-12 |
|---|---|---|---|
| **`pytest-regressions`** | 2.11.0 | 2026-05-25 | `ESSS/pytest-regressions`, pushed 2026-08-25, 220 stars, 19 open issues, not archived |
| **`syrupy`** | 6.0.0 | 2026-08-22 | `syrupy-project/syrupy`, pushed **2026-09-11**, 881 stars, 8 open issues, not archived |

`pytest-regressions` is the better fit for research: its fixtures are
`data_regression`, `file_regression`, `image_regression`, **`num_regression`**
and **`dataframe_regression`** — the last two aimed squarely at numeric and
tabular output. First run writes the baseline; later runs diff against it;
`--force-regen` re-baselines deliberately. `syrupy` is the general snapshot
tool (`assert actual == snapshot`, `--snapshot-update`), zero-dependency, and
fails on a *missing* snapshot rather than silently creating one.

**JOSS sets the bar usefully low**, from
https://joss.readthedocs.io/en/latest/review_criteria.html (accessed 2026-09-12).
"Good" is an automated suite wired to CI; **"OK" is merely "documented manual
steps that can be followed to objectively check the expected functionality."**
The only unacceptable state is no objective way for a reviewer to check at all.
That is a permission slip worth quoting to a reluctant reader.

**Software Carpentry's cheaper entry point still** — assertions inline, before
any test file exists
(https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html,
accessed 2026-09-12): "Add assertions to our code so that it checks itself as it
runs", split into preconditions, postconditions and invariants. Also the maxim
that when you find a bug, turn it into a test.

---

## 4. Share — what goes in git and what does not

### 4.1 GitHub's actual numbers, verified at the source of truth

**These were checked twice: once against the rendered docs, and once against the
raw Markdown and YAML in `github/docs` — so the numbers below are the values
GitHub's own build substitutes into the page.** Accessed 2026-09-12.

**From `data/variables/large_files.yml`**
(https://raw.githubusercontent.com/github/docs/main/data/variables/large_files.yml):

| Variable | Value |
|---|---|
| `warning_size` | **50 MiB** |
| `max_github_size` | **100 MiB** |
| `max_github_browser_size` | **25 MiB** |
| LFS included bandwidth & storage, Free / Pro | **10 GiB each, per month** |
| LFS included bandwidth & storage, Team / Enterprise | **250 GiB each, per month** |

**From `about-large-files-on-github.md`**
(https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github):

> "If you attempt to add or update a file that is larger than 50 MiB, you will receive a warning from Git."
> — GitHub Docs (the push still succeeds)

> "GitHub blocks files larger than 100 MiB."
> — GitHub Docs

> "We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended."
> — GitHub Docs (17 words — trim)

Web-UI uploads are capped at **25 MiB**.

**From `repository-limits.md`**
(https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits),
verified against the raw source:

| Limit | Recommended maximum | Enforced |
|---|---|---|
| **On-disk size** (the `.git` folder) | **10 GB** | — |
| Directory width (entries in one directory) | 3,000 | — |
| Directory depth | 50 | — |
| Number of branches | 5,000 | — |
| **Push size** | — | **2 GB** |
| **Single object size** | **1 MB** | **100 MB** |
| Git read operations | 15 per second per repo | — |
| Push rate | 6 per minute per repo | — |

> "Push size: This limit is enforced at 2GB."
> — GitHub Docs, repository limits

> "The recommended maximum limit is 1MB. … This is enforced at 100 MB."
> — GitHub Docs, single object size

**⚠️ GitHub's two pages disagree with each other, and the article can use this.**
`about-large-files-on-github` says "ideally less than 1 GB … less than 5 GB is
strongly recommended"; `repository-limits` gives an on-disk recommendation of
**10 GB**. Both are current on 2026-09-12. **State which page you are citing.**
Also note **the recommended single-object size is 1 MB** — two orders of
magnitude below the enforced 100 MiB block. Almost nobody knows that number, and
it makes the argument better than the 100 MB one does: *GitHub would prefer your
individual files were under a megabyte.*

**Why git is bad at this, mechanically.** Git stores each version of a tracked
file as a complete blob, not a diff. Delta and zlib compression, which work well
on text, do very little on already-compressed binaries — Parquet, PNG, model
weights. And `git clone` fetches the whole object history by default, so a 2 GB
CSV added once and deleted three commits later still costs every future clone,
forever, unless the history is rewritten. GitHub's own framing: "Smaller
repositories are faster to clone and easier to work with and maintain."
(**The mechanism paragraph is synthesis, not a quotation. The quoted clause is
from GitHub Docs.**)

GitHub recommends `git filter-repo` for removing files already in history, and
points at [`github/git-sizer`](https://github.com/github/git-sizer) for analysis.

### 4.2 Git LFS

https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
and https://git-lfs.com (both accessed 2026-09-12).

**What it does:** LFS "replaces large files such as audio samples, videos,
datasets, and graphics with text pointers inside Git, while storing the file
contents on a remote server" (git-lfs.com). The tracked file becomes a small
pointer recording a version, an `oid` and a size; the bytes live elsewhere and
are fetched on checkout. Configured via `git lfs track` and `.gitattributes`.

**Maximum file size, by plan** (verbatim table from GitHub Docs):

| Product | Maximum file size |
|---|---|
| GitHub Free | 2 GB |
| GitHub Pro | 2 GB |
| GitHub Team | 4 GB |
| GitHub Enterprise Cloud | 5 GB |

Quotas: 10 GiB bandwidth and 10 GiB storage per month on Free and Pro; 250 GiB
each on Team and Enterprise Cloud. Pre-paid data packs have been replaced by
metered billing — "Bandwidth is billed for each GiB of data downloaded. Storage
is billed by calculating an hourly usage rate." **No per-GiB price was stated on
the page fetched; do not print one.**

**The downsides, from GitHub's own notes rather than from critics:**

> "Git LFS cannot be used with GitHub Pages sites."
> — GitHub Docs

> "Git LFS cannot be used with template repositories."
> — GitHub Docs

And the one that actually bites a researcher: whether LFS objects are included in
source-archive downloads (the "Download ZIP" button, `git archive`) is a separate
setting. **A reader can download your repo as a zip and silently get pointer
files instead of data.** That is a reproducibility failure with a friendly UI.

Note also that git-lfs.com itself discusses **no** costs or limitations — it is
marketing copy. Cite it for mechanism only.

### 4.3 DVC, and the simpler things people actually use

**DVC** — https://doc.dvc.org/ (`dvc.org/doc` redirects there), accessed
2026-09-12. Tagline: *"Git for data scientists — manage your code and data
together."* Current PyPI version **3.67.1** (https://pypi.org/pypi/dvc/json;
**the release date for that version was not captured — do not print one**).
GitHub `iterative/dvc`: last push **2026-09-07**, **15,867 stars**, not archived
— actively maintained.

**How it differs from LFS.** LFS is coupled to your git *host* and does one
thing: swap big blobs for pointers. DVC is storage-backend agnostic (S3, Azure
Blob, GCS, Google Drive, SSH/SFTP, HDFS, plain HTTP) and layers a pipeline DAG
(`dvc.yaml`) and experiment tracking (`dvc exp`) on top of the same pointer idea.
It is less an LFS alternative than a light MLOps layer that solves the LFS
problem as a side effect.

**Honest assessment (editorial, not quoted):** for one researcher with one
dataset and one analysis script, DVC is more moving parts than the problem
justifies — a `.dvc` file per artefact, a configured remote, and `dvc pull`/`dvc
push` added to everyone's workflow. Recommend it when there are pipeline stages
and experiments to compare, not when there is a CSV.

**The three lighter options, in ascending order of effort:**

1. **Don't. Commit the small file.** If the data is a few hundred kilobytes — and
   for a teaching example it should be — put it in the repo. Every limit above
   is irrelevant. This is what the article's worked example should do.
2. **Host the data, reference it by DOI, verify a checksum.** Put the dataset in
   Zenodo (§5), keep only the DOI and a SHA256 in the repo, and fetch at run
   time. Zenodo accepts "up to 50GB per record with a maximum of 100 files,"
   with a one-time increase "of up to 200GB for a single record" on request
   (https://support.zenodo.org/help/en-gb/1-upload-deposit/80-what-are-the-size-limitations-of-zenodo,
   accessed 2026-09-12).
3. **`pooch`** — https://www.fatiando.org/pooch/, accessed 2026-09-12. "a Python
   library that can manage data by downloading files from a server (only when
   needed) and storing them locally in a data cache", verifying registered
   checksums. Version **1.9.0**, released **2026-01-30**
   (https://pypi.org/pypi/pooch/json); GitHub last push **2026-09-09**, 737
   stars — actively maintained, and used across the Fatiando/PyData geoscience
   stack. This is option 2, packaged.

### 4.4 Should notebook outputs be committed?

**`nbstripout`** — https://github.com/kynan/nbstripout, accessed 2026-09-12.
Does one thing: "Strips outputs from Jupyter and IPython notebooks." Version
**0.9.1**, released **2026-02-21**; GitHub last push **2026-04-11**, 1,481 stars,
10 open issues, not archived — maintained, low-drama.

**The mechanism matters and is often misunderstood.** `nbstripout --install`
registers a git **`clean` filter** in `.git/config` and `.gitattributes`. Outputs
are stripped *on the way into git*. Your working copy on disk keeps its outputs.
You go on seeing your plots; git only ever stores code and markdown.

**The case FOR stripping:** every re-run changes execution counts and can embed
base64 image blobs, so two runs of identical code produce a large unreviewable
diff. Stripped notebooks diff like source. This connects to Rule et al.'s
complaint about "abstruse JSON metadata" (§1.6).

**The case AGAINST stripping:** outputs are the only visible evidence, on
GitHub's own notebook renderer, that a cell ran and produced the numbers claimed.
A stripped notebook viewed on github.com shows no plots, no printed values,
nothing — a real cost for a reader who lands on the repo and will not clone it.

**⚠️ Confidence note: the AGAINST case above is reasoned, not quoted.** No single
canonical source stating it cleanly was reachable this session (reddit is blocked
to the fetcher; two guessed blog URLs 404'd). **Present it as an argument, not as
a citation.** Also: **JOSS's review criteria do not mention notebooks or notebook
outputs at all** (https://joss.readthedocs.io/en/latest/review_criteria.html,
checked 2026-09-12). Do not claim JOSS requires visible outputs.

**The middle path is `nbdime`** — https://nbdime.readthedocs.io/, accessed
2026-09-12. A structure-aware diff and merge tool for notebooks: `nbdiff`,
`nbdiff-web`, plus a merge driver. It makes "intelligent decisions when diffing
and merging notebooks, such as: eliding base64-encoded images for terminal
output, using existing diff tools for inputs and outputs, rendering image diffs
in a web view, auto-resolving conflicts on generated values such as execution
counters." Installed as git's driver for `.ipynb` with
`nbdime config-git --enable --global`.

**That nbdime exists, and specifically handles output diffing and
execution-counter conflicts, is itself the evidence that "keep the outputs,
fix the diff tool" is a real position in the ecosystem — not a strawman.** Three
live answers, not two: strip (`nbstripout`), pair with text (`jupytext`, §2.4),
or teach git to read notebooks (`nbdime`). The article should present all three
and pick.

### 4.5 What should be committed

**`.gitignore` first.** The canonical
https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
(accessed 2026-09-12) excludes byte-compiled files (`__pycache__/`, `*.pyc`),
build and dist artefacts, virtual environments (`.venv/`, `venv/`), `.env`,
**`.ipynb_checkpoints`**, test and coverage caches, IDE settings, Sphinx build
output and type-checker caches.

**A distinction worth making explicitly in the article:** the template does
**not** exclude `.ipynb` files, and says nothing about notebook *output content*.
`.gitignore` keeps build junk out of the repo; `nbstripout`/`nbdime`/`jupytext`
govern what lives *inside* a tracked file. Different problems, different tools,
often conflated.

Cookiecutter Data Science goes further and puts **`data/` in `.gitignore` by
default** (§2.2).

**The positive list.** No single authoritative "minimum reproducible repo"
checklist was retrievable this session. **Present the list as consensus across
the sources in §7, not as a quotation.** The strongest citable anchors are
Wilson et al. 2017's Project Organization and Software rules (§7.3), Pimentel
et al.'s best practices 4, 5, 7 and 8 (§1.1), and Sandve et al.'s Rules 1, 2, 4
and 6 (§7.3). The list itself is in §7.5.

---

## 5. Archiving and citation — the persistent-identifier stage

### 5.1 The GitHub–Zenodo integration

All from Zenodo's own help docs and GitHub's docs, accessed 2026-09-12:
https://help.zenodo.org/docs/github/enable-repository/,
https://help.zenodo.org/docs/github/archive-software/github-upload/,
https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content

**The flow, step by step:**

1. Link accounts — "Click the profile menu in the header and click **GitHub**," then "Click **Sync now**."
2. Enable the repo — "Find a repository you wish to enable, then toggle the slider to connect it to Zenodo." Zenodo manages the GitHub webhook itself; you do not configure one.
3. Once enabled, "new releases from the repository will be automatically ingested and archived."
4. Cut a GitHub Release as normal.
5. Zenodo ingests the release tarball: "This could take some time, depending on the size of the release file and the load of Zenodo at that time."
6. A DOI is minted on the resulting Zenodo record. Archival status appears on the record under "External resources > Archived in".

GitHub's own page states the same thing from its side:

> "Zenodo archives your repository and issues a new DOI each time you create a new GitHub release"
> — GitHub Docs, referencing and citing content (16 words — trim)

GitHub also notes that "Zenodo can only access public repositories" and
recommends including a licence "so readers know how they can reuse your work."

**Two 2024–2026 notes worth getting right:**

- **Zenodo now pushes software records into Software Heritage as part of the same pipeline.** Its GitHub-integration docs state that "software records are archived in Software Heritage." So one GitHub release, run through Zenodo, lands in **two** archives. This reflects Zenodo's platform rebuild onto InvenioRDM ("Zenodo RDM"). **Confidence: the current-state statement was read on help.zenodo.org 2026-09-12; no page narrating the rebuild's history was located. Do not date the rebuild.**
- **GitHub's own docs have not caught up.** The GitHub "referencing and citing content" page mentions Zenodo and Figshare but **not** Software Heritage. A small, checkable discrepancy — good for one honest sentence.

### 5.2 Concept DOI versus version DOI

Zenodo's own terminology, verbatim from
https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning
(read in full, accessed 2026-09-12):

> "'Version DOIs' denote individual releases, while 'Concept DOIs' represent the entire collection and underlying concept."
> — Zenodo support (16 words — trim to the two clauses separately)

**Zenodo's own worked example**, which is the clearest possible illustration and
should go in the article as-is — two releases produce **three** DOIs:

| | DOI |
|---|---|
| v1.0 (version DOI) | `10.5281/zenodo.60943` |
| v1.1 (version DOI) | `10.5281/zenodo.800648` |
| Concept (all versions) | `10.5281/zenodo.705645` |

**⚠️ On "does the concept DOI always resolve to the latest version?" — be
careful.** The versioning article does not state a resolution *rule* in the text
retrieved. Zenodo's citations FAQ
(https://support.zenodo.org/help/en-gb/25-citations/234-how-to-share-or-cite-a-zenodo-record,
accessed 2026-09-12) instead instructs readers who want to cite the current
release to "replace the default DOI in the citation … by a concept DOI." **So
the honest phrasing is: Zenodo's own guidance treats the concept DOI as the
version-independent citation target. Do not write "it always redirects to the
latest version" as though Zenodo said so.**

The article's practical rule: **cite the version DOI in a paper (it is what you
actually ran); put the concept DOI in the README (it is what the reader should
follow).**

### 5.3 `CITATION.cff`

https://citation-file-format.github.io/ and the raw schema at
https://raw.githubusercontent.com/citation-file-format/citation-file-format/main/schema.json
(both accessed 2026-09-12).

**Current schema version: `1.2.0`** — confirmed two ways: the site's own example
uses `cff-version: 1.2.0`, and the raw JSON schema's `cff-version` field pattern
requires exactly the string `"1.2.0"`. **This is verified, not assumed.**

> "CITATION.cff files are plain text files with human- and machine-readable citation information"
> — Citation File Format (trimmed)

**What GitHub does with it:**

> "it is automatically linked from the repository landing page, and the citation information is rendered on the repository page"
> — Citation File Format (trimmed)

That is the **"Cite this repository"** button, which GitHub renders as APA and
BibTeX from the CFF fields.

**Does Zenodo read it? Yes — and this answers the question directly:**

> "Zenodo will use the citation information you've provided to populate the publication entry!"
> — Citation File Format (on making a release via the Zenodo–GitHub integration)

So `CITATION.cff` is not a GitHub-UI-only ornament: it is the metadata source for
the archived record. That is a good reason to add it *before* the first release.

**Minimal fields** (from the site's own example): `cff-version`, `message`,
`authors` (`family-names`, `given-names`, optional `orcid`), `title`, `version`,
`date-released`, and `identifiers` (a `type` + `value` pair for a DOI).

**Tooling:** `cffinit` (https://github.com/citation-file-format/cffinit) is a web
initialiser that generates a valid file interactively. `cffconvert` (PyPI package
`cffconvert`, repo `citation-file-format/cff-converter-python`) is a "Command
line program to validate and convert CITATION.cff files" to BibTeX, CodeMeta,
EndNote, RIS, schema.org JSON and Zenodo JSON. **No version or release date was
captured for `cffconvert`; the repo shows ongoing CI activity. Do not print a
version.**

### 5.4 Software Heritage

**SWHID format — verified** from https://docs.softwareheritage.org (persistent
identifiers page, accessed 2026-09-12):

```
swh:1:<object_type>:<object_id>[;qualifiers]
```

Prefix `swh:1:`, one of five object types, then a 40-hex-character SHA1. The five
types:

| Type | Object |
|---|---|
| `cnt` | file content |
| `dir` | directory tree |
| `rev` | a commit — the SHA1 matches the underlying git commit hash |
| `rel` | a tag/release — matches the git tag object hash |
| `snp` | a full repository snapshot at a point in time |

Example: `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.

**⚠️ `softwareheritage.org` itself returned repeated TLS certificate errors to
the fetcher on 2026-09-12 ("unable to get local issuer certificate"), across
three attempts. Its mission-statement wording was NOT read. Quote only the
SWHID spec, which came from `docs.softwareheritage.org`.**

**Complement, not alternative.** The distinction to draw:

| | Software Heritage | Zenodo |
|---|---|---|
| Trigger | continuous crawl of public forges; no release needed | deposit on release |
| Identifier | SWHID, content-addressed from git's own hashes | DOI |
| Answers | "did this exact byte sequence ever exist publicly?" | "how do I cite this release?" |
| Metadata | minimal, structural | curated, authored, with a landing page |

**And the practical 2026 answer:** since Zenodo's GitHub pipeline now also pushes
into Software Heritage (§5.1), enabling the Zenodo integration already gets you
both. Software Heritage rides along; it is not a separate step to configure.
*(This inference rests on the Zenodo docs statement in §5.1.)*

### 5.5 FAIR4RS — FAIR Principles for Research Software

**There are two citable objects, and the article should distinguish them.**

1. **The RDA Recommendation — canonical.** "FAIR Principles for Research Software (FAIR4RS Principles)", v1.0, Research Data Alliance. **DOI [10.15497/RDA00068](https://doi.org/10.15497/RDA00068)**. Lead authors, marked as equal contributors: **Neil P. Chue Hong, Daniel S. Katz, Michelle Barker**, then Anna-Lena Lamprecht, Carlos Martinez, Fotis E. Psomopoulos, Jen Harrow, Leyla Jael Castro, Morane Gruenpeter, Paula Andrea Martinez, Tom Honeyman, "and the FAIR4RS WG" (~70 contributors, credited by contribution, not alphabetically). **Two dates appear in the document itself** — the version-history table gives v1.0 as **15 March 2022**; the cover page says "Published: 24th May 2022". Report both or neither; do not pick one silently.
2. **The peer-reviewed companion.** Chue Hong et al., "Introducing the FAIR Principles for research software", *Scientific Data* **9**, article **622** (2022), **DOI [10.1038/s41597-022-01710-x](https://doi.org/10.1038/s41597-022-01710-x)**, published **14 October 2022** — confirmed via the Crossref API (https://api.crossref.org/works/10.1038/s41597-022-01710-x, accessed 2026-09-12).

**The principles, verbatim from Table 1 of the RDA PDF** (read directly,
2026-09-12):

**F — Findable.** "Software, and its associated metadata, is easy for both humans and machines to find."
- F1. Software is assigned a globally unique and persistent identifier.
  - F1.1. Components of the software representing levels of granularity are assigned distinct identifiers.
  - F1.2. Different versions of the software are assigned distinct identifiers.
- F2. Software is described with rich metadata.
- F3. Metadata clearly and explicitly include the identifier of the software they describe.
- F4. Metadata are FAIR, searchable and indexable.

**A — Accessible.** "Software, and its metadata, is retrievable via standardized protocols."
- A1. Software is retrievable by its identifier using a standardized communications protocol.
  - A1.1. The protocol is open, free, and universally implementable.
  - A1.2. The protocol allows for an authentication and authorization procedure, where necessary.
- A2. Metadata are accessible, even when the software is no longer available.

**I — Interoperable.** "Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards."
- I1. Software reads, writes and exchanges data in a way that meets domain-relevant community standards.
- I2. Software includes qualified references to other objects.

**R — Reusable.** "Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)."
- R1. Software is described with a plurality of accurate and relevant attributes.
  - R1.1. Software is given a clear and accessible license.
  - R1.2. Software is associated with detailed provenance.
- R2. Software includes qualified references to other software.
- R3. Software meets domain-relevant community standards.

**How software-FAIR differs from data-FAIR — in the document's own words:**

> "such as its executability, composite nature, and continuous evolution and versioning"
> — FAIR4RS, on the characteristics requiring revision of the principles

Three concrete adaptations worth a paragraph each:
- **Interoperability is deliberately narrowed.** Unlike data, where "two pieces of data combine to form new data", almost all software "is integrated with, or depends on, other software." That dependency relationship is placed under **Reusability (R2)**, not Interoperability. `I` is reserved for independently executable software exchanging data or APIs.
- **Accessible means retrievable.** The document explicitly notes the disability-accessibility sense of the word does not map, and pushes that concern into R3 and separate guidance.
- **F1.1 and F1.2 exist because software has granularity and versions.** A library versus a function within it; v1.0 versus v1.1. Flat datasets rarely pose those identity questions as sharply. **This is the direct justification for the concept-DOI/version-DOI distinction in §5.2** — F1.2 is exactly why Zenodo mints both.

**Its scope definition**, useful for a reader who is not sure the term applies to
them: "Research Software includes source code files, algorithms, scripts,
computational workflows and executables that were created during the research
process or for a research purpose" — explicitly **excluding** general-purpose
tools and libraries used but not created for the research (citing Gruenpeter et
al., 2021, within the document).

### 5.6 Funder and journal requirements — the weakest section; verify before publishing

**⚠️ Read this warning first.** Most `.gov` domains (whitehouse.gov,
grants.nih.gov, osp.od.nih.gov, sharing.nih.gov, federalregister.gov) returned
403 or 404 to the fetcher throughout 2026-09-12, and nature.com and science.org
bounced every attempt into a login wall. **Several widely known dates could not
be confirmed from any reachable source. They are marked. Do not publish an
unverified date.**

**Verified:**

- **PLOS code-sharing policy** — https://journals.plos.org/plosone/s/materials-software-and-code-sharing, read in full 2026-09-12. This is the strongest verified journal policy available, and PLOS is the right journal to cite anyway given §7.3.

  > "we expect all researchers with submissions to PLOS in which author-generated code underpins the findings … to make all author-generated code available"
  > — PLOS (heavily trimmed; the full sentence continues "without restrictions upon publication of the work")

  PLOS may "require the code to be made available as a condition of publication" when it is central; expects code to be "reusable and well documented"; recommends "a repository that issues persistent identifiers, such as DOIs" with "an open source license"; and requires a code-availability statement, or an explanation plus a route for editors and reviewers if access is restricted.

- **Horizon Europe** — https://rea.ec.europa.eu/open-science_en, accessed 2026-09-12. Beneficiaries "must create and keep an updated Data Management Plan (DMP)"; must deposit data in a trusted repository "as 'soon as possible'"; the governing principle is **"as open as possible, as closed as necessary"**; and "The research data of EU-funded projects must be FAIR". **Caveat: this page covers research *data*. It contained no explicit contractual language extending the obligation to software in the same terms. Do not claim Horizon Europe mandates code sharing on the strength of this page.**

- **cOAlition S / Plan S** — https://www.coalition-s.org/, accessed 2026-09-12. Launched September 2018; "from 2021, scientific publications that result from research funded by public grants must be published in compliant Open Access journals or platforms". Publications-focused, not data or code. **2026 status confirmed live:** new Director Curt Rice (May 2026), OPERAS as new Host Secretariat (May 2026), a "Bengaluru Roadmap and Action Plan on Diamond Open Access" (May 2026), a 2026 Annual Review (June 2026), and a new 2026–2030 strategy adopted. Active and evolving.

- **OSTP "Nelson memo" issue date** — 25 August 2022. Confirmed only via https://en.wikipedia.org/wiki/Office_of_Science_and_Technology_Policy (accessed 2026-09-12): "On August 25, 2022, OSTP issued guidance to make all federally funded research in the United States freely available without delay". **Secondary source. Primary sources were unreachable.**

**NOT verified — do not state these:**

- **The Nelson memo's implementation deadline.** Commonly cited as agency policies taking effect by end of 2025. **Unconfirmed. Blocked from OSTP and Federal Register all session.**
- **The NIH Data Management and Sharing Policy's effective date** (commonly cited as 25 January 2023) **and its in-force status in 2026.** Every NIH domain returned 403 or a deprecated-page notice. **Completely unverified this session.** If the article needs it, someone must check `sharing.nih.gov` by hand.
- **Nature's and Science's current code-availability wording.** Both blocked. Both are known in general terms to require a Code Availability statement, but **no 2026 wording was fetched.** Do not quote either.
- **Whether Horizon Europe's FAIR/DMP mandate extends to software** as firmly as to data. Unconfirmed.

**Editorial recommendation:** the funder/journal material is the thinnest in this
note and the most likely to date badly. Use **PLOS** as the worked example
(verified, quotable, and the same publisher as Wilson et al., Sandve et al. and
Noble in §7.3), mention that funders increasingly require data management plans
without enumerating specific deadlines, and leave the rest out. The article does
not need it, and the cost of getting a policy date wrong in front of this
audience is high.

---

## 6. The Turing Way

**Cite `book.the-turing-way.org`.** `the-turing-way.netlify.app` 301-redirects
there. (Already recorded in `tooling.md`; repeating because it bites.)

**What it is.** Self-described on its GitHub repo as "a handbook to reproducible,
ethical and collaborative data science"
(https://github.com/the-turing-way/the-turing-way, accessed 2026-09-12); the repo
description reads "an open source community-driven guide to reproducible,
ethical, inclusive and collaborative data science." 576 listed contributors.
Governed by a Steering Committee and Working Groups (`the-turing-way/governance`,
last updated 2026-09-09). Strongly associated with the Alan Turing Institute,
though the book frames itself as community-authored rather than institute-authored.

**Is it still alive in 2026? Yes — verified, not assumed.** GitHub API on
2026-09-12 shows `pushed_at` = 2026-09-12 (same day), with 119 open PRs and 489
open issues. Latest tagged release **v1.2.3, 14 April 2025**
(https://github.com/the-turing-way/the-turing-way/releases). Version history runs
back to v1.0.0 on 2020-11-09.

**Zenodo concept DOI: `10.5281/zenodo.3233853`** (badge on the repo README,
accessed 2026-09-12). **A version-specific DOI for v1.2.3 was not verified — do
not print one.**

### 6.1 Reproducible research overview and the definitions matrix

https://book.the-turing-way.org/reproducible-research/overview (accessed 2026-09-12)

> "Scientific results and evidence are strengthened if those results can be replicated and confirmed by several independent researchers"
> — The Turing Way, Reproducible Research overview (21 words — trim)

**The 2×2**, from `/overview/overview-definitions` (accessed 2026-09-12). Axes
are **same/different data** × **same/different analysis**:

| | Same data | Different data |
|---|---|---|
| **Same analysis** | **Reproducible** | **Replicable** |
| **Different analysis** | **Robust** | **Generalisable** |

Definitions, verbatim (trimmed to under 15 words each):

> "same analysis steps performed on the same dataset consistently produces the same answer"
> — The Turing Way, Reproducible (13 words)

> "same analysis performed on different datasets produces qualitatively similar answers"
> — The Turing Way, Replicable (10 words)

> "same dataset is subjected to different analysis workflows to answer the same research question"
> — The Turing Way, Robust (14 words)

> "Combining replicable and robust findings allow us to form generalisable results"
> — The Turing Way, Generalisable (11 words)

**This matrix is the article's best framing device.** The article is *only* about
the top-left cell, and saying so early earns credibility with a reader who is
tired of "reproducibility crisis" prose that conflates all four.

**Note a URL correction:** there is no `overview-why` or `overview-motivation`
page (the latter returns a confirmed 404). The "why it matters" material lives at
`/overview/overview-benefit`. Subpages that do exist: `overview-definitions`,
`overview-benefit`, `overview-barriers`, `overview-resources`.

From `/overview/overview-benefit` (**snippet-level, quote with care**):

> "Working reproducibly, we can develop validated research work, avoid misinformation"
> — The Turing Way, overview-benefit

The page also mentions "10–40% reproducibility rates" in some fields. **This is
page-reported, and the underlying citation was not traced. Do not use this
number — §1 has better-sourced figures.**

### 6.2 Code quality and testing

https://book.the-turing-way.org/reproducible-research/code-quality (accessed 2026-09-12)

> "Static code analysis is a method that examines code and detects software vulnerabilities before your code is executed."
> — The Turing Way, Code Quality (18 words — trim)

Subpages: Code Style and Formatting; Writing Robust Code; File and Variable
Naming; Code Readability; Style and Formatting Tools; Checklist and Resources.
Includes a linter table by language.

Testing quotes are in §3.4 above. The two that carry the article:

> "You should write tests *because* you are short on time"
> — The Turing Way, Testing

> "Testing one tiny thing in a code that's thousands of lines long is infinitely better than testing nothing."
> — The Turing Way, testing guidance (19 words — trim, e.g. "infinitely better than testing nothing")

### 6.3 Version control

https://book.the-turing-way.org/reproducible-research/vcs (accessed 2026-09-12)

> "Version control is an approach to record changes made in a file or set of files over time"
> — The Turing Way, Version Control (18 words — trim)

> "changes made by different people can be tracked and often automatically combined"
> — The Turing Way, Version Control (12 words)

Confirmed subpage slugs: `/vcs/vcs-workflow`, `/vcs/vcs-workflow-branches`,
`/vcs/vcs-git-general`, `/vcs/vcs-git-in-research`, `/vcs/vcs-git`,
**`/vcs/vcs-data`**, `/vcs/vcs-personal-stories`, `/vcs/vcs-checklist`,
`/vcs/vcs-resources`.

**`vcs-data` is the one to pull for §4** (data under version control) — it was
not read in full in this pass. Flagged as a gap.

**There is no standalone "commit messages" page** — that guidance sits inside
`vcs-workflow` or `vcs-git-in-research`. Not verified at subpage level.

### 6.4 Research data management

https://book.the-turing-way.org/reproducible-research/rdm (accessed 2026-09-12)

> "Managing your data allows you to always find your data and ensure the quality of scientific practice."
> — The Turing Way, RDM (17 words — trim)

> "FAIR (Findable, Accessible, Interoperable and Reusable)"
> — The Turing Way, RDM

21 confirmed subpages: `rdm-data`, `rdm-find`, `rdm-dmp`, `rdm-smp`, `rdm-fair`,
`rdm-care`, `rdm-personal`, `rdm-storage`, `rdm-spreadsheets`, `rdm-metadata`,
**`rdm-pid`** (persistent identifiers — relevant to §5), `rdm-methods`,
`rdm-elns`, `rdm-cleaning`, `rdm-data-curation`, `rdm-visualisation`,
`rdm-repository`, `rdm-sharing`, `rdm-article`, `rdm-checklist`, `rdm-stories`,
`rdm-resources`. **There is no standalone "file naming" page** — that material
sits inside `rdm-metadata`/`rdm-storage`.

`rdm-metadata` (read in full, 2026-09-12) is the README guidance: use a plain
text `README.txt` or `README.md`, or PDF "when text formatting is important";
give "context for your work" so that "collaborators, colleagues and future you"
can understand it. It points at the Cornell and 4TU.ResearchData README
templates.

### 6.5 Other chapters worth knowing

- **Licensing** — https://book.the-turing-way.org/reproducible-research/licensing (read in full). "A license is a legal agreement between the creator or owner of a resource and its users." And, disarmingly: "Good legal advice is timely, specific, and given by an expert; this chapter is none of these." Recommends a plain-text `LICENSE` at the project root using SPDX identifiers, and mentions FSFE's REUSE tool.
- **Open research** — https://book.the-turing-way.org/reproducible-research/open (read in full). Covers Open Data / Open Source / Open Hardware / Open Access / Open Notebooks. **It does not address "making code citable" as its own topic** — for that, see Wilson et al.'s Collaboration rule "Make the project citable" (§7.2) and §5.
- **Reproducible environments** — `/reproducible-research/reproducible-environments` returns a **confirmed 404**. The correct slug was not chased (out of scope).

### 6.6 The Turing Way's own project template — and a nice piece of self-inflicted evidence

https://github.com/the-turing-way/reproducible-project-template (GitHub API,
accessed 2026-09-12): `is_template: true`, 45 stars, 14 forks, licence "Other"
(see `LICENSE.md`), last code push 2025-03-19.

Root listing, verbatim via `gh api`:

```
.all-contributorsrc  .github  .gitignore  CHANGES.md  CODE_OF_CONDUCT.md
CONTRIBUTING.md  LICENSE.md  README.md  assets  data  models
project-management  src
```

`src/` contains `data`, `models`, `visualisation`. `data/` contains `processed`,
`raw`. The README prescribes a skeleton: Project Quick Start / Vision and
Mission / About / Roadmap & Milestones / The Team / Contributing / Licensing /
Citing & Acknowledgement.

**The self-inflicted evidence:** that template's README still links to
`https://the-turing-way.netlify.app/project-design/project-repo/project-repo-readme.html`,
and the live-domain equivalents (`/project-design/project-repo` and
`/project-design/project-repo/project-repo-readme`) both **404** as of
2026-09-12. The Turing Way's own official template points at a dead page.
**This is an excellent, concrete, non-snarky illustration for the article: link
rot is a reproducibility failure too, and it happens to the people who write the
handbook.**

---

## 7. A concrete minimal example — what a good one contains

The author writes the example. This section records what real templates include
and what reviewers actually check.

### 7.1 The templates people actually recommend

| Template | URL | State on 2026-09-12 |
|---|---|---|
| **Cookiecutter Data Science v2** | https://cookiecutter-data-science.drivendata.org/ | 10,050 stars, v2.3.0 (2025-07-24), pushed 2026-08-07. See §2.2 for the full tree. |
| **The Turing Way reproducible-project-template** | https://github.com/the-turing-way/reproducible-project-template | 45 stars, template repo, pushed 2025-03-19. See §6.6. |
| **scientific-python/cookie** | https://github.com/scientific-python/cookie | "Scientific Python Library Development Guide and Cookiecutter", 411 stars, 80 forks, BSD-3-Clause, pushed **2026-09-11**. Guide at https://learn.scientific-python.org/development |
| **pyOpenSci/pyos-package-template** | https://github.com/pyOpenSci/pyos-package-template | 30 stars, Copier-based (`copier copy gh:pyopensci/pyos-package-template .`), pushed 2026-04-07 |

The pyOpenSci template's root listing, verbatim: `.editorconfig`, `.github`,
`.gitignore`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`,
`DEVELOPMENT.md`, `LICENSE`, `README.md`, `copier.yml`, `includes`,
`pyproject.toml`, `template`, `tests`.

**Finding worth stating plainly: the space is fragmented.** A direct GitHub
search for "reproducible research template" style repos turned up mostly
single-digit-star personal projects. Beyond the four above there is no dominant
canonical minimal-repo template. That is itself a reason for the article to
build one.

### 7.2 The Good Research Code Handbook (Patrick Mineault)

https://goodresearch.dev/ (accessed 2026-09-12). Confirmed chapter list:
Roadmap; Brains & coding; **Set up your project** (`/setup`); **Keep things
tidy** (`/tidy`); Write decoupled code (`/decoupled`); Test your code
(`/testing`); Document your code (`/docs`); **Document your project**
(`/pipelines`); Make it social (`/social`); **A sample project: Zipf's law**
(`/zipf`).

From `/setup` (fetched 2026-09-12):
- **"One project = one paper = one folder = one git repository"** — the single most quotable line in the handbook for this article.
- Commit "a few times a day to a few times per week."
- Make the project pip-installable and use `pip install -e .`.
- Recommended folders: `data`, `docs`, `results`, `scripts`, `src`, `tests`, plus `.gitignore`, `README.md`, `environment.yml`.
- (He gives a blunt, profane reason for isolated environments. Paraphrase it.)

From `/tidy`: no directory guidance; PEP 8 consistency, dead-code removal, and
notebook hygiene — "run top-to-bottom", separate IO and functions into modules.

> "Keeping things consistent and tidy will free your working memory."
> — Patrick Mineault, Good Research Code Handbook (10 words)

From `/pipelines` — **the README chapter, and his position is interesting
because it disagrees with the obvious advice.** He recommends a README with a
one-sentence description, a longer description, install instructions, "general
orientation to the codebase and usage instructions", links to papers and extended
docs, and a licence. But he deliberately **keeps runtime, expected output and
verification detail out of the README** and pushes it into runnable shell scripts
and Makefiles — "runnable code and as documentation for the pipeline", with
Makefiles documenting "inputs and outputs to different scripts."

**His argument, which the article should adopt: prose claims about how to run
something rot; a Makefile cannot lie as easily.** `/zipf` is a worked minimal
example and is worth the author's own inspection before writing theirs.

### 7.3 The three citable papers

**Wilson, Bryan, Cranston, Kitzes, Nederbragt, Teal (2017), "Good Enough
Practices in Scientific Computing", *PLOS Computational Biology*, 22 June 2017.
DOI [10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510).**
Read in full 2026-09-12 (rendered article plus the source repo
https://github.com/swcarpentry/good-enough-practices-in-scientific-computing).
**This is the best numbered source for the article's layout recommendations.**

Its **Project Organization** rules, verbatim — all six, and they are short enough
to reproduce:

1. "Put each project in its own directory, which is named after the project"
2. "Put text documents associated with the project in the doc directory"
3. "Put raw data and metadata in a data directory and files generated during cleanup and analysis in a results directory"
4. "Put project source code in the src directory"
5. "Put external scripts or compiled programs in the bin directory"
6. "Name all files to reflect their content or function"

Selected rules from its other sections:
- *Data Management*: "Save the raw data"; "Create analysis-friendly data"; "Submit data to a reputable DOI-issuing repository so that others can access and cite it."
- *Software*: "Place a brief explanatory comment at the start of every program"; "Decompose programs into functions"; "Make dependencies and requirements explicit"; **"Provide a simple example or test data set"**; "Submit code to a reputable DOI-issuing repository."
- *Collaboration*: "Create an overview of your project"; "Make the license explicit"; **"Make the project citable."**
- *Keeping Track of Changes*: "Use a version control system"; "Add a file called CHANGELOG.txt to the project's docs subfolder."

**Sandve, Nekrutenko, Taylor, Hovig (2013), "Ten Simple Rules for Reproducible
Computational Research", *PLOS Computational Biology*.
DOI [10.1371/journal.pcbi.1003285](https://doi.org/10.1371/journal.pcbi.1003285).**
Read in full 2026-09-12. The ten rules, exact titles:

1. For Every Result, Keep Track of How It Was Produced
2. Avoid Manual Data Manipulation Steps
3. Archive the Exact Versions of All External Programs Used
4. Version Control All Custom Scripts
5. Record All Intermediate Results, When Possible in Standardized Formats
6. **For Analyses That Include Randomness, Note Underlying Random Seeds**
7. Always Store Raw Data behind Plots
8. Generate Hierarchical Analysis Output, Allowing Layers of Increasing Detail to Be Inspected
9. Connect Textual Statements to Underlying Results
10. Provide Public Access to Scripts, Runs, and Results

Rule 6 is the citation for the seeds discussion in §3.2. Rule 2 is the citation
for "the script regenerates the figure."

**Noble (2009), "A Quick Guide to Organizing Computational Biology Projects",
*PLOS Computational Biology*, 31 July 2009.
DOI [10.1371/journal.pcbi.1000424](https://doi.org/10.1371/journal.pcbi.1000424).**
Read in full 2026-09-12. Scheme: `data` ("for storing fixed data sets"),
`results` ("for tracking computational experiments performed on that data"),
`doc` (one subdirectory per manuscript), `src`, `bin`.

**A genuine disagreement worth surfacing:** Noble organises `data/` and
`results/` by **date-stamped subdirectories** (`YYYY-MM-DD`), arguing
chronological tracking beats a tidy logical taxonomy. Wilson et al. do not. Two
canonical PLOS papers, eight years apart, disagreeing about the second level of
the directory tree, is a good, honest note for a skeptical reader — there is no
single right answer below the top level.

### 7.4 What reviewers actually look for

**JOSS review checklist** — https://joss.readthedocs.io/en/latest/review_checklist.html
(read in full 2026-09-12). Current structure:

- Conflict of Interest
- Code of Conduct
- **General checks**: Repository; **License** — must be "a plain-text LICENSE file with the contents of an OSI approved software license"; Contribution and authorship; Scope and significance
- **Development History and Open-Source Practice**: development timeline, open development, collaborative effort, good practices
- **Functionality**: Installation; Functionality; Performance
- **Documentation**: statement of need; installation instructions; example usage; functionality documentation; **automated tests**; community guidelines
- **Software Paper**: Summary; Statement of need; State of the field; Software design; Research impact statement; **AI usage disclosure**; Quality of writing; References

**⚠️ Cite the current wording.** The 2026 checklist is more elaborate than the
version most people remember — the "Development History and Open-Source
Practice" section and the required **AI usage disclosure** are recent additions.
Verified by direct fetch on 2026-09-12, not from memory.

The tests bar, from https://joss.readthedocs.io/en/latest/review_criteria.html
(accessed 2026-09-12) — quoted in §3.5 — is deliberately low: "Good" is an
automated suite in CI; **"OK" is "documented manual steps that can be followed to
objectively check the expected functionality."**

**ACM Artifact Review and Badging**, five badges
(https://www.acm.org/publications/policies/artifact-review-and-badging-current):

| Badge | Requirement (as retrieved) |
|---|---|
| **Artifacts Available** | "Author-created artifacts relevant to this paper have been placed on a publically accessible archival repository." |
| **Artifacts Evaluated – Functional** | artifacts are "documented, consistent, complete, exercisable, and include appropriate evidence of verification and validation" |
| **Artifacts Evaluated – Reusable** | exceeds Functional; documentation and structure "facilitates" reuse to community norms |
| **Results Reproduced** | "main results of the paper have been obtained in a subsequent study by a person or team other than the authors, using, in part, artifacts provided by the author" |
| **Results Replicated** | main results "independently obtained … without the use of author-supplied artifacts" |

**⚠️ Access caveat: acm.org returned HTTP 403 to direct fetch. This content was
retrieved through the `r.jina.ai` reader proxy on 2026-09-12.** The wording
matches the well-known ACM taxonomy, but it was not confirmed from ACM's own
server. **Spot-check before publishing a direct quote.**

Note the ACM vocabulary **inverts** the common usage: for ACM, "Reproduced"
means a different team using the author's artifacts, and "Replicated" means a
different team without them. That is the opposite of The Turing Way's matrix in
§6.1. **Do not let the article use both vocabularies without flagging the clash
— this is a real trap and naming it is a service to the reader.**

**pyOpenSci** — https://www.pyopensci.org/software-peer-review/ (accessed
2026-09-12). Confirmed only that it reviews packages "to promote open and
reproducible research" and is "a diverse community that supports the open Python
tools that drive open science." **Its exact enumerated review checklist could not
be retrieved (repeated 404s on guessed sub-paths). Treat as unconfirmed.** From
its Python Package Guide (https://www.pyopensci.org/python-package-guide/,
fetched 2026-09-12) the required elements referenced are: README, Code of
Conduct, License, tests (with CI), code style/linting, package file structure and
`pyproject.toml` metadata.

### 7.5 What the minimal example should therefore contain

Assembled from the above, with the source for each line:

| Element | Why it is there |
|---|---|
| `README.md` — one-line description, install, **how to run it**, licence | JOSS "installation instructions" + "example usage"; Mineault `/pipelines`; Turing Way `rdm-metadata` |
| `LICENSE` — plain text, OSI-approved, SPDX identifier | JOSS General checks (explicit); Turing Way Licensing |
| One **small** data file, committed, treated as immutable | Wilson et al. "Save the raw data"; CCDS "raw data must be treated as immutable"; Sandve Rule 7 |
| One module with **one testable pure function** | Wilson et al. "Decompose programs into functions"; Pimentel best practice 3; Rule et al. Rule 4 |
| One test — a **characterisation test** against a committed baseline | §3.5; JOSS "automated tests"; Turing Way regression testing |
| One **script that regenerates the figure or table** from the data | Sandve Rules 1 and 2; Mineault's Makefile argument; CCDS `Makefile` |
| A **lockfile** | Pimentel best practices 4 and 5 — the #1 cause of failure in every study in §1 |
| An explicit **seed**, set in the script, not the notebook | Sandve Rule 6; §3.2 |
| `CITATION.cff` | §5; Wilson et al. "Make the project citable" |
| Relative paths only | Pimentel best practice 7; `FileNotFoundError` = 12.59% of failures |
| A notebook that **imports the module** rather than defining the logic | CCDS opinions; only 10.30% of real notebooks do this (§1.1) |

**And a verification step**, which none of the canonical sources states in those
exact words but which all of them imply: a way for the reader to know they got
the right answer. Wilson et al.'s "Provide a simple example or test data set" and
JOSS's requirement that a *reviewer* independently confirm functionality are the
closest citable anchors. **Present this as the author's own synthesis, not as a
quotation from any single source.** That is exactly what the characterisation
test in §3.5 provides, and it is the neatest closing move available: *the test
is the verification step.*

---

## 8. Proposed article outline

Six sections, in the order the evidence supports. The stage names from the
course (Explore → Organize → Share) survive, but the article is organised around
what breaks rather than around the stages.

**1. Four per cent.** Opens on Pimentel: 1.16 million notebooks, 863,878
attempted executions, **24.11% ran, 4.03% produced the same results**. Then the
2021 replication that removed every excuse — Docker, top-down execution, a
container stuffed with every package, image-difference forgiveness — and still
got **4.90% to 15.04%**. Then Samuel & Mietchen: notebooks attached to
*peer-reviewed* papers, **879 of 27,271** reproduced. Close the section by
disarming the reader: 24.11% is within a point of Collberg's 24.9% for computer
systems research generally. This is not a notebook problem. It is a
*handing-work-to-someone-else* problem, and the notebook is where it shows.
*(§1.1–1.3)*

**2. What actually breaks.** Not a lecture — a ranked list from the failure
data. Missing dependencies (29.23%), hidden state and out-of-order execution
(`NameError`, 14.53%; 36% of notebooks have out-of-order cells; 77% have an
execution-counter skip), absolute paths (12.59%). The counter-intuitive finding
that declaring dependencies made things *worse* (45.18% vs 31.24%) because the
declarations were incomplete. Then the fair hearing: Jupyter's own docs sell "a
fast interactive environment for prototyping and explaining code", Rule et al.
2019 — with Fernando Pérez as a co-author — concede the hidden-state problem and
prescribe the same fixes this article does, and short notebooks (≤9 cells)
reproduce 2.2× better. The thesis: the notebook is the explore stage, and it
should get *shorter* as the module grows. *(§1.1, §1.5, §1.6)*

**3. Organize: move the logic, keep the notebook.** The trigger, from
Cookiecutter Data Science: you are ready to leave the notebook when you start
"duplicating old notebooks", "copy/pasting functions between notebooks" and
"creating object-oriented classes within notebooks". Only **10.30%** of real
notebooks import any code from their own repository — that number is the whole
section. Then: `src/` versus flat (PyPA is descriptive, not prescriptive; the
real argument is Hynek's — your tests run against the project directory, not the
installed package); CCDS v2's tree, noting that v2 **renamed `src/` to the
project module**; `pip install -e .` and PEP 660 as the answer to
`sys.path.append('../src')`; `%load_ext autoreload` with its honest caveats; and
jupytext pairing so the notebook diffs like source. *(§2)*

**4. Test one thing.** Aimed squarely at someone who has never written a test —
**1.54%** of notebooks import a test framework. Lead with the permission slip
(The Turing Way: "infinitely better than testing nothing"; JOSS accepts
"documented manual steps" as OK). Then the single highest-value first test: a
**characterisation test** against a committed baseline, which requires no
knowledge of the right answer, only that today's answer not change silently. Then
the three things that will actually bite: `pytest.approx` defaults rel 1e-6 /
abs 1e-12 versus `assert_allclose` rel 1e-7 / **atol 0**; seeds, and NumPy's own
statement that `default_rng` carries *no* cross-version bit-stream guarantee
while the legacy API does; and `tmp_path` + `parametrize` as the only two pytest
features that earn their keep on day one. Hypothesis gets a paragraph as where
the road goes, with the honest note that pandas does not use it. *(§3)*

**5. Share: what goes in git, and the numbers that decide it.** GitHub warns at
**50 MiB**, blocks at **100 MiB**, and — the number nobody knows — *recommends*
single objects stay under **1 MB**. Repositories: "ideally less than 1 GB" on one
page, a 10 GB on-disk recommendation on another, and a 2 GB enforced push limit.
Why git is structurally bad at this (whole blobs, whole history, every clone).
Then the ladder: commit it if it is small; otherwise Zenodo + a checksum, or
`pooch`; LFS if you must, with the trap that "Download ZIP" may hand your reader
pointer files; DVC only when there is a pipeline. Then the notebook-outputs
question presented as three live answers rather than two — strip
(`nbstripout`), pair (`jupytext`), or teach git to read notebooks (`nbdime`) —
and a recommendation. *(§4)*

**6. Make it citable, then make it findable.** The Zenodo–GitHub flow in five
steps, and the **concept DOI versus version DOI** distinction with Zenodo's own
worked example (two releases, three DOIs). The rule: version DOI in the paper,
concept DOI in the README. `CITATION.cff` at schema **1.2.0**, and the fact that
earns it a place — **Zenodo reads it** to populate the archived record, so it is
not just a GitHub button. Software Heritage rides along automatically now, so it
is one checkbox, not two. Close on FAIR4RS, and specifically on **F1.2**
("Different versions of the software are assigned distinct identifiers") as the
principle that explains why Zenodo mints two DOIs in the first place — the
article's own structure turning out to be the standard's. *(§5)*

**7. The whole thing, in eleven files.** The worked minimal example. One data
file, one module with one testable function, one characterisation test, one
script that regenerates the figure, a lockfile, a seed, relative paths, a README
that says how to run it and how to know you got the right answer, a LICENSE, a
`CITATION.cff`, and a notebook that *imports the module*. Each file annotated
with which failure from §2 it closes. *(§7.5)*

**A note on ordering.** Testing sits before sharing deliberately. The
characterisation test is what makes "the analysis that regenerates the outputs"
a checkable claim rather than a promise, and it is the thing that lets §7's
README answer "how do I know I got the right answer?" — which is the question the
whole article is really about.

**Two traps to handle explicitly somewhere:**
- **The vocabulary clash.** ACM's badging uses "Reproduced" for *with* the
  author's artifacts and "Replicated" for *without* them. The Turing Way's 2×2
  uses "reproducible" for same-data-same-analysis and "replicable" for
  different-data-same-analysis. The article must not use both without flagging
  the collision. (§6.1, §7.4)
- **Funder and journal policy.** Thin and volatile. Use PLOS as the one verified
  worked example; do not print NIH, OSTP, Nature or Science dates from this
  note — they are explicitly unverified. (§5.6)
