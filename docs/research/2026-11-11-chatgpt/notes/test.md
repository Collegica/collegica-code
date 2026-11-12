# Test log: the five common tasks (version 2), and four leads

Run on Wednesday 11 November 2026, 20:20 to 20:48 UTC, on the test machine,
with the tasks in
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
(**version 2** of the tasks and answer key) and marked against its
`answer-key.md`, `check_t3.py` and `count_words.py`. Task 3 plain was
re-marked on 11 November (evening) with `check_t3.py --plain`, as version 2.1
of the key says; both results are below. Each run's outputs are in
[`../example/results/<task>-<plain|practice>-r<n>/`](../example/results/).
The Claude guide has since run version 2 too, so its marks are comparable
with these (it marked task 3 plain the same way, under version 2.1).

## How every run was made

| | |
|---|---|
| App | Codex CLI 0.166.0 (`codex --version`; `cli_version` in every session log). Newer versions were out and were not installed. |
| Account | the owner's ChatGPT plan, signed in (`codex login status`: "Logged in using ChatGPT") |
| Model | `-m gpt-6.1-sol` on every run; **`gpt-6.1-sol` reported** in every session log, every turn |
| Effort | not set on the command line; **`low` reported** in every run. That was the test account's existing setting; no vendor page read says `low` is the default for GPT-6.1 Sol (the models page says to "start with the reasoning effort available by default in your client"). One lead set `high`. |
| Command | `python3 example/run.py <run-dir> <prompt>`, which runs `codex exec -m gpt-6.1-sol --skip-git-repo-check --json -o <file> -s workspace-write -C <folder> <overrides> "<prompt>"` from inside the folder |
| Task 3, second turn | `codex exec resume <session-id> -m gpt-6.1-sol -c sandbox_mode="workspace-write" <overrides> "<prompt>"` (resume has no `-s`) |
| Task 2 practice | `house-rules.md` copied into the folder as `AGENTS.md` |
| Folder | a fresh copy from `make_folder.py` for every run, in a temporary folder outside every git repository |
| Parallel | three runs at a time |
| What is kept | each run's folder after the run, the JSON event stream, the last message, and `run.json` (start time, wall time, session id, token use, and the model, effort and version copied from Codex's own session log). The session logs themselves are not copied: they hold account ids. Whether each run loaded an instruction file was read from the logs afterwards into [`instructions-loaded.txt`](../example/results/instructions-loaded.txt). Paths are shortened to `<tmp>/`, the user name to `<user>`, and the name of the owner's bundled plugin to `[bundled-plugin]`. |

### No MCP servers: what was tried, and the evidence

The owner's existing configuration (`~/.codex/config.toml`) defines MCP
servers and plugins. It was read, never edited. All switching-off is done
with command-line flags, in `example/run.py`, which reads the names from the
file at run time:

1. **First try** (`tools-check`): `-c mcp_servers.<name>.enabled=false` for
   each server, `-c plugins."<name>".enabled=false` for each plugin,
   `--disable apps` (connectors), `--disable memories`, `-c notify=[]`.
   Asked to list its tools, Codex reported **two MCP tools still loaded**,
   provided by a plugin bundled with the desktop app (shown as
   `[bundled-plugin]` in the saved output). The session log confirmed the
   tool namespace.
2. **Second try** (`tools-check-2`): added `-c plugins._default.enabled=false`,
   `--disable computer_use`, and
   `-c plugins."<plugin>".mcp_servers.<server>.enabled=false` for each MCP
   server named in each plugin's cached `.mcp.json`. **Still loaded**, same
   two tools.
3. **A probe** with `--ephemeral` and three variants: top-level
   `-c mcp_servers.<that server>.enabled=false` (no answer returned);
   `--disable plugins` ("NONE"); `--ignore-user-config` ("NONE").
4. **Third try** (`tools-check-3`): everything in 1 and 2 plus
   **`--disable plugins`** (that is, `features.plugins=false`). Codex's
   answer: "**No MCP server tools, plugin tools, or connector/app tools are
   exposed in this session.**" The session log lists only three tool
   namespaces, `clock`, `collaboration` and `functions`; no `mcp__` namespace.
   (The only `mcp__` text in the log is an example name inside Codex's own
   instructions.)

Every task and lead run used the third set. **Every run's `run.json`
records `tool_namespaces: clock, collaboration, functions`**, read from its
session log. `--ignore-user-config` was not used: it also drops the rest of
the owner's settings, which the shared README says should load.

