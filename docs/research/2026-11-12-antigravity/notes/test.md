# Test log

Thirty runs of the common tasks on Gemini 4 Argon (Medium), made on
12 November 2026 between 03:18 and 03:42 UTC, after the owner's Google AI
Pro plan reached Antigravity. Three earlier runs of task 1 on Gemini 3.8
Flash are kept as earlier evidence. Tasks from
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
(version 2.1), marked against `answer-key.md`, `check_t3.py` (with
`--plain` for the plain prompt) and `count_words.py`. Outputs are in
[`../example/results/`](../example/results/): `folder/` is the test folder
as the run left it, `turnN.json` the JSON reply, `turnN.time` the wall time,
`turnN.err` stderr. Temporary paths are shortened to `<tmp>`.

## How the Argon runs were made

| | |
|---|---|
| App | Antigravity CLI 1.5.6 |
| Model asked for | `--model gemini-4-argon-medium`, the default `agy -p /model` reported once the Pro plan showed |
| Model reported | not in the JSON reply (Antigravity's `json` output has no model field). Evidence it was Argon: the "Gemini 4 Argon Weekly Limit" fell from 99% to 81% over the runs while the general Gemini weekly and five-hour figures stayed at 100% |
| Account | the owner's personal Google account, Google AI Pro |
| Folder | a fresh copy from `make_folder.py` per run, in a temporary folder outside any git repository |
| Parallel | two at a time, in batches of three, `/usage` read after each batch ([`../example/agyplan.py`](../example/agyplan.py)) |
| Task 3, second turn | the same command with `--conversation <id>`; the JSON confirms the same conversation in all three runs |
| Task 2 practice | `house-rules.md` saved as `AGENTS.md` in the folder |
| Connectors | none: `agy mcp list` "No MCP servers configured", `agy plugin list` "No plugins installed", re-checked before the first run; `mcp(*)` denied in the session settings |

The command ([`../example/agyrun.sh`](../example/agyrun.sh)):

```sh
agy -p "<prompt>" --model gemini-4-argon-medium \
  --mode accept-edits --sandbox \
  --settings agy-session-settings.json --output-format json
```

### The permission mode, and why

The earlier Flash runs used `--dangerously-skip-permissions --sandbox`.
These do not. What was checked first, with no task run:

1. `--mode auto --sandbox`: still "--mode auto is not available for this
   account; continuing in the default mode", after the Pro plan arrived.
2. `--mode accept-edits --sandbox` with `toolPermission: proceed-in-sandbox`:
   file writes ran, but `mv` was refused ("a tool required the 'command'
   permission that headless mode cannot prompt for, so it was
   auto-denied").
3. The same plus a short **allow list** passed with `--settings`, which the
   CLI documents as "Settings for this session only, never saved"
   ([`../example/agy-session-settings.json`](../example/agy-session-settings.json)):
   `ls`, `cat`, `head`, `tail`, `wc`, `mv`, `cp`, `mkdir`, `diff`, `cmp`,
   `shasum`, `sha256sum`, `md5`, `stat`, `grep`, `sort`, `uniq`, `awk`,
   `sed`, `find`, `echo`, `printf`, `python3`, `cd`, `pwd`, `file`, `tr`,
   `cut`; **denied**: `rm`, `sudo`, `curl`, `wget`, `git`, any command
   outside the sandbox (`unsandboxed(*)`), web pages (`read_url(*)`,
   `execute_url(*)`) and MCP (`mcp(*)`); `allowNonWorkspaceAccess: false`.
   A probe then created a file and renamed it with `mv`, inside the
   sandbox.

So every file edit in the folder is allowed, commands on the list run in
the sandbox, and anything else is refused, because a headless run cannot
ask. That is narrower than skipping permissions, and enough for every task:
task 3's renames used `mv`.

**What a reader should take from it:** at the keyboard, `accept-edits` asks
before every command; a short allow list in your own settings gives the
same result as here without approving everything.

**Permission rules already saved in the CLI's user settings still
loaded;** session settings add to them rather than replace them. None was
used in these runs as far as the outputs show.

**Two runs were stopped by the allow list.** Task 5 plain runs 2 and 3 each
tried to read a file the session settings did not allow (`denied_actions:
read_file`), and ended after about 7 seconds with an empty reply. The JSON
does not say which file. With `allowNonWorkspaceAccess: false`, the likeliest
reading is a file outside the test folder. They are marked "no answer".

## Quota

| When (UTC, 12 November) | Gemini weekly | Gemini five-hour | Argon weekly |
|---|---|---|---|
| 03:14, before any check | 100% | 100% | 100% |
| 03:18, after three mode probes | 100% | 100% | 99% |
| After task 1 plain run 1 | 100% | 100% | 98% |
| After each later batch of three | 100% | 100% | 96, 94, 93, 91, 88, 86, 84, 83, 82, 81% |

So about **0.6% of the weekly Argon limit per run** (18 points for 30 runs
and three probes; `/usage` reports whole percentages). The five-hour figure
never moved. At 03:42 UTC, after the thirty runs, `agy models` and
`agy -p /usage` showed the free-tier view again (see below).

## Results, Gemini 4 Argon (Medium)

### Task 1: open actions (marks out of 9)

| Run | Plain | Practice | Wall time, plain / practice |
|---|---|---|---|
| 1 | 9 | 9 | 117.0 s / 78.0 s |
| 2 | 9 | 9 | 74.6 s / 74.2 s |
| 3 | 9 | 9 | 65.1 s / 68.3 s |

- Plain: all five actions, right people and dates, the roofer once at
  10 November, the tap with Dov. Every run also listed the unpaid fee, Bram
  Lindqvist's duplicate row and Sabela Pascoe's vacant plot, and suggested
  "provide soup" and, in runs 2 and 3, paying the 2026 water bill. 342 to
  415 words; each claim linked to a line of a note.
- Practice: the same five in `actions.md`, and a list of doubts: paying the
  roofer, who brings soup, whether Dov counts as committee (he is not on the
  committee), finalising the checklist, past-due dates.

### Task 2: the notice (marks out of 10)

| Run | Plain | Practice (`AGENTS.md`) | Words, plain / practice |
|---|---|---|---|
| 1 | 7 | 10 | 165 / 93 |
| 2 | 7 | 10 | 176 / 107 |
| 3 | 7 | 10 | 153 / 79 |

- Plain, all three: all four facts, full date with weekday and year, 24-hour
  times, British spelling ("metres"); but each ended "We look forward to
  seeing you there!", ran past 120 words, and was signed "Ibrahim Solheim,
  On behalf of the … Committee" (run 2 also listed all five committee
  members). Each also named Wren for the water shut-off.
- Practice, all three: every rule, signed "The committee".

### Task 3: tidy the notes

| Run | Plain: `--plain` | Plain: strict | Plain: said how it checked | Practice: `check_t3.py` | Practice: said how it checked |
|---|---|---|---|---|---|
| 1 | passed | failed (names) | no | passed | yes: SHA-256 and sizes |
| 2 | passed | failed (names) | no | passed | yes: SHA-256 and sizes, `ls -la` |
| 3 | passed | failed (names) | no | passed | yes: SHA-256 and sizes, `ls -la` |

Wall time, plain: 70.0, 86.1, 77.9 s. Practice, two turns: 51.3 + 55.1,
31.0 + 71.5, 62.0 + 51.9 s. All six noticed the 25/26 August difference.
Plain runs named the notes `YYYY-MM-DD.md` and wrote `notes/index.md`.
Practice turn 1 gave the plan and said no files had been changed yet
(runs 1 and 3 in so many words), then stopped.

### Task 4: fees (marks out of 5)

| Run | Plain | Practice |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |

- $855.00 in all six, with the duplicate, the blank and the refund named.
  The plain runs also gave the breakdown (18 × $45.00 and 2 × $22.50) and
  the $900.00 raw sum.
- Practice: member count given and explained (22 on the roster, 20 paying),
  and two checks each: bottom-up by fee and top-down from the raw sum.

### Task 5: water in 2025

| Run | Plain | Practice |
|---|---|---|
| 1 | right | right |
| 2 | no answer (read refused) | right |
| 3 | no answer (read refused) | right |

- Every answer given said the 2025 figure is not in the files, gave the 2026
  figures ($312.40, $486.75) and named the $96.20 electricity bill as a
  different utility. None offered a 2025 water figure.

## Earlier runs, Gemini 3.8 Flash (High), before the Pro plan reached Antigravity

Three runs of task 1 plain, 12 November 01:47 UTC, with
`--dangerously-skip-permissions --sandbox` (no other mode was available
then). Outputs: `../example/results/flash-t1-plain-r*/`.

| Run | Marks (/9) | Wall time | Tokens | Status |
|---|---|---|---|---|
| 1 | 9 | 73.2 s | 109,038 | ERROR (429 partway; full answer given) |
| 2 | 9 | 64.3 s | 177,712 | SUCCESS |
| 3 | 9 | 70.1 s | 180,456 | ERROR (429 partway; full answer given) |

They used 17% of the free tier's weekly Gemini limit between them.

## Leads

None tested. Two were attempted after the thirty runs (house rules as
`GEMINI.md`; task 3 in `--mode plan`). Each stopped in about 2 seconds:
"model gemini-4-argon-medium is not recognized". `agy models` then listed
only the free-tier models again, and `/usage` showed one Gemini weekly line
at 33% (reset 2026-11-18T17:41Z) and no Argon line. Nothing ran, so nothing
was used. They are not retried on Flash, to keep the guide on one model.

## Totals

33 Argon turns (30 runs, three with two turns), 798,125 tokens in all.
