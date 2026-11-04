# bocrates — a minimal reproducible analysis

The worked example from [Python for Reproducible
Research](https://www.collegica.org/python/reproducible-research/). Eleven files,
nothing hidden, and a reader can run it.

**Question:** what was the average Bank of Canada overnight rate each year?

## Run it

```bash
pixi run all        # run the tests, then regenerate the outputs
```

Or the two halves separately:

```bash
pixi run test       # pytest
pixi run summary    # writes outputs/annual-average.csv
```

## What is where, and why

| Path | What it is |
|---|---|
| `data/overnight.csv` | 69 monthly observations, 2021–2026, from the Bank of Canada Valet API. Committed because it is small and public. |
| `src/bocrates/summary.py` | The logic. Pure functions: everything arrives as an argument, everything leaves as a return value. No file paths, no printing. That is what makes it testable. |
| `tests/test_summary.py` | Five tests. They take under a second and they are the reason a refactor is safe. |
| `analysis/annual_summary.py` | The script that regenerates every output from the data. Deterministic. |
| `outputs/` | **Not committed.** Regenerable by definition — if it is not, the pipeline is broken. |
| `pixi.toml` + `pixi.lock` | The environment, and the exact packages that environment resolved to. |
| `pyproject.toml` | Package metadata, so `src/` is importable without `sys.path` games. |
| `CITATION.cff` | How to cite it. GitHub renders it; Zenodo reads it on release. |

## Data source

Bank of Canada Valet API, series `V39079` (target for the overnight rate):
<https://www.bankofcanada.ca/valet/observations/V39079/csv?start_date=2021-01-01>

The committed CSV keeps the first observation of each month, to stay small.
