# Tooling research — "Environments are not packages"

Research date: **2026-09-12**. All version numbers checked live on this date.
Audience: technically literate researchers/engineers, skeptical, long-time pip/conda/Poetry users.

---

## Access and confidence

### Fetched in full (high confidence — primary sources, read directly)

| Source | URL | Accessed |
|---|---|---|
| PyPI JSON API, poetry | https://pypi.org/pypi/poetry/json | 2026-09-12 |
| GitHub API, pixi latest release | https://api.github.com/repos/prefix-dev/pixi/releases/latest | 2026-09-12 |
| GitHub API, uv latest release | https://api.github.com/repos/astral-sh/uv/releases/latest | 2026-09-12 |
| GitHub API, Poetry latest release | https://api.github.com/repos/python-poetry/poetry/releases/latest | 2026-09-12 |
| pixi docs home | https://pixi.prefix.dev/latest/ | 2026-09-12 |
| pixi manifest reference | https://pixi.prefix.dev/latest/reference/pixi_manifest/ | 2026-09-12 |
| pixi lock file | https://pixi.prefix.dev/latest/workspace/lock_file/ | 2026-09-12 |
| pixi multi-platform config | https://pixi.prefix.dev/latest/workspace/multi_platform_configuration/ | 2026-09-12 |
| pixi advanced tasks | https://pixi.prefix.dev/latest/workspace/advanced_tasks/ | 2026-09-12 |
| pixi global tools | https://pixi.prefix.dev/latest/global_tools/introduction/ | 2026-09-12 |
| pixi conda+PyPI concepts | https://pixi.prefix.dev/latest/concepts/conda_pypi/ | 2026-09-12 |
| pixi "switching from uv" | https://pixi.prefix.dev/latest/switching_from/uv/ | 2026-09-12 |
| pixi "switching from Poetry" | https://pixi.prefix.dev/latest/switching_from/poetry/ | 2026-09-12 |
| pixi FAQ | https://pixi.prefix.dev/latest/misc/FAQ/ | 2026-09-12 |
| pixi GitHub README | https://github.com/prefix-dev/pixi | 2026-09-12 |
| prefix.dev company site | https://prefix.dev/ | 2026-09-12 |
| Poetry docs home | https://python-poetry.org/docs/ | 2026-09-12 |
| Poetry basic usage | https://python-poetry.org/docs/basic-usage/ | 2026-09-12 |
| Poetry libraries | https://python-poetry.org/docs/libraries/ | 2026-09-12 |
| Poetry pyproject reference | https://python-poetry.org/docs/pyproject/ | 2026-09-12 |
| Poetry CLI reference | https://python-poetry.org/docs/cli/ | 2026-09-12 |
| Poetry FAQ | https://python-poetry.org/docs/faq/ | 2026-09-12 |
| Poetry changelog/history | https://python-poetry.org/history/ | 2026-09-12 |
| uv docs home | https://docs.astral.sh/uv/ | 2026-09-12 |
| uv project layout / uv.lock | https://docs.astral.sh/uv/concepts/projects/layout/ | 2026-09-12 |
| uv locking & syncing | https://docs.astral.sh/uv/concepts/projects/sync/ | 2026-09-12 |
| uv init / apps vs libs | https://docs.astral.sh/uv/concepts/projects/init/ | 2026-09-12 |
| uv packaging guide | https://docs.astral.sh/uv/guides/package/ | 2026-09-12 |
| uv scripts / PEP 723 | https://docs.astral.sh/uv/guides/scripts/ | 2026-09-12 |
| uv PyTorch integration | https://docs.astral.sh/uv/guides/integration/pytorch/ | 2026-09-12 |
| PEP 517 | https://peps.python.org/pep-0517/ | 2026-09-12 |
| PEP 621 | https://peps.python.org/pep-0621/ | 2026-09-12 |
| PEP 723 | https://peps.python.org/pep-0723/ | 2026-09-12 |
| PEP 751 | https://peps.python.org/pep-0751/ | 2026-09-12 |
| PyPA install_requires vs requirements | https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/ | 2026-09-12 |
| PyPA tool recommendations | https://packaging.python.org/en/latest/guides/tool-recommendations/ | 2026-09-12 |
| The Turing Way — definitions | https://book.the-turing-way.org/reproducible-research/overview/overview-definitions | 2026-09-12 |
| The Turing Way — package management | https://book.the-turing-way.org/reproducible-research/renv/renv-package | 2026-09-12 |
| Henry Schreiner, "Poetry Versions" | https://iscinumpy.dev/post/poetry-versions/ | 2026-09-12 |
| Jacob Tomlinson, uv vs pixi | https://jacobtomlinson.dev/posts/2025/python-package-managers-uv-vs-pixi/ | 2026-09-12 |
| Simon Willison on OpenAI/Astral | https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/ | 2026-09-12 |
| QuantCo, pixi in production | https://tech.quantco.com/blog/pixi-production/ | 2026-09-12 |
| pydevtools, when to choose pixi over uv | https://pydevtools.com/handbook/explanation/when-should-i-choose-pixi-over-uv/ | 2026-09-12 |
| pydevtools, uv vs pixi vs conda | https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ | 2026-09-12 |
| pydevtools, can you trust uv long-term | https://pydevtools.com/handbook/explanation/can-you-trust-uv-long-term/ | 2026-09-12 |
| Bite Code!, a year of uv | https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should | 2026-09-12 |
| Poetry issue #3747 | https://github.com/python-poetry/poetry/issues/3747 | 2026-09-12 |

### Redirects discovered (correct these if the article cites the old URLs)

- **`https://pixi.sh/...` now 301-redirects to `https://pixi.prefix.dev/...`.** The brief's URL still works but resolves elsewhere. Cite `pixi.prefix.dev`.
- **`https://the-turing-way.netlify.app/...` now 301-redirects to `https://book.the-turing-way.org/...`.** The brief's URL is stale. Cite `book.the-turing-way.org`.

### Blocked, empty, or unreadable

- **`https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md`** — fetched, but the actual numbers are **rendered as embedded chart images**, not text. I could not extract a single published figure from Astral's own benchmarks. Only the methodology is readable.
- **`https://github.com/conda/conda-lock/issues/615`** ("Should we endorse Pixi?") — only the issue header and opening post rendered; **the comment thread did not load**. I have maresb's opening framing but no counter-arguments from the thread.
- **`https://pixi.prefix.dev/latest/workspace/lockfile/`** and **`/latest/concepts/lockfile/`** — 404 / redirect stub. Correct path is `/latest/workspace/lock_file/` (underscore).

### Snippet-only (search-result summaries, NOT read in full — treat as weaker)

- Independent verification of uv's speed claims. See §3.4 — **this is the weakest area in the whole file.**
- GDAL `gdal-config` build-failure specifics (§5.1) — assembled from search snippets of rasterio/pyogrio/OSGeo docs, not fetched directly.
- PyTorch/CUDA conda-channel priority details (§5.2) — search snippets from Carpentries Incubator material, not fetched directly.
- pixi criticism from community forums (§7.1) — **I searched HN and Reddit angles repeatedly and found very little genuine critical writing.** What exists is thin. Flagged.

### Explicitly NOT verified — do not state these in the article

- **pixi's GitHub star count.** The README fetch reported "7.7k stars", which I believe is a misparse of the rendered page and is inconsistent with pixi's apparent adoption. **Do not cite a star count.**
- **Whether uv can be said to "replace" Poetry in any officially-endorsed sense.** Astral claims it; PyPA does not endorse it (see §4.3).
- **Any independent, methodologically-transparent benchmark of uv vs Poetry.** I did not find one I would stand behind.

---

## 1. pixi

### 1.1 Version, provenance, licence

- **Current version: v0.80.0, published 2026-09-07.** Source: https://api.github.com/repos/prefix-dev/pixi/releases/latest (accessed 2026-09-12).
- **Still pre-1.0.** This matters for the maturity argument in §7.
- **Licence: BSD-3-Clause.** Source: https://github.com/prefix-dev/pixi (accessed 2026-09-12).
- **Developed at prefix.dev**, a company whose stated mission is "to solve the challenges developers face every day by providing a seamless, efficient, and intuitive platform." Source: https://prefix.dev/ (accessed 2026-09-12).
- Written in Rust, built on the `rattler` library. Source: https://github.com/prefix-dev/pixi (accessed 2026-09-12).
- v0.80.0's headline feature is experimental **conda-scripts** — single-file scripts in any language with embedded conda dependencies, behind `pixi config set experimental.conda-script true --global`. This is pixi's answer to PEP 723, generalised beyond Python. Source: release notes, https://api.github.com/repos/prefix-dev/pixi/releases/latest (accessed 2026-09-12).

### 1.2 What it claims to be

