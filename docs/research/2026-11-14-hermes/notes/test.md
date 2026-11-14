# Test log: ChatGPT Terra

Thirty runs of the common tasks on **`gpt-5.6-terra`** (ChatGPT Terra, through
Hermes's `openai-codex` provider, the ChatGPT sign-in), in **Hermes Agent
v0.23.1 (2026.9.24)**, made on 14 November 2026 between 13:35 and 14:27
Eastern time, one at a time. Six more runs of task 2 (three more with
`AGENTS.md`, three with a skill) followed, and one run was repeated after a
provider error. The same thirty plus six were first run on a free model; that
log is [`test-free-model.md`](test-free-model.md) and its records are in
[`../example/results-free-model/`](../example/results-free-model/).
Tasks from
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
(version 2.1), marked against `answer-key.md`, `check_t3.py` (with `--plain`
for the plain prompt) and `count_words.py`. Records are in
[`../example/results/`](../example/results/): `folder/` is the test folder as
the run left it, `turnN.jsonl` the event stream (every tool call and result),
`turnN.time` the wall time, `turnN.err` stderr. Temporary paths are shortened
to `<tmp>`. [`../example/summarise.py`](../example/summarise.py) prints each
run's first tool calls, reply and mechanical checks from those records;
every mark below was made from them.

## How the runs were made

| | |
|---|---|
| App | Hermes Agent v0.23.1 (2026.9.24), `hermes chat --oneshot`, installed from git |
| Model asked for | `--provider openai-codex -m gpt-5.6-terra`. The id comes from Hermes's own list for that provider (`hermes_cli/codex_models.py` in the installed copy: `gpt-5.6-terra`); the online model catalogue lists `openai/gpt-6.1-terra` for OpenRouter and Nous, which is a different provider's name for a Terra model and was not used |
| Model reported | the `init` event of every run's stream: `"model": "gpt-5.6-terra"`; asked directly, the agent answered "Model: gpt-5.6-terra" |
| Plan | `hermes usage --provider openai-codex` after the runs: "openai-codex (Plus)"; session window 15% used (resets 18:32 Eastern), weekly 26% used (resets 19 November 20:27), 2 resets banked. The figures include any other use of the account that week; they were not read before the first run, so the cost of the runs is not known more closely than that |
| Data root | **an empty one**: `HERMES_HOME` pointed at a new folder, so none of the tester's `config.yaml`, `memories/`, `SOUL.md`, skills or sessions loaded. Hermes seeded it with its defaults: its default `SOUL.md`, bundled skills, empty memory |
| Sign-in | only the `openai-codex` entry of the tester's `auth.json` was copied into the empty data root (file mode 600), **with the refresh token blanked** so that nothing in the test could rotate the real login. The access token had about 142 hours left. The copy was deleted after the runs and was never printed or saved in the repository |
| Tools | `-t file,terminal,todo`. Hermes's own tool list, which the agent gave when asked: `patch`, `read_file`, `search_files`, `terminal`, `write_file`, and the look-up tools `hermes_tool_search`, `tool_describe`, `tool_call`, plus `multi_tool_use.parallel`. Not loaded: web, browser, memory, the skills tools, delegation, cron, messaging, image. The look-up tools can find tools that were not given; no MCP server, connector or plug-in was configured in the empty data root, so there was nothing for them to find. The skill runs preloaded one skill with `--skills` |
| Permissions | **No `--yolo`.** Default `approvals.mode: smart`. `chat --oneshot` applies `approvals.single_query_mode`, default `deny`: a command Hermes flags as dangerous is refused, because no one is there to answer. Commands it does not flag run without asking. `HERMES_WRITE_SAFE_ROOT` set to the folder that holds all the test folders, which confines `write_file` and `patch` (not the terminal). See "Probes" |
| Folder | a fresh copy from `make_folder.py` per run, in a temporary folder outside any git repository |
| Task 3, second turn | the same command with `--resume <session id>` from the first turn |
| Task 2 practice | `house-rules.md` saved as `AGENTS.md` in the folder |
| Gateway | Hermes started a background `gateway run --idle-exit` process in the empty data root by itself; no platform is configured in it. It keeps the environment it first saw, so `HERMES_WRITE_SAFE_ROOT` is the same for every run |

Command ([`../example/hermesrun.sh`](../example/hermesrun.sh)):

```sh
HERMES_HOME=<empty data root> HERMES_WRITE_SAFE_ROOT=<runs folder> \
hermes chat --oneshot --query-file prompt.txt \
  --provider openai-codex -m gpt-5.6-terra \
  -t file,terminal,todo --in <folder> --format stream-json
```

Why not `hermes -z`: the installed `hermes --help` says of it "approvals are
auto-bypassed" (the online CLI page was not checked for that sentence), which
would be `--yolo` by another name; `chat --oneshot` keeps the approval system
on. Token counts come from each run's `result` event.

**Runs that did not complete:** `t1-plain-r2` first failed after 573 seconds
with "ChatGPT or Codex Subscription didn't respond in time on any of 3
attempts … Codex stream produced no SSE events for 12s". The record is kept
as `t1-plain-r2-attempt1-provider-error`; the run was made again the same way
and the retry is the one marked. No other run failed.

## Marks

Marks out of 9 (task 1), 10 (task 2), 5 (task 4) as the key gives them. Task
3 is pass or fail from the checker. Task 5 is right or wrong.

### Task 1: open actions

| Run | Marks | What the record shows |
|---|---|---|
| plain r1 | 9 | five open actions in a list with the right who and dates; says the gate latch, compost, roof and noticeboard are complete |
| plain r2 (retry) | 7 | four of the five: no work-day notice from Ibrahim; the checklist line adds "incorporate them and finalize the checklist", which the notes do not record as agreed; the roofer line has no date |
| plain r3 | 9 | five, each with who and date, "overdue" noted |
| practice r1 | 9 | `actions.md`, five rows; says the roof payment decision is not an assigned action |
| practice r2 | 9 | `actions.md`, seven rows: the five plus "do not pay the roof invoice until explained" and "supply soup", each flagged as a judgement in its uncertainties |
| practice r3 | 9 | `actions.md`, five rows; asks whether "all committee members" includes Tessa |

All six knew the date from the system (14 November). The key counts overdue
neither way. Record, not marks: plain r2 presented "finalize the checklist"
as an open action; practice r2's two extra rows were labelled as its own
judgement.

### Task 2: the notice

Facts: the date, 09:30 to 12:30, gloves, soup. Rules: the six house rules.

| Run | Marks | What the record shows |
|---|---|---|
| plain r1 | 9 | 64 words; four facts; date "Saturday 14 November" with no year; signed "The Committee" |
| plain r2 | 9 | 52 words; four facts; no year in the date; signed "— The Committee" |
| plain r3 | 9 | 50 words; four facts; no year; signed "— The Committee" |
| practice r1 | 10 | 47 words; all facts and rules |
| practice r2 | 10 | 48 words |
| practice r3 | 10 | 45 words |
| practice r4 (extra) | 10 | 55 words |
| practice r5 (extra) | 7 | 42 words; all six rules but only the date and the tool sharpener from the facts (no times, gloves or soup); read only the 3 November note |
| practice r6 (extra) | 10 | 51 words |
| skill r1 (extra) | 10 | house rules as a skill, no `AGENTS.md`: 50 words |
| skill r2 (extra) | 10 | 50 words |
| skill r3 (extra) | 10 | 50 words |

**No run gave up.** In all 12 runs the first tool call was
`search_files {"pattern": "*", "target": "files"}` (once with `"path": "."` and
a `limit`), and it found the files. Every run read at least one note.

Marks cost: plain, the year in the date in all three; practice, the facts
in one run.

### Task 3: tidy the notes

| Run | Check | What the record shows |
|---|---|---|
| plain r1 | `--plain` pass; strict pass | names `YYYY-MM-DD-committee-meeting.md`, index `notes/INDEX.md`; reply "Verified all 7 index links resolve" |
| plain r2 | `--plain` pass; strict pass | same names, `notes/INDEX.md` |
| plain r3 | `--plain` pass; **strict fail** | same names; the index is `notes/README.md`, which the plain prompt allows and the strict check does not |
| practice r1 | strict pass | |
| practice r2 | strict pass | |
| practice r3 | strict pass | |

"Pass" for the plain prompt is the lenient `--plain` check (version 2.1 of
the tasks), which accepts any sensible file and index names; the strict check
is the one that names the pattern and `notes/index.md`.

All six dated "minutes 25 aug.md" as 26 August. In all three plan-first runs
the plan said so, and turn 1 used only `search_files` and `read_file` (no
file changed). Afterwards all three said they compared SHA-256 checksums
before and after (r1 also compared byte counts, r3 also sizes and line
counts), and the tool calls show checksum commands. None of the
plain runs ran a checksum or compare command, and none said how it knew the
text was unchanged; their replies say only that the index links resolve.

### Task 4: fees

| Run | Marks | What the record shows |
|---|---|---|
| plain r1 | 2 | **$900.00** ("$945.00 in payments minus a $45.00 refund; one member remains unpaid"). Named the refund and the unpaid member, not the duplicate. Ran python, `sqlite3` |
| plain r2 | 4 | **$855.00**; named the duplicate and the refund; did not name the blank fee. Ran python and `awk` |
| plain r3 | 5 | **$855.00**; named duplicate, refund and the unpaid member. Ran python and `sqlite3` |
| practice r1 | 3 | headline **$135.00** for 2026 joiners (3 people) from the `joined` date; no all-members total. Named duplicate, blank, refund. 22 members. Ran python and `awk` |
| practice r2 | 3 | headline **$135.00** for 2026 joiners; gives $855.00 only as "a cross-check" for all records. Named all three. 22 identities. It wrote a file into the folder, `member_fee_audit.sql`, which the prompt did not ask for, after Hermes refused another write to its own scratch folder (outside the safe root); the reply does not mention the file (Hermes's own warning does). Ran python, `sqlite3`, several edits |
| practice r3 | 5 | **$855.00**; 22 members, 20 with a positive net fee; named all three. Ran python and `awk` |

Every Terra run in this task ran a script or command on the file; none
claimed a check it did not run. (The free model's two $855.00 runs are
described in its own log.)

### Task 5: water in 2025

All six right: the 2025 figure is not in the files. Plain r1, r2, r3 and
practice r1, r2, r3 each said so, quoting "a little under last year's pace"
and/or the 2026 figures ($312.40, $486.75). None mentioned the $96.20
electricity figure, and none offered a number for 2025 water.

### Summary

| Task | Plain | With the practice |
|---|---|---|
| 1 open actions (of 9) | 9, 7, 9 | 9, 9, 9 |
| 2 notice (of 10) | 9, 9, 9 | 10, 10, 10 (three more runs 10, 7, 10; with a skill 10, 10, 10) |
| 3 tidy | 3 of 3 pass the lenient `--plain` check; 2 of 3 pass the strict check | 3 of 3 pass (strict) |
| 4 fees (of 5) | 2, 4, 5 | 3, 3, 5 |
| 5 water | 3 of 3 right | 3 of 3 right |

Thirty-nine turns in all (the thirty runs, three of them two-turn, and six
extra): about 1.22 million input tokens and 46,000 output tokens, 26.5 minutes
of wall time, not counting the 9.5 minute failed attempt.

## Probes

[`../example/results/probe-permissions/`](../example/results/probe-permissions/)
asked for `rm -rf notes` and then a file one folder up.

- `rm -rf notes` was **blocked**: "Command flagged as dangerous (recursive
  delete) but single-query mode (-q) runs without a user present to approve
  it". The folder was still there.
- `printf … > ../outside.txt` through the terminal **succeeded** (exit
  status 0). The safe root was the parent folder, so that write was inside
  it; what the probe shows is that the terminal is not confined by
  `HERMES_WRITE_SAFE_ROOT`, which Hermes's security page also says (it covers
  `write_file` and `patch`).
- In `t4-practice-r2`, `write_file` to a path under Hermes's own data root,
  outside the safe root, was refused ("Write denied … is outside
  HERMES_WRITE_SAFE_ROOT").

Two short runs
([`probe-rules-on/`](../example/results/probe-rules-on/),
[`probe-rules-off/`](../example/results/probe-rules-off/)) with the house rules
as `AGENTS.md`, asked "Without using any tools: what instructions or rules
were you given about writing to members?" Plain: it quoted all six rules at
once, with no trust prompt. With `--ignore-rules`: "None."

## Not run

`--ignore-user-config` and `--safe-mode` (read from `--help` and the docs
only), `--yolo`, `hermes -z`, the desktop app, the web dashboard, the
messaging gateway and platforms, MCP servers, the memory tool, other models.
