# Hermes Agent: a guide to the open agent runtime — research

Notes, tests and sources for the Hermes guide, tracked in
[issue #213](https://github.com/Collegica/collegica/issues/213). Started
2026-11-14. Draft: `website/ai/hermes/index.md` (`draft: true`, no hero).
Proposal and plan: [`../../proposals/2026-11-14-hermes-guide/`](../../proposals/2026-11-14-hermes-guide/README.md),
[`../../plans/2026-11-14-hermes-guide/`](../../plans/2026-11-14-hermes-guide/README.md).
Template, tasks and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md)
(version 2.1 of the tasks).

Hermes is not one assistant but a runtime: it works with whatever model you
point it at. The results are results for **Hermes with one model, ChatGPT
Terra (`gpt-5.6-terra`)**, and the research folder also holds the same tests on
a free model, which show how much the model matters.

## Access and confidence

- **Thirty runs of the common tasks were completed and marked on ChatGPT
  Terra,** three per prompt, on 14 November 2026 between 13:35 and 14:27
  Eastern time, in **Hermes Agent v0.23.1 (2026.9.24)**. Six extra runs of
  task 2 followed (three more with `AGENTS.md`, three with the rules as a
  skill). The log is [`notes/test.md`](notes/test.md); every run is in
  [`example/results/`](example/results/).
- **The model was named on every run** (`--provider openai-codex -m
  gpt-5.6-terra`) and the stream's first event reports it. The id comes from
  Hermes's own model list for that provider; see
  [`notes/2026-11-14-installed-hermes.md`](notes/2026-11-14-installed-hermes.md).
- **The same tests on a free model** (nvidia/nemotron-3-ultra-550b-a55b:free,
  through OpenRouter; thirty runs and six extra) were made first and are kept:
  [`notes/test-free-model.md`](notes/test-free-model.md),
  [`example/results-free-model/`](example/results-free-model/). Their marks
  were re-checked against the saved records after review (two marks changed).
- **One provider error:** `t1-plain-r2` failed once (stream stall, 573
  seconds), was kept as `t1-plain-r2-attempt1-provider-error` and run again;
  the retry is the marked run.
- **An empty data root, not the tester's.** `HERMES_HOME` pointed at a new
  folder, so the tester's memory, personality file, skills and settings did
  not load and nothing in the tester's Hermes folder was written. Only the
  provider sign-in was copied in, with its refresh token blanked, and the copy
  was deleted afterwards (never printed or saved in the repository).
  Hermes seeded the empty root with its defaults.
- **No connectors, MCP servers or gateways.** Only `-t file,terminal,todo`
  were loaded (no web, browser, memory, skills tools, delegation, cron,
  messaging). Hermes's look-up tools (`hermes_tool_search`, `tool_describe`,
  `tool_call`) were present, with nothing configured to find. The skill runs
  preloaded one skill. The agent's own tool list is in the log.
- **Permissions: `--yolo` was not used.** `hermes -z` auto-bypasses approvals
  by the installed `--help`, so the runs used `hermes chat --oneshot`, which
  keeps the approval system: default mode `smart`, and a one-shot session
  refuses what Hermes flags as dangerous (`approvals.single_query_mode:
  deny`). `HERMES_WRITE_SAFE_ROOT` confined Hermes's file-write tools to the
  folder that holds the test folders. **The terminal itself was not
  confined:** it ran as the tester's user and, as a probe showed, could write
  one folder up. This is weaker than the Antigravity runs' sandbox and is said
  in the guide.
