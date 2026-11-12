# Gemini: a guide to the assistant — research

Notes, the test attempt and sources for the Gemini guide, one of the four
assistant guides. Started 2026-11-11. The draft was not published: Gemini CLI
closed to personal accounts, and the guide became
[Working with Antigravity, Tested](https://topics.pages.dev/ai/antigravity/).
Template, tasks and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md).

## Access and confidence

- **No test was run.** The plan names Gemini CLI (`gemini`) as the app to
  test with. On this Mac it is signed in with a personal Google account, and
  Google refuses that sign-in: "This client is no longer supported for Gemini
  Code Assist for individuals". Google's own pages say Gemini CLI stopped
  serving personal accounts, free or on Google AI Pro and Ultra, on 18 June
  2026, and point them to Antigravity CLI. The brief says to stop testing when
  the app cannot sign in; testing stopped after one attempt to list the tools.
  Every practice in the draft is therefore from Google's pages, and the draft
  says so. Details: [`notes/test.md`](notes/test.md).
- **No run free of the owner's add-ons was shown either.** Gemini CLI loads
  the owner's agent skills whatever the flags; MCP servers and extensions were
  excluded by flags, but the run failed before that could be confirmed.
- **Vendor pages were read as their own text** where Google serves them that
  way (help centre, developer docs, release notes, plans page, the CLI's own
  docs in its repository). The Antigravity pages are built in the browser and
  were read through a summarising fetch; the notes mark them. The Gemini Apps
  Privacy Notice, Google's Privacy Policy and the Workspace privacy hub were
  not read.
- **Prices are in CAD**, as the plans page shows them when fetched from
  Canada. Business plans and Antigravity's business plan are in US dollars,
  as the pages give them.
- **Nothing in the Gemini app was tried.** Skills, Gems, memory,
  instructions and plan limits are from the help centre only. See *For the
  owner*.
- **Leads were collected, not tested**: fifteen, all *untested*
  ([`notes/leads.md`](notes/leads.md)).

## What is here

