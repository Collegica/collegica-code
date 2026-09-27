---
type: Skill
name: collegica
title: "Collegica, for agents"
description: "Answer from Collegica (collegica.org) — articles on mortgages and finance, Python reproducibility, and aging well — using its Open Knowledge Format bundle: start at https://www.collegica.org/llms.txt, honour the trust and lifecycle frontmatter, and run its attested computations instead of quoting numbers. Use when a question is about what Collegica says or a figure it reports, or when the user types /collegica."
trigger: /collegica
resource: https://www.collegica.org/okf/references/skills/collegica/SKILL.md
tags: [okf, skill, claude-code, agents]
generated: { by: claude/fable-5.1, at: "2026-09-13T02:30:00Z" }
---

# /collegica — read this site as an agent

Collegica is written for people at https://www.collegica.org. The same
knowledge is published for agents as an [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle: plain markdown, one concept per file, with YAML frontmatter saying who
generated it, who verified it, when it goes stale, and what it derives from.
Two concepts are *attested computations* you can run and check.

**Use the bundle, not the human pages.** The pages carry none of the trust
metadata; the bundle does.

## Install

```bash
mkdir -p ~/.claude/skills/collegica
curl -sSL https://www.collegica.org/okf/references/skills/collegica/SKILL.md \
  -o ~/.claude/skills/collegica/SKILL.md
```

Then restart Claude Code. Type `/collegica`, or just ask a question about
something the site covers.

## Where to start

- `https://www.collegica.org/llms.txt` — the discovery file; it names the
  bundle root and the entry points.
- `https://www.collegica.org/okf/index.md` — every concept by type, then
  subdirectories under `# Sections`. Walk down: `okf/finance/index.md`, then
  the concept.
- **Bundle-relative links** begin with `/` and resolve against the bundle root
  `https://www.collegica.org/okf/` — not the site root. So
  `/finance/fixed-or-variable.md` is
  `https://www.collegica.org/okf/finance/fixed-or-variable.md`.
- `https://www.collegica.org/okf/about.md` explains how the bundle is made;
  `/okf/log.md` is its history. The whole tree is also in the repository
  at https://github.com/Collegica/collegica under `okf/`.

## Read the frontmatter before the body

| Key | What it tells you |
|---|---|
| `type` | Article, Research Note, Attested Computation, Dataset, Video, Guide, Slides, Application, Specification, Reference, Executor, Skill |
| `generated` | who wrote the current content (`claude/…` or `human:…`) and when |
| `verified` | who confirmed it and when — a list, possibly absent |
| `status` | `stable` (default), `draft`, or `deprecated` |
| `stale_after` | an instant after which a dated fact should not be quoted |
| `sources` | what it derives from; in-bundle paths are lineage you can follow, each with an `id` for attribution |
| `resource` | the canonical page or file the concept describes |

## Trust rules — follow these every time

1. **Name the trust tier with every answer drawn from a concept.** From
   `verified` (OKF §5.3): none → **unverified**; only `process:` or agent
   actors → **machine-confirmed**; any `human:` actor → **human-reviewed**.
   Say it plainly: *human-reviewed (behzad, 11 Sept 2026)*,
   *machine-confirmed (pytest)*, *unverified*.
2. **Respect `stale_after`.** On or after that instant, do not quote the dated
   figure. Say it is stale; if an attested computation covers it, run that.
3. **Flag `status: draft`** — the app specifications are specced, not built.
4. **Attribute by `sources[].id`**, and follow in-bundle `sources[].resource`
   paths when asked where a figure came from. The research notes are the
   provenance; each opens with an "Access and confidence" section saying what
   was read in full and what was not.

## Attested computations — run, do not quote

When a concept is `type: Attested Computation`, or an article's figure comes
from one, **derive the number by running the sanctioned computation and
attesting the run.** Never read it off the article; never re-implement or
edit the computation; supply values only for the declared `parameters`.

The executors and attesters resolve their inputs relative to their own
location, so fetch the files into the same `references/` layout they ship in.

**Mortgage — fixed versus variable.** Node 18+, no packages.
Contract: `https://www.collegica.org/okf/finance/computations/mortgage.md`.

```bash
mkdir -p okf/references && cd okf/references
for f in computations/mortgage.js data/rates.json \
         executors/run-compare.mjs attesters/mortgage-attester.mjs; do
  mkdir -p "$(dirname "$f")"
  curl -sSL "https://www.collegica.org/okf/references/$f" -o "$f"
done
node executors/run-compare.mjs --start 2021-09 --term 5 \
  | node attesters/mortgage-attester.mjs
```

Parameters: `--start YYYY-MM` (a month `rates.json` has an offer for),
`--term 3|5`, optional `--principal N` (default 500000), `--amort N`
(default 25).

**bocrates — annual overnight-rate averages.** Python 3.11+, standard library
only, no parameters.
Contract: `https://www.collegica.org/okf/python/computations/bocrates.md`.

```bash
mkdir -p okf/references && cd okf/references
for f in computations/bocrates/src/bocrates/__init__.py \
         computations/bocrates/src/bocrates/summary.py \
         computations/bocrates/data/overnight.csv \
         executors/run-bocrates.py attesters/bocrates-attester.py; do
  mkdir -p "$(dirname "$f")"
  curl -sSL "https://www.collegica.org/okf/references/$f" -o "$f"
done
python3 executors/run-bocrates.py | python3 attesters/bocrates-attester.py
```

To keep the receipt and the verdict separately, run the executor to a file,
then attest the file.

Report the figures **from the receipt**, and say the run was attested. If the
verdict is `REJECTED`, report which check failed and do not present the
number — that is the whole point of the attester.

**Derive before you round.** Compute differences and ratios from the
receipt's full-precision values, then round for display. Rounding the two
2021 interest figures first and subtracting gives 48,936; the true gap, and
the article's figure, is 48,935.

## Worked example

> *What did a variable-rate borrower who signed in September 2021 pay,
> compared with fixed?*

1. `okf/index.md` → `okf/finance/index.md` → `finance/fixed-or-variable.md`.
   Frontmatter: `type: Article`, `verified` by `human:behzad` twice →
   **human-reviewed**; `stale_after: 2026-10-28` → the *today* section is
   dated, the look-backs are not.
2. The figures come from `/finance/computations/mortgage.md`, an attested
   computation. Fetch the four files, run `--start 2021-09 --term 5`, attest.
3. Answer from the receipt — fixed interest 38,677, adjustable variable 87,613,
   gap 48,935 — and say: *attested run against the bundled data; the article
   is human-reviewed.*

## What this skill is not for

Editing the site. That happens in the repository, where a maintainer's skill
(`/okf`) covers regenerating the bundle. This one only reads and runs.