**What still loaded, as it would for anyone:** the rest of the owner's
existing configuration, including its reasoning effort (`low`) and a global
instruction file that added no rules; the default web search (`cached`, an
OpenAI index, not live). No run used web search (no `web_search` item in any
event stream).

**Switched off besides MCP, and why:** the app's local memories
(`--disable memories`), so that one run could not be remembered by the next
and no test run was written into a memory store. The `notify` program (a
desktop notification) was set to nothing so the runs had no side effects on
the test machine.

## Results

Wall time is from the start of the `codex exec` call to its end. Input
tokens are mostly the same cached context (Codex's own instructions and
tools): about 77,000 per turn, of which about 67,000 cached.

### Task 1: open actions (marks out of 9)

| Run | Plain | Practice | Wall time, plain / practice |
|---|---|---|---|
| 1 | 9 | 9 | 21.0 s / 22.6 s |
| 2 | 9 | 9 | 20.5 s / 24.7 s |
| 3 | 9 | 9 | 19.0 s / 25.5 s |

- **Plain, all three:** all five open actions with the right person and
  date; the roofer question once, at 10 November; the tap with Dov; nothing
  finished listed as open. All three began "As of **11 November**" and
  called the 7 and 10 November items overdue or unconfirmed (neither right
  nor wrong, per the key). All three added things the key does not ask for:
  "Run the work day" (runs 1 and 3), "Complete winter closing" (1 and 3), the
  blank fee for Leontyne Quist (all three; run 1 gave it to Ibrahim, an owner
  the notes do not name), and the duplicate and refund rows in
  `members.csv`. Each listed the finished items as finished. No file was
  written, as none was asked for.
- **Practice, all three:** `actions.md` with exactly the five, the right
  people, dates and source note, and a list of doubts under the table. Runs
  1 and 2 noted that `minutes 25 aug.md` is headed 26 August. Each said no
  other file was changed.

### Task 2: the notice (marks out of 10: four facts, six house rules)

| Run | Plain (no instruction file) | Practice (`AGENTS.md` with the house rules) | Words, plain / practice |
|---|---|---|---|
| 1 | 8 | 10 | 82 / 63 |
| 2 | 9 | 10 | 96 / 63 |
| 3 | 7 | 10 | 102 / 63 |

Words by `count_words.py`. Wall time, plain: 16.6, 16.7, 14.2 s; practice:
16.3, 13.9, 14.5 s.

- **Facts:** all four in all six runs. All six also gave the tool sharpener
  at 10:00 and the water shut-off.
- **Plain, rules missed:** 12-hour times ("9:30 a.m.", "9:30 am") in runs 1
  and 3; an exclamation mark in run 3; signed "The Committee" (run 1) or "The
  Alder Lane Community Garden Committee" (runs 2 and 3). The signature rule
  quotes "The committee", so a capital C is marked as a miss; marked the
  other way, run 1 scores 9. The date in full with weekday and year, British
  spelling and the length held in all three without being asked.
- **Practice:** every rule in all three. The session logs showed the file
  loaded as instructions before the first turn in all three (an
  `<INSTRUCTIONS>` block holding the house rules; see
  `instructions-loaded.txt`). Two of the three notices are word for word
  the same.

### Task 3: tidy the notes

| Run | Plain: `check_t3.py --plain` (v2.1, the mark) | Plain: strict `check_t3.py` (v2) | Plain: said how it checked | Practice: `check_t3.py` | Practice: said how it checked |
|---|---|---|---|---|---|
| 1 | passed (exit 0) | failed: no `notes/index.md` | no | passed (exit 0) | yes: SHA-256 and byte count, before and after |
| 2 | passed | failed: no `notes/index.md` | no | passed | yes: SHA-256 and byte count |
| 3 | passed | failed: no `notes/index.md` | no | passed | yes: "byte-for-byte identical"; the plan named SHA-256 |

The plain runs were first marked with the strict version 2 check, which
wants the names and the index the careful prompt gives. Version 2.1 of the
key marks the plain prompt with `--plain`, which accepts any name starting
with the right date and any new file listing every note as the index;
re-run on the saved folders, all three pass. The strict result is kept for
the record.

Wall time, plain: 27.1, 25.9, 25.7 s. Practice, two turns: 18.7 + 25.5,
24.1 + 23.5, 22.5 + 24.9 s.

