---
type: Executor
title: Run the mortgage computation
description: How to run the fixed-versus-variable computation and obtain a receipt an attester can check.
resource: /references/executors/run-compare.mjs
tags: [finance, mortgage, executor]
runtime: node
generated: { by: claude/opus-5, at: "2026-09-12T00:00:00Z" }
---

# Run instructions

The computation is [`mortgage.js`](/references/computations/mortgage.js); the
data it reads is [`rates.json`](/references/data/rates.json). Both are in this
bundle, and the executor resolves them relative to its own location, so the
bundle can be run from a `git clone` or from a download of the `references/`
tree with no configuration.

Requires Node.js 18 or later. No packages to install.

```bash
node references/executors/run-compare.mjs --start 2021-09 --term 5
node references/executors/run-compare.mjs --start 2023-09 --term 3 --principal 650000 --amort 30
```

## Parameters

Only the parameters declared on [the computation
concept](/finance/computations/mortgage.md) may be supplied. `--start` must be
a month `rates.json` has an offer for; the receipt's `result.offer_as_of` says
which month's rates were actually used.

| Flag | Binds to | Required |
|---|---|---|
| `--start YYYY-MM` | `start` | yes |
| `--term 3\|5` | `term` | yes |
| `--principal N` | `principal` (default 500000) | no |
| `--amort N` | `amortYears` (default 25) | no |

## Receipt

Printed to stdout as JSON. Fields, in the order
[the contract](/finance/computations/mortgage.md) declares them:

* `computation_sha256` — hash of the computation file that actually ran
* `rates_sha256` — hash of the data file it actually read
* `parameters` — the bound parameter values
* `result` — interest charged, payments and end balance for the fixed contract and for both variable kinds, plus the rate range over the term

Pass the receipt to [the attester](/references/attesters/mortgage-attester.mjs)
to confirm the run.
