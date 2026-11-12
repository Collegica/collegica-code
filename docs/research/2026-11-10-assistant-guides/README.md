# Assistant guides — template, common tasks and the source rule

Common ground for the guides to Claude, ChatGPT, Gemini and Grok, made
2026-11-10 as the first step of the series.
Each guide has its own research folder beside this one; this folder holds
what they share.

## Access and confidence

- **Version 2, 2026-11-11.** The first version was run thirty times for the
  Claude guide ([its research](../2026-11-10-claude/README.md)): plain and
  careful prompts scored nearly the same, and the marking rewarded asking
  rather than the practice. This version adds two notes (an action that
  changes hands, one closed only by implication, a file name with the wrong
  day, a near-miss 2025 figure), marks task 4 the same for both prompts, and
  defines the word count. Claude, ChatGPT and Grok have since run version
  2, thirty runs each, on 11 November 2026. Careful prompts scored higher on
  task 2 for Claude and ChatGPT, and by one mark in one ChatGPT run of task
  4; Grok scored the same plain and careful on all five. See each guide's
  `notes/test.md`.
- **The folder and key were checked on 2026-11-11:** built with
  `tasks/make_folder.py`; the fee total recomputed by script ($855.00 net,
  $900.00 as a plain sum); `tasks/check_t3.py` run on the untouched folder
  (fails) and on a copy tidied from each note's heading (passes).
- **Version 2.1, 11 November 2026: marking and procedure only.** The folder and
  prompts are unchanged, so every version 2 run stays comparable. ChatGPT
  and Grok both failed task 3's plain prompt only because the checker
  demanded a file name and index name the plain prompt never asks for;
  `check_t3.py --plain` now accepts any reasonable choice, and older runs
  are re-marked. Task 1 still scored full marks plain and careful on every
  assistant tested; that is reported as a finding, not fixed by changing
  the task mid-series.
- **The open actions and the notice in the key were worked out by hand** from
  the seven notes, not by a script.

## What is here

| File | What it is |
|---|---|
| [`template.md`](template.md) | The article skeleton every guide fills in |
| [`tasks/make_folder.py`](tasks/make_folder.py) | Builds the made-up folder: a garden club's seven meeting notes and members list |
| [`tasks/prompts/`](tasks/prompts/) | The prompts, a plain one and a careful one for each task |
| [`tasks/house-rules.md`](tasks/house-rules.md) | The rules that go into the assistant's instruction file for task 2 |
| [`tasks/answer-key.md`](tasks/answer-key.md) | The right answers and how to mark |
| [`tasks/check_t3.py`](tasks/check_t3.py) | Checks the folder after task 3 |
| [`tasks/count_words.py`](tasks/count_words.py) | Counts the words in task 2's notice, the way the key does |

## The five tasks

Each task tests one practice by asking the same thing twice: plainly, then
with the practice.

| | Practice | Plain | With the practice |
|---|---|---|---|
| 1 | A brief, not a question | `t1-plain.txt` | `t1-practice.txt`: goal, what counts, output, what to do when unsure |
| 2 | An instruction file | `t2.txt`, no instruction file | `t2.txt` again, with `house-rules.md` in the assistant's instruction file |
| 3 | Plan first, then act | `t3-plain.txt` | `t3-practice-1.txt`, read the plan, then `t3-practice-2.txt` in the same session |
| 4 | Ask it to check its work | `t4-plain.txt` | `t4-practice.txt` |
| 5 | Permission to say "not there" | `t5-plain.txt` | `t5-practice.txt` |

## Before the first run

Check these, and write the answers at the top of `notes/test.md`. Stop and
ask the owner if any is a problem.

1. **The product is still offered to individuals.** Read the vendor's own
   page on it first. (Gemini CLI closed to personal accounts on 18 June 2026;
   the plan named it anyway.)
2. **Signed in, and on which plan.** Run one trivial prompt.
3. **The vendor's terms on scripted use.** Some consumer plans forbid
   running the app from another program; Google's Antigravity FAQ says
   wrapping `agy` in third-party coding agents "is not supported under
   consumer plans". If the terms forbid it, the owner runs the script.
4. **Usage left and the cost of one run.** Read the app's own usage figure,
   run one prompt, read it again, and agree a budget with the owner before
   the rest. Antigravity's free tier spent about 6% of a week a run.
