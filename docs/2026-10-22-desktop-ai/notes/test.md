# One task, three apps — run on 2026-10-22

The same task, in the terminal version of each app, on its own copy of a
made-up receipts folder, run at the same time on a MacBook (Apple M4). Folder
built by [`../example/make_receipts.py`](../example/make_receipts.py); prompt
in [`../example/task.txt`](../example/task.txt); answer key in
[`../example/answer-key.csv`](../example/answer-key.csv); each app's
`expenses.xlsx` and `notes.md` in [`../example/results/`](../example/results/).

The folder: 20 receipts — 8 text files, 6 text PDFs, 6 PNG images — with
three traps: the same Amazon purchase as a PDF and as a photo, a refund, and
one purchase in US dollars. Right answer: 19 rows (18 purchases and the
refund), CAD 585.40, USD 12.99.

## How each was run

| App | Version | Command | Model |
|---|---|---|---|
| Claude Code | 2.1.293 | `claude -p "…" --permission-mode auto` | Claude Opus 5.5 (subscription) |
| Codex CLI | 0.163.0 | `codex exec --skip-git-repo-check -s workspace-write "…"` | GPT-6.1 Sol, reasoning low (ChatGPT sign-in) |
| Hermes CLI | 0.21.5 | `hermes chat --query-file task.txt --oneshot --in .` | `nvidia/nemotron-3-ultra-550b-a55b:free` via OpenRouter |

Each was the user's existing configuration; nothing was tuned for the test.

## Results

| | Claude Code | Codex | Hermes |
|---|---|---|---|
| Wall time | 78 s | 92 s | 214 s |
| Rows | 19 | 19 | 19 |
| CAD / USD totals | 585.40 / 12.99 | 585.40 / 12.99 | 585.40 / 12.99 |
| Duplicate listed once, both files named | Yes | Yes | Yes |
| Refund as a negative row | Yes | Yes | Yes |
| Receipts unchanged (SHA-256 before/after) | Yes | Yes | Yes |
| Totals as spreadsheet formulas | Yes (`SUMIF`) | Yes (`SUMIFS`) | No (typed numbers) |
| Categories matching the key | 19/19 | 18/19 (Indigo → Other, flagged) | 19/19 |
| `notes.md` | 23 lines | 10 lines | 22 lines |
| Usage | $0.59 API-equivalent, on the plan | 45,682 tokens, on the plan | $0; 235K tokens in, 6.6K out |

Every date, vendor and amount matched the key in all three (the grader's one
"miss" in each, the bus pass, is `97` against `97.00`).

## What differed

- **Reading the pictures.** Claude read the PNG receipts with its own vision
  ("I read the PNG receipts by eye"). Hermes ran OCR, which dropped the
  decimal points on one receipt ("749", "112", "861"); it noticed, corrected
  them to 7.49, 1.12 and 8.61, and said so in its notes.
- **Self-checking.** Claude checked items → subtotal → total on every
  receipt. Codex hashed the receipts before and after to prove it changed
  nothing, and checked the workbook was a valid archive.
- **Judgement calls, flagged.** All three put pharmacy items under Other and
  said so. The Indigo receipt (a notebook and a book) went to Office in two,
  Other in Codex, which explained why. The key's choice is no more right.

## Traps hit running it

- **Codex 0.154 could not use the configured model.** The installed CLI was
  nine minor versions behind; `gpt-6.1-sol` returned "not supported when using
  Codex with a ChatGPT account". `brew upgrade --cask codex` (to 0.163.0)
  fixed it.
- **`codex exec` is read-only by default.** The first run read all 20 files,
  got every number right, and saved nothing: "this session's read-only
  filesystem prevents creating `expenses.xlsx`". Interactive Codex defaults
  to workspace-write; the scripted form needs `-s workspace-write`.
- **Hermes was not updated to 0.22** for the test; the 0.22 changes in the
  article are from the release notes. Its log repeats a harmless "Failed to
  load bundled provider plugin solstice: No module named 'httpx'".
- **OpenRouter's free tier** allows 50 requests a day until $10 of credit has
  been bought; this one task used 44.

## What it does not show

One task, one run each, three different models; the apps are not the
variable on their own. The desktop apps were not used — their terminal twins
were, because a script can time them. A harder task, or a weaker model, would
separate them more.
