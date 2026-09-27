---
type: Executor
title: Run the bocrates computation
description: How to run the annual-average computation from the Python reproducible-research example and obtain a receipt an attester can check.
resource: /references/executors/run-bocrates.py
tags: [python, reproducibility, executor]
runtime: python
generated: { by: claude/fable-5.1, at: "2026-09-12T00:00:00Z" }
---

# Run instructions

The computation is the `annual_average` function in
[`summary.py`](/references/computations/bocrates/src/bocrates/summary.py); the
data it reads is [`overnight.csv`](/references/computations/bocrates/data/overnight.csv).
The whole example project is in this bundle under
`references/computations/bocrates/`, and the executor resolves both relative to
its own location, so the bundle runs from a `git clone` or from a download of
the `references/` tree with no configuration.

Requires Python 3.11 or later. **Standard library only** — the example has no
third-party dependencies, which is part of its point. The project's own
`pixi.toml` and `pixi.lock` are included for anyone who wants the exact
environment it was developed in, but the executor does not need them.

```bash
python3 references/executors/run-bocrates.py
```

## Parameters

None. The computation declares no parameters (see [the computation
concept](/python/computations/bocrates.md)): the data is fixed and committed,
and the result is a function of that data alone. There is nothing for an agent
to supply and nothing for it to edit.

## Receipt

Printed to stdout as JSON:

* `computation_sha256` — hash of `summary.py` as it actually ran
* `data_sha256` — hash of `overnight.csv` as it was actually read
* `parameters` — empty
* `result.annual_average` — mean overnight rate per calendar year, 2021–2026
* `result.observations`, `first`, `last` — how many rows, and the date range

Pass the receipt to [the attester](/references/attesters/bocrates-attester.py):

```bash
python3 references/executors/run-bocrates.py | python3 references/attesters/bocrates-attester.py
```

## Relationship to the project's own test suite

The example ships with five pytest tests and a `pixi run all` task that runs
them and regenerates its outputs. Those are the project's *own* checks. This
executor and attester are the *bundle's* checks: they confirm that a value an
agent quotes was produced by the sanctioned code and data, which the test
suite does not do.