5. **What loads.** List what the app loads in the test folder from its own
   listing (`grok inspect`, `codex` session log, `agy mcp list`), not only by
   asking the model. Keep out: connectors, MCP servers, plugins, the app's
   memory, and other apps' set-ups it reads by default (Grok Build reads
   `~/.claude/`). Use command-line flags or environment variables, never
   edits to the owner's files.

What worked, so far:

| App | Model | No connectors | Also |
|---|---|---|---|
| Claude Code | `--model claude-opus-5-5` | `--strict-mcp-config`, `--no-chrome` | |
| Codex | `-m gpt-6.1-sol` | `--disable plugins --disable apps`, and `-c mcp_servers.<name>.enabled=false` for each server | `--disable memories` |
| Grok Build | `-m grok-4.7` | `GROK_CLAUDE_MCPS_ENABLED=false GROK_CURSOR_MCPS_ENABLED=false`, `--deny MCPTool --disallowed-tools search_tool,use_tool,CallMcpTool,FetchMcpResource,ListMcpResources` | `GROK_FOLDER_TRUST=0`; never `--trust`, which writes to `~/.grok` |
| Antigravity CLI | account default, `gemini-3.8-flash-high` | none configured | `--sandbox`; `--mode auto` is not on free plans |

## How to run them

1. **A fresh folder for every run:** `python3 tasks/make_folder.py <dir>`,
   outside the repository and outside any git repository, so one run cannot
   see another's output and no instruction file of this repository is
   picked up.
2. **The assistant's own command-line app, with the model pinned.** Pass the
   model on the command line every run, and log the model the app reports in
   its own output, not the one you asked for. For Claude the model is
   **Claude Opus 5.5** (owner's decision, 2026-11-11). For the others, the
   vendor's own default model for that app on the owner's plan, read from
   its documentation on the day, named explicitly.
3. **No connectors or MCP servers.** Each run gets only the folder: no
   connectors, MCP servers or extensions from the owner's set-up (owner's
   decision, 2026-11-11). Use the app's own flag for this, never an edit to
   the owner's configuration files (for Claude Code:
   `--strict-mcp-config` with no `--mcp-config`). Before the first run, ask
   the assistant to list its tools and log the answer, to show none are
   loaded. If an app cannot run without them except by editing its
   configuration, stop and report it. The owner's instruction files and
   other settings still load, as they would for anyone; say so in the log.
4. **Permission to write in that folder only.** Name the mode in the log.
   Where the app's only non-interactive mode skips approval, pair it with
   its sandbox, and say so in the guide.
5. **Three runs of each prompt.** Ten prompts, so thirty runs an assistant.
   Report marks as the answer key gives them, for each run, never an average
   alone.
6. **Copy each run into `example/results/` as soon as it finishes,** and
   commit after every batch. Temporary folders have been emptied mid-work.
7. **Log every run** in the guide's own `notes/test.md`: date, command, app
   version, model reported, wall time, marks, and anything odd.
8. **Task 2's instruction file** is whatever that assistant reads at the
   start of every session; finding its name and place in the vendor's
   documentation is part of the guide.

**Mark task 3 plain with `check_t3.py --plain`** (version 2.1).

**Cost.** For Claude, every run draws on the owner's subscription limit, the
same limit the drafting agent uses; it stopped the first guide twice. At API
list prices a run cost about US$1 on Fable 5.2. Run three at a time, not
thirty. The other assistants draw on their own vendors' plans.

One run of thirty is small evidence. A guide says "in three runs out of
three", not "always", and says so when plain and careful prompts scored the
same: a practice that made no difference on this model is a finding.

## The source rule

A practice goes into a guide only if it was reproduced here, with its line in
`notes/test.md`, or is stated in the vendor's own documentation, with the
link and the date read. Everything from X, Reddit, YouTube or a third-party
write-up is a lead: it goes in `notes/leads.md` marked *untested*, and then
becomes *passed* or *failed*. Failed leads are kept; they are the material
for "What did not hold up".

Prices in Canadian dollars where the vendor gives them; otherwise in the
vendor's own currency, labelled (US$20 a month).

## Each guide's research folder

    docs/research/YYYY-MM-DD-<slug>/
      README.md        Access and confidence; decisions; For the owner
      watch.md         changelog and feed addresses to check each month
      notes/           one file per vendor source read, with the date
      notes/leads.md   every lead, its link, and untested / passed / failed
      notes/test.md    the run log
      example/results/ outputs of each run