| File | What it is |
|---|---|
| [`notes/cli-and-antigravity.md`](notes/cli-and-antigravity.md) | Gemini CLI's end for personal accounts, `GEMINI.md`, headless flags, Antigravity CLI, Antigravity pricing |
| [`notes/app-and-plans.md`](notes/app-and-plans.md) | Plans and CAD prices, release notes, file upload limits |
| [`notes/gems-skills-memory.md`](notes/gems-skills-memory.md) | Gems and their replacement by skills, memory, instructions |
| [`notes/data.md`](notes/data.md) | Training, human review, retention, Keep Activity |
| [`notes/leads.md`](notes/leads.md) | Fifteen repeated tips, with links, all untested |
| [`notes/test.md`](notes/test.md) | The attempt, what was tried, and what would make tests possible |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/results/t0-tools-list/`](example/results/t0-tools-list/) | The one attempt: prompt, command, the error |

## Decisions

1. **Stopped testing, did not switch apps.** Antigravity CLI (`agy` 1.5.6) is
   installed and is Google's named successor, but the plan and the brief name
   `gemini`, and *One Repository, Three Agents* already covers Antigravity.
   Switching is for the lead to decide (see *What the template and tasks got
   wrong*, item 1).
2. **The guide is written as a draft without a "Practices that held up"
   section of its own.** The template's section is kept, with a note that no
   practice has been tested, and with the practices Google itself states,
   each with its page. Nothing from the leads is presented as working.
3. **Gems are described as ending.** Google's page gives 17 November 2026
   (read-only) and 17 December 2026 (removed) for personal accounts, six and
   36 days after this draft. The guide describes skills, with Gems as what
   they replace.
4. **No default model is named.** None of the pages read today says which
   model a new chat in the Gemini app starts on, and Gemini CLI has none for a
   personal account. Model names appear only in *The moving parts*, as the
   plans page gives them per plan.
5. **The instruction file is reported as `GEMINI.md`**, which both Gemini CLI
   and Antigravity CLI read, with `AGENTS.md` read by Antigravity as well
   (migration guide). In the Gemini app the nearest equivalents are
   *Instructions for Gemini* and skills.

## For the owner

Things that live only in the Gemini app, to check by hand before
`draft: true` comes off. Each says what to look for.

1. **Gems on your account.** Open gemini.google.com > Gems (or *Customise*):
   are your Gems still editable today, and is there a banner about 17
   November? After 17 November, check they appear under Skills, and which
   knowledge files did not come across (Google says `.doc`, `.xls`, `.ppt` and
   archives do not).
2. **Skills.** Customise > Skills: does *Create manually* exist, can you
   upload a folder with a `SKILL.md`, and does typing `/` in a chat list
   them? Try the house rules from `tasks/house-rules.md` as a skill and ask
   for the work-day notice: does it follow all six rules?
3. **Instructions for Gemini.** Settings > Personal Intelligence >
   Instructions for Gemini: what is in it now, and is it switched on? Google
   says asking it to *remember* facts is US-only and needs a paid plan; from
   Canada, does "Remember that…" work, or only typed instructions?
4. **Memory of past chats.** Settings > Personal Intelligence: is memory on?
   Ask "Did you use any info from past chats?" after a chat that should have
   used one, as Google suggests.
5. **Keep Activity and training.** myactivity.google.com/product/gemini: is
   Keep Activity on (Google says it is on by default for adults), and what is
   the auto-delete period (default 18 months)? Is the separate audio and Live
   box ticked?
6. **Temporary chat.** Is there a temporary-chat button in the web app and
   the Mac app, and does a temporary chat stay out of Activity?
7. **Your plan and its limits.** Which Google AI plan is on the account, what
   is charged in CAD with tax, and does the app show any usage meter? The
   plans page gives limits only as multiples ("4x higher usage access than
   Free-of-charge").
8. **Which model a new chat starts on.** In the model drop-down, what is
   selected by default on your plan, and are Gemini 4 Argon and Carbon
   listed?
9. **Antigravity in the Mac app.** The 13 October release note says
   Antigravity is built into the Gemini Mac app. Is the *Antigravity* button
   there, and does it ask for a folder?
10. **Connected apps.** Customise or Settings > Apps: which Google and other
    apps are connected? With Keep Activity off, Google says Workspace apps
    are unavailable.
11. **The upload limits.** Upload the test folder's nine files at once
    (README, members list, seven notes): does it accept all of them in one
    prompt? Google says up to 10.

## What the template and tasks got wrong

For the lead. Nothing under `../2026-11-10-assistant-guides/` was edited.

1. **The test app is gone for personal accounts.** The plan's table says
   Gemini is tested with `gemini`; since 18 June 2026 that works only with a
   Code Assist Standard or Enterprise licence or a paid API key, and Google's
   README says not to use it to benchmark Gemini 4 models. *Change:* test
   Gemini with Antigravity CLI (`agy -p … --model <m> --mode accept-edits
   --output-format json`, second turn with `--conversation <id>`), and add a
   step to the shared README: "Before testing, run one trivial prompt and
   check the app signs in; check the vendor's status page for the app." The
   guide's section on apps should then say plainly that Google's coding agent
   for individuals is Antigravity, and link to *Three Agents*.
2. **"No MCP servers or extensions" is not enough for Gemini CLI or
   Antigravity: agent skills load too.** Gemini CLI 0.38.2 loaded the
   owner's skills from two folders with every flag set, and has no flag to
   stop it. Antigravity reads the same skill folders. *Change:* the README
   should name skills alongside connectors and MCP servers, say how each app
   excludes them, and accept "skills loaded, none relevant to the task, list
   logged" when an app has no switch, rather than forbid the run.
3. **"Ask the assistant to list its tools" cannot be the only evidence.** An
   app that fails at sign-in, or a model that lists tools loosely, gives no
   proof. *Change:* where the app has a command that lists MCP servers and
   extensions without the model (`gemini mcp list`, `gemini -l`, `agy mcp
   list`), log its output as well.
4. **The template has no shape for a guide whose tests could not run.**
   *Change:* allow "Practices that held up" to be replaced, until tests run,
   by "What Google recommends" with each item tied to a vendor page, and say
   in the "Last checked" line that no test was run.
5. **Plans change faster than monthly for Gemini.** Gems disappear within
   five weeks of this draft. *Change:* the watch list should include each
   vendor's announced retirement dates, and the monthly agent should flag any
   date that falls before the next check.
6. **This guide adds no evidence on version 2 of the tasks.** Whether it
   separates plain from careful prompts has to come from the other guides.
