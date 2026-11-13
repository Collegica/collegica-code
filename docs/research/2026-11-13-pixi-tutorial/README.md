# pixi tutorial: research and test run

Notes behind [*Your First Project with
pixi*](https://www.collegica.org/python/pixi/) and its
[slides](https://www.collegica.org/slides/python/pixi/). Started and finished
13 November 2026, from the draft in issue #1 (written November 2025 for a
January 2026 date that passed).

## Access and confidence

| | |
|---|---|
| **Run, not read** | Every step of the article, from an empty folder, on macOS (Apple silicon) with pixi 0.78.0. The teammate step (install from the lockfile, run, test) also on Linux x86_64 in Docker with 0.78.0. Every step again on Linux x86_64 with pixi 0.84.2, the current release. Log: [`notes/test.md`](notes/test.md). |
| **Read** | pixi's documentation and release notes 0.78.0 to 0.84.2; PyPI's file lists for GDAL and opencv-python; Poetry's repositories page. All on 13 November 2026. List: [`notes/sources.md`](notes/sources.md). |
| **Not run** | Windows. Native macOS with 0.84.2: the session could not run a downloaded binary outside a container, and the installed 0.78.0 was not to be upgraded. Poetry: not installed. `pixi global`: would change the machine's setup. |
| **Confidence** | High for the commands and output shown in the article, which are copied from the run. High that the lockfile works on Linux x86_64 (emulated on Apple silicon, so speed figures there mean little). Medium for Windows: the lockfile solves for `win-64`, nothing more is known. |
| **Owner details** | `pixi init` copied the local git name and email into `authors`; the committed example uses a made-up `Sam Rivera <sam@example.com>`. |

## What was tested and how

A temp folder outside the repository, an **empty package cache** (so the
first-install times are real, not cache hits), and the article's commands
typed in its order. Afterwards a second folder holding only the files the
article says to commit, with another empty cache, stood in for a
colleague's machine. The same set of files was mounted into
`ghcr.io/prefix-dev/pixi:0.78.0` and `:0.84.2` containers run as
`linux/amd64`. Temp folders and the containers were deleted afterwards.

Results that changed the article:

- `pixi init` writes `[workspace]`, one platform, and no lockfile.
- `python` must be added from conda-forge before any `--pypi` package.
- `import gdal` fails; it is `from osgeo import gdal`.
- `pixi add --channel` does not exist.
- There is no pip in the environment, so the draft's pip fallback fails,
  as well as being bad advice.
- Feature, environment and pin need three commands in a fixed order.
- The first Python run after a fresh install took 30 to 40 s on the Mac,
  then 2 s.
- The Linux GeoTIFF was byte-identical to the Mac's.

The finished project is [`example/`](example/): `pixi.toml`, `pixi.lock`
(made by 0.78.0 on macOS; accepted by `--locked` on 0.84.2), `analyse.py`,
an eight-line CSV of invented gauges, and a two-test pytest file. To run it:
`cd example && pixi install --locked && pixi run analyse && pixi run test`.

## Decisions

1. **A new example instead of the draft's.** The draft downloaded a
   GeoTIFF from GDAL's repository and only read it. Now an eight-line CSV
   in the repository is the whole input, and the script exercises all
   four libraries the title promises (GDAL writes, OpenCV smooths,
   scikit-learn fits, pandas reads). Nothing is downloaded but packages.
2. **Kept:** the aim (conda-forge plus PyPI, tasks, lockfile, three
   platforms), the links to the Substack comparison and the Poetry guide.
3. **Cut, as untested or wrong:** the pip/uv "escape hatch" section and its
   `requirements-pip.txt` pattern (pip is absent, and installs outside the
   lockfile defeat the point); the CUDA/PyTorch environment example; the
   "Coming soon" series list; the template repository link (it did not
   exist); timing claims ("15 minutes", "~1 second ⚡", uv 3 s vs pip 45 s);
   the community links and placeholder social links; the "Use pixi when …
   / Use Poetry when …" lists, replaced by a link to *Environments Are Not
   Packages*, which covers it with sources.
4. **Corrected:** OpenCV does have wheels on PyPI; GDAL does not. The article
   says so rather than implying both need conda.
5. **Added:** task `inputs`/`outputs` caching, `--locked`, a test in a `dev`
   feature, what to do on a lockfile merge conflict, `pixi.toml` vs
   `pyproject.toml`.
6. **One dated place for versions:** a callout near the top. Output blocks
   keep the real version numbers from the run, and the callout says they
   will differ.
7. **0.82.1 is a security release.** The article tells readers to install
   the current version even though the main run used 0.78.0.

## Not covered, or not verified

- **Windows** not run. The `win-64` part of the lockfile lists numpy from
  both conda-forge and PyPI (the other platforms only from conda-forge).
  pixi's docs say conda wins duplicates; not checked on a Windows machine.
- `pixi shell` was not used interactively; the same activation was checked
  through `pixi shell-hook`.
- The lockfile merge-conflict advice (keep either side, then `pixi lock`)
  follows from how `pixi lock` and `.gitattributes` work; pixi's docs do not
  discuss conflicts and it was not exercised.
- `pixi global`, conda package building, GPUs: mentioned or left out, not
  tested.
- Poetry was not run. The claim about it is limited to "installs from PyPI",
  from its docs.
- **Public copy:** the article links to this folder on
  `Collegica/collegica-code`. It needs an entry in
  `scripts/collegica-code/manifest.yml` before the article is published,
  or the link is a 404. Not added here (outside this change's scope).
