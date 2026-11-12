# Test log: the five common tasks, and four leads

Run on 11 November 2026, 21:20 to 21:45 UTC, on
the test machine, after the owner signed Grok Build in. Tasks from
[`../../2026-11-10-assistant-guides/tasks/`](../../2026-11-10-assistant-guides/tasks/)
(version 2), marked against its `answer-key.md`, `check_t3.py` and
`count_words.py`. Each run's outputs are in
[`../example/results/<task>-<variant>-r<n>/`](../example/results/):
`folder/` is the test folder as the run left it, `turnN-prompt.txt` the
prompt, `turnN.json` Grok's JSON output (reply, session, usage, cost),
`turnN.time` the wall time, `turnN.err` anything on stderr. Temporary paths
are shortened to `<tmp>`.

An earlier version of this file said no run had been made: the app was not
signed in at 20:20 UTC. The owner signed in at 21:17 UTC.

## How every run was made

| | |
|---|---|
| App | Grok Build 1.0.70 (`grok --version`: `grok 1.0.70 (f50904eaee6c)`) |
| Model asked for | `-m grok-4.7`, the default `grok models` reported once signed in ("* grok-4.7 (default)"; also offered: grok-4.7-build-fast, grok-4.6, grok-4.5) |
| Model reported | `grok-4.7-build` in every run's `modelUsage` |
| Effort | not set |
| Account | the owner's grok.com account, signed in by the owner |
| Folder | a fresh copy from `make_folder.py` for every run, in a temporary folder outside any git repository |
| Parallel | three runs at a time |
| Task 3, second turn | the same command with `-r <sessionId of turn 1>`; the JSON confirms the same session in all three runs |
| Task 2 practice | `house-rules.md` saved as `AGENTS.md` in the test folder |

The command, from inside the test folder (the script is `run.sh`, kept
outside the repository; this is all it does):

```sh
GROK_FOLDER_TRUST=0 \
GROK_CLAUDE_MCPS_ENABLED=false GROK_CURSOR_MCPS_ENABLED=false \
GROK_CLAUDE_AGENTS_ENABLED=false GROK_CLAUDE_SKILLS_ENABLED=false \
GROK_CLAUDE_HOOKS_ENABLED=false GROK_CLAUDE_RULES_ENABLED=false \
GROK_CURSOR_AGENTS_ENABLED=false GROK_CURSOR_SKILLS_ENABLED=false \
GROK_CURSOR_HOOKS_ENABLED=false GROK_CURSOR_RULES_ENABLED=false \
grok -p "<prompt>" -m grok-4.7 \
  --permission-mode bypassPermissions --sandbox workspace \
  --deny MCPTool \
  --disallowed-tools search_tool,use_tool,CallMcpTool,FetchMcpResource,ListMcpResources \
  --disable-web-search --output-format json
```

### Why each part is there

- **The `GROK_CLAUDE_*` and `GROK_CURSOR_*` variables** switch off, for this
  command only, Grok Build's default reading of Claude Code's and Cursor's
  set-up: instruction files, skills, hooks, rules and MCP servers
  (`26-config-reference.md`, `compat.*`). Without them, every run would have
  had the tester's Claude Code set-up: its global instruction file, its
  skills and its MCP servers. `grok inspect` with them set shows each of
  those `[disabled]` (`../example/results/preflight/`). Claude Code's
  permission rules from `~/.claude/settings.json` still load; there is no
  variable for them.
- **`GROK_FOLDER_TRUST=0`.** Without it, a project `AGENTS.md` is not loaded
  in a fresh folder: `grok inspect` listed no project file and "Project
  trusted: no", and a headless run asked to quote its project rules
  answered "None." With `--trust` it quoted the house rules, but `--trust`
  also writes the folder into `~/.grok/trusted_folders.toml`, which happened
  once, for the check folder, before this was noticed. `GROK_FOLDER_TRUST=0`
  (documented in `10-hooks.md`) turns the trust gate off for the one command
  and writes nothing; the trust file was unchanged after all the runs. It
  was set for every run, plain and practice, so they differ only in the
  file.
- **MCP.** Two tools checks were run before the first task, in a scratch
  folder, with the flags above but only the two `*_MCPS_ENABLED` variables
  set. The first (with `--disallowed-tools CallMcpTool,GetMcpTools,…`) listed 29 tools,
  including `search_tool` and `use_tool`, and said MCP tools "are reached
  only through `search_tool` and `use_tool`". `GetMcpTools` "names no tool"
  (stderr warning). Removing `search_tool` and `use_tool` as well, the
  second check listed 27 tools and said: "No MCP tools are available to
  call." Both checks also said the one remaining configured server, which
  comes with a plugin, "failed to connect because authentication is
  required"; it exposed no tools. Both answers are in
  `../example/results/toolcheck-1.txt` and `toolcheck-2.txt`.
