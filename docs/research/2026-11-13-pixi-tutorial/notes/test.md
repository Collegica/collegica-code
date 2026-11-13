# Test run: the article's steps, from an empty folder

Run on 13 November 2026, following the article as a reader would, in a temp
folder outside the repository (deleted afterwards). Times are wall-clock from
`time`, rounded. Output is trimmed; nothing is paraphrased.

## Machines

| | Where | pixi | What ran |
|---|---|---|---|
| A | macOS, Apple silicon (`osx-arm64`) | 0.78.0, the installed copy | every step below |
| B | Linux `x86_64` in Docker on the same Mac (`--platform linux/amd64`, emulated), image `ghcr.io/prefix-dev/pixi:0.78.0`, Ubuntu 24.04 | 0.78.0 | the teammate step: `pixi install --locked`, `pixi run analyse`, `pixi run test` against the lockfile made on A |
| C | Same as B, image `ghcr.io/prefix-dev/pixi:0.84.2` | 0.84.2 (current release) | the lockfile from A with `--locked`, then every step again from an empty folder |
| — | Windows | — | **not run** |

pixi 0.84.2 could not be run natively on the Mac: running a downloaded binary
outside a container was refused by the session's permissions, and the
installed 0.78.0 was not to be upgraded. C is the substitute.

### Caches

The machine already had a pixi package cache. To get honest first-time
numbers on A, every command ran with a fresh, empty cache:

```bash
export PIXI_CACHE_DIR=<tmp>/cache RATTLER_CACHE_DIR=<tmp>/cache UV_CACHE_DIR=<tmp>/cache/uv
```

The teammate step used a second empty cache. One aside, not a reader-facing
issue: giving `PIXI_CACHE_DIR` as a *relative* path (`../cache`) made 0.78.0
panic (`Tokio executor failed, was there a panic?`). With an absolute path it
was fine.

## Step 1. Create the workspace (A)

```console
$ pixi init river-gauges
✔ Created …/river-gauges/pixi.toml
[0.1 s]
```

Created `pixi.toml`, `.gitignore`, `.gitattributes`. **No `pixi.lock` yet**
(the 2025 draft showed one at this point). `pixi.toml`:

```toml
[workspace]
authors = ["<name> <email>"]   # filled in from the local git config
channels = ["conda-forge"]
name = "river-gauges"
platforms = ["osx-arm64"]
version = "0.1.0"

[tasks]

[dependencies]
```

Differences from the draft: the table is `[workspace]`, not `[project]`;
there is no `description`; `platforms` is **only the current machine**, not
three; `authors` is copied from git config (replaced by a made-up
`Sam Rivera <sam@example.com>` in the committed example).

`.gitignore`: `.pixi/*` and `!.pixi/config.toml`.
`.gitattributes`: `pixi.lock merge=binary linguist-language=YAML linguist-generated=true -diff`.

## Step 2. Add platforms (A)

```console
$ pixi workspace platform add linux-64 win-64
✔ Added linux-64
✔ Added win-64
[0.1 s]
```

`platforms = ["osx-arm64", "linux-64", "win-64"]`.

## Step 3. conda-forge packages (A)

```console
$ pixi add python gdal opencv
✔ Added python >=3.15.2,<3.16
✔ Added gdal >=3.13.3,<4
✔ Added opencv >=5.0.0,<6
[5.0 s, empty cache; 910 MB downloaded into the cache, 797 MB environment]
```

The draft added `gdal` and `opencv` without `python`. pixi's manifest
reference says Python must be a conda dependency when there are PyPI
dependencies, so it is added here explicitly.

## Step 4. PyPI packages (A)

```console
$ pixi add --pypi pandas scikit-learn
✔ Added pandas >=3.1.1, <4
✔ Added scikit-learn >=1.9.1, <2
Added these as pypi-dependencies.
[3.0 s]
```

`pixi list` afterwards: `numpy 2.5.4 … conda`, `pandas 3.1.1 … pypi`,
`scikit_learn 1.9.1 … pypi`, `scipy 1.18.1 … pypi`. numpy came from
conda-forge (GDAL and OpenCV need it) and pandas used that copy.

## Step 5. Check the imports (A)