> "a cross-platform, multi-language package manager and workflow tool built on the foundation of the conda ecosystem."
> — pixi README, https://github.com/prefix-dev/pixi (accessed 2026-09-12)

> "fast, modern, and reproducible"
> — pixi docs home, https://pixi.prefix.dev/latest/ (accessed 2026-09-12)

The docs home lists five headline features: **Tasks** ("Manage complex pipelines effortlessly"), **Multi-Platform**, **Conda-Forge & PyPI support**, **Pixi Global**, and **Lock Files** ("Isolated, easily recreated environments with lock files built-in"). Source: https://pixi.prefix.dev/latest/ (accessed 2026-09-12).

Note the framing to use in the article: pixi describes itself with the vocabulary of *workspaces, environments and workflows* — not of *packages*. The README explicitly analogises to cargo/npm ("an exceptional experience similar to popular package managers like cargo or npm, but for any language"), which is an environment/workspace metaphor, not a distribution metaphor.

### 1.3 The manifest: `pixi.toml` (or `pyproject.toml`)

Tables, per https://pixi.prefix.dev/latest/reference/pixi_manifest/ (accessed 2026-09-12):

- **`[workspace]`** — `channels`, `platforms`, `name`, `version`, metadata. Minimum required: `channels`, `name`, `platforms`.
- **`[dependencies]`** — **conda** packages, using conda MatchSpec syntax.
- **`[pypi-dependencies]`** — **PyPI** packages, using PEP 440 specifiers.
- **`[tasks]`** — cross-platform commands run via `pixi run`.
- **`[feature]`** / **`[environments]`** — features are reusable bundles of dependencies; environments compose features. Docs: "Features are the right tool when you want to share dependencies between environments."
- **`[target.<platform>.dependencies]`** — per-platform overrides.

**It can live in `pyproject.toml`:**

> "We also support the `pyproject.toml` file. It has the same structure as the `pixi.toml` file, except that you need to prepend the tables with `tool.pixi`."
> — https://pixi.prefix.dev/latest/reference/pixi_manifest/ (accessed 2026-09-12)

So `[workspace]` becomes `[tool.pixi.workspace]`. **This is the single most important fact for §4 of the article**: pixi sits in the `[tool.*]` namespace that PEP 621 explicitly reserved for tools, and leaves `[project]` alone. The file is shared; the tables are not.

### 1.4 What `pixi.lock` actually pins

Source: https://pixi.prefix.dev/latest/workspace/lock_file/ (accessed 2026-09-12).

The lockfile records "the exact dependencies that were resolved during this resolution process—the packages, their versions, and other metadata." Concretely it contains:

- **Exact versions** (e.g. Python 3.12.2)
- **Both SHA256 and MD5 hashes** — content-addressed integrity, not just a version string
- **Per-platform solves** — a separate resolved package set per declared platform (linux-64, osx-64, osx-arm64, win-64…)
- **Per-environment solves** — one entry per named environment, and within each, one entry per platform
- **Channels** (source repository URLs) and **direct download URLs** per artefact
- **Build strings and subdir** — the conda build variant, not just the version
- A **lock file format version number** (currently 6)

Two properties worth quoting:

> "human readable, so you can take a look at which packages are listed without extra tools"

> backward compatible but "not forward compatible" — an older lockfile works with newer pixi, not the reverse.

— both https://pixi.prefix.dev/latest/workspace/lock_file/ (accessed 2026-09-12)

**Commit it.** The docs recommend committing for most projects, on the grounds that "reproducibility is very important." But note the carve-out, which is directly on the article's thesis: **libraries** are called out as a special case — they should test against multiple dependency versions and may want CI workflows that resolve against latest packages rather than the lock. (Same URL.)

### 1.5 Conda + PyPI in one manifest — the mechanism and its seams

Source: https://pixi.prefix.dev/latest/concepts/conda_pypi/ (accessed 2026-09-12).

Resolution is **conda-first**, in three steps:
1. "Resolve the conda dependencies"
2. "Map the conda packages to PyPI packages"
3. "Resolve the remaining PyPI dependencies"

Two separate solvers: **`resolvo`** (via `rattler`) for conda, **PubGrub** (via **uv**) for PyPI. Name mapping between ecosystems is done by **`parselmouth`**.

Stated caveats — useful for a fair article:
- "Pixi will install the conda package (and not the PyPI package) if both are available and specified as dependencies."
- **The two-stage solve can fail where a single solve would not.** The docs' own worked example: conda supplying `typing-extensions==4.15.0` conflicting with a PyPI requirement of `typing-extensions==4.14`.
- Default name-mapping **requires internet access**; "firewall-restricted environments" need alternative configuration.

The conda packages are treated as **locked** during the PyPI pass, "preventing uv from installing its own versions." Source: https://pixi.prefix.dev/latest/reference/pixi_manifest/ (accessed 2026-09-12).

### 1.6 Tasks

Source: https://pixi.prefix.dev/latest/workspace/advanced_tasks/ (accessed 2026-09-12).

- Defined in `pixi.toml` / `pyproject.toml`; run with `pixi run <task>`.
- **`depends-on`**: "Just like packages can depend on other packages, our tasks can depend on other tasks." Sequential; a failure halts the chain.
- **`inputs` / `outputs`**: content-based caching. "Pixi will reuse the result of the task" when environment, inputs, outputs and command are unchanged. This is a build-system feature, not a package-manager feature — worth flagging as evidence pixi is a *workflow* tool.
- **`cwd`**, **`env`** per task.
- Runs on **`deno_task_shell`**, a portable shell giving the same `cp`/`mv`/`rm`/`mkdir`/`echo`, pipes, globs and command substitution on Windows, macOS and Linux. This is how "cross-platform tasks" are actually delivered.

### 1.7 `pixi global`

Source: https://pixi.prefix.dev/latest/global_tools/introduction/ (accessed 2026-09-12).

- Manages "globally installed tools in a way that makes them available from any directory", exposed to `PATH`.
- "isolates each package in its own environment, exposing only the necessary entry points."
- Explicitly likened to pipx: "quite similar to that of `pipx`" — but extended to the whole conda ecosystem, so it installs non-Python CLI tools too.
- Backed by a global manifest recording environments, dependencies, exposed executables and channels — i.e. **your global tool set is itself a declarative, reproducible artefact**, which pipx does not give you.
- `--with` adds packages to an environment without exposing their executables.

### 1.8 Multi-platform solving

Source: https://pixi.prefix.dev/latest/workspace/multi_platform_configuration/ (accessed 2026-09-12).

- **pixi solves for every declared platform at once, from whatever machine you are on.** Declare `workspace.platforms`, and pixi "determines which dependencies to install for each platform individually. All of this is stored in a lock file." One `pixi lock` on a Mac produces the Linux and Windows solves too.
- Platforms are conda subdirs (`linux-64`, `win-64`, `osx-64`, `osx-arm64`) **or** named custom platforms carrying virtual-package constraints, e.g. `{ name = "jetson-nano", platform = "linux-aarch64", cuda = "12.8" }`. Friendly virtual-package keys include `cuda`, `glibc`, `macos`, `archspec`.
- If a dependency is unavailable on a declared platform you get a warning, e.g. `WARN Not installing dependency for (default) on current platform: (osx-arm64) as it is not part of this project's supported platforms.`

