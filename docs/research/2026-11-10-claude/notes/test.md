# Test log

Two rounds. **Version 2** (11 November 2026, local time; 02:00 to 02:07 UTC on 12 November) is the one the guide rests on: the revised tasks, Claude Opus
5.5 pinned, no connectors. **Version 1** (11 November 2026) used the first
version of the tasks on the model the owner's account had selected at the time (Fable 5.2, then Sonnet 5.5); it is kept below, labelled, as earlier evidence.

# Version 2: Opus 5.5, revised tasks, no connectors

Tasks, prompts and key:
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
as revised on 2026-11-11 (seven notes; a 25/26 August date trap; a 2025
electricity figure as a near miss; task 4 marked out of 5 for both prompts).
Each run's outputs are in
[`../example/results-v2/<task>-<plain|practice>-r<n>/`](../example/results-v2/):
the prompt, the reply, `run.json` (model, tools, MCP servers, wall time,
API-equivalent cost) and `folder-after/`, the test folder as the run left it.

## How every run was made

| | |
|---|---|
| Date | 11 November 2026, local time; 02:00 to 02:07 UTC on 12 November (the end time of each run is in its `run.json`) |
| App | Claude Code 2.1.322, as reported in each run's own `init` event |
| Model | `claude-opus-5-5`, pinned with `--model`, and reported as `claude-opus-5-5` by every one of the 43 turns, both in the `init` event and in `modelUsage` |
| Effort | not passed, so the owner's own effort setting applied, which is not the default (`medium`); not changed |
| Command | `claude -p "<prompt>" --model claude-opus-5-5 --strict-mcp-config --no-chrome --permission-mode auto --output-format stream-json --verbose`, run from inside the test folder |
| Task 3, second turn | the same, with `--resume <session id>` |
| Task 2 practice | `house-rules.md` saved as `CLAUDE.md` in the test folder |
| Folder | a fresh copy from `make_folder.py` for every run, in a temporary folder outside the repository and outside any git repository; copied here as soon as the run ended, and committed after every batch of three |
| Loaded as configured | the tester's own Claude Code set-up (instruction file, settings and hooks); nothing was changed or switched off except by the flags above |

### No connectors: the evidence

Before the first run, a run in a fresh folder was asked to list its tools
([`../example/results-v2/tools-check/`](../example/results-v2/tools-check/)).

- The app's own `init` event: `"mcp_servers": []`, and 25 tools, none with
  an `mcp__` name: Task, Bash, CronCreate, CronDelete, CronList,
  DesignSync, Edit, EnterWorktree, ExitWorktree, ListAgents, Monitor,
  NotebookEdit, PushNotification, Read, RemoteTrigger, ReportFindings,
  ScheduleWakeup, SendMessage, Skill, TaskStop, ToolSearch, WebFetch,
  WebSearch, Workflow, Write.
- Its reply: "None of these are MCP or connector tools: no tool has an
  `mcp__` prefix, and none is backed by a connector."
- Every one of the 42 turns after it logged the same: `mcp_servers` empty,
  no `mcp__` tool.

`--no-chrome` was passed as well, so the built-in Chrome integration could
not load. Web search and web fetch remained available (they are built-in
tools, not connectors); no reply cites the web.

**No usage limit was hit.** All 30 runs and the lead's 9 turns completed.
API-equivalent cost of everything in version 2, tools check included:
US$9.75, about US$0.22 a single-turn run, against about US$1 a run on
Fable 5.2 in version 1. No run had a command refused (`permission_denials` 0 in all),
unlike version 1, where every run had at least one.

## Results

### Task 1: open actions (marks out of 9)

| Run | Plain | Practice | Wall time, plain / practice |
|---|---|---|---|
| 1 | 9 | 9 | 36.1 s / 41.3 s |
| 2 | 9 | 9 | 35.9 s / 44.4 s |
| 3 | 9 | 9 | 35.8 s / 39.7 s |