```console
$ pixi run python --version
Python 3.15.2
$ pixi run python -c "import gdal"
ModuleNotFoundError: No module named 'gdal'
$ pixi run python -c "from osgeo import gdal; import cv2, pandas, sklearn; print(gdal.__version__, cv2.__version__, pandas.__version__, sklearn.__version__)"
3.13.3 5.0.0 3.1.1 1.9.1
$ pixi run python -m pip --version
…/.pixi/envs/default/bin/python: No module named pip
```

Two draft claims fail: `import gdal` (the module is `osgeo.gdal`), and
"use pip inside `pixi shell`" (conda-forge's Python here has no pip).

## Step 6. Script, data, task (A)

`analyse.py`, `data/gauges.csv` (eight made-up gauges) written as in the
article.

```console
$ pixi task add analyse "python analyse.py" --description "Grid the gauge readings into a GeoTIFF and a picture"
✔ Added task `analyse`: python analyse.py, description = "Grid the gauge readings into a GeoTIFF and a picture"
$ pixi run analyse
✨ Pixi task (analyse): python analyse.py: (Grid the gauge readings into a GeoTIFF and a picture)
8 gauges, flow 2.6 to 16.0 m3/s
Flow rises 0.035 m3/s per km2 of catchment (R squared 0.96)
Wrote output/flow.tif: 50 x 50 cells, EPSG:4326, mean flow 8.0 m3/s
Wrote output/flow.png
```

`file output/*`: PNG 400 x 400 RGB; TIFF 50 x 50, 32-bit float.

GDAL's command-line tools come with the package:

```console
$ pixi run gdalinfo -stats output/flow.tif
Driver: GTiff/GeoTIFF
Size is 50, 50
    ID["EPSG",4326]]
  Minimum=2.605, Maximum=15.995, Mean=7.987, StdDev=3.340
```

(`-stats` leaves a `flow.tif.aux.xml` beside the file.)

## Step 7. `pixi shell` (A)

`pixi shell` is interactive; piping commands into it from a script hung and
was stopped. The same activation, through `pixi shell-hook`, was checked
instead:

```console
$ eval "$(pixi shell-hook)"; which python; python -c "import cv2; print(cv2.__version__)"
…/river-gauges/.pixi/envs/default/bin/python
5.0.0
```

## Step 8. Task caching (A)

`inputs` and `outputs` added to the task by hand (final form in
`example/pixi.toml`).

```console
$ pixi run analyse        # output/ deleted first
Wrote output/flow.png
$ pixi run analyse
✨ Pixi task (analyse): python analyse.py: (Grid the gauge readings into a GeoTIFF and a picture)
Task 'analyse' can be skipped (cache hit) 🚀
```

## Step 9. A dev environment with pytest (A)

```console
$ pixi add --feature dev pytest
✔ Added pytest
Added these only for feature: dev
⚠️ The feature dev is not used in any environment, so the added dependencies were not resolved or pinned
  Add it to an environment with `pixi workspace environment add <environment> --feature dev`
  Then run `pixi upgrade --feature dev pytest` to resolve and pin the dependencies
$ pixi workspace environment add dev --feature dev
✔ Added environment dev
$ pixi upgrade --feature dev pytest
[1.0 s]  → pytest = ">=9.2.0,<10"
$ pixi task add --feature dev test "python -m pytest -q tests"
✔ Added task `test`: python -m pytest -q tests
$ pixi run test
✨ Pixi task (test in dev): python -m pytest -q tests
..                                                                       [100%]
2 passed
```

The order matters: `pixi workspace environment add dev --feature dev` run
*before* the feature exists fails with `the feature 'dev' is not defined in
the project manifest` (checked in a throwaway workspace). Without the
`upgrade`, pytest stays as `"*"`. `pixi run test` picks the `dev` environment
by itself because the task exists only there.

## Step 10. The lockfile

`pixi.lock`: 397 KB, 10,398 lines, `version: 7`. Default environment:

| Platform | conda packages | PyPI packages |
|---|---:|---:|
| `osx-arm64` | 164 | 9 |
| `linux-64` | 223 | 9 |
| `win-64` | 144 | 10 |

Linux uses OpenCV's `qt6` build, macOS the `headless` build; same version.

**Unexplained, not tested:** on `win-64` the lockfile lists numpy twice:
the conda-forge `numpy-2.5.4` *and* the PyPI wheel
`numpy-2.5.4-cp315-cp315-win_amd64.whl`. On the other two platforms numpy
is conda-only. pixi's docs say conda wins when both are present; without a
Windows machine this could not be checked. Recorded in the README as not
verified.

## Step 11. A teammate's machine

Copied only `pixi.toml`, `pixi.lock`, `analyse.py`, `data/`, `tests/` to a
fresh folder, empty cache.

**A (macOS):**

```console
$ pixi install --locked
✔ The default environment has been installed.
[5.2 s]
$ pixi run analyse
… same four lines as step 6 …
[39.9 s]
$ pixi run test
2 passed in 31.66s
[36.7 s]
$ pixi run analyse          # second time, output/ deleted
[2.2 s]
```

The first Python run after installing a fresh environment took 30 to 40
seconds on this Mac, the second about 2. The first run in step 6 had been
preceded by step 5's imports, which absorbed it. The cost is in the first
import of the new native libraries, not in pixi (`pixi run python -c pass`:
0.04 s).

`cmp` of `pixi.lock` before and after: unchanged.

**B (Linux x86_64, pixi 0.78.0):** `pixi install --locked`, then
`pixi run analyse` (7 s) and `pixi run test` (`2 passed in 4.45s`). Same
four lines of output. `output/flow.tif` was **byte-identical** to the one
made on macOS (`cmp`). Whole container run: 50 s.

**C (Linux x86_64, pixi 0.84.2):** the 0.78.0 lockfile passed
`pixi install --locked` (7.5 s) and `pixi run analyse` gave the same output.
0.84.0's release notes warn that older lockfiles "may need to have hashes
updated by `pixi lock`"; this one did not. Linux printed one warning, on
both versions:

```
WARN Skipped running the post-link scripts because `run-post-link-scripts` = `false`
	- bin/.gdk-pixbuf-post-link.sh
```

(from OpenCV's Qt build pulling in gdk-pixbuf; harmless for this project).

Then every step from an empty folder on 0.84.2: same commands, same
messages apart from the ✔ marks, same resolved versions (python 3.15.2,
gdal 3.13.3, opencv 5.0.0, pandas 3.1.1, scikit-learn 1.9.1, pytest 9.2),
same output, `2 passed`. Times: `add python gdal opencv` 3.1 s, `add --pypi`
2.3 s, `run analyse` 3.5 s, `run test` 5.6 s. (No ✔ marks because the output
was not a terminal.) The image has no git, so `pixi init` wrote no `authors`
line. On Linux the starting platform is `linux-64`, so this step added
`osx-arm64 win-64` instead.

## Draft commands that fail on 0.78.0

| Draft | Result | In the article |
|---|---|---|
| `[project]` table | `pixi init` writes `[workspace]`; `[project]` is the deprecated alias | `[workspace]` |
| `pixi.lock` after `pixi init` | not created until the first solve | said so |
| three platforms by default | only the current one | `pixi workspace platform add` |
| `import gdal` | `ModuleNotFoundError` | `from osgeo import gdal` |
| `pixi add gdal --channel conda-forge` | `error: unexpected argument '--channel' found` | dropped |
| `pip install` inside `pixi shell` | no pip in the environment | dropped; `pixi add --pypi` |
| `depends_on` | docs use `depends-on` | not used |
| `pixi --version` → 0.28.1 | 0.78.0 here, 0.84.2 current | one dated note |
| `download-sample` task fetching a GeoTIFF from GDAL's repo | not needed; no downloads | eight-line CSV |

## Also checked

`pixi search gdal` works (`gdal-3.13.3 … (+ 194 builds)`), 1.2 s.

PyPI, to support the comparison: `uv pip install gdal` in a throwaway
virtualenv (uv 0.10.12, the copy on this machine, not the latest) fails in
1.2 s with `Could not find gdal-config. Make sure you have installed the GDAL
native library and development headers.` PyPI's GDAL 3.13.3 is a source
archive only (`gdal-3.13.3.tar.gz`, no wheels); its description lists
`libgdal` and SWIG as build requirements. OpenCV, by contrast, ships wheels
on PyPI (`opencv-python 5.0.0.93`, 9 files). Poetry is not installed here and
was not run; it installs the same source archive from PyPI.