**This is the single sharpest technical contrast with conda/mamba** and worth a paragraph: conda "doesn't allow us to install Windows environments on Linux and vice versa" (QuantCo, https://tech.quantco.com/blog/pixi-production/, 2024-07-11, accessed 2026-09-12), whereas pixi's lockfile is cross-platform by construction.

### 1.9 How pixi says it differs from conda / mamba / pip / Poetry

Source: pixi FAQ, https://pixi.prefix.dev/latest/misc/FAQ/ (accessed 2026-09-12). The FAQ is a self-serving comparison table — flag it as vendor framing — but its axes are informative:

| | installs Python | builds packages | task runner | lock file | fast | usable without Python |
|---|---|---|---|---|---|---|
| conda | yes | no | no | no | no | no |
| mamba | yes | no | no | no | yes | via micromamba |
| pip | no | yes | no | no | no | no |
| **Poetry** | no | **yes** | no | **yes** | no | no |
| **pixi** | yes | **work in progress** | yes | yes | yes | yes |

**The FAQ's own table concedes the article's thesis.** pixi marks package *building* as "work in progress"; Poetry marks it as done. That is the boundary, stated by pixi itself.

The FAQ does **not** discuss uv (there is a separate "Switching From… uv" page).

### 1.10 What pixi says about uv

Source: https://pixi.prefix.dev/latest/switching_from/uv/ (accessed 2026-09-12).

pixi concedes uv "is a fast Python package manager" but calls it "limited to the PyPI ecosystem." Its four claimed advantages:

1. "System dependencies included. Need CUDA, OpenSSL, compilers, or C libraries? Conda packages bundle them."
2. "A single Pixi workspace can manage Python, R, C/C++, Rust, Node.js, and more, while uv only handles Python."
3. Binary-first: "Conda packages are pre-compiled, so you rarely need a build toolchain on your machine."
4. "Conda environments contain everything (interpreters, libraries, headers, compilers, CLI tools), all managed by the solver."

Plus "True cross-platform lock files" and a "Built-in task runner."

**And the line the article should absolutely use:**

> "Pixi fully supports PyPI packages alongside conda packages, powered by uv under the hood."
> — https://pixi.prefix.dev/latest/switching_from/uv/ (accessed 2026-09-12)

pixi and uv are not rivals at the layer most people argue about. pixi *embeds* uv. The disagreement is about scope, not about resolvers.

---

## 2. Poetry

### 2.1 Version and provenance

- **Current version: 2.4.3, published 2026-09-05.** Sources: https://pypi.org/pypi/poetry/json and https://api.github.com/repos/python-poetry/poetry/releases/latest (both accessed 2026-09-12).
- 2.4.3 is a patch release fixing sdist extraction on Python 3.10.0–3.10.12 and 3.11.0–3.11.4.
- **Requires Python 3.10+.** Source: https://python-poetry.org/docs/ (accessed 2026-09-12).
- **Poetry is past 1.0 and has been for years.** Contrast with pixi (0.80) and uv (0.12). Worth noting for the skeptical reader: maturity is one axis on which the incumbent still wins.

### 2.2 What Poetry claims

Four functions, per https://python-poetry.org/docs/ (accessed 2026-09-12):

1. Dependency management — "allows you to declare the libraries your project depends on and it will manage (install/update) them for you"
2. A lockfile "to ensure repeatable installs"
3. **"can build your project for distribution"**
4. Environment isolation — "makes project environment isolation one of its core features"

Tagline: "Python dependency management and packaging made easy."

### 2.3 Build and publish — the part pixi does not do

Source: https://python-poetry.org/docs/cli/ (accessed 2026-09-12).

**`poetry build`**
> "The `build` command builds the source and wheels archives."

Invokes the PEP 517 build backend declared in `pyproject.toml`, in an isolated environment if needed. Outputs an **sdist** and a **wheel**. Options: `--format/-f` (`wheel` or `sdist`), `--clean`, `--output/-o` (default `dist`), `--config-settings/-c` passed through to the backend.

**`poetry publish`**
> "This command publishes the package, previously built with the `build` command, to the remote repository."

Auto-registers on first submission; defaults to PyPI. Options: `--repository/-r` (this is how you target **TestPyPI**), `--build`, `--dry-run`, `--skip-existing`, `--username/-u`, `--password/-p`.

**`poetry lock`** resolves and records exact versions without installing. **`poetry install`** uses `poetry.lock` if present, creates it if not. **`poetry add`** "adds required packages to your `pyproject.toml` and installs them."

### 2.4 `pyproject.toml`: which tables are whose

Source: https://python-poetry.org/docs/pyproject/ (accessed 2026-09-12).

- **`[project]`** — standard PEP 621 metadata. "Poetry supports specifying main dependencies in the project.dependencies section of your pyproject.toml according to PEP 621."
- **`[tool.poetry]`** — Poetry-specific configuration only.
- **Poetry 2.0 pushed users toward the standard table**: "Prior Poetry 2.0, dependencies had to be declared in the tool.poetry.dependencies section of the pyproject.toml file. With Poetry 2.0, you should consider using the project.dependencies section instead." Many `[tool.poetry]` fields are now explicitly marked **Deprecated** with notes like "Use `project.name` instead."
- **Genuinely Poetry-only fields** (no standard equivalent): `packages`, `include`/`exclude`, file-type `scripts`, `requires-poetry`, `requires-plugins`, `build-constraints`.
- **Build system**:
  ```toml
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  "Poetry is compliant with PEP-517, by providing a lightweight core library" — and you reference **`poetry-core`**, not `poetry`. This separation is the point: `poetry-core` is a small build backend that a consumer's `pip install` can invoke without dragging in Poetry's resolver, venv manager and CLI.

### 2.5 PEP 517 / 518 / 621 — the history

- **PEP 518** established `[build-system].requires` in `pyproject.toml` (build-time dependencies). *(Not fetched directly this session — I fetched 517, 621, 723, 751. Verify before citing specifics.)*
- **PEP 517** — "A build-system independent format for source trees". **Status: Final. Created 2015-09-30, resolved September 2017.** Standardises the `build-backend` key (`"module:object"` form, e.g. `"flit.api:main"`) and the hooks `build_wheel()` / `build_sdist()` (mandatory) plus `get_requires_for_build_wheel()`, `prepare_metadata_for_build_wheel()`, `get_requires_for_build_sdist()` (optional). Source: https://peps.python.org/pep-0517/ (accessed 2026-09-12).

  The problem it solved, in the PEP's own words: distutils/setuptools suffered from "(a) missing important features," "(b) difficulty extending them," and "(c) it's very difficult to use anything else." The stated goal was to "get distutils-sig out of the business of being a gatekeeper for Python build systems." **PEP 517 is why Poetry can exist at all.**

- **PEP 621** — core metadata in `pyproject.toml`. **Status: Final. Created 2020-06-22**, post-history through 2020-10-31. Standardises `[project]`: name, version, description, readme, requires-python, dependencies, optional-dependencies, authors, maintainers, keywords, classifiers, license, urls, scripts, gui-scripts, entry-points, dynamic. Source: https://peps.python.org/pep-0621/ (accessed 2026-09-12).

  **The governing sentence for §4 of the article:**
  > "No tools may add fields to this table which are not defined by this PEP or subsequent PEPs. For tools wishing to store their own settings in pyproject.toml, they may use the [tool] table"
  > — PEP 621, https://peps.python.org/pep-0621/ (accessed 2026-09-12)

- **Poetry's own PEP 621 timeline — and this is the awkward bit.** PEP 621 was Final in 2020. Poetry added `[project]` support in **Poetry 2.0.0, released 2025-01-05** — the changelog entry reads "Add support for the `project` section in the `pyproject.toml` file according to PEP 621." Source: https://python-poetry.org/history/ (accessed 2026-09-12). **That is roughly a four-year gap between the standard going Final and Poetry implementing it**, and it is the core of the "non-standard behaviour" criticism in §7.2.

  Other Poetry 2.0 changes: `poetry lock` default flipped to `--no-update` (with a new `--regenerate` for the old behaviour); `poetry export` removed from the default install (moved to `poetry-plugin-export`); `poetry add --optional` now requires naming the extra; `--directory`/`-C` now actually changes directory; Python 3.8 and earlier dropped.

### 2.6 Where Poetry overlaps pixi, and where it does not

**Overlap (both do these):** dependency resolution; a committed lockfile; a managed project-local environment; a `pyproject.toml` manifest; add/install/lock verbs.

**Poetry does, pixi does not (or not yet):**
- `poetry build` → sdist + wheel
- `poetry publish` → PyPI / TestPyPI
- a PEP 517 build backend (`poetry-core`) that arbitrary consumers invoke via plain `pip install`
- pixi's own FAQ marks package building "work in progress" (§1.9)

**pixi does, Poetry does not:**
- conda-forge packages, i.e. compiled non-Python libraries, compilers, CUDA, R, Node (§5)
- cross-platform solving from one machine (§1.8)
- a task runner with content-based caching (§1.6)
- global tool management (§1.7)
- environment management without a pre-existing Python at all

**The crisp statement:** Poetry's output is an artefact you upload. pixi's output is a machine state you recreate. They are not competitors; they answer different questions.

---

## 3. uv

### 3.1 Version and provenance

- **Current version: 0.12.13, published 2026-09-10** (two days before research date — the release cadence is genuinely fast). Source: https://api.github.com/repos/astral-sh/uv/releases/latest (accessed 2026-09-12).
- 0.12.13 adds GraalPy 3.13.0 support, hash verification for PEP 658 metadata downloads, and reuse of hashes from direct-URL fragments to avoid full downloads.
- **Still pre-1.0**, like pixi.
- Built by **Astral** (also Ruff and ty). **Dual-licensed Apache 2.0 / MIT.** Source: https://pydevtools.com/handbook/explanation/can-you-trust-uv-long-term/ (accessed 2026-09-12).
- **Astral was acquired by OpenAI in 2026.** See §7.3 — this is essential context and the article must not omit it.

### 3.2 What uv does

Source: https://docs.astral.sh/uv/ (accessed 2026-09-12).

> "An extremely fast Python package and project manager, written in Rust."

> "A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more."

Note the list **names Poetry and twine** — i.e. uv explicitly claims the packaging/publishing role, not just the environment role. It does **not** name conda, mamba or pixi.

Capabilities: project management with universal lockfiles; script running with inline metadata; Python version installation and management; tool install/run via `uvx`/`uv tool`; "a pip-compatible interface for a performance boost with a familiar CLI"; Cargo-style workspaces; a global cache that deduplicates across projects.

### 3.3 `uv.lock`

Source: https://docs.astral.sh/uv/concepts/projects/layout/ (accessed 2026-09-12).

- Created automatically next to `pyproject.toml`.
- Captures "the packages that would be installed across all possible Python markers such as operating system, architecture, and Python version" — i.e. it is **"a _universal_ or _cross-platform_ lockfile."** One lockfile, all platforms, like pixi and unlike a `requirements.txt` from `pip freeze`.
- Should "be checked into version control, allowing for consistent and reproducible installations across machines."
- **The lock-in sentence, verbatim:**
  > "uv.lock is a human-readable TOML file but is managed by uv and should not be edited manually. The uv.lock format is specific to uv and not usable by other tools."
  > — https://docs.astral.sh/uv/concepts/projects/layout/ (accessed 2026-09-12)

  **This is uv's own admission of format lock-in**, and it is why PEP 751 / `pylock.toml` matters (§4.1). Use it in §7.3 for fairness — the same criticism levelled at `pixi.lock` applies verbatim to `uv.lock`.

**`--locked` vs `--frozen`** (https://docs.astral.sh/uv/concepts/projects/sync/, accessed 2026-09-12):
- "Locking is the process of resolving your project's dependencies into a lockfile. Syncing is the process of installing a subset of packages from the lockfile into the project environment."
- "Locking and syncing are _automatic_ in uv" — `uv run` locks and syncs before executing.
- `--locked`: "If the lockfile is not up-to-date, uv will raise an error instead of updating the lockfile." **This is the CI flag**, and the exact analogue of `pixi install --locked`.
- `--frozen`: "use the lockfile without checking if it is up-to-date".

### 3.4 Speed claims — and how well substantiated they actually are

**The claim:** "10-100x faster than `pip`". Source: https://docs.astral.sh/uv/ (accessed 2026-09-12). **This is a vendor claim on Astral's own homepage.**

**What I could verify about Astral's benchmarks** (https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md, accessed 2026-09-12):
- Four scenarios: warm install, cold install, warm resolution, cold resolution.
- Compared against pip-compile, Poetry and PDM (resolution); pip-sync, Poetry and PDM (installation).
- Workload: "Trio's `docs-requirements.in`, as a representative example of a real-world project" — **a single, small, documentation-only requirement set**.
- Tooling: `hyperfine` under a wrapper script.
- Astral's own honest caveat: "benchmark performance may vary dramatically across different operating systems and filesystems", because uv uses reflinking on macOS and hardlinking on Linux.
- **I could not extract a single number.** The results are published as chart images, not text or tables.

**Honest assessment for the article:** the direction of the claim is not in dispute — uv is dramatically faster, and nobody serious argues otherwise. But:
1. Astral's headline range (10–100x) is vendor-published, benchmarked against **one small workload**, and **the numbers are not machine-readable**.
2. The "100x" end is almost certainly the warm-cache install case, which is the least representative of the reproducibility workflows this article is about (CI, cold, from scratch).
3. Independent figures exist but the ones surfaced by search were low-quality SEO content with unstated methodology. A Real Python measurement of roughly 8x on a JupyterLab install was cited second-hand in search results; **I did not fetch it and would not cite it without doing so.**

**Recommended article line:** say uv is *unambiguously and dramatically faster*, note that the specific "10–100x" figure is Astral's own and rests on a single small benchmark, and resist repeating the number as though it were independently established. Bite Code! (Feb 2025) offers a concrete, human-scale datum instead: uv "installed Python 3.8.16 in 2.71s". Source: https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should (accessed 2026-09-12).

### 3.5 `uv build` and `uv publish` — can it replace Poetry?

Source: https://docs.astral.sh/uv/guides/package/ (accessed 2026-09-12).

- **`uv build`**: "will build the project in the current directory, and place the built artifacts in a `dist/` subdirectory." Produces sdist and wheel by default. Respects `[build-system]` in `pyproject.toml`; falls back to setuptools if absent, though the docs "strongly recommend configuring a build system."
- **`uv publish`**: uploads to PyPI and other registries. Token auth (the docs note "PyPI does not support publishing with username and password anymore"). Supports attestations (pairing `.publish.attestation` files with distributions), custom indexes via `[[tool.uv.index]]`, retry logic, and **trusted publishing** from CI.

**Answer: yes, functionally.** uv covers build + publish, so on the packaging axis it is a genuine Poetry replacement, and it adds trusted publishing and attestations, which are the modern supply-chain-security path. Astral's own tagline naming `twine` confirms the intent.

**One caveat I could not resolve:** the packaging guide I fetched does not enumerate which build backends uv supports beyond mentioning the setuptools fallback. uv ships its own `uv_build` backend, but **I did not verify its current status or feature set this session** — check before asserting anything about it.

### 3.6 PEP 723 inline script metadata

Sources: https://docs.astral.sh/uv/guides/scripts/ and https://peps.python.org/pep-0723/ (both accessed 2026-09-12).

**PEP 723: Status Final. Created 2023-08-04, resolved 2024-01-08.** It "specifies a metadata format that can be embedded in single-file Python scripts to assist launchers, IDEs and other external tools." Fields: `dependencies` (PEP 508), `requires-python` (PEP 440), and a `[tool]` table.

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint
```

uv: "uv will automatically create an environment with the dependencies necessary to run the script" — `uv run example.py` and nothing else. **Scripts can be locked**: "uv supports locking dependencies for PEP 723 scripts using the `uv.lock` file format", via `uv lock --script example.py`, producing a lockfile beside the script.

**Why this matters to the article's thesis:** PEP 723 is the boundary at its purest. A single analysis script is an *application*: it declares dependencies, it can be locked, and it is never consumed by anything downstream. Nobody `pip install`s a PEP 723 script. It is an environment with a `.py` extension. And pixi v0.80.0's experimental conda-scripts (§1.1) is the same idea generalised past Python's reach.

### 3.7 Applications vs libraries, in uv's own model

Source: https://docs.astral.sh/uv/concepts/projects/init/ (accessed 2026-09-12).

uv bakes the distinction into `uv init`:
- **Application**: "suitable for web servers, scripts, and command-line interfaces"
- **Library**: "provides functions and objects for other projects to consume. Libraries are intended to be built and distributed"
- `--lib` creates a library, which "always require[s] a packaged project" (a build system + `src/<name>/` layout)
- `--no-package` drops the build system for simple applications
- `--bare` emits only a minimal `pyproject.toml`

**This is a strong citation for §4.** A major, standards-oriented tool encodes the environment/package boundary as a first-class choice at project creation time, and ties it directly to whether a build backend exists. "Intended to be built and distributed" is the definition of a package.

### 3.8 Can uv replace pixi for environments? — the decisive question

**No, not where non-Python dependencies are involved. This is not a maturity gap; it is architectural.**

- uv resolves from PyPI plus Git URLs, local paths and private indexes. Per pydevtools: "It cannot install non-Python dependencies like the CUDA toolkit, GDAL, or HDF5." Source: https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ (Tim Hopper, updated 2026-09-07, accessed 2026-09-12).
- pixi's framing: "Pixi pulls from conda channels (typically conda-forge) and PyPI, which means it can install system-level dependencies and non-Python software that PyPI does not distribute." Source: https://pydevtools.com/handbook/explanation/when-should-i-choose-pixi-over-uv/ (Tim Hopper, updated 2026-09-07, accessed 2026-09-12).
- Jacob Tomlinson puts it as a containment relation: "pixi has a superset of uv's functionality because it also supports conda-forge packages". Source: https://jacobtomlinson.dev/posts/2025/python-package-managers-uv-vs-pixi/ (2025-11-18, accessed 2026-09-12).

**The honest partial exception — PyTorch.** uv handles the CUDA-variant problem well, and the article should concede this rather than overclaim. Source: https://docs.astral.sh/uv/guides/integration/pytorch/ (accessed 2026-09-12):
- "PyTorch produces distinct builds for each accelerator (e.g., CPU-only, CUDA)" and "Builds for different accelerators are published to different indexes."
- uv routes via `tool.uv.sources`, with environment markers per platform, and extras (`uv sync --extra cu130`).
- `--torch-backend=auto` / `UV_TORCH_BACKEND=auto` detects GPU hardware and picks the index.
- Acknowledged gaps: "PyTorch doesn't publish CUDA builds for macOS"; "PyTorch doesn't publish ROCm builds for macOS or Windows"; and the docs warn a `cu130` extra "will fail to install on macOS when the `cu130` extra is enabled."
- **But**: uv installs *packages from the right index*. It does not install a system CUDA toolkit, compilers, or headers.

pydevtools' scenario table lands in the same place and is a good structure to borrow:

| Scenario | Tool | Why |
|---|---|---|
| Pure Python, everything on PyPI | **uv** | simplest, fastest, most portable |
| Native libraries, new project | **pixi** | modern workflow, unified lockfile |
| Native libraries, existing conda estate | **conda** | proven infrastructure, institutional knowledge |
| **PyTorch only** | **uv** | index routing handles CUDA variants |
| **Mixed GPU stacks (PyTorch + RAPIDS)** | **pixi or conda** | single solver pass resolves CUDA conflicts |

Source: https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ (accessed 2026-09-12).

---

## 4. The boundary the article rests on

### 4.1 Why a lockfile is right for an application/analysis and wrong to ship in a library

**The cleanest quote available, and it is from Poetry itself:**

> "The application ignores your library's lock file. It can use whatever dependency version meets the constraints in your `pyproject.toml`."
> — Poetry docs, https://python-poetry.org/docs/basic-usage/ (accessed 2026-09-12)

That is the whole argument in two sentences. A lockfile in a published library is **inert** — not harmful so much as *ignored*. It is a file that cannot do the job it looks like it is doing.

Supporting statements:

- Poetry, same page: "You should commit the `poetry.lock` file to your project repo so that all people working on the project are locked to the same versions of dependencies" and "Application developers commit `poetry.lock` to get more reproducible builds" — "your CI server, production machines, other developers in your team, everything and everyone runs on the same dependencies."
- Poetry on libraries, hedged: "For your library, you may commit the `poetry.lock` file if you want to. This can help your team to always test against the same dependency versions. However, this lock file will not have any effect on other projects that depend on it." Source: https://python-poetry.org/docs/libraries/ (accessed 2026-09-12).
- Poetry's mitigation advice for libraries that do commit one: "consider a regular refresh of `poetry.lock` to stay up-to-date and reduce the risk of sudden breakage for users." Source: basic-usage, same URL. **The useful nuance**: a library's lockfile is a *CI testing artefact*, not a distribution artefact. That distinction is worth a paragraph.
- pixi's docs make the same carve-out: commit `pixi.lock` for reproducibility, but libraries "should test against multiple dependency versions and may want custom CI workflows testing against latest packages." Source: https://pixi.prefix.dev/latest/workspace/lock_file/ (accessed 2026-09-12).

**PEP 751 corroborates from the standards side.** "A file format to record Python dependencies for installation reproducibility." **Status: Final. Created 2024-07-24, accepted 2025-03-31.** Source: https://peps.python.org/pep-0751/ (accessed 2026-09-12).

- The motivating gap: "Currently, no standard exists to create an immutable record, such as a lock file, which specifies what direct and indirect dependencies should be installed."
- The role split that makes the boundary concrete: **lockers** write lock files (and must record hashes and file sizes); **installers** consume them. "Installers consuming the file should be able to calculate what to install without the need for dependency resolution at install-time."
- **Scope exclusions, verbatim**: locking build requirements for sdists "was deemed unnecessary"; the format "does NOT fully replace requirements files because: They support specifying installation options at install-time (e.g. `--index-url`, `--constraint`)"; and it "does not solve all potential security concerns."
- Naming: `pylock.toml`, or matching `^pylock\.([^.]+)\.toml$` for multiple lock files.

**Caveat to record honestly:** PEP 751 nowhere says in so many words "do not ship a lockfile in a wheel." My reading — that it is scoped to environment reproduction rather than distribution metadata — follows from the locker/installer framing and the absence of any sdist/wheel inclusion mechanism, but **it is an inference, not a quotation.** Do not present it as a direct prohibition. The Poetry quote above is the one that actually says it.

### 4.2 Why libraries declare ranges and applications pin

**The canonical PyPA framing, and it predates all three tools.** Source: https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/ (accessed 2026-09-12):

- "`install_requires` is a listing of 'Abstract' requirements, i.e just names and version restrictions that don't determine where the dependencies will be fulfilled from"
- requirements files "often contain pip options like `--index-url` or `--find-links` to make requirements 'Concrete.'"
- "`install_requires` requirements are minimal"
- requirements files "often contain an exhaustive listing of pinned versions for the purpose of achieving repeatable installations of a complete environment"
- "`install_requires` defines the dependencies for a single project" whereas "Requirements Files are often used to define the requirements for a complete Python environment"

**The abstract/concrete distinction is the intellectual core of the article.** A library declares *what it can work with* (abstract, a constraint on a solution space). An application declares *what it did work with* (concrete, a point in that space). `pyproject.toml` holds the first; a lockfile holds the second. pixi and Poetry are not competing tools — they are tools for the two halves of that sentence.

**The failure mode when a library pins tightly** (Henry Schreiner, https://iscinumpy.dev/post/poetry-versions/, 2021-12-09, updated 2026-06-09, accessed 2026-09-12): a cap propagates transitively and cannot be overridden downstream. If your dependency caps the Python version, "all Poetry users who depend on your package will have to have a cap on the Python version" — even after the original dependency loosens. His summary of why the practice is indefensible: you "can't predict the future" about what a future release will break.

### 4.3 `pyproject.toml` as the shared file — which table belongs to whom

The clean allocation, all verified this session:

| Table | Owner | Semantics | Source |
|---|---|---|---|
| `[project]` | **the standard** (PEP 621) | Abstract, distributable metadata. Name, version, `dependencies`, `requires-python`, entry points. What a consumer's installer reads. | https://peps.python.org/pep-0621/ |
| `[build-system]` | **the standard** (PEP 517/518) | `requires` + `build-backend`. How a wheel gets built. `poetry-core`, `hatchling`, `setuptools`, `uv_build`. | https://peps.python.org/pep-0517/ |
| `[tool.poetry]` | Poetry | Build-time and packaging specifics with no standard equivalent: `packages`, `include`/`exclude`, `requires-poetry`, `build-constraints`. | https://python-poetry.org/docs/pyproject/ |
| `[tool.pixi.*]` | pixi | The whole environment model: `workspace`, `dependencies` (conda), `pypi-dependencies`, `tasks`, `feature`, `environments`, `target`. | https://pixi.prefix.dev/latest/reference/pixi_manifest/ |
| `[tool.uv]` | uv | `sources` (index routing), `[[tool.uv.index]]`, workspace config. | https://docs.astral.sh/uv/ |

**The rule PEP 621 wrote down, and the sentence the article should build this section around:**

> "No tools may add fields to this table which are not defined by this PEP or subsequent PEPs. For tools wishing to store their own settings in pyproject.toml, they may use the [tool] table"
> — PEP 621, https://peps.python.org/pep-0621/ (accessed 2026-09-12)

The `[tool]` namespace *is* the environment/package boundary, drawn in 2020, before pixi or uv existed. `[project]` is what you publish. `[tool.*]` is how you work. Everything else in this article is a consequence.

The portability argument follows: pydevtools' advice for surviving tool churn is to keep "runtime dependencies in `[project.dependencies]`" and use standardised formats (PEP 621, PEP 735) rather than tool-specific tables. Source: https://pydevtools.com/handbook/explanation/can-you-trust-uv-long-term/ (2026-09-07, accessed 2026-09-12). Same advice insulates you from pixi, Poetry and uv equally.

### 4.4 Can pixi and Poetry coexist in one repo?

**Yes — and pixi documents exactly how, while advising against a specific version of it. Both halves matter.**

Source: https://pixi.prefix.dev/latest/switching_from/poetry/ (accessed 2026-09-12).

**Supported:**
> "You can allow users to use `poetry` and `pixi` in the same workspace, they will not touch each other's parts of the configuration or system."

The mechanism: duplicate the dependency list across the two tables.
> "It's best to duplicate the dependencies, basically making an exact copy of the `tool.poetry.dependencies` into `tool.pixi.pypi-dependencies`."

With one specific rule: ensure "`python` is only defined in the `tool.pixi.dependencies` and not in the `tool.pixi.pypi-dependencies`" — because the interpreter is a conda package in pixi's model, not a PyPI one. **That single line is a beautiful illustration of the article's thesis**: to pixi, Python itself is just another system dependency to be solved for; to Poetry, Python is a constraint declared about the outside world.

**Discouraged:**
> "Mixing `pixi` and `poetry` is advised against"

because they "handle PyPI dependencies differently", risking "unexpected behavior". And: "As you can only use one package manager at a time, it's best to stick to one."

**Read the warning precisely — it is narrower than it first appears.** pixi is warning against *running Poetry inside a pixi environment to install packages* — two resolvers fighting over the same `site-packages`. It is **not** warning against using pixi for the environment and `poetry build`/`poetry publish` for the artefact, which touch entirely disjoint machinery. The docs' own "they will not touch each other's parts of the configuration or system" supports the split-responsibility reading.

**Honest limitation to declare:** I did **not** find a well-known, named open-source repository publicly practising exactly this split (pixi for env, poetry-core for build). The pixi docs describe the configuration, and Jacob Tomlinson independently names the cost — pixi creates "duplication of developer dependencies if you want to support both uv and pixi" (https://jacobtomlinson.dev/posts/2025/python-package-managers-uv-vs-pixi/, 2025-11-18) — which is the same duplication tax the Poetry recipe imposes. **The article should present this as a documented-and-workable pattern with a real maintenance cost, not as a widely-adopted best practice.** If a named exemplar is needed, that is a remaining research task.

**The simpler coexistence that actually needs no duplication:** pixi manages the environment; `[build-system]` names `poetry-core`; `[project]` carries the abstract metadata. `pixi run poetry build` then works because `poetry-core` is a build backend invoked through PEP 517, not a resolver competing for the environment. *(This follows from the documented mechanisms in §2.4 and §1.3 — I did not find it written out as such in any source. Present as reasoning, not citation.)*

---

## 5. Non-Python dependencies — the case conda-forge exists to solve

The general statement, from pixi's own comparison page: "Conda environments contain everything (interpreters, libraries, headers, compilers, CLI tools), all managed by the solver." Source: https://pixi.prefix.dev/latest/switching_from/uv/ (accessed 2026-09-12).

Named examples where PyPI alone is insufficient (https://pydevtools.com/handbook/explanation/when-should-i-choose-pixi-over-uv/, 2026-09-07, accessed 2026-09-12):
- **CUDA and cuDNN** — GPU toolkits
- **GDAL** — geospatial
- **HDF5, NetCDF, FFTW, MKL** — scientific computing libraries
- **R, Julia, Node.js** — non-Python languages
- **OpenCV**

### 5.1 GDAL — the canonical horror story

*(Snippet-level sourcing — see Access and confidence. Verify before quoting specifics.)*

- `pip install gdal` fetches only the **Python bindings**. The C/C++ library and development headers are not on PyPI in installable form for every platform.
- When no wheel matches your platform and Python version, pip falls back to a source build, which requires `libgdal`, its development headers, and the **`gdal-config`** utility on `PATH`. The characteristic failure is `No such file or directory: 'gdal-config'`.
- rasterio's installation docs note GDAL "can be quite complex to build and install, particularly on Windows and MacOS."
- The workaround that is not a fix: `GDAL_CONFIG=/path/to/gdal-config python -m pip install …` — you have moved the problem to "the user must already have GDAL installed", which is precisely the non-reproducibility the exercise was meant to eliminate.
- conda-forge's `conda install -c conda-forge gdal` installs "the complete dependency tree" — library, headers, bindings, in one solve.

Sources (search-snippet level): https://github.com/rasterio/rasterio/blob/main/docs/installation.rst, https://pyogrio.readthedocs.io/en/latest/install.html, https://github.com/OSGeo/gdal/issues/8966, https://anaconda.org/conda-forge/gdal (all surfaced 2026-09-12, **not fetched in full**).

**GDAL is the best example for this article** because the failure is not "slow" or "awkward" — it is a hard build error on a clean machine, and no amount of pinning in `pyproject.toml` prevents it. The missing thing is not a Python package.

### 5.2 PyTorch with CUDA — the interesting, contested case

**Give uv its due here.** As established in §3.8, uv's index routing plus `--torch-backend=auto` handles the common PyTorch case well, and pydevtools recommends **uv** for "PyTorch only". The article weakens itself if it uses PyTorch as a simple pip-fails example, because in 2026 it largely does not.

Where it still breaks (snippet-level, https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/05-managing-cuda-dependencies/index.html and https://discuss.pytorch.org/t/difference-in-pip-install-and-conda-install-pytorch-with-gpu/178832, surfaced 2026-09-12, not fetched in full):
- With pip you encode the CUDA version into the version string (`torch==1.13.1+cu117`) — rigid, and it does not compose with other CUDA-dependent packages.
- conda-forge models CUDA availability as a **virtual package** (`__cuda`), so the solver reasons about the target machine's CUDA rather than you hard-coding it. pixi extends this with declared platform constraints, e.g. `{ name = "jetson-nano", platform = "linux-aarch64", cuda = "12.8" }` (§1.8).
- The genuine break is **mixed GPU stacks**: PyTorch + RAPIDS, where two packages need compatible CUDA runtimes. pydevtools puts these in the "pixi or conda" column precisely because "a single solver pass resolves CUDA conflicts", whereas index routing resolves each package against its own index independently.

**Recommended framing:** PyTorch alone is a solved problem for uv. PyTorch *plus something else that also wants CUDA* is where the single-solver model earns its keep.

### 5.3 HDF5, MKL, compilers, R interop

- **HDF5** and **MKL** appear on the pydevtools list of things uv "cannot install" (§3.8) — C libraries with Python bindings, same shape of problem as GDAL.
- **Compilers** are the structural point: conda-forge ships compilers *as packages*. pixi's claim — "Conda packages are pre-compiled, so you rarely need a build toolchain on your machine" (§1.10) — is the inverse benefit: because the ecosystem builds binaries centrally, the user's machine needs no toolchain at all. PyPI's wheel system does this for Python extension modules but has no mechanism for shipping the *toolchain itself*.
- **R interop** is where the argument stops being about Python: pixi claims "A single Pixi workspace can manage Python, R, C/C++, Rust, Node.js, and more, while uv only handles Python" (§1.10). An analysis that calls R from Python via rpy2 has a dependency graph that `pyproject.toml` structurally cannot express — there is no PyPI package for "R 4.4 with these CRAN packages."
- **The Turing Way** makes the same point about conda from the research-practice side: it is "well-integrated for use with other languages" beyond Python (§6).

### 5.4 The deployment reality (good concrete material)

QuantCo's production write-up (Pavel Zwerschke, 2024-07-11, https://tech.quantco.com/blog/pixi-production/, accessed 2026-09-12) is useful because it reports costs, not just benefits:

- Docker image sizes through successive optimisations: **691MB naive → 402MB** (drop the rattler cache) **→ 363MB** (multi-stage, drop the pixi binary) **→ 265MB** (production-only environment, not the dev one) **→ 209MB** (distroless base).
- Real constraints: conda environments are **"not relocatable"** — identical paths needed at build and runtime. **Alpine cannot host conda environments** because it uses "musl instead of glibc". Distroless images lack the shell that activation scripts need.
- `pixi-pack` for non-container deployment: "a simple tool that takes a pixi environment and packs it into a compressed archive."
- On the older tools: conda-pack archives may contain "files that are not in a 'clean' environment", producing non-reproducible artefacts; and "conda doesn't allow us to install Windows environments on Linux and vice versa."

**The 265MB-vs-363MB step is a nice detail**: the saving comes from having declared *separate environments* (dev vs production) from the same manifest — a capability that only exists because pixi models environments as first-class composable objects (§1.3, features/environments).

---

## 6. The Turing Way

**URL correction: the brief's `the-turing-way.netlify.app` 301-redirects to `book.the-turing-way.org`.** Cite the new domain.

### 6.1 The four definitions (verbatim)

Source: https://book.the-turing-way.org/reproducible-research/overview/overview-definitions (accessed 2026-09-12).

> **Reproducible:** "A result is reproducible when the _same_ analysis steps performed on the _same_ dataset consistently produces the _same_ answer."

> **Replicable:** "A result is replicable when the _same_ analysis performed on _different_ datasets produces qualitatively similar answers."

> **Robust:** "A result is robust when the _same_ dataset is subjected to _different_ analysis workflows to answer the same research question (for example one pipeline written in R and another written in Python) and a qualitatively similar or identical answer is produced."

> **Generalisable:** "Combining replicable and robust findings allow us to form generalisable results."

The 2×2:

| | Same data | Different data |
|---|---|---|
| **Same analysis** | Reproducible | Replicable |
| **Different analysis** | Robust | Generalisable |

**Why this matters to the thesis, and it is worth being explicit about in the article:** *only the top-left cell is a tooling problem.* Reproducibility — same data, same analysis, same answer — is exactly what a lockfile delivers and exactly the whole of what it delivers. Robustness requires a *different* environment by definition (the R pipeline and the Python pipeline). A researcher who believes `pixi.lock` is making their work robust has confused the cells. That is a genuinely useful thing to tell this audience, and it is the strongest reason the environment/package distinction is not pedantry.

### 6.2 On environments and package management

Source: https://book.the-turing-way.org/reproducible-research/renv (accessed 2026-09-12). The landing page enumerates the options — **package management systems, YAML, virtual machines, containers, BinderHub** — and frames the requirement as needing to "capture, preserve and share computational environments and code to ensure research is reproducible." **It does not, on that page, state a single recommendation**; the comparative material lives in the subsections.

Source: https://book.the-turing-way.org/reproducible-research/renv/renv-package (accessed 2026-09-12). The package-management subsection centres on **Conda**:

> "Conda allows users to create any number of entirely separate environments"

Cited advantages: works without "admin privileges on the machines they are working on"; "well-integrated for use with other languages"; and "Conda environments can be exported easily to human-readable files in the YAML format".

**The mixing warning**, which the article can use to good effect:
> "running Conda after pip may potentially overwrite or break packages installed via pip"

with the recommendation to install "as many requirements as possible with Conda, and then use pip".

**Two observations for the article, stated as observations not facts about the text:**

1. That ordering rule — conda first, then pip, and never conda again — is *precisely the algorithm pixi automated* (§1.5: resolve conda, map names, resolve PyPI with conda packages held locked). pixi's core mechanism is a hand-written Turing Way best practice turned into a solver invariant. **That is a genuinely strong paragraph for the article.**

2. The Turing Way's recommended artefact is an exported **YAML environment file**, which is a *specification*, not a *lock*: it records what you asked for, not what you got, and re-solving it next year gives different packages. The gap between `environment.yml` and `pixi.lock` is the gap between "reproducible in principle" and "reproducible in fact" — and it is the gap the whole tooling generation of 2024–2026 was built to close.

**Caveat:** I fetched two Turing Way pages. I did **not** check whether newer sections of the book now discuss pixi, uv, or PEP 751. Given the book is community-maintained and actively updated, **check before writing that it "recommends conda"** — that is accurate for the page I read, and may be out of date relative to the book as a whole.

### 6.3 Quotable fragments, all under 15 words

- "Conda allows users to create any number of entirely separate environments" (The Turing Way)
- "running Conda after pip may potentially overwrite or break packages installed via pip" (The Turing Way)
- "the _same_ analysis steps performed on the _same_ dataset consistently produces the _same_ answer" (The Turing Way, on reproducible)
- "Pixi fully supports PyPI packages alongside conda packages, powered by uv under the hood" (pixi docs)
- "The application ignores your library's lock file." (Poetry docs)
- "The uv.lock format is specific to uv and not usable by other tools." (uv docs)
- "Mixing `pixi` and `poetry` is advised against" (pixi docs)

---

## 7. Counter-arguments

### 7.1 Against pixi

**Finding to report honestly: sustained, well-argued public criticism of pixi is scarce.** I ran several searches aimed at HN, Reddit and critical blogs; nearly everything written about pixi is positive or promotional, much of it from prefix.dev itself. That absence is itself worth one sentence in the article — an ecosystem with no critics usually means an ecosystem without enough users yet, not a tool without flaws.

What genuine criticism exists:

1. **Pre-1.0 maturity.** pixi is at **v0.80.0** (§1.1); pydevtools notes both pixi and uv are pre-1.0 while "conda has 14+ years of production history", describing them as "different points on the maturity spectrum" rather than a simple win. Source: https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ (2026-09-07, accessed 2026-09-12).

2. **conda-forge dependence is the whole value proposition and the whole risk.** pixi's advantages all reduce to "conda-forge has the packages" (§1.10). If a package is not packaged for conda-forge, pixi's advantage evaporates and you are back in `[pypi-dependencies]`. The article should state this plainly: **pixi's moat is somebody else's volunteer-maintained package collection.**

3. **The two-solver seam is real and documented by pixi itself.** Conda-first resolution followed by a PyPI pass can fail where a single solve would not — pixi's own worked example is `typing-extensions==4.15.0` (conda) against `typing-extensions==4.14` (PyPI). Source: https://pixi.prefix.dev/latest/concepts/conda_pypi/ (accessed 2026-09-12).

4. **Manifest lock-in.** `pixi.toml` "isn't portable to other tools", though "using `[tool.pixi]` preserves standard metadata." Source: https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ (accessed 2026-09-12). **Be fair: this applies identically to `uv.lock` (§3.3) and `poetry.lock`.** No lockfile in current use is portable; PEP 751 exists because of this.

5. **Awkwardness for PyPI-first work, and a duplication tax.** Jacob Tomlinson: pixi feels "awkward being a conda first project" for mostly-PyPI work; supporting both uv and pixi causes "duplication of developer dependencies"; the manifest-path approach is "clunky" for interdependent projects. Source: https://jacobtomlinson.dev/posts/2025/python-package-managers-uv-vs-pixi/ (2025-11-18, accessed 2026-09-12).

6. **Deployment friction inherited from conda**, per QuantCo (§5.4): environments "not relocatable"; no Alpine/musl; distroless needs shell workarounds; large Docker layers.

7. **Commercial alignment.** prefix.dev is a company selling conda channel hosting — "Channel Hosting on prefix.dev is now generally available" — with pricing tiers and API keys. Source: https://prefix.dev/ (accessed 2026-09-12). pixi is BSD-3-Clause and genuinely open, so this is not a licensing risk; but a free tool that makes hosted private conda channels more valuable has a commercial logic worth naming. **Note for balance: this is structurally the same critique as Astral/pyx (§7.3), and the article should apply it evenly or not at all.**

8. **Reported bugs around lockfile staleness**, e.g. prefix-dev/pixi#5256 (lockfile reported out of date with `--locked` even after `pixi lock`) and #3915 (lock file not up to date after fresh update, with a CUDA system dependency). *(Surfaced via search; issue bodies not fetched. Verify status before citing — these may be fixed.)*

**Not found, and I looked:** any substantial argument that pixi's reproducibility guarantees are weaker than claimed, or any notable project publicly migrating *away* from pixi.

### 7.2 Against Poetry

1. **Slow resolution — conceded by Poetry itself.** The FAQ's explanation: "not all libraries on PyPI have properly declared their metadata and, as such, they are not available via the PyPI JSON API", forcing Poetry to download and inspect packages. Source: https://python-poetry.org/docs/faq/ (accessed 2026-09-12). **Be fair to Poetry here**: this is a real property of PyPI, not incompetence; and uv faces the same metadata gaps but mitigates them aggressively (0.12.13's PEP 658 metadata handling, §3.1, is exactly this work).

2. **Default upper-bound capping — the substantive standards complaint.** Henry Schreiner (https://iscinumpy.dev/post/poetry-versions/, 2021-12-09, updated 2026-06-09, accessed 2026-09-12):
   - `poetry add <package>` "automatically use[s] `^<latest>`", and new projects get caret caps on pytest and on Python itself by default.
   - The propagation problem: cap Python in a library and "all Poetry users who depend on your package will have to have a cap on the Python version", even after the upstream loosens. You "can't predict the future."
   - On metadata: "a tool that lets you produce PyPI packages should not force you to set a metadata slot as important as `Requires-Python` based on a lock file you are not even including in the package."
   - He dismisses Poetry's FAQ justification as "invalid", and calls the JS-borrowed practice "completely impossible and destructive" in Python's shared-dependency ecosystem.

   **This quote is the single best citation in the file for the article's thesis**, because it is exactly the environment/package confusion: Poetry let a fact about *one developer's environment* leak into *published package metadata* that constrains everyone downstream.

   Poetry's own defence, for fairness: "The `^` operator works very well with libraries following semantic versioning", and the FAQ acknowledges the genuine trade-off — unbounded `>=3.4` avoids conflicts but risks breakage; `^3.4` protects against breakage but blocks users from compatible newer versions until you cut a release. Source: https://python-poetry.org/docs/faq/ (accessed 2026-09-12).

   Community pressure is long-standing: python-poetry/poetry#3747, "please stop pinning to major versions by default / forcing SemVer, especially for Python itself", opened by NickleDave 2021-03-03, now **closed**. The argument: there is "no reason to assume that 4.0 will be drastically different from 3.x", cascading pins cause `SolverProblemError`, and `>=` should be the default. Source: https://github.com/python-poetry/poetry/issues/3747 (accessed 2026-09-12). *(I did not determine how it was closed — fixed, or closed as wontfix. Check before characterising the outcome.)*

3. **Four years late to PEP 621.** The standard was Final in 2020; Poetry shipped `[project]` support in **2.0.0 on 2025-01-05** (§2.5). Schreiner's characterisation is that Poetry resisted, claiming its own system was "better" than an open standard its developers had helped write. Sources: https://peps.python.org/pep-0621/, https://python-poetry.org/history/, https://iscinumpy.dev/post/poetry-versions/ (all accessed 2026-09-12). **Credit where due: Poetry 2.x has now largely corrected this**, deprecating the `[tool.poetry]` equivalents in favour of `[project]`.

4. **PEP 517 enforcement with no escape hatch.** Users have reported install failures under Poetry's PEP 517 enforcement with no option to disable it (python-poetry/poetry#10294, #6453). *(Search-snippet level; issues not fetched. Verify.)*

5. **PyPA does not single Poetry out.** The packaging guide names Poetry, Hatch and PDM as build backends but states it "does not seek to steer the reader towards a particular tool, only to enumerate common tools", and names **`build`** as "The standard tool to build source distributions and wheels for uploading to PyPI", with **Trusted Publishing** preferred for upload and twine as the manual alternative. Source: https://packaging.python.org/en/latest/guides/tool-recommendations/ (accessed 2026-09-12). **Notably, that page did not mention uv or pixi in what I fetched** — worth flagging that the official guide lags the tools people actually use. *(Medium confidence: the fetch may have been truncated. Re-check before asserting an omission.)*

### 7.3 Against "just use uv for everything"

This is the position the article most needs to engage, because it is currently the default opinion.

1. **It cannot install non-Python dependencies. This is architectural, not a roadmap item.** uv resolves from PyPI, Git, paths and private indexes; "It cannot install non-Python dependencies like the CUDA toolkit, GDAL, or HDF5." Source: https://pydevtools.com/handbook/explanation/uv-vs-pixi-vs-conda-for-scientific-python/ (2026-09-07, accessed 2026-09-12). No amount of uv development changes this without uv becoming a conda client — and the piece of pixi that talks to PyPI *is already uv* (§1.10).

2. **OpenAI acquired Astral — and the sources disagree on when.**
   - Simon Willison: the acquisition was **announced 2026-03-19**. Astral said "OpenAI will continue supporting our open source tools after the deal closes"; OpenAI said it would "support Astral's open source products" while accelerating Codex. Source: https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/ (accessed 2026-09-12).
   - pydevtools states "OpenAI acquired Astral in **May 2026**". Source: https://pydevtools.com/handbook/explanation/can-you-trust-uv-long-term/ (2026-09-07, accessed 2026-09-12).
   - **Most likely announced in March and closed in May** (Willison's own wording is "after the deal closes"), but **I did not verify the closing date.** If the article states a date, say "announced March 2026" and cite Willison, or give both.

   Willison's concerns, worth representing accurately:
   - Whether OpenAI might use ownership of uv as leverage against competitors in the coding-agent market.
   - **pyx**, Astral's private package registry — its commercial product — was "notably absent from announcements."
   - OpenAI has little track record maintaining acquired open-source projects.
   - The mitigation is permissive licensing: a "fork and move on" safety valve, which Willison notes "remains theoretical."
   - Scale of the stakes: uv has been downloaded **126 million times monthly** since February 2024, making it "genuinely load-bearing infrastructure."

3. **The counter-case, which the article should give fairly.** pydevtools' post-acquisition assessment (2026-09-07): uv "is dual-licensed under Apache 2.0 and MIT" and "That license cannot be revoked"; "uv, Ruff, and ty all stayed open source through the transition and uv's release cadence held" — and 0.12.13 landing on 2026-09-10 (§3.1) corroborates that the cadence is still intact. Maintaining a fork is "a much smaller job, well within reach of a handful of paid maintainers or a corporate sponsor", as pip and virtualenv demonstrate. Their stated watch-list: licence unchanged, bug-fix pace held, continued standards work (PEP 723, PEP 751), and no "opaque telemetry or closed components". Source: https://pydevtools.com/handbook/explanation/can-you-trust-uv-long-term/ (accessed 2026-09-12).

4. **uv has its own lock-in, by its own admission.** "The uv.lock format is specific to uv and not usable by other tools." Source: https://docs.astral.sh/uv/concepts/projects/layout/ (accessed 2026-09-12). Anyone criticising pixi for lock-in must apply the same standard here. The standards answer to both is **PEP 751 / `pylock.toml`** (§4.1).

5. **Practical drawbacks**, from Bite Code! (2025-02-15, https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should, accessed 2026-09-12) — a broadly pro-uv piece, which makes its complaints more credible:
   - Cannot resolve dependencies in some older codebases
   - "limited to the versions of Python that have been built"
   - Cache growth: "more than 20Gb" after a year
   - Blocked in locked-down enterprise environments
   - CLI-only, a barrier for non-technical users
   - Astral "not profitable yet" *(written pre-acquisition; now superseded by §7.3.2 — note the irony that the sustainability worry resolved into a different worry)*
   - `uvx` can break when tools need specific Python versions

6. **`uv pip` inherits pip's problems.** Jacob Tomlinson: "uv pip still has many of the problems that pip has", because it reimplements pip's interface directly. Source: https://jacobtomlinson.dev/posts/2025/python-package-managers-uv-vs-pixi/ (2025-11-18, accessed 2026-09-12). Speed does not fix a semantics problem.

7. **No task runner.** Both Tomlinson and pixi's docs note uv lacks one. For an *analysis* — the article's core use case — the environment is only half the reproducibility story; the commands that were run are the other half, and uv has no answer for that (§1.6).

8. **The broader structural worry** raised in community writing: a VC-funded Rust tool became load-bearing for millions of Python installs and was then absorbed by a company with unrelated strategic goals, concentrating uv, ruff and ty under one owner and raising supply-chain and neutrality questions for the Python build ecosystem. *(Search-snippet level, from dev.to and dasroot.net posts I did not fetch in full — treat as representative sentiment rather than citable analysis. Willison, §7.3.2, is the source to actually cite.)*

---

## 8. Synthesis for the article

### The boundary, five lines

1. **An environment is a machine state you recreate; a package is an artefact you distribute.** One is reproduced, the other is consumed.
2. **Environments are pinned exactly — versions, hashes, per-platform, including non-Python libraries — because there is exactly one right answer: the one that worked.** That artefact is a lockfile (`pixi.lock`, `uv.lock`, `poetry.lock`, `pylock.toml`).
3. **Packages declare loose ranges, because the right answer belongs to whoever installs them, and you cannot know their other dependencies.** That artefact is `[project]` metadata inside a wheel.
4. **A lockfile shipped in a library is not dangerous, it is inert** — "The application ignores your library's lock file" (Poetry docs) — while a library's exact pin *is* dangerous, because upper bounds propagate transitively and cannot be overridden downstream (Schreiner).
5. **`pyproject.toml` is one file with two owners, and PEP 621 drew the line in 2020: `[project]` is what you publish, `[tool.*]` is how you work.** pixi lives in `[tool.pixi]`, uv in `[tool.uv]`, Poetry's build config in `[tool.poetry]` and `[build-system]` — so pixi managing the environment and poetry-core building the wheel is not a hack, it is the design.

### Where the sources disagree

| Question | Position A | Position B |
|---|---|---|
| Astral acquisition date | Announced 2026-03-19 (Willison) | "May 2026" (pydevtools) — likely close vs announce |
| Is uv enough for scientific Python? | Yes for PyTorch-only (pydevtools) | No for mixed GPU stacks / native libs (pydevtools, pixi, Tomlinson) — *same source, different scenarios* |
| Should libraries commit a lockfile? | "you may commit it if you want to", as a CI aid (Poetry) | Libraries should test across versions, so a lock works against you (pixi docs) |
| Can pixi and Poetry coexist? | "they will not touch each other's parts" (pixi docs) | "Mixing pixi and poetry is advised against" (pixi docs, same page) — the warning is about *resolvers*, not about *building* |
| Is uv's 10–100x real? | Astral homepage claim | Unverifiable from published benchmarks (charts are images); independent figures cluster nearer 8–30x |

### Strongest quotes (all under 15 words, attributed)

1. "The application ignores your library's lock file." — Poetry docs
2. "Pixi fully supports PyPI packages alongside conda packages, powered by uv under the hood." — pixi docs
3. "The uv.lock format is specific to uv and not usable by other tools." — uv docs
4. "running Conda after pip may potentially overwrite or break packages installed via pip" — The Turing Way
5. "Mixing `pixi` and `poetry` is advised against" — pixi docs
6. "System dependencies included. Need CUDA, OpenSSL, compilers, or C libraries? Conda packages bundle them." — pixi docs

### Remaining research gaps

- A named, real open-source repo using pixi-for-env + poetry-core-for-build (§4.4).
- Numeric figures from Astral's own benchmarks (charts are images) (§3.4).
- A methodologically sound independent uv-vs-Poetry benchmark (§3.4).
- The comment thread on conda/conda-lock#615 — the conda ecosystem's own reservations about pixi (§7.1).
- PEP 518 read directly (§2.5).
- Status of `uv_build` as a build backend (§3.5).
- Whether The Turing Way's newer sections now cover pixi/uv/PEP 751 (§6.2).
- Resolution of python-poetry/poetry#3747 — fixed or wontfix (§7.2).
