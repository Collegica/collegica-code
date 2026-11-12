# ChatGPT: a guide to the assistant — research

Notes, tests and sources for the ChatGPT guide, one of the four assistant
guides, published at <https://topics.pages.dev/ai/chatgpt/>.
Started 2026-11-11. Draft: `website/ai/chatgpt/index.md` (`draft: true`).
Template, tasks (version 2) and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md).

## Access and confidence

- **OpenAI's documentation was read as its own text,** the Markdown twin of
  each learn.chatgpt.com page, downloaded with `curl` on 11 November 2026.
  Two pages rendered only by script (best practices, and the prices on
  chatgpt.com/pricing) were read through a summarising fetch or not at all;
  each note says which.
- **OpenAI's Help Centre and policy pages could not be read.** Every
  help.openai.com and openai.com/policies address returned HTTP 403 to every
  tool here. So the training switch, the Help Centre's model and limit
  tables per plan, and ChatGPT (web) memory rest on what the readable pages
  say, and on search-result excerpts that are recorded but **not used as
  sources** ([`notes/2026-11-11-data.md`](notes/2026-11-11-data.md)). See
  *For the owner*.
- **Thirty runs of the common tasks (version 2) were completed and marked,**
  plus four leads at three runs each: 51 Codex turns, all on 11 November
  2026 between 20:20 and 20:48 UTC, all with exit code 0, none stopped by a
  usage limit. Codex CLI 0.166.0; the model pinned with `-m gpt-6.1-sol`;
  `gpt-6.1-sol` and effort `low` reported in every session log (one lead set
  `high`, reported `high`). Low was the test account's existing setting; no
  page read says it is the default. Task 3 plain was re-marked with
  `check_t3.py --plain` (key version 2.1) after the checker's review.
- **The model was pinned from what the pages say, not one sentence.** No
  page read says "the default model for Codex on a paid plan is X". The
  models page says an unset model means "a recommended model"; its CLI
  examples, the config example and the GPT-5.5 retirement notice all name
  `gpt-6.1-sol` for Plus and above. That is the model used.
- **No MCP servers, connectors or plugins in any run,** shown by asking
  Codex for its tools and by the tool list in each session log. It took
  three tries: a plugin bundled with the desktop app kept its MCP server
  loaded until `--disable plugins`. Every flag and the evidence are in
  [`notes/test.md`](notes/test.md). The owner's existing configuration was
  read, never edited.
- **The app's local memories were switched off for the runs**
  (`--disable memories`), beyond the brief, so that runs could not see each
  other and no test was written into a memory store.
- **Nothing in Chat, Work or the desktop app was tested.**
- **Prices are in US dollars.** The Codex pricing page shows "$" and, on the
  Pro card, "USD"; no Canadian price is shown.
- **The outputs were copied as each batch finished,** with the temporary
  path shortened to `<tmp>/`, the user name to `<user>` and a bundled
  plugin's name to `[bundled-plugin]`. Codex's own session logs were not
  copied (they hold account ids); the model, effort, version and tool list
  were copied from them into each `run.json`, and whether each run loaded an
  instruction file into `example/results/instructions-loaded.txt`.

## What is here

