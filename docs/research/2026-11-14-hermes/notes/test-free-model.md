# Test log: the same tests on a free model

This is the first set of runs, made before the switch to ChatGPT Terra
instead. The marks below were re-checked against the saved records on 14
November after a review; two marks changed (task 1 plain r1, task 2 plain r3)
and claims of checks that the record does not show were corrected. The Terra log is
[`test.md`](test.md).

Thirty runs of the common tasks on **nvidia/nemotron-3-ultra-550b-a55b:free**
(through OpenRouter), in **Hermes Agent v0.23.1 (2026.9.24)**, made on 14
November 2026 between 10:59 and 11:47 Eastern time (with the extra runs below), one at a time. Six
more runs (three of task 2 again with `AGENTS.md`, three with the rules as a skill) were made afterwards.
Tasks from
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
(version 2.1), marked against `answer-key.md`, `check_t3.py` (with `--plain`
for the plain prompt) and `count_words.py`. Outputs are in
[`../example/results/`](../example/results/): `folder/` is the test folder as
the run left it, `turnN.jsonl` the event stream, `turnN.time` the wall time,
`turnN.err` stderr. Temporary paths are shortened to `<tmp>`.
[`../example/summarise.py`](../example/summarise.py) prints each run's reply
and the mechanical checks.

## How the runs were made

