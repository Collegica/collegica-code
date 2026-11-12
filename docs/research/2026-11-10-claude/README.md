# Claude: a guide to the assistant — research

Notes, tests and sources for the Claude guide, the first of four
assistant guides: <https://topics.pages.dev/ai/claude/> once published.
Started 2026-11-10.
Template, tasks and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md).

## Access and confidence

- **Version 2 (11 November 2026, local time; 02:00 to 02:07 UTC on 12
  November) is what the guide now rests on.** The
  thirty common-task runs and the one lead that had passed were run again on
  version 2 of the tasks, with Claude Opus 5.5 pinned (`--model
  claude-opus-5-5`) and no connectors (`--strict-mcp-config --no-chrome`).
  Every turn reported `claude-opus-5-5`; every turn's own `init` event
  listed no MCP servers and no `mcp__` tools. No usage limit was hit. Each
  run was copied into [`example/results-v2/`](example/results-v2/) as it
  finished and committed after every batch of three. Log:
  [`notes/test.md`](notes/test.md), *Version 2*. The points below about
  version 1 still describe the earlier round, which is kept as earlier
  evidence.
- **Vendor pages were read as their own text,** not through a summarising
  tool: Claude Code's documentation in its Markdown form, the support and
  privacy pages as downloaded HTML stripped to text. The pricing page was
  also read once through a summarising fetch; the two agree. Each note
  gives the page, the date read and what part of it was read. The Consumer
  Terms and Privacy Policy themselves were not read.
- **Version 1 (11 November 2026), kept as earlier evidence:** thirty runs
  of the first version of the tasks on Claude Code 2.1.322 with Claude Fable
  5.2, the model the owner's account had selected. Four leads were tested
  three times each: two on Fable 5.2, and two on Sonnet 5.5 after the
  account's model changed (one of them three turns long). The log is
  [`notes/test.md`](notes/test.md), *Version 1*.
- **Two interruptions.** The shared usage limit stopped the first batch
  after three runs; the other 27 returned the limit message without working
  and were run again in full the next morning. Later, the temporary folder
  holding the test folders was emptied before its contents were copied; the
  outputs were rebuilt from Claude Code's own session transcripts with
  [`example/recover.py`](example/recover.py). The marks were made on the
  live folders first. Details in `notes/test.md`.
- **Version 1's model changed under the tests.** The account's model was
  switched from Fable to Sonnet between lead 2 and lead 3 (not by this
  work). Version 1's leads 3 and 4 ran on Sonnet 5.5; everything else in
  version 1 on Fable 5.2.
- **Effort was the owner's, not the default, in every run.** No run passed
  `--effort`, so the owner's own effort setting applied; Claude Code's
  default is `medium`. Version 2 is therefore Opus 5.5 at the owner's effort
  setting, which is close to, but not exactly, what a new subscriber gets.
- **Nothing in the chat or desktop apps was tested.** Projects, memory,
  plan limits and the training switch are from Anthropic's pages only. See
  *For the owner*.
- **Prices are in US dollars, not CAD.** The pricing page shows "$" and
  "US$" and no Canadian price.

## What is here