- All six found the five open actions, with the second tap given to Dov
  (not Nell) and due 17 November, and the roofer question once at 10
  November. All six counted the noticeboard as done.
- **Plain** answered in the chat, no file, and added the fee problems in
  `members.csv`, a doubt about the half-season rates, and in run 2 "the club
  supplies soup, so someone needs to arrange it". The key costs nothing for
  these.
- **Practice** wrote `actions.md` with exactly the five, listed the finished
  actions separately, and put doubts (paying the roofer, finishing the
  checklist, soup, Dov not being on the committee, the 25/26 August file
  name) under the table.
- **No difference in marks**, as in the ChatGPT guide's runs.
- **Recorded separately (key v2.1): actions nobody agreed to.** Plain run 2
  listed two: "Close the garden at the end of November, using the finished
  checklist" (the notes record a decision to close, not an action anyone
  took on) and "The club supplies soup, so someone needs to arrange it".
  Plain runs 1 and 3 also listed closing the garden at the end of November,
  with no owner ("Tessa's checklist needs finishing before then" in run 1;
  "close the garden using the finished checklist" in run 3). No practice run listed any; all three put these
  under "unsure".

### Task 2: the notice (marks out of 10)

Words by `count_words.py`.

| Run | Plain | Practice | Words, plain / practice |
|---|---|---|---|
| 1 | 7 | 10 | 132 / 87 |
| 2 | 8 | 10 | 137 / 99 |
| 3 | 7 | 10 | 138 / 80 |

- Facts: all four in all six.
- **Plain, rules missed:** over 120 words in all three; signed "The Alder
  Lane Community Garden committee" (runs 1, 3) or "Ibrahim Solheim, for the
  Alder Lane Community Garden committee" (run 2, a personal name); the year
  missing from the date in runs 1 and 3. 24-hour times, British spelling
  and no exclamation marks held without being asked.
- **Practice:** every rule, in three runs out of three.

Wall time, plain: 31.4, 31.4, 31.8 s; practice: 30.6, 29.6, 30.7 s.

### Task 3: tidy the notes

| Run | Plain: strict `check_t3.py` | Why strict failed | Plain: `check_t3.py --plain` (v2.1) | Practice: strict `check_t3.py` |
|---|---|---|---|---|
| 1 | fail | file-name pattern only: `2026-08-11.md`, no words after the date | pass | pass |
| 2 | fail | file-name pattern, and the index named `INDEX.md`, which the strict check counts as an eighth note | pass | pass |
| 3 | fail | file-name pattern, and `INDEX.md` counted as an eighth note | pass | pass |

Summary: plain, strict fail / `--plain` pass in three runs out of three;
practice, strict pass in three runs out of three. `--plain` was run on
11 November 2026 (local time) on the saved `folder-after/` of each run.

- **The plain failures under the strict check are the checker's, not the work's.** In all three
  plain runs every note's text was unchanged (the checker's own "text
  unchanged" lines pass) and each was named for its own meeting date,
  including `2026-08-26.md` for the file called `minutes 25 aug.md`. The
  checker wants `YYYY-MM-DD-<words>.md` and `notes/index.md`, which the plain
  prompt does not ask for. The guide counts them as right and says so.