- **Plain:** in all three, the seven notes were renamed correctly
  (`YYYY-MM-DD-minutes.md` or `-committee-meeting.md`), dates taken from the
  headings, text unchanged, **and the index written as `notes/README.md`**,
  linked from the top-level README. The strict check wants
  `notes/index.md`, so it failed every plain run; `--plain` passes all
  three. The plain prompt says "and an index"; it does not name the file. Each reply said the contents were "unchanged" or
  "preserved" without saying how; run 1's script did hash the files, but the
  reply did not say so. All three noticed the 26 August heading and used it.
- **Practice, turn 1 (plan only):** all three changed nothing ("No files
  have been changed"), gave the rename table, said the date comes from each
  heading, flagged the 25/26 August mismatch, and named SHA-256 hashes and
  byte counts as the check. Turn 2: renamed, wrote `notes/index.md`, and
  listed what it checked.
- **All six** ran `find .. -name AGENTS.md` at the start, looking one folder
  up for instruction files. That folder held only the run's own files.

### Task 4: fees (marks out of 5)

| Run | Plain | Practice |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 4 | 5 |

Wall time, plain: 16.8, 18.5, 19.0 s; practice: 28.6, 33.6, 33.8 s.

- **The total was right in all six: $855** ("CAD $855 net"), each saying it
  was $900 less a $45 refund.
- **Plain:** all three named the duplicate (Bram Lindqvist) and the refund.
  Run 1 named the blank (Leontyne Quist), run 2 said "One member's fee remains
  unpaid", run 3 did not mention it: the lost mark. None gave a member count
  or said how it checked, which the plain prompt does not ask for.
- **Practice:** all four planted problems named and treated, plus the two
  half-season fees. Member count: 22 in all three (run 3: "or 21 remaining"),
  explained. Checks: two independent sums in each ("19 × $45 + 2 × $22.50 −
  $45 refund = $855.00"; "$900.00 − $45 duplicate = $855.00"). Run 2 added
  that the file cannot prove the fees are for 2026.

### Task 5: water in 2025

| Run | Plain | Practice |
|---|---|---|
| 1 | right | right |
| 2 | right | right |
| 3 | right | right |

Wall time, plain: 14.7, 14.1, 15.3 s; practice: 12.7, 12.6, 13.3 s.

- No run gave a figure for 2025, and none used the $96.20 electricity
  figure. All six said the records do not state it.
- **Plain** cited the 8 September note ("Paolo didn't have last year's
  figure"); runs 1 and 3 also said the $486.75 is for 2026. None gave the
  $312.40.
- **Practice:** all three gave both 2026 figures ($312.40 by September,
  $486.75 for the year) and the "slightly below the previous year's pace"
  line, as asked.

### All thirty, in one table

| Task | Plain, runs 1 / 2 / 3 | Practice, runs 1 / 2 / 3 | Did the practice change the result? |
|---|---|---|---|
| 1 Open actions (of 9) | 9 / 9 / 9 | 9 / 9 / 9 | No for the marks; yes for the form (a file, only the five, the doubts listed) |
| 2 Notice (of 10) | 8 / 9 / 7 | 10 / 10 / 10 | Yes: the rules held only with `AGENTS.md` |
| 3 Tidy (`check_t3.py`; plain with `--plain`) | pass / pass / pass | pass / pass / pass | No for the result (strict v2 check: plain failed ×3, on the index's file name only); yes for saying how it checked |
| 4 Fees (of 5) | 5 / 5 / 4 | 5 / 5 / 5 | Barely: one mark, one plain run left out the blank fee |
| 5 Water 2025 | right ×3 | right ×3 | No for the answer; yes for giving what the files do hold |

## Leads tested

Four of the leads in [`leads.md`](leads.md), three runs each, the same
set-up as above. The prompts and files are in `../example/leads/`.

### Lead A: rules in capitals, with IMPORTANT and NEVER

Task 2 with the house rules rewritten in capitals
([`caps-rules.md`](../example/leads/caps-rules.md)) as `AGENTS.md`, against
the plainly worded `AGENTS.md` of task 2 practice.

| Run | Plain-worded rules | Rules in capitals | Words, plain-worded / capitals |
|---|---|---|---|
| 1 | 10 | 10 | 63 / 65 |
| 2 | 10 | 10 | 63 / 63 |
| 3 | 10 | 10 | 63 / 64 |

**Failed** as a tip: the capitals added nothing, because the plain wording
already scored full marks in three runs out of three. Wall time 17.0, 15.0,
14.5 s.

### Lead B: "Codex only reads AGENTS.md; a CLAUDE.md is ignored"

Task 2 with the house rules saved as `CLAUDE.md` and no `AGENTS.md`.

| Run | Marks (of 10) | Words | Rules loaded as instructions? | Read the file anyway? |
|---|---|---|---|---|
| 1 | 10 | 63 | no | yes: `cat CLAUDE.md README.md notes/*.md` |
| 2 | 10 | 65 | no | yes, same command |
| 3 | 10 | 65 | no | yes, same command |

**Passed as stated, made no difference here.** In three runs out of three
the session log had no instruction block (recorded per run in
[`instructions-loaded.txt`](../example/results/instructions-loaded.txt); the
logs themselves are not kept, because they hold account ids): Codex did not
load `CLAUDE.md` as instructions, as its documentation says. But in a folder this small it
listed every file, opened `CLAUDE.md` with the notes, and followed every
rule. In a large folder, where it opens only what looks relevant, that
cannot be counted on. Wall time 14.7, 14.4, 14.5 s.

### Lead C: turn the reasoning effort up

The plain task 4 prompt with `-c model_reasoning_effort="high"` (reported
`high` in all three).

| Run | Marks (of 5) | Wall time | Reasoning tokens |
|---|---|---|---|
| 1 | 5 | 22.8 s | 57 |
| 2 | 5 | 25.8 s | 0 |
| 3 | 5 | 23.4 s | 54 |

All three: $855, the duplicate, the refund, and "One member's fee remains
unpaid". None gave a member count or said how it checked. Against the plain
prompt at `low` (5, 5, 4), one mark in one run.

**Failed to show a difference** worth the cost: the same answer as at `low`,
about 6 seconds slower on average (24.0 s against 18.1 s) and about 14,000
more input tokens a run on average (113,000 against 99,000). Asking for
the check in words (task 4 practice) got the count and the check; turning
the effort up did not, in three runs out of three.

### Lead D: correct it once, and ask it to update AGENTS.md

Three turns, in a fresh folder with no instruction file:

1. The task 2 prompt.
2. In the same session (`codex exec resume`), the correction
   ([`correction.txt`](../example/leads/correction.txt)): the six rules in
   one paragraph, then "Fix notice.md, then update your AGENTS.md so you
   don't make that mistake again."
3. `notice.md` moved out of the folder, and the task 2 prompt again in a
   **new** session, which has only what turn 2 wrote down.

| Run | 1. First notice | 2. After the correction | 3. New session | Words, 1 / 2 / 3 |
|---|---|---|---|---|
| 1 | 8 | 10 | 10 | 88 / 88 / 54 |
| 2 | 7 | 10 | 10 | 97 / 90 / 50 |
| 3 | 8 | 10 | 10 | 100 / 93 / 55 |

- **First notices:** exclamation mark (runs 1 and 2), 12-hour times (2 and
  3), signed "The Committee" or the garden's committee (all three), and run 3
  named a person ("Wren will shut off the garden's water").
- **Turn 2** wrote an `AGENTS.md` in all three (kept as `AGENTS-written.md`):
  the six rules in its own words, plus a line it added unasked, worded
  differently each time. Run 1: "Check every member communication against
  these rules before saving it." Run 2: "Check every rule before saving a
  member communication. Use the committee's notes as the source of factual
  details." Run 3: "Before saving a member communication, check every rule
  above and count all words, including the heading and signature."
- **Turn 3:** the session logs showed the new `AGENTS.md` loaded as
  instructions in all three, and every rule held. The notices were shorter
  than any other in the tests (50 to 55 words).

**Passed:** in three runs out of three, one correction turned into a file
that fixed the next session. OpenAI's best-practice page says the same:
"When Codex makes the same mistake twice, ask it for a retrospective and
update `AGENTS.md`."

## Not done

- No run of the chat or the desktop app: nothing there can be scripted from
  here. See the README, *For the owner*.
- No lead about the chat app (custom instructions, memory, Temporary Chat)
  was tested, for the same reason.
- The interactive `/plan` mode was not tested; task 3's "tell me your plan,
  then stop" is the nearest thing a script can do.