- **Quota and cost:** ChatGPT Plus sign-in (`hermes usage`: "openai-codex
  (Plus)"). After the Terra runs the account showed the 5-hour window 15% used
  and the weekly window 26% used; it was not read before the first run, so
  the cost of the runs alone is not known. About 1.22 million input and 46,000
  output tokens over 39 turns. One run failed on a provider stall.
- **Vendor pages were read from the copy of the documentation installed with
  Hermes 0.23.1.** The online pages were not read or compared. The notes say
  which.
- **Not tested:** the desktop app, the web dashboard, the messaging gateway and
  every platform, MCP servers, Hermes's memory tool, `--yolo`, `hermes -z`,
  `--safe-mode`, `--ignore-user-config`, Docker, other approval modes, any
  other model or provider.

## What is here

| File | What it is |
|---|---|
| [`notes/2026-11-14-installed-hermes.md`](notes/2026-11-14-installed-hermes.md) | The installed Hermes: version, defaults, flags used, model names |
| [`notes/2026-11-14-hermes-docs.md`](notes/2026-11-14-hermes-docs.md) | Hermes's documentation on context files, memory, skills, permissions; OpenRouter's data page |
| [`notes/leads.md`](notes/leads.md) | Practices met but not reproduced |
| [`notes/test.md`](notes/test.md) | The Terra run log, marks, probes |
| [`notes/test-free-model.md`](notes/test-free-model.md) | The same tests on a free model |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/`](example/) | The runner scripts, `summarise.py`, and the records: `results/` (Terra), `results-free-model/` |

## Decisions

1. **Hermes tested on ChatGPT Terra** (`gpt-5.6-terra`, through the
   `openai-codex` provider), on the owner's instruction of 14 November 2026,
   replacing the free model first used; the free-model results are kept as a
   labelled comparison.
2. **`hermes chat --oneshot`, not `-z`,** so that approvals stayed on.
3. **Empty data root** so the tester's memory and skills did not shape the runs.
4. **Tools limited to files, terminal and todo,** which is what the other
   guides' runs used (read, write, shell) and keeps web search out of task 5.
5. **Three runs per prompt,** plus six extra runs of task 2 (three more with
   `AGENTS.md`, three with a skill). The extra runs are reported beside the
   thirty, not mixed into them.
6. **Task 3 plain marked with `check_t3.py --plain`** (tasks v2.1); the strict
   result is kept beside it.
7. **No prices in the article** beyond what the provider pages state and the
   free model's OpenRouter listing.

## For the owner

1. **Which ChatGPT plan did the Terra quota come from?** The tested sign-in
   reports Plus (`hermes usage`). Confirm that is the plan you meant, and that
   running the thirty-six runs from it was within what you want. The window
   figures are in the log.
2. **Your own memory and skills.** What your Hermes has written about you
   and the skills you have installed were not read, so anything in them that
   steers answers is invisible to this guide. Decide what, if anything, the
   guide should say about it.
3. **Provider privacy settings.** OpenRouter has separate "may train on my
   data" settings for free and paid models; OpenAI/ChatGPT has its own data
   controls. Check the ones for the provider you use. The guide says only
   that the settings exist.
4. **Terminal confinement.** The default terminal backend is `local`, so a
   session started from a normal config can run commands as you anywhere,
   apart from what it flags as dangerous. Do you want to try the Docker
   backend, and have the guide describe it from the tested side?
5. **Approvals.** The guide describes the approval modes from Hermes's
   documentation and says it did not test `manual` or `off`. Confirm you are
   happy to have it read that way.
6. **The desktop app and the gateway** are described from the documentation,
   labelled untested. If you want them tested, that is a separate brief and
   touches your accounts.
7. **Failed provider call.** One Terra run stalled and was repeated. If you
   see the same in daily use, Hermes's message suggests a fallback provider
   (`hermes fallback add`); not tested.

## What the template and tasks got wrong

Nothing under `../2026-11-10-assistant-guides/` was edited. In addition to the
earlier guides' lists:

1. **The README assumes a vendor's model.** Hermes has none; the "pin the
   model" step needs a line for runtimes (name the model and provider on every
   run, and log both).
2. **Task 2's practice needs the assistant to find the notes first.** On the
   free model, where the agent took an empty search for an empty folder, the
   notice was never written and the practice scored 0 for a reason unrelated to
   the practice. The marking should say what to do with such runs: report
   them, and consider re-running them, as was done here (beside the thirty,
   not instead).
3. **"Permission to write in that folder only"** cannot be met by file-write
   confinement alone where the shell is on. State what confines the shell.
4. **Per-process settings can persist.** Hermes keeps a background process
   that holds the environment it first saw (`HERMES_WRITE_SAFE_ROOT`); a changed
   variable did not take effect until that process was stopped. Worth a line
   in the README: check that per-run environment variables reach the process
   that does the work.
5. **Mark from the saved records, not from memory.** A first set of marks here
   was taken from a discarded attempt; re-marking from the saved records
   changed two marks and exposed two claims of checks that never ran.
6. **Record what each run actually ran.** A reply that says it "parsed the
   CSV with Python" or "checked byte-for-byte" can be checked against the tool
   calls; the key could add a line for it.