| | |
|---|---|
| App | Hermes Agent v0.23.1 (2026.9.24), `hermes chat --oneshot`, installed from git at `~/.hermes/hermes-agent` |
| Model asked for | `--provider openrouter -m nvidia/nemotron-3-ultra-550b-a55b:free`, the tester's configured default (`hermes config get model`), named on every run |
| Model reported | the `init` event of every run's stream: `"model": "nvidia/nemotron-3-ultra-550b-a55b:free"`; asked directly, the agent answered "nvidia/nemotron-3-ultra-550b-a55b:free (via openrouter)". OpenRouter lists the model with 1,000,000 tokens of context and a price of 0 |
| Account | the tester's OpenRouter key, read from `~/.hermes/.env` into the environment of the run only, never written anywhere |
| Data root | **an empty one**: `HERMES_HOME` pointed at a new folder, so none of the tester's `config.yaml`, `memories/`, `SOUL.md`, skills or sessions loaded. Hermes seeded it with its defaults: its default `SOUL.md`, 12 bundled skills, empty memory. This is how the tester's connectors, MCP servers, memory and personal skills were kept out. Nothing in the tester's Hermes folder was changed except that its OpenRouter key was read |
| Tools | `-t file,terminal,todo`. Not loaded: web, browser, memory, skills, delegation, cron, messaging, image and the rest. The agent listed its tools when asked: `patch`, `read_file`, `search_files`, `terminal`, `write_file`, plus `tool_search`, `tool_describe`, `tool_call` (Hermes's own way of looking up tools it was not given). No MCP servers or connectors configured in the empty data root |
| Permissions | **No `--yolo`.** Default `approvals.mode: smart`. `chat --oneshot` applies `approvals.single_query_mode`, default `deny`: a command Hermes flags as dangerous is refused, because no one is there to answer. Commands it does not flag run without asking. `HERMES_WRITE_SAFE_ROOT` set to the folder that holds all the test folders, which confines `write_file` and `patch` (not the terminal). See "Permission probes" |
| Folder | a fresh copy from `make_folder.py` per run, in a temporary folder outside any git repository |
| Task 3, second turn | the same command with `--resume <session id>` from the first turn |
| Task 2 practice | `house-rules.md` saved as `AGENTS.md` in the folder |
| Gateway | Hermes started a background `gateway run --idle-exit` process in the empty data root on its own; no platform is configured in it. It was stopped between attempts and left to exit at the end |

Command ([`../example/hermesrun.sh`](../example/hermesrun.sh)):

```sh
HERMES_HOME=<empty data root> HERMES_WRITE_SAFE_ROOT=<runs folder> \
hermes chat --oneshot --query-file prompt.txt \
  --provider openrouter -m nvidia/nemotron-3-ultra-550b-a55b:free \
  -t file,terminal,todo --in <folder> --format stream-json
```

Why not `hermes -z`: its `--help` says "approvals are auto-bypassed", which
would be `--yolo` by another name. `chat --oneshot` keeps the approval system
on. `-z` also has `--usage-file`, which `chat` does not, so token counts
come from each run's `result` event.

### Things that went wrong first, and were redone

- **First attempt, discarded (three runs):** the safe-root variable was set
  to a probe folder during a trial run; Hermes's background process kept it,
  and every later write was refused as "outside HERMES_WRITE_SAFE_ROOT". The
  process was stopped, the runs deleted and the whole batch started again
  with one fixed safe root. The refusal is the evidence that the write
  confinement works for `write_file`.
- **A second start** was made with an old copy of the script by mistake, and
  also stopped and deleted after two runs. Everything below is from the
  third start, run once, nothing selected.

## Marks

Marks out of 9 (task 1), 10 (task 2), 5 (task 4) as the key gives them. Task
3 is pass or fail from the checker. Task 5 is right or wrong.

### Task 1: open actions

| Run | Marks | Notes |
|---|---|---|
| plain r1 | 9 | five open actions in a list with the right who and dates; the tool sharpener mentioned as a fact; "no further meetings this year" |
| plain r2 | 9 | five open actions with the right who and date; also listed members.csv problems unasked |
| plain r3 | 9 | table of five; members.csv problems, the 2026 water bill and an offer to "clean up the CSV" appended |
| practice r1 | 9 | `actions.md`, five rows; doubts listed (Dov's role, group action) |
| practice r2 | 9 | five rows |
| practice r3 | 9 | five rows, dates with the year |

All six knew the date from the system (14 November) and called past dates
overdue; the key counts neither way. No run presented an action the notes do
not record as agreed.

### Task 2: the notice

| Run | Marks | Notes |
|---|---|---|
| plain r1 | 9 | 118 words; all four facts; signed with "Contact Ibrahim (committee secretary)" instead of "The committee", personal names in the text |
| plain r2 | 6 | 132 words; date and gloves only (no times, no soup); signed "Committee" followed by all five names |
| plain r3 | 8 | 105 words; four facts; an exclamation mark ("See you there!"); signed "Collegica Committee" |
| practice r1 | 0 | no notice. Its first and only search listed no files ("workspace is empty") and it asked for the notes |
| practice r2 | 7 | 42 words; only the date among the facts; all six rules followed; signed "The committee". It names Wren in the text |
| practice r3 | 0 | no notice, same "workspace is empty" |
| practice r4 (extra) | 7 | 45 words; date only; all six rules; invented tasks ("gutter clearing, path sweeping") |
| practice r5 (extra) | 0 | no notice, "workspace is empty" |
| practice r6 (extra) | 0 | no notice, "workspace is empty" |
| skill r1 (extra) | 7 | house rules as a Hermes skill, no `AGENTS.md`: 44 words, date only, all six rules |
| skill r2 (extra) | 0 | no notice, "can't find any committee notes" |
| skill r3 (extra) | 0 | no notice, "no committee notes" |

Where a notice was written with the rules loaded it followed all six rules
(3 of 3 notices: two with `AGENTS.md`, one with the skill), and none had the
times, gloves or soup, because those runs read only the 3 November note. In
the runs that gave up, the first call was
`search_files {"pattern": ".", "target": "files"}`, which returned
`total_count: 0` in a folder that was not empty, and the agent took that for
an empty folder (five of the six began with it; skill r2 made
three searches, one of them in Hermes's own data folder, then asked for the
notes). A possible tool quirk as much as a model slip: the plain runs
searched with `"*"` or for words, or listed the folder with the terminal, and
found the files; practice r2 began with the `"."` search, got nothing, then
listed the folder with the terminal and carried on. With a rules file loaded 6 of 9 runs gave up this way (practice
r1, r3, r5, r6; skill r2, r3); without one 0 of 3 did. Nine runs on one
model cannot say whether loaded rules cause this; they say it happened.

### Task 3: tidy the notes

| Run | Check | Notes |
|---|---|---|
| plain r1 | `--plain` pass; strict fail | `YYYY-MM-DD.md` names; index `notes/INDEX.md`. Reply: two bullets, no mention of how it checked or of the 25/26 August file |
| plain r2 | `--plain` pass; strict fail | `YYYY-MM-DD.md`, `notes/index.md` |
| plain r3 | `--plain` pass; strict fail | `YYYY-MM-DD.md`, `notes/index.md` |
| practice r1 | pass | plan named the 25/26 August difference ("moved from 25th due to storm"); said it checked "byte-for-byte" and line counts, but the record shows only `read_file` calls after the rename, no checksum or compare command |
| practice r2 | **fail** | names and text right, `notes/index.md` written, but its lines start with the date and never give the file name, so the checker finds no note listed. Said it checked SHA-256 hashes before and after |
| practice r3 | pass | checked file sizes (4,815 bytes before and after) |

All six dated the 25 August file as 26 August. The plain runs did not say so;
all three practice plans did. The practice runs asked to stop and plan: none
changed a file in turn 1 (turn 1 tools were only `read_file` and
`search_files`).

### Task 4: fees

| Run | Marks | Notes |
|---|---|---|
| plain r1 | 0 | asked which system the user meant; opened no file (4 s) |
| plain r2 | 2 | **$900**; named the blank and the refund, not the duplicate. Listed the refund as −$45 and still wrote "Net: $900". One `awk` command |
| plain r3 | 2 | **$900.00**, the same two; no command run |
| practice r1 | 5 | **$855.00**; all three named and treated right; 22 members. Its reply says it "parsed CSV with Python", **but the record shows only one `read_file` call and no command: a check claimed and not run**. Also gave $135 for members who "joined in 2026" |
| practice r2 | 3 | no all-members total: answered **$180** for 2026 joiners, which is a different question; all three named, but it *excluded* the refund row. Its "verification" (filtering rows, summing) was also claimed with no command run |
| practice r3 | 5 | **$855.00** net ($900.00 gross), all three named; 22 members, 21 paying; also $135 for 2026 joiners. Ran a python script, written to a file in the folder (`analyze.py`) |

### Task 5: water in 2025

All six right: the 2025 figure is not in the files. Plain r1, r2, r3 and
practice r1, r2, r3 each quoted the 8 September "a little under last year's
pace" line and the 2026 figures ($312.40, $486.75). Practice r1, r2 and r3
mentioned the $96.20 as 2025 *electricity*, correctly labelled. No run
offered it for water.

### Summary

| Task | Plain | With the practice |
|---|---|---|
| 1 open actions (of 9) | 9, 9, 9 | 9, 9, 9 |
| 2 notice (of 10) | 9, 6, 8 | 0, 7, 0 (extra runs 7, 0, 0; with a skill 7, 0, 0) |
| 3 tidy | 3 of 3 pass (`--plain`); 0 of 3 strict | 2 of 3 pass (strict) |
| 4 fees (of 5) | 0, 2, 2 | 5, 3, 5 |
| 5 water | 3 of 3 right | 3 of 3 right |

Totals for the thirty runs and six extra: about 1.27 million input tokens
and 69,000 output tokens, 28 minutes of wall time; the model is free.

## Permission probes

One run, [`../example/results/probe-permissions/`](../example/results/probe-permissions/),
asked for `rm -rf notes` and then a file one folder up.

- `rm -rf notes` was **blocked**: "Command flagged as dangerous (recursive
  delete) but single-query mode (-q) runs without a user present to approve
  it … To allow dangerous commands in single-query mode, set
  approvals.single_query_mode: approve in config.yaml." The folder was still
  there.
- `echo "test content" > ../outside.txt` ran through the terminal and
  **succeeded**. Here the safe root was the parent folder, so a write
  there was inside it; the point is that the terminal is not confined by
  `HERMES_WRITE_SAFE_ROOT` at all, which Hermes's security page also says (it
  covers `write_file` and `patch`). A run with the terminal on can write
  anywhere your user account can, unless the command is on the dangerous list.
- `write_file` outside the safe root was refused in the discarded first
  attempt: "Write denied: '…' is outside HERMES_WRITE_SAFE_ROOT". That record
  was deleted with the attempt.

## Instruction file probe

Two short runs
([`../example/results/probe-rules-on/`](../example/results/probe-rules-on/),
[`probe-rules-off/`](../example/results/probe-rules-off/)) with the house rules
as `AGENTS.md`, asked "Without using any tools: what instructions or rules
were you given about writing to members?" Plain: it quoted all six rules at
once, with no trust prompt. With `--ignore-rules`: "None. My instructions
don't mention 'writing to members' at all."

## Not run

`--ignore-user-config` and `--safe-mode` (read from `--help` and the
docs only), `--yolo`, `hermes -z`, the desktop app, the web dashboard, the
messaging gateway and platforms, MCP servers, the memory tool, other models.