- **The tools left** (second check): four X search tools (`x_user_search`,
  `x_semantic_search`, `x_keyword_search`, `x_thread_fetch`), shell, read,
  edit, write, list, grep, to-do, subagents and their controls, a
  scheduler, `monitor`, `workflow`, plan mode on and off,
  `ask_user_question`, `send_feedback`, and four image and video tools.
  None is a connector. The X search tools are Grok's own and survive
  `--disable-web-search`; no run used them for these tasks as far as the
  replies show.
- **`bypassPermissions` with `--sandbox workspace`**: a headless run cannot
  answer a prompt, and task 3 needs shell renames; the sandbox limits writes
  to the folder. One run (task 3 practice, run 1) said it copied the notes
  to `/tmp` for its check and deleted the copies afterwards, so the sandbox
  allows the system temporary folder.

**Cost.** The JSON gives `total_cost_usd` for each turn. The thirty runs of
the common tasks came to **US$4.12**, the twelve lead runs to US$2.07: about
US$0.07 to US$0.33 a turn. On a subscription this is drawn from the weekly
pool rather than charged; how far it moved the bar is for the owner to look
at (README, *For the owner*).

**Oddities.** `~/.grok/memtrace/` filled with small process-memory logs, one
of which names version 1.0.69, not 1.0.70. Every reply opened with a
sentence of what it was about to do ("I'll look through the workspace…")
run straight into the answer without a line break.

## Results

Wall time from the start of `grok -p` to its end. Cost is `total_cost_usd`
(US$), as Grok reports it.

### Task 1: open actions (marks out of 9)

| Run | Plain | Practice | Wall time, plain / practice | Cost, plain / practice |
|---|---|---|---|---|
| 1 | 9 | 9 | 72.0 s / 219.0 s | 0.088 / 0.191 |
| 2 | 9 | 9 | 56.0 s / 200.7 s | 0.081 / 0.189 |
| 3 | 9 | 9 | 56.4 s / 148.2 s | 0.085 / 0.141 |