| File | What it is |
|---|---|
| [`notes/apps-and-plans.md`](notes/apps-and-plans.md) | Pricing, desktop app, Cowork, release notes, usage limits |
| [`notes/projects-and-memory.md`](notes/projects-and-memory.md) | Projects, memory, chat search, incognito |
| [`notes/claude-code.md`](notes/claude-code.md) | Claude Code, `CLAUDE.md` and `AGENTS.md`, best practices, models, permission modes, the prompting guide |
| [`notes/data.md`](notes/data.md) | Training, retention, what Claude Code sends and keeps |
| [`notes/leads.md`](notes/leads.md) | Thirteen repeated tips, with links, and what became of each |
| [`notes/test.md`](notes/test.md) | The run log and the marks |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/results/`](example/results/) | Each run's prompt, last reply and the files it wrote |
| [`example/results-v2/`](example/results-v2/) | Version 2: each run's prompts, replies, `run.json` (model, tools, MCP servers, time, cost) and the folder as it left it |
| [`example/recover.py`](example/recover.py) | Rebuilds those outputs from Claude Code's session transcripts |

## Decisions

1. **The command-line app stands in for the assistant.** The plan says so;
   the article says plainly that the tests ran in Claude Code and that the
   chat app was not tested.
2. **Report the model the tests ran on, and the one a beginner gets.**
   Version 2, which the article rests on, pinned Opus 5.5, the model Claude
   Code gives a new subscriber, but at the owner's effort setting, not the
   default; the article says so. Version 1 (Fable 5.2, then Sonnet 5.5) is
   mentioned only as earlier evidence.
3. **No "practice" without a mark that moved, or a vendor line.** On
   version 2, tasks 1, 3, 4 and 5 scored the same plain and careful, so the
   article reports them as habits that changed what Claude *told you*, not
   what it got right.
4. **Prices as the page shows them, in US dollars, labelled.** The template
   asks for CAD; there was no CAD figure to give.
5. **The common tasks are reported as one table** of marks per run, plain
   against practice, so the other three guides can use the same table.
6. **Leads 3 and 4 kept, with their model named.** Lead 3 compares within
   itself and stands. Lead 4 is reported as inconclusive.

## For the owner

Things that live only in the chat or desktop app, to check by hand before
`draft: true` comes off. Each says what to look for.

1. **The training switch.** Settings > Privacy (or
   claude.ai/settings/data-privacy-controls): what is the switch called, and
   was it on for your account before you touched it? The pricing page says
   "Opt-out", which implies on; no page says so in a sentence.
2. **What a Canadian card is charged for Pro.** The page shows $17 / $20
   with no currency on the consumer plans. Is it US$20 converted, or a CAD
   price, and is tax added?
3. **Memory.** Settings > Your Claude > Manage: is memory on, what topics
   are listed, and is "Include sensitive topics in memory" off? Start a chat
   with "+" > Memory off and confirm the crossed-out icon appears.
4. **Project memory.** Open a project: is there a "Use account memory"
   switch under Memory, as the support page says?
5. **Projects on your plan.** Does the sidebar show the new Projects (beta)
   in the Code tab, or only the old projects in chat? Free accounts: is the
   limit five?
6. **Instruction file in the desktop app.** In the Code tab and in Cowork
   with a folder connected: does a `CLAUDE.md` or `AGENTS.md` in the folder
   change what it writes? (Repeat task 2 there, once with the file and once
   without.)
7. **Usage.** Settings > Usage: the five-hour and weekly bars, and the
   separate Fable bar. How far did these tests move them? (The thirty runs
   came to about US$32 at API list price in version 1 and about US$7 in
   version 2, which is not what the plan charges.)
8. **Incognito in the new experience.** Does the ghost icon still open an
   incognito chat that cannot create files, as the support page says?
9. **Free plan and Cowork.** The pricing page lists "create files, and run
   code" for Free; the Cowork page says Cowork is paid only. What does a
   Free account see when asked to make a spreadsheet?
10. **Connectors reaching outside the folder.** In version 1, task 5
    (plain), Claude tried a connected service from the owner's account to
    find a figure that was not in the folder. Check which connectors are on in Settings > Connectors, and
    whether that matters for private folders.

## What the template and tasks got wrong

Found while drafting the first guide; for the lead to fix on the issue
branch before the other three start. Nothing under
`../2026-11-10-assistant-guides/` was edited.

1. **The tasks barely separate plain from careful prompts on a strong
   model.** Tasks 3 and 5 scored the same in all six runs; task 1 by one
   mark. *Change:* make each task harder in the way its practice is meant
   to help. Task 1: more notes (ten or twelve), an action carried over
   twice with a changed owner, and one closed only implicitly. Task 3: a
   note whose file name and heading disagree on the date, so "plan first"
   has something to catch. Task 5: a question whose answer is *nearly*
   there (a 2025 figure in a members' email quoted inside a note, for a
   different service), so the plain prompt is tempted.
2. **Task 4's marks reward asking, not the practice.** Two of seven marks
   (the member count and "says how it checked") are only asked for in the
   careful prompt. The plain prompt got the total right in three runs out
   of three. *Change:* mark the plain and careful prompts on the same thing
   (the total, and each problem found), and record "said how it checked"
   separately as in task 3.
3. **"22 members" is ambiguous.** Twenty-two people are on the list; 21 are
   members now (one was refunded and left); 20 have paid. Each careful run
   gave all three. *Change:* the key should say which number is wanted, or
   accept any number that is explained.
4. **"No finished action listed" catches context.** The plain runs list the
   tool sharpener as "booked … nothing more to do", which is a done action
   shown as done. *Change:* say whether a done item marked as done costs the
   mark.
5. **Task 2's word count is not defined.** 121 words with Markdown symbols
   stripped, 126 with them; the heading and signature are in or out. Two
   plain runs fall either side of 120 depending on this. *Change:* say "with
   the heading and signature, Markdown symbols not counted", or give a
   counting script, as task 3 has `check_t3.py`.
6. **The date rule's year.** The house rule's example has the year; the rule
   does not say "with the year". Two plain notices wrote "Saturday, 14
   November". *Change:* say "with the weekday and the year".
7. **Today's date leaks in.** Runs on 10 and 11 November treated the 7 and
   10 November actions as overdue or "due today". A run in December will
   read the same notes differently. *Change:* add to the key that the date
   of the run is to be logged, and that "overdue" remarks are neither right
   nor wrong.
8. **"As the owner has it configured" is not stable.** The owner's model
   setting changed in the middle of the tests (Fable to Sonnet), and the
   owner's connectors were reachable from the test folder. *Change:* the
   README should say: log the model of every run from the app's own output;
   if it changes, say so and do not compare across it; and pass the model
   explicitly (`--model`) when the owner agrees, so a guide reports one
   model.
9. **Nothing tells the agent the tests use the owner's usage limit.**
   Thirty runs plus leads cost about a day's plan limit and stopped the
   tests twice. *Change:* say so in the README, give the cost seen here
   (about US$1 a run at API list price on Fable 5.2, a quarter of that on
   Sonnet 5.5), and tell agents to run three at a time and copy outputs into
   the research folder after each batch.
10. **Temporary folders are not safe.** The test folders were lost before
    copying. *Change:* "copy each run's folder into `example/results/` as
    soon as it finishes", not at the end.
11. **The template's "what it costs in CAD".** Anthropic shows US dollars.
    *Change:* "in CAD where the vendor gives them, otherwise in the vendor's
    currency, labelled".
12. **The template has no place for "what the tests do not show".** The
    model article had one ("What it does not show"); a guide that reports
    small tests needs it. *Change:* add it as the last part of "Practices
    that held up", or its own short section.
13. **Plain-prompt runs that write no file.** Task 1 plain asks a question
    and gets an answer in the chat; task 1 practice asks for `actions.md`.
    The difference in output form is part of the practice, but the key does
    not say how to mark a reply with no file. *Change:* say "mark the reply
    or the file, whichever there is".

### Found on version 2 (11 November 2026, Opus 5.5)

14. **Tasks 1, 4 and 5 still do not separate on Opus 5.5.** Plain and
    careful scored the same in all six runs of each; only task 2 moved the
    marks (7, 8, 7 against 10, 10, 10). The ChatGPT guide found the same. The
    practices show in what the reply contains (a file, a stated check, a
    second check of the total), which the key records separately and does
    not mark. *Change:* either accept that this is the finding and say so in
    the shared README, or add marks for the evidence itself ("says how no
    text was lost", "checks the total a second way") to both prompts'
    keys.
15. **`check_t3.py` fails correct plain work.** All three plain runs named
    the notes `2026-08-11.md` (no words after the date) and two named the
    index `INDEX.md`; text, dates and the 25/26 August trap were all right.
    Same flaw the ChatGPT guide reports (`README.md` as the index).
    *Change:* accept `YYYY-MM-DD.md` and any Markdown file in `notes/` that
    lists every note, case-insensitively, and report the names separately.
16. **Runs change files nobody mentioned, and one wrote outside the
    folder.** All three plain task 3 runs edited the top-level `README.md`;
    a practice run kept its checksums in a `check/` folder one level above
    the test folder. The key has no place to record either. *Change:* add
    "files changed or created outside what was asked" as a recorded item
    for every task, and diff the folder (and its parent) after each run.

## Checker's report

A fresh checker reviewed the guide and this folder after version 2 was
merged. Each finding and what was done, 11 November 2026:

| # | Finding | Change |
|---|---|---|
| 1 | Local place and time named in the test log, and the time zone in the 27 limit-hit stubs | Times given in UTC only; the stubs read "([time zone redacted])" |
| 2 | The owner's configuration described: what the global instruction file is about, values from the settings file, the kind of connector | Described only as "the owner's effort setting, not the default", "the model the owner's account had selected", "a connected service from the owner's account". Two version 1 replies redacted to "[a connected service]". The tools list in `tools-check/` and `run.json` was kept: it names only Claude Code's built-in tools, no plugins or skills, and it is the evidence that no MCP server loaded |
| 3 | Links to the private issue and to non-exported paths | Replaced with the published article address |
| 4 | Effort: runs used the owner's effort setting, not the default | Said under *What the tests do not show*, in the opening, here and in the test log |
| 5 | *What the tests do not show* was a sub-section | Its own section, after *What did not hold up*; adds that web search and fetch stayed available |
| 6 | Task 3: the strict checker also failed runs 2 and 3 on `INDEX.md`; `check_t3.py --plain` (v2.1) passes all three plain runs | Logged as "strict fail / `--plain` pass ×3"; the article says the plain runs pass the plain-prompt check |
| 7 | "Unchanged" is not the replies' word; one run "made no claim" | Quoted the replies' own words. Checked: all three plain replies did claim the text was untouched ("I didn't change what's written…", "I didn't change anything inside the minutes", "nothing inside the notes was edited"); none said how it knew. "Changed nothing" after turn 1 is now said to rest on the replies, with no snapshot between turns |
| 8 | `AGENTS.md` lead ran on Fable 5.2 only | Corrected |
| 9 | `ultrathink` lead was inconclusive | Said so, with the reason, and the best-practices quote |
| 10 | Incognito is not "the only kind" | "The one switch that does two things at once" |
| 11 | No page states the training default | Says the pricing page calls it "Opt-out" and the pages do not say in words whether it starts on |
| 12 | Quoted `CLAUDE.md` lines each come from one run; task 4 practice run 2 gave 21 paid; task 3 practice run 1 said "checksum", not SHA-256 | Attributed to runs; corrected in the article and the test log |
| 13 | Mixed date conventions | 11 November 2026 (local) for "Last checked", "Tested" and `date:`; pages "read on 10 and 11 November" |
| 14 | Prices without US$ | US$ on every figure; Ultra's "no 5-hour limit" marked "(verified accounts)" |
| 15 | Volatile facts outside *The moving parts* (default model, five projects, plan availability, "Since September", version numbers, plan names, retention periods) | Moved there, or referred to it |
| 16 | Cowork described as working on a local folder | Runs in the cloud with files in the Claude account; a local folder is optional on the desktop |
| 17 | "Knowing nothing about you" against memory on by default; "every time" for counts; "every run, in both rounds"; thumbs feedback "up to" 5 years; the desktop app reading `CLAUDE.md` untested | Reworded: "knowing only what you give it and what its memory has kept"; counts; "12 of 12 … and 6 of 6"; "up to 5 years"; only the Code tab follows from the docs |
| 18 | *In short* items 2 and 4 did not fit the template | Item 2: "do by hand: the final read for your house style", noting nothing called for another assistant; item 4: the habit that protects your files, from what the runs did |
| 19 | Decision 2 and *Access and confidence* still said Fable 5.2 | Updated for version 2 on Opus 5.5 |
| 20 | The "Mention that a deadline moved…" quote was not in the notes | Added to `notes/projects-and-memory.md` with its date |
| 21 | Task 1 v2.1 "record separately" item | Logged: plain run 2 listed closing the garden and arranging soup; runs 1 and 3 closing the garden |