| File | What it is |
|---|---|
| [`notes/2026-11-11-apps-plans-models.md`](notes/2026-11-11-apps-plans-models.md) | Apps, plans, prices, limits, models, versions; why `gpt-6.1-sol` |
| [`notes/2026-11-11-context.md`](notes/2026-11-11-context.md) | Projects, custom instructions, memory, `AGENTS.md`, best practices |
| [`notes/2026-11-11-codex.md`](notes/2026-11-11-codex.md) | `codex exec`, the switches for MCP and plugins, prompting advice, sandbox, slash commands |
| [`notes/2026-11-11-data.md`](notes/2026-11-11-data.md) | Training, retention, local transcripts; what could not be read |
| [`notes/leads.md`](notes/leads.md) | Fourteen repeated tips, with links, and what became of each |
| [`notes/test.md`](notes/test.md) | The run log, the MCP evidence and the marks |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/run.py`](example/run.py) | Runs one task in a fresh folder with every MCP server and plugin switched off |
| [`example/leads/`](example/leads/) | The capitals file and the correction used by two leads |
| [`example/results/`](example/results/) | Each run: the folder afterwards, the event stream, the last message, `run.json`; `tools-check*` are the three tool listings; `instructions-loaded.txt` records, per run, whether an instruction file was loaded |

## Decisions

1. **The command-line app stands in for the assistant,** as the plan says.
   The article says the tests ran in Codex CLI and that Chat, Work and the
   desktop app were not tested.
2. **`gpt-6.1-sol` at the effort the account was set to (low).** See
   *Access and confidence*. The article says a Free or Go account gets GPT-6 Luna, in the
   desktop app only.
3. **`--disable plugins`, not `--ignore-user-config`.** Both removed every
   MCP tool. The second also drops the rest of the owner's settings, which
   the shared README says should load.
4. **Memories and the desktop notification switched off** for the runs:
   isolation between runs, and no side effects on the test machine.
5. **"The Committee" with a capital C is marked as missing the signature
   rule,** because the rule quotes "The committee". It affects task 2 plain
   run 1 (8, or 9 the other way) and lead D run 1's first notice; the article
   uses the strict marks.
6. **Task 3 plain is marked with `check_t3.py --plain`** (key version 2.1):
   passed in all three. The strict version 2 result (failed in all three,
   because the index was named `notes/README.md`) is kept beside it in
   `notes/test.md`.
7. **Lead B (`CLAUDE.md`) is reported as "true, and no difference here"**
   rather than forced into passed or failed: the file was not loaded as
   instructions (as the vendor says), but was read anyway in a folder this
   small.
8. **The data section uses only what was readable:** the pricing page's
   "Content is used to train our models / Opt-out available", the
   authentication page, and the local-transcript setting. The switch's name
   and place come only from search snippets, so the article gives neither;
   they are left for the owner to confirm.

## For the owner

Things that live only in the chat or desktop app, or behind the Help Centre,
to check by hand before `draft: true` comes off. Each says what to look for.

1. **The training switch.** In ChatGPT (web or desktop) settings: is it
   under Data Controls, as search snippets say, and is it called *Improve the
   model for everyone* (its name in the October article)? Was it on before
   you touched it? Does it say it also covers Codex? If confirmed, the
   article's *Where your data goes* can name it. Open
   <https://help.openai.com/en/articles/7730893-data-controls-faq> in a
   browser and check the guide's *Where your data goes* against it.
2. **Temporary Chat.** Is it still there, and does it say it is neither
   remembered nor used for training?
3. **Memory.** Settings > Personalization: is ChatGPT memory on, what has it
   saved, and is "reference chat history" (or its current name) on? In the
   desktop app, is **Enable Codex memories** on, and is **Allow memories from
   tool-assisted chats** on?
4. **Custom instructions.** Settings > Personalization: where are custom
   instructions now, and does the desktop app show your global Codex
   `AGENTS.md` there, as the Personalize page says?
5. **Projects.** In the desktop app's Projects view: can you make a *local
   project* attached to a folder, and a ChatGPT project with uploaded files?
   On the web, do project instructions appear? Is Projects on your plan (the
   pricing page lists it for Plus)?
6. **The instruction file in the desktop app.** In Codex mode with the test
   folder open: does an `AGENTS.md` change what it writes? (Repeat task 2
   there, once with the file and once without.) And in Work mode with a
   folder: does Work read `AGENTS.md` at all? No page read says so.
7. **The default model.** In the desktop app's Codex mode, with nothing set,
   what model and effort does a new chat start on? (The tests pinned
   GPT-6.1 Sol and ran at low effort, the test account's setting, so a fresh
   account may show something else.) On a Free account, is it GPT-6 Luna?
8. **Usage.** <https://chatgpt.com/codex/settings/usage>: how far did 51
   turns move the five-hour and weekly bars?
9. **The price in CAD.** The pages show US$20 for Plus. Is there a CAD
   price at checkout, and is tax added?
10. **Plugins and connectors.** A plugin bundled with the desktop app kept
    its tools loaded in the tests even when switched off by name. Check in
    the desktop app's settings which plugins and connectors are on, and
    whether you want them on for private folders.

## What the template and tasks got wrong

Found while drafting this guide on version 2 of the tasks; for the lead to
fix on the issue branch. Nothing under `../2026-11-10-assistant-guides/`
was edited.

1. **Task 3's checker fails a reasonable plain answer.** The plain prompt
   says "and an index" and names no file; `check_t3.py` demands
   `notes/index.md`. All three plain runs named it `notes/README.md`, renamed
   every note correctly and kept the text, and failed. *Change:* either say
   "an index, notes/index.md" in the plain prompt, or have `check_t3.py`
   accept any new Markdown file in `notes/` that lists every note, and
   report the index's name separately.
2. **Task 1 still does not separate plain from careful on this model.** Both
   scored 9 of 9 in all six runs; the brief changed the form (a file, only the
   five, doubts listed), not the marks. The plain runs added things nobody
   agreed to do, and once gave a task an owner the notes do not name, at no
   cost. *Change:* take a mark off for an item listed as an open action that
   no note records as agreed, and for an owner or date the notes do not
   give.
3. **Task 4's plain prompt is still easy.** The total was right in six of
   six; the one lost mark was a plain answer that left out the blank fee.
   That may be enough, but say in the key whether "One member's fee remains
   unpaid", without the name, counts as naming the blank (it was counted
   here).
4. **The signature rule's capital letter.** "The Committee" against "The
   committee": the key does not say whether case matters. *Change:* say so.
5. **The README's "no connectors" rule needs an app-specific note for
   Codex.** Disabling each MCP server and each plugin by name was not
   enough: a bundled plugin's MCP server stayed loaded until
   `--disable plugins`. *Change:* for Codex, list the flags that worked
   (`--disable plugins --disable apps`, plus each MCP server
   `enabled=false`) and say to confirm with the tool list in the session log,
   not only the model's own answer.
6. **The README should say what to do about the app's memory.** Codex
   memories, if the owner has them on, carry one run into the next and write
   the tests into the owner's memory. *Change:* "switch off the app's memory
   for the runs, with its own flag, and say so".
7. **"The vendor's default model, read from its documentation" assumes the
   documentation names one.** OpenAI's does not, in one sentence. *Change:*
   allow "the model the vendor's pages give for the owner's plan, with the
   lines quoted".
8. **The template's "In short" item 4 ("the setting or habit that protects
   your files") invites an untested claim.** Nothing in the tasks tests
   protection. *Change:* tie it to a vendor page or to what the runs did
   (read-only by default; what it looked at outside the folder).
9. **Task 2 practice gives identical notices.** Two of three practice
   notices were word for word the same; with the house rules the task has
   one right answer. That is fine for marking but says nothing about
   variety. No change needed; worth knowing when comparing word counts.

## Checker's report

A fresh checker reviewed the draft after PR #190 was merged. Each finding,
and what was changed (branch `guide/chatgpt-fixes`):

1. **Task 3 plain marked with the strict check.** Re-marked the saved
   folders with `check_t3.py --plain` (key version 2.1): passed, passed,
   passed. `notes/test.md` keeps the strict result beside it. The article now
   shows plain and careful both passing, says four of five tasks scored the
   same or one mark apart (was three), and drops every claim built on the
   plain fail.
2. **"Default (low) reasoning effort".** Now said everywhere as the test
   account's existing setting; no vendor page read gives a default
   (`notes/test.md`, the models note, the article, this README).
3. **"Claude Code reads that too".** Now "when there is no `CLAUDE.md` in
   the folder", as the Claude guide reports from Anthropic's page.
4. **Match the raw outputs.** The self-added rule in lead D is quoted per
   run in `notes/test.md`, and the article says it was worded differently
   each time and quotes two. The article says task 2 plain's 8-mark run lost
   one mark on a capitalised "The Committee". "Every problem in a table" is
   now "two of the three in a table". Lead C now shows 5, 5, 5 against 5, 5,
   4, with the time difference "on average" (also in `notes/test.md`).
5. **Overreach.** The 32 KiB limit is now described as the combined size of
   all instruction files, and a default that can be changed. "Many reports"
   is now "an OpenAI community thread". "List the instruction sources you
   loaded" is kept as a quote but attributed to where it comes from: it is
   the example prompt on OpenAI's AGENTS.md page ("Layer project
   instructions", step 3), checked again in the saved copy of that page. The
   `CLAUDE.md`-not-loaded claim is now backed by
   `example/results/instructions-loaded.txt`, read from the session logs
   (which stay out of the repository because they hold account ids), and the
   article says "session records showed". Settings > Data Controls is gone
   from the article; it is item 1 of *For the owner*, marked as coming from
   search snippets.
6. **Codex version.** The "Last checked" line no longer names the version;
   *The moving parts* says the tests ran on 0.166.0 and that 0.167.2 came out
   on 11 November 2026 (GitHub release `rust-v0.167.2`, 22:44 UTC), after
   the tests.
7. **Personal details.** Removed the time zone, the make of the test machine, the card
   reference, and every description of the owner's own Codex set-up
   (which MCP servers, plugins or memory settings it has) from the notes,
   this README and the article; replaced by "the test machine" and "the
   owner's existing configuration". The bundled plugin's name is replaced
   in the saved tool listings. Grepped afterwards (see below).
8. **Structure.** "What the tests do not show" is now `##`. Plan and model
   facts left the "Which one you are using" table and the tests section for
   *The moving parts* (a Chat row and a reasoning-effort line were added
   there). The connectors advice in *In short* is now a separate item marked
   "Advice, not tested here", with its vendor reason. "Everything below the
   first two sections" is now "The practices in this guide". Quotes cut
   mid-sentence were completed: the Chat/Work/Codex line, the sign-in and
   API-key data lines, the folder-sync line and the connector-traffic line.

Left as it was: the "Last checked" line still names the model, as the
template asks; only the version moved. Item 1 of *What the template and
tasks got wrong* below is now answered by version 2.1 of the key.
