# Grok: a guide to the assistant — research

Notes, tests and sources for the Grok guide, one of the four assistant
guides, published at <https://topics.pages.dev/ai/grok/>.
Started 2026-11-11. Draft: `website/ai/grok/index.md` (`draft: true`).
Template, tasks and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md)
(version 2 of the tasks).

## Access and confidence

- **Thirty runs of the common tasks were completed and marked, and four
  leads three times each,** on 11 November 2026 in Grok Build 1.0.70, with
  `-m grok-4.7`, the default `grok models` reported on the owner's account.
  Every run's JSON reports the model as `grok-4.7-build`. The log is
  [`notes/test.md`](notes/test.md).
- **The app was not signed in at first.** The pre-flight checks at 20:20
  UTC found no credential, and testing stopped there as the brief
  says; the owner signed in at 21:17 UTC and the runs followed.
- **The installed `grok` is xAI's own Grok Build,** checked four ways (its
  `--help`, its bundled guide, the install script address, xAI's launch
  post). Not the unofficial `grok-cli`.
  [`notes/2026-11-11-installed-grok.md`](notes/2026-11-11-installed-grok.md).
- **No MCP server or connector was reachable in any run.** Grok Build reads
  Claude Code's and Cursor's set-up by default, including their MCP servers;
  environment variables switched that off for each command, and two tools
  were removed by flag. A signed-in tools check then said "No MCP tools are
  available to call." Nothing in the owner's configuration was edited.
- **Claude Code's instruction file and skills were kept out of the runs**
  the same way. So, unlike the Claude guide, the owner's own instruction
  files did not load; a reader who uses both apps would have them load.
- **One write to `~/.grok` was caused by a check.** Testing whether
  `--trust` loads `AGENTS.md` added one scratch folder to
  `~/.grok/trusted_folders.toml`. It was not repeated: the runs used
  `GROK_FOLDER_TRUST=0`, which writes nothing (the file was unchanged
  afterwards). The entry is harmless; the owner may delete it.
- **Vendor pages were read as their own text.** docs.x.ai as Markdown with
  `curl`; x.ai and help.x.com, which refuse plain downloads, as rendered text
  in a browser tab with no sign-in; the user guide bundled with 1.0.70 on
  disk.
- **The chat app's projects, memory and custom instructions are not on any
  xAI page found today,** and nothing in the chat was tested. See *For the
  owner*.
- **Prices are as x.ai shows them, "$" with no currency named,** before tax.
  No Canadian price was shown.
- **The company has a new name on its pages:** "SpaceX Super Intelligence
  LLC (SpaceXSI)". The article calls it xAI and gives the new name once.

## What is here