- **The 25/26 August trap** was caught in six runs out of six. Each plain
  reply said so ("the file called `minutes 25 aug.md` is dated 26 August …
  moved from the 25th because of the storm"); each practice plan flagged it
  before changing anything.
- **Said how it checked that no text was lost:** plain, none of three. Run
  1: "I didn't change what's written in any of the minutes"; run 2: "I
  didn't change anything inside the minutes"; run 3: "Only the file names
  changed; nothing inside the notes was edited". None said how it knew.
  Practice, three of three: a checksum of every note before and after (run
  1 says "checksum … a fingerprint of the exact contents"; runs 2 and 3 say
  SHA-256), plus links and file count.
- **"Changed nothing" after turn 1** rests on the practice replies ("Nothing
  has been changed" or the like); the folder was not snapshotted between
  the two turns, so it is not independently checked.
- **Two things not asked for.** All three plain runs also edited the
  folder's `README.md` to mention the new names. Practice run 2 kept its
  checksums in a `check/` folder "one level above the garden folder",
  outside the folder it was given, and said so; runs 1 and 3 kept theirs in
  a temporary folder and deleted them.

Wall time, plain: 34.6, 38.5, 33.7 s; practice (two turns): 69.2, 69.1,
76.3 s.

### Task 4: fees (marks out of 5, the same for both prompts)

| Run | Plain | Practice |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |

- **$855.00 in all six**, with the duplicate, the blank and the refund
  named. All six also said that a plain sum gives $900 only because the
  duplicate and the refund cancel out.
- Recorded separately: **member count.** Plain runs 1 and 2 gave 22 listed
  and 21 paid, unprompted; run 3 gave none. Practice runs 1 and 3 gave 22 listed,
  21 current, 20 paid; practice run 2 gave 22 listed, 21 paid, 1 not, and 21
  current once the refunded member is left out. All explained. **How it checked:** the plain runs
  explained the arithmetic but did no second check; all three practice runs
  checked twice (a script grouping rows by email, and a hand count).

Wall time, plain: 28.2, 28.9, 32.5 s; practice: 37.7, 36.7, 35.1 s.

### Task 5: water in 2025

| Run | Plain | Practice |
|---|---|---|
| 1 | right | right |
| 2 | right | right |
| 3 | right | right |

All six said the 2025 water figure is not in the files, gave the 2026
figures, and named the $96.20 as **electricity**, not water. None offered a
2025 water amount. With no connectors, no run had anywhere to look but the
folder and the web.

Wall time, plain: 22.3, 24.8, 26.1 s; practice: 21.7, 21.1, 21.3 s.

### All thirty, in one table

| Task | Plain, runs 1 / 2 / 3 | Practice, runs 1 / 2 / 3 | Did the practice change the result? |
|---|---|---|---|
| 1 Open actions (of 9) | 9 / 9 / 9 | 9 / 9 / 9 | No; it changed the form (a file, only the five, doubts listed) |
| 2 Notice (of 10) | 7 / 8 / 7 | 10 / 10 / 10 | Yes |
| 3 Tidy (`check_t3.py`) | strict fail / `--plain` pass, ×3 (strict fails only on the name pattern and `INDEX.md`) | strict pass / pass / pass | The work was right either way; the plan made it state its check |
| 4 Fees (of 5) | 5 / 5 / 5 | 5 / 5 / 5 | No; it added a second check of the total |
| 5 Water 2025 | right ×3 | right ×3 | No |

## The lead, on Opus 5.5: correct once, then update CLAUDE.md

The one lead that passed in version 1 (on Sonnet 5.5), run again the same
way, three times: the task 2 prompt in a folder with no instruction file;
then in the same session the correction ("That notice breaks our house
rules … [the six rules] … Fix notice.md, then update your CLAUDE.md so you
don't make that mistake again."); then `notice.md` deleted and the task 2
prompt in a **new** session. Outputs in
[`../example/results-v2/learn-r<n>/`](../example/results-v2/).

| Run | First notice | After the correction | New session | Words (`count_words.py`), 1 / 2 / 3 |
|---|---|---|---|---|
| 1 | 8 | 10 | 10 | 123 / 100 / 80 |
| 2 | 8 | 10 | 10 | 122 / 98 / 107 |
| 3 | 7 | 10 | 10 | 126 / 91 / 105 |

- First notices: over 120 words and signed "The Alder Lane Community Garden
  Committee" in all three; the year missing in run 3; run 2 named a person
  ("Wren will turn off the garden's water").
- After the correction each wrote a `CLAUDE.md` with the six rules,
  sharpened with examples of what not to do ("Never write '14 Nov' … or a
  date without its weekday and year"; "Say 'the water will be turned off',
  not 'Wren will turn off the water'") and a way to check the length ("Count
  with `wc -w` before saving").
- The new session left `CLAUDE.md` unchanged and followed every rule.

**Passed on Opus 5.5**, in three runs out of three, as on Sonnet 5.5.

Wall time per turn: run 1 34.4, 29.0, 31.5 s; run 2 33.7, 31.3, 30.5 s;
run 3 36.3, 27.0, 29.7 s.

---

# Version 1: Fable 5.2 and Sonnet 5.5, first version of the tasks

Kept as earlier evidence. These runs used the first version of the tasks
(five notes; task 1 out of 7, task 4 out of 7) and are not comparable mark
for mark with version 2.

Run on 11 November 2026 (UTC; the first attempt at 03:27 UTC), with the tasks in
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
and marked against its `answer-key.md` and `check_t3.py`. Each run's outputs
are in [`../example/results/<task>-<plain|practice>-r<n>/`](../example/results/).

### How every run was made

| | |
|---|---|
| App | Claude Code 2.1.322 (`claude --version`) |
| Model | `claude-fable-5-2` in every run (from each run's `modelUsage`) |
| Effort | not passed, so the owner's own effort setting applied, whatever it was at the time (not recorded); the default is `medium` |
| Account | the owner's subscription, signed in |
| Command | `claude -p "<prompt>" --permission-mode auto --output-format json`, from inside the test folder |
| Task 3, second turn | the same command with `--resume <session id>` from the first turn |
| Task 2 practice | the content of `house-rules.md` saved as `CLAUDE.md` in the test folder |
| Folder | a fresh copy from `make_folder.py` for every run, in a temporary folder outside the repository and outside any git repository |
| Parallel | three runs at a time, each in its own folder |

**As the owner has it configured.** The tester's own Claude Code set-up
(instruction file, settings, hooks and connectors) loaded in every run; nothing was changed or switched off. That file holds no writing rules, so it should not have helped task 2. The model was Fable 5.2 because the owner's account had selected it; **a new Pro, Max or Ultra subscriber starts
on Opus 5.5** (model-config page, read 2026-11-10), so these results are for
a model a beginner would not get by default.

**Two things a reader of the results should know.**

- **Every run hit at least one blocked command, and every run still
  finished.** The safety check in auto mode refused Bash loops such as
  `for f in notes/*; do cat "$f"; done`: each of the thirty runs of the
  common tasks has at least one such refusal in its `permission_denials`. Claude then read the
  files with its own Read tool and carried on. None of the marks below was
  lost to a refusal.
- **One plain run reached outside the folder.** In task 5 run 3 (plain), it
  tried a connected service from the owner's account "in case the club's books are there", and was stopped only because the connector needed signing in
  again. The careful prompt ("Answer only from the files in this folder")
  did not do this in any run.

**The usage limit stopped the first attempt.** The first batch, started 2026-11-11 at 03:27 UTC, ran task 1 (plain) three times and then
hit "You've hit your 5-hour limit". The 27 runs after that returned the
limit message in about 2 seconds without doing anything. They are **not
run**, not failed; their stubs are kept under `limit-hit-attempt/` in each
result folder. All 27 were run again from 13:10 UTC, each in a
new fresh folder. Two of the limit-hit attempts (task 1 practice, runs 1 to
3) had started work before being cut off; those partial outputs are not
marked.

**How the outputs were kept.** The temporary folder holding the test
folders was emptied before its contents had been copied here. The outputs in
`example/results/` were rebuilt from Claude Code's own session transcripts by
[`../example/recover.py`](../example/recover.py): each file the run wrote with
its Write or Edit tool, every Bash command it ran, its prompt and its last
reply. The marks below were made from the live folders before they were
lost, and checked again against the rebuilt files. Wall times and the
API-equivalent cost were read from each run's JSON before the loss and are
copied here; the JSON itself was not kept. The paths in the rebuilt files are
shortened to `<tmp>/`, and one connector's name is replaced in task 5 run 3.

### Results

Wall time is from the start of the `claude -p` call to its end. "API
equivalent" is the `total_cost_usd` Claude Code reports: what the run would
have cost on the API at list price, in US dollars. On a subscription it is
not charged; it is a measure of how much of the plan's limit a run uses.

#### Task 1: open actions (marks out of 7)

| Run | Plain | Practice | Wall time, plain / practice | API equiv., plain / practice |
|---|---|---|---|---|
| 1 | 6 | 7 | 35.7 s / 39.1 s | $0.94 / $0.98 |
| 2 | 6 | 7 | 36.9 s / 50.2 s | $0.94 / $1.04 |
| 3 | 6 | 7 | 36.8 s / 47.1 s | $0.94 / $0.99 |

- **Plain, all three:** all four open actions, with the right person and
  date; the roofer question once, at 10 November. The lost mark: each lists
  the tool sharpener under the work day ("booked by Nell … nothing more to
  do"), which the key counts as a finished action. All three also added
  things the key does not ask for (the unpaid fee, the duplicate row in
  `members.csv`, soup with no one assigned, the vacant plot), and all three
  answered in the chat without writing a file, as the prompt did not ask for
  one.
- **Practice, all three:** the same four actions in `actions.md`, nothing
  finished in the table, and the doubtful cases (paying the invoice,
  finalising the checklist, soup) listed under it as unsure, as asked. Every
  run said "no other file was changed".

#### Task 2: the notice (marks out of 10: four facts, six house rules)

| Run | Plain (no instruction file) | Practice (`CLAUDE.md` with the house rules) | Words, plain / practice |
|---|---|---|---|
| 1 | 8 | 10 | 121 / 88 |
| 2 | 7 | 10 | 121 / 80 |
| 3 | 9 | 10 | 98 / 99 |

Words counted with the Markdown symbols removed, heading and signature
included.

- **Facts:** all four (date, 09:30 to 12:30, gloves, soup) in all six runs.
- **Plain, rules missed:** date without the year in runs 1 and 2 ("Saturday,
  14 November"); over 120 words in runs 1 and 2; signed with the garden's
  name instead of "The committee" in runs 2 and 3. 24-hour times, British
  spelling and no exclamation marks held in all three without being asked.
- **Practice:** every rule in all three. Each reply said it had followed the
  house rules.

#### Task 3: tidy the notes

| Run | Plain: `check_t3.py` | Plain: said how it checked | Practice: `check_t3.py` | Practice: said how it checked |
|---|---|---|---|---|
| 1 | passed (exit 0) | no | passed (exit 0) | yes: SHA-256 before and after |
| 2 | passed | no | passed | yes: SHA-256 before and after |
| 3 | passed | no | passed | yes: SHA-256 before and after |

Wall time, plain: 31.2, 31.4, 39.5 s. Practice, two turns: 57.9, 78.1,
64.1 s.

- **Plain:** renamed to `YYYY-MM-DD-minutes.md`, took the dates from the
  first line of each note, wrote an index. Each said the text was
  "unchanged" or "untouched" without saying how it knew.
- **Practice, turn 1 (plan only):** all three changed nothing, gave the
  rename table, said dates came from each note's heading and cross-checked
  them against the "Next meeting" line of the note before. Turn 2: renamed,
  hashed each file before and after, and gave the hashes in a table.

#### Task 4: fees (marks out of 7)

| Run | Plain | Practice |
|---|---|---|
| 1 | 5 | 7 |
| 2 | 5 | 7 |
| 3 | 5 | 7 |

Wall time, plain: 32.5, 21.7, 27.0 s. Practice: 35.9, 41.7, 48.9 s.

- **The total was right in all six: $855.00.** Every plain run found and
  named the duplicate, the blank and the refund without being asked.
- **Plain lost two marks in each run:** none gave 22 as the number of
  members (they gave 20 or 21, as paying or current members, or none), and
  none said how the total was checked. Both are things the careful prompt
  asks for in so many words.
- **Practice:** 22 members (with 20 paying and 21 current, explained), and
  two or three independent checks of the total in each run.

#### Task 5: water in 2025

| Run | Plain | Practice |
|---|---|---|
| 1 | right | right |
| 2 | right | right |
| 3 | right (but tried a connector outside the folder) | right |

Wall time, plain: 15.9, 22.6, 30.9 s. Practice: 17.6, 16.7, 23.4 s.

- No run gave a figure for 2025. All six said it is not in the files and
  gave the 2026 figures ($312.40 by 8 September, $486.75 for the year).
- Plain run 1 added "the most the notes support is that 2025 was running
  somewhat higher than $312.40 by early September": an inference from "a
  little under last year's pace", not a 2025 amount. Marked right, noted.

#### All thirty, in one table

| Task | Plain, runs 1 / 2 / 3 | Practice, runs 1 / 2 / 3 | Did the practice change the result? |
|---|---|---|---|
| 1 Open actions (of 7) | 6 / 6 / 6 | 7 / 7 / 7 | Barely: one mark, for listing a finished item |
| 2 Notice (of 10) | 8 / 7 / 9 | 10 / 10 / 10 | Yes: the rules only held with the instruction file |
| 3 Tidy (check_t3) | pass / pass / pass | pass / pass / pass | No for the result; yes for saying how it checked |
| 4 Fees (of 7) | 5 / 5 / 5 | 7 / 7 / 7 | The total was right either way; the extra marks are for things the careful prompt asks for |
| 5 Water 2025 | right / right / right | right / right / right | No for the answer; yes for staying inside the folder |

Total API-equivalent use for the thirty completed runs, from the run JSON:
about $32 (each turn between $0.83 and $1.31). Most of each run's input was
the same cached context (the app's own instructions and set-up), which is why a two-line question cost much the
same as the longest task.

### Leads tested

Four of the leads in [`leads.md`](leads.md), each three times, same
command and set-up as above.

#### Lead 1: capitals and "IMPORTANT" in the instruction file

Task 2 with the same six house rules rewritten in capitals with "IMPORTANT",
"CRITICAL", "YOU MUST" and "NEVER, EVER" (copied below), against the plain-worded `CLAUDE.md` of
task 2 practice.

| Run | Plain-worded rules | Rules in capitals | Words, plain-worded / capitals |
|---|---|---|---|
| 1 | 10 | 10 | 88 / 71 |
| 2 | 10 | 10 | 80 / 77 |
| 3 | 10 | 10 | 99 / 91 |

**Failed** as a tip: the capitals added nothing, because the plain wording
already scored full marks in three runs out of three. The notices were
shorter with the capitals in all three pairs, which fits the vendor's own
warning that emphasis "mostly makes Claude over-apply the rule"; three
pairs is too few to say more.

The rules in capitals, as used:

    # HOUSE RULES FOR ANYTHING WRITTEN TO MEMBERS
    IMPORTANT: YOU MUST FOLLOW EVERY ONE OF THESE RULES. NO EXCEPTIONS!!!
    - CRITICAL: ALWAYS write dates IN FULL, WITH THE WEEKDAY: Saturday 14 November 2026.
    - CRITICAL: ALWAYS use the 24-HOUR CLOCK: 09:30, NEVER 9:30 am.
    - YOU MUST use BRITISH SPELLING.
    - NEVER, EVER use exclamation marks.
    - IMPORTANT: UNDER 120 WORDS. THIS IS A HARD LIMIT.
    - YOU MUST sign it "The committee", with NO PERSONAL NAMES. NEVER FORGET THIS.

#### Lead 2: "Claude Code ignores AGENTS.md; you need a CLAUDE.md"

Task 2 with the house rules saved as `AGENTS.md` instead of `CLAUDE.md`, and
no `CLAUDE.md` in the folder.

| Run | Marks (of 10) | Words |
|---|---|---|
| 1 | 10 | 104 |
| 2 | 10 | 105 |
| 3 | 10 | 83 |

**Failed** as a tip: in three runs out of three Claude Code read `AGENTS.md`
and followed every rule, and each reply named the file ("it follows the
house rules in `AGENTS.md`"). The memory page says Claude Code has read
`AGENTS.md` on its own since v2.1.277, when there is no `CLAUDE.md`. The
lead was true of older versions.

**The model changed before leads 3 and 4.** Between the lead 2 runs (13:25
UTC) and the lead 3 runs (about 14:10 UTC), the model and effort selected on the owner's account changed (not by this work). So leads 3 and 4 ran on `claude-sonnet-5-5` at the owner's effort setting, not the default, as every run's `modelUsage` shows, not
on Fable 5.2. Lead 3 compares runs within itself, so it still
stands. Lead 4 has no plain run on the same model to compare with; see
below. No more runs were made, to stay within the four-lead cap and the
shared usage limit.

#### Lead 3: correct it once, and ask it to update CLAUDE.md

From a widely shared list of tips from Claude Code's creator: "After every
correction, tell Claude: 'Update your CLAUDE.md so you don't make that
mistake again.'" Three runs, each in a fresh folder with **no** instruction
file:

1. The task 2 prompt.
2. In the same session (`--resume`), the correction: the six house rules in
   one paragraph, then "Fix notice.md, then update your CLAUDE.md so you
   don't make that mistake again."
3. `notice.md` moved out of the folder, and the task 2 prompt again in a
   **new** session, which sees only what step 2 wrote down.

| Run | 1. First notice | 2. After the correction | 3. New session | Words, 1 / 2 / 3 |
|---|---|---|---|---|
| 1 | 8 | 10 | 10 | 114 / 80 / 81 |
| 2 | 7 | 10 | 10 | 127 / 81 / 92 |
| 3 | 7 | 10 | 10 | 130 / 94 / 92 |

(Marks of 10 as for task 2; words with the Markdown removed, as before.)

- **First notices** missed the year in the date (all three), went over 120
  words (runs 2 and 3), signed as the garden's committee rather than "The
  committee" (all three), and named a person, "Wren will shut off the
  water" (all three).
- **Step 2** wrote a `CLAUDE.md` in all three runs, with the six rules in
  its own words plus one it added unasked: "Check the finished text against
  this list before saving it" (run 1), and in runs 2 and 3 "Do not name
  individual committee members anywhere in the text, even to say who is
  doing a task", which is the mistake it had just made.
- **Step 3**, the new session, followed every rule in three runs out of
  three, and each reply said it had checked against the house rules.

**Passed**, on Sonnet 5.5 at high effort: in three runs out of three, one
correction turned into a file that fixed the next session.

#### Lead 4: "ultrathink" on the fees question

The plain task 4 prompt with the word `ultrathink` on its own line at the
end. The vendor's best-practice page says "`ultrathink` still works: it
asks for deeper reasoning on that single turn".

| Run | Marks (of 7) | Wall time | Thinking tokens |
|---|---|---|---|
| 1 | 5 | 26.8 s | 928 |
| 2 | 5 | 15.4 s | 640 |
| 3 | 5 | 18.0 s | 792 |

All three gave $855.00 and named the duplicate, the blank and the refund;
none gave 22 members or said how the total was checked. That is the same
5 of 7 as the plain prompt on Fable 5.2, but on another model (Sonnet 5.5,
high effort) and with no plain Sonnet run beside it.

**Failed to show a difference**, and inconclusive: the extra thinking did
not buy the two marks the careful prompt earned by asking for them in
words. Asking for the check (task 4 practice) worked; asking it to think
harder did not, in three runs out of three, on a different model.

### Leads not tested

Two more were prepared and not run: a role line ("You are a meticulous
senior accountant…") on task 4, and "ask me clarifying questions until you
are 95% confident" on task 1. The second cannot be tested in `claude -p`
(there is no one to answer), and both would have gone past the cap of four.
