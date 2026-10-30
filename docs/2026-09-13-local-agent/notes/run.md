# The measured run — Gemma 4 12B through Ollama and Hermes, 2026-09-13

## Access and confidence

Everything here was measured on one machine, once. It is a sample of one,
on a laptop with other applications open. Treat the numbers as the order of
magnitude, not the value.

**Machine:** Apple M4, 24 GB unified memory, macOS, 15 GiB free on disk at
the start. **Software:** Ollama 0.33.3 (`brew install ollama`), `gemma4:12b`
(7.6 GB on disk, Ollama's QAT 4-bit), Hermes Agent v0.21.2, an isolated
Hermes profile with `terminal`, `file` and `clarify` toolsets and everything
outward disabled.

## Setup that took

```
OLLAMA_CONTEXT_LENGTH=65536 ollama serve
ollama pull gemma4:12b
```

Hermes profile config: `model: {default: gemma4:12b, provider: custom,
base_url: http://localhost:11434/v1, context_length: 64000}`. After the first
request, `ollama ps` showed `8.2 GB · 100% GPU · CONTEXT 65536` — the
environment variable took, and the whole model sat in GPU memory.

## Raw speed (Ollama HTTP API, `num_predict: 200`)

| | Prompt | Generation | Wall for a 3-sentence answer |
|---|---|---|---|
| thinking on (default) | 56 tok/s | 11.5 tok/s | 22.5 s — 809 characters of thinking, then 200 tokens |
| thinking off (`think: false`) | 61 tok/s | 12.1 tok/s | 7.2 s — 80 tokens |

Cold start, first ever request through the CLI: 61 s wall to a one-sentence
answer, thinking on (model load plus reasoning). Free RAM with the model
loaded and a browser, an editor and two Hermes gateways running: 0.1 GB.

## The tool-using task

The same task as the cloud run in the OWL Planner work: run the budget tool
on a scratch copy of the invented household, read `ask-your-ai.md` (two
unclassified merchants), write the rules fragment, merge it, rerun, report.
No human at the keyboard, so the agent was told not to use `clarify` and to
mark anything unobvious `unsure`.

| | Cloud model (free tier, via OpenRouter) | Gemma 4 12B, local, thinking on |
|---|---|---|
| Wall time | 2 min 11 s | **20 min 0 s** |
| Tool calls | 10 | **22** |
| Errors on the way | none | a merchant-name typo, a path typo, an empty pattern (refused by the tool) |
| What it merged | `newtown dental` → Dentist | `newton dental` → Dentist (mistyped: matches nothing), plus `'transfer'` and `'income'` as patterns |
| `the book` | left `unsure` | left `unsure` |
| Its own report | correct | **wrong** — claimed 0 merchants remained; both still did |

The local model's reasoning trace shows it *noticing* the typo ("fixed
newton to newtown") and then writing the typo anyway. The two junk patterns
came from a workaround: the tool refused an empty string as a pattern, and
the model filled the sections with placeholder words rather than removing
them. A pattern of `transfer` would match every description containing that
word. That is the "wrong rule is worse than no rule" failure the pack warns
against, produced in the act of avoiding a refusal.

Two things went right and are the point: the tool's own gate refused the
empty pattern, and `the book` stayed unsure. And one caveat: this run forced
the model to decide alone. The skill's real mode asks the person through
`clarify` and only writes what they answered — a smaller job, and the one a
12B is more likely to be good at. That mode was not measured here.

## What follows

- **Thinking is the cost.** Most of the twenty minutes was reasoning
  between tool calls — minutes per step. Hermes's `--reasoning` flag (levels
  from `none` up) and Ollama's `think` parameter are the knobs; a session
  with reasoning off was not run.
- **Speed is fine for chat, slow for loops.** Twelve tokens a second reads
  comfortably. Twenty-two tool calls at that rate, each preceded by a
  paragraph of thought, is an afternoon.
- **A bigger model needs a bigger machine.** Google's table: 26B A4B at
  4-bit is 14.4 GB of weights, 31B is 17.5 GB, before the context cache. On
  24 GB, the 12B was the honest choice.