- **Plain, all three:** all five open actions with the right person and
  date; the roofer question once, at 10 November; the tap with Dov; no
  finished action listed as open (the tool sharpener appears as "already
  booked"). All three answered in the chat, wrote no file, and added the
  unpaid fee in `members.csv`. Run 3 counted the work day itself as a sixth
  "item"; it is an event, not a finished action, so no mark lost.
  Replies 215 to 266 words.
- **Recorded separately (key v2.1): anything presented as agreed that the
  notes do not record.** All three plain runs added Leontyne Quist's unpaid
  fee, under a heading of its own, beside the five actions; plain run 3
  also counted the work day itself as a sixth open item. Neither was given
  an owner the notes do not name. No practice run added either; their
  doubts went under the table.
- **Practice, all three:** the same five in `actions.md`, one table, and a
  list of doubts under it (whether holding the roof payment is its own
  action, whether Tessa owes comments on her own draft, who brings the
  soup, the second tap passed from Nell to Dov). Run 2 also listed what it
  had treated as done. Run 1 calls Wren "he"; the notes give no pronoun.
  The practice runs took about three times as long.

### Task 2: the notice (marks out of 10: four facts, six house rules)

| Run | Plain (no instruction file) | Practice (`AGENTS.md`) | Words (`count_words.py`), plain / practice |
|---|---|---|---|
| 1 | 10 | 10 | 63 / 46 |
| 2 | 10 | 10 | 74 / 50 |
| 3 | 10 | 10 | 83 / 48 |

- **Every notice had all four facts and kept all six rules,** with or
  without the file: the full date with weekday and year, 09:30 to 12:30,
  British spelling, no exclamation marks, well under 120 words, signed
  "The committee" with no names.
- With the file the notices were shorter (46 to 50 words against 63 to 83)
  and plainer: each was headed "# Work day". The plain ones added a date
  line, "Dear members," or "We hope to see you there."
- Practice run 2's reply said the notice "stays within the house rules",
  which shows it read the file.

### Task 3: tidy the notes

Re-marked on 11 November 2026 under version 2.1 of the answer key, which
marks the plain prompt with `check_t3.py --plain`; both results are kept.

| Run | Plain: `check_t3.py --plain` (v2.1) | Plain: strict `check_t3.py` (v2) | Plain: said how it checked | Practice: `check_t3.py` | Practice: said how it checked |
|---|---|---|---|---|---|
| 1 | passed (exit 0) | failed: names only | no | passed (exit 0) | yes: copies compared with `cmp`, then SHA-256 and byte counts |
| 2 | passed (exit 0) | failed: names only | no | passed | yes: SHA-256 and byte counts before and after |
| 3 | passed (exit 0) | failed: names only | no | passed | yes: SHA-256 and byte counts before and after |

Wall time, plain: 48.2, 53.0, 53.6 s. Practice, turn 1 + turn 2: 100.3 +
62.7, 114.8 + 52.4, 89.7 + 36.2 s.

- **Plain:** in all three, the seven notes renamed `YYYY-MM-DD.md` with the
  right date, including `2026-08-26.md` for `minutes 25 aug.md`; text
  unchanged; every note in `notes/index.md`. `check_t3.py` fails them only
  because it requires `YYYY-MM-DD-<words>.md`, a pattern the plain prompt
  does not ask for. Each said the text was "unchanged" without saying how
  it knew.
- **Practice, turn 1:** each gave a rename table, said the dates came from
  each note's heading, named the 26 August meeting, and laid out a
  before-and-after check with SHA-256 hashes, then stopped. (That nothing
  changed in turn 1 rests on the replies; the folder was not copied
  between turns.)
- **Practice, turn 2:** renamed to `YYYY-MM-DD-committee-meeting.md`, wrote
  the index, and reported the check: hashes and byte counts (548, 421, 914,
  795, 591, 732 and 814 bytes) matched in every run.
- **Noticed 25/26 August:** yes, in all six runs.

### Task 4: fees (marks out of 5)

| Run | Plain | Practice |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |

Wall time, plain: 57.9, 84.2, 59.7 s. Practice: 113.9, 160.2, 106.8 s.

- **$855.00 in all six,** each naming the duplicate (Bram Lindqvist), the
  blank (Leontyne Quist, unpaid) and the refund (Sabela Pascoe).
- Recorded separately: the plain runs gave no member count and no check
  (run 3 added "Gross payments before that refund were $900.00", which is
  right once Bram is counted once). The practice runs gave 22 members,
  explained, and two or three independent checks each (for example
  "18 full fees × 45.00 = 810.00, plus 2 × 22.50 = 45.00"; run 2 used
  Python's `csv` and `Decimal`). All three also named Idris Rasku's `45`.

### Task 5: water in 2025

| Run | Plain | Practice |
|---|---|---|
| 1 | right | right |
| 2 | right | right |
| 3 | right | right |

Wall time, plain: 21.6, 20.1, 21.4 s. Practice: 16.4, 19.2, 18.7 s.

- All six said the 2025 water bill is not in the files and gave the 2026
  figures ($312.40 by 8 September, $486.75 for the year). None offered a
  figure for 2025. Plain runs 1 and 3 and practice runs 1 and 3 named the
  $96.20 electricity bill as the only 2025 utility figure, and said it was
  not water.
- The practice runs listed the other water notes as asked (the second tap,
  the shut-off).

## Leads, three runs each

| Lead | How tested | Result | Status |
|---|---|---|---|
| 2: Grok reads `CLAUDE.md` too | task 2 with the house rules saved as `CLAUDE.md` only | 10, 10, 10; 59, 51 and 62 words; `grok inspect` in the folder lists it as a project file | **passed** (but see below) |
| 3: start multi-file work in plan mode | task 3 *plain* prompt with `--permission-mode plan` for turn 1, then "Go ahead with that plan. When you finish, tell me what you checked." in the same session | `check_t3.py --plain` (v2.1) passed in all three; the strict v2 check failed all three. Runs 1 and 3 made `notes/README.md` the index, and run 2 also edited the folder's `README.md`; each had said so in the plan it was told to go ahead with. Text unchanged in all three; runs 2 and 3 checked with SHA-1, run 1 by listing files and links only | **passed, with a caveat** (re-marked 11 November 2026): said how it checked in 2 of 3, against 0 of 3 for the plain prompt without plan mode; it does what its plan says, so read the plan |
| 4: rein in Grok's length with a line in `AGENTS.md` | task 1 *plain* with `AGENTS.md`: "Keep every reply to ten lines or fewer." | 8, 9 and 9 non-empty lines; 123, 152 and 137 words against 215 to 266 plain. Marks 8, 8, 8 against 9, 9, 9: runs 1 and 3 dropped who owes the checklist comments; run 2 listed Sabela Pascoe's refund, already made, as an open action | **passed** for length; it cost a mark each time |
| 6: keep files out with `.grokignore` | task 4 *plain* with `.grokignore` containing `members.csv` | read `members.csv` and gave $855.00 in all three | **failed**: the file was ignored |

Lead 2 is a pass on a task where the plain prompt also scored 10, so it
shows the file was read and shortened the notice, not that it improved the
marks.

Wall time, CLAUDE.md: 54.2, 62.1, 52.4 s. Plan mode, two turns: 42.4 +
66.0, 59.0 + 80.5, 50.0 + 88.2 s. Ten-line rule: 42.0, 41.6, 36.2 s.
`.grokignore`: 105.7, 66.1, 105.7 s.