| File | What it is |
|---|---|
| [`notes/2026-11-11-installed-grok.md`](notes/2026-11-11-installed-grok.md) | What the installed `grok` is; sign-in; what loads; excluding MCP servers |
| [`notes/2026-11-11-grok-build.md`](notes/2026-11-11-grok-build.md) | Grok Build: instruction files, memory, plan mode, permissions, headless, models, data |
| [`notes/2026-11-11-plans-and-apps.md`](notes/2026-11-11-plans-and-apps.md) | grok.com and the apps, The X Subscription, usage, files |
| [`notes/2026-11-11-data.md`](notes/2026-11-11-data.md) | Training, retention and the switches, for grok.com, Grok in X and Grok Build |
| [`notes/leads.md`](notes/leads.md) | Fourteen repeated tips, with links; four tested |
| [`notes/test.md`](notes/test.md) | The run log and the marks |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/results/`](example/results/) | Each run's folder as it left it, prompts, JSON replies and times; the pre-flight output; the two tools checks |

## Decisions

1. **Stopped at sign-in, then resumed when the owner signed in.** An agent
   does not sign in to the owner's account.
2. **Model pinned to what the app reported as default once signed in,**
   `grok-4.7`. xAI's pages give three different answers (built-in list
   grok-4.6; example config `grok-build`; API "latest" grok-4.7). The model
   the runs report, `grok-4.7-build`, is named in the article.
3. **Claude Code's set-up switched off for the runs,** not only its MCP
   servers. Otherwise every Grok run would have carried the tester's Claude Code
   set-up (its instruction file and skills), which no other reader has.
4. **The same `GROK_FOLDER_TRUST=0` for plain and practice runs,** so that
   they differ only in the instruction file.
5. **Task 3's plain runs reported as "failed: names only".** The checking
   script wants `YYYY-MM-DD-<words>.md`; the plain prompt asks only for
   "consistent file names", and all three runs used `YYYY-MM-DD.md` with the
   right dates and unchanged text. Re-marked on 11 November 2026 under
   version 2.1 of the answer key (`check_t3.py --plain`): all three pass, and
   so do the three plan-mode lead runs. Both results are kept in the log.
6. **A practice that made no difference is reported as such.** All five
   tasks scored the same plain and careful (task 3 once re-marked under
   version 2.1). The article reports what the
   practice changed (a file, a list of doubts, a member count and a check,
   shorter notices) and does not claim better marks.
7. **Grok Bot and Cursor are mentioned, not covered.**

## For the owner

To check by hand before `draft: true` comes off.

1. **Usage.** Settings > Usage on grok.com: the weekly bar, and the Build
   share. The tests reported US$6.19 of API-equivalent cost (US$4.12 for the
   thirty runs, US$2.07 for the leads). How far did that move the bar?
2. **The first-run data screen.** Did signing in show "a screen to allow us
   to retain data to improve the product and model"? What was preselected?
   Then `/privacy` in Grok Build: is "Coding data, retention, and training"
   on Opt in or Opt out?
3. **Which plan the account is on,** and whether it is the old SuperGrok or
   X Premium, or The X Subscription. (x.ai's comparison table has a "Grok
   Build: Limited" cell whose column was not clear.)
4. **The price in Canada.** x.ai shows "$8 / $30 / $100 / $200" with no
   currency. What does checkout show from a Canadian card, and is tax added?
5. **Training switch on grok.com:** Settings > Data > "Improve the Model".
   Was it on before you touched it? (xAI's FAQ does not say what the
   default is.) Same on the phone app: Settings > Data Controls.
6. **Training switch in X:** Settings > Privacy & Safety > Data sharing and
   personalization > Grok & Third-party Collaborators. Was "Data Sharing"
   ticked?
7. **Projects.** Does grok.com have Projects (or "Workspaces")? Each with
   its own files and instructions? Do chats in one project see each other?
8. **Memory.** Is there a memory setting in grok.com? Where, is it on, can
   you see and delete what it remembers, and does Private Chat bypass it?
9. **Custom instructions.** Is there a box for instructions that apply to
   every chat? Where? (Leads 9 and 13 disagree on whether it exists.)
10. **Desktop app.** Is there a Grok app for Mac or Windows, or only the web
    and phones?
11. **Claude compatibility.** Grok Build reads your `~/.claude/` instruction
    files, skills, permission rules and MCP servers by default. Is that what
    you want? It is switched off per vendor under `[compat.claude]` in
    `~/.grok/config.toml`. (Not changed by the agent.)
12. **The trust entry.** `~/.grok/trusted_folders.toml` has one entry for a
    deleted scratch folder, added by a check.
    Delete it if you like.
13. **Repeat task 2 in the chat.** In a grok.com project (if there is one),
    put the house rules in its instructions and ask for the notice: does it
    keep them?

## What the template and tasks got wrong

Nothing under `../2026-11-10-assistant-guides/` was edited.

1. **No sign-in check comes first.** *Change:* step 0 in the shared README:
   "check the app is signed in (`grok models`, `codex login status`, and so
   on) and on the plan the tests need; if not, ask the owner before
   starting".
2. **The owner's Claude Code set-up leaks into other assistants.** Grok
   Build reads `~/.claude/` instruction files, skills, hooks, rules and MCP
   servers by default, so "the owner's instruction files … still load, as
   they would for anyone" is not true for Grok: they load because the owner
   also uses Claude Code. *Change:* per app, run `grok inspect` (or the
   equivalent) in a test folder before the first run, log what loads, and
   for Grok set the `GROK_CLAUDE_*` and `GROK_CURSOR_*` variables to `false`
   for every run (the list is in `notes/test.md`).
3. **"The vendor's own default model, read from its documentation" has no
   single answer for Grok.** *Change:* "the model the app itself reports as
   default on the owner's account (for example `grok models`), with what the
   docs say logged beside it, and the model each run reports".
4. **Task 2's practice does not load in a fresh folder unless trust is
   handled.** Without it, Grok Build ignored `AGENTS.md`. `--trust` works but
   writes to the owner's configuration; `GROK_FOLDER_TRUST=0` does not.
   *Change:* "before the first practice run, confirm the instruction file
   is loaded in the test folder (`grok inspect`, `/memory` in Claude Code,
   and so on), and use the same trust setting for plain and practice runs".
5. **`check_t3.py` fails reasonable plain runs.** It requires
   `YYYY-MM-DD-<words>.md`; the plain prompt asks only for "consistent file
   names". All three plain Grok runs named the files `YYYY-MM-DD.md`, with
   the right dates (26 August included), unchanged text and a full index,
   and failed only on the pattern. *Change:* accept `YYYY-MM-DD(-words)?.md`
   for the plain prompt, or mark plain runs on dates, text and index only.
6. **Version 2 still does not separate plain from careful prompts on
   Grok 4.7.** Tasks 1, 2, 4 and 5 scored the same plain and careful in all
   six runs each. The practices changed what came back (a file, a list of
   doubts, checks, shorter notices), not whether it was right. *Change:*
   either accept that the practices are about verifiability and record that
   as the measure (as task 3 already does with "said how it checked"), or
   make the traps harder: a note that contradicts an earlier one without
   saying so; a refund recorded only in a note, not in `members.csv`.
7. **Prices in CAD.** x.ai, like Anthropic, shows "$" with no currency.
   *Change:* "if the currency is not named, quote the figure as shown and
   say so".
8. **One subscription now covers Grok, Cursor and X.** *Change:* let the
   template's apps table have a "comes with" column.
9. **Permission mode.** "Permission to write in that folder only" means, for
   Grok, `bypassPermissions` plus `--sandbox workspace`, and even then one
   run wrote temporary copies to `/tmp`. *Change:* name the per-app mode and
   confinement in the README, and say that the system temporary folder may
   be used.

## Checker's report, 11 November 2026

A fresh agent checked the article and this folder against the sources and
raw outputs. Fixed on `guide/grok-tests`: the plan-mode lead re-marked as
passed with a caveat; task 3 plain re-marked under v2.1; "four of five" made
"all five"; Claude Code's permission rules noted as still loading; the
desktop-app line hedged ("Grok Desktop" is mentioned in Grok Build's guide);
the Grok Build plan cell hedged; deletion "up to 30 days" quoted as the notes
have it; "likes and reposts" changed to "metadata"; the Grok Personalization
purpose dropped; "first sign-in" changed to "first use"; the unread
changelog address dropped; "every time" replaced by counts; the task 4 plain
breakdown acknowledged; the British-spelling rule noted as untested by these
notices; heading "Check which `grok` you have"; "setup"; a link to *One
Repository, Three Agents*; upload limits and the model list moved to *The
moving parts*; "First published." in *What changed*; local times removed
from these notes.

Not fixed here, for the lead: the two links to collegica-code (this folder
and `2026-11-10-assistant-guides`) return 404 until both are added to
`scripts/collegica-code/manifest.yml`.

