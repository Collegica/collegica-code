# Antigravity: a guide to Google's assistant — research

Notes, tests and sources for the Antigravity guide, the Google guide among
the assistant guides. Published at <https://topics.pages.dev/ai/antigravity/>.
Started 2026-11-12. Draft: `website/ai/antigravity/index.md` (`draft: true`).
Template, tasks and source rule:
[`../2026-11-10-assistant-guides/`](../2026-11-10-assistant-guides/README.md)
(version 2.1 of the tasks).

**It replaces the Gemini guide.** Google ended Gemini CLI for individual
accounts on 18 June 2026 and moved it into Antigravity
([Google's post, 19 May 2026](https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)).
The Gemini draft, written on 11 November without noticing this, is removed
from the site in the same pull request; its research stays in
[`../2026-11-11-gemini/`](../2026-11-11-gemini/) as the record of why Gemini
CLI is not covered.

## Access and confidence

- **Thirty runs of the common tasks were completed and marked,** three per
  prompt, on 12 November 2026 between 03:18 and about 03:41 UTC, on
  **Gemini 4 Argon (Medium)**, in Antigravity CLI 1.5.6. The log is
  [`notes/test.md`](notes/test.md).
- **The owner's Google AI Pro plan reached Antigravity late, and only for a
  while.** Until at least 02:25 UTC on 12 November the CLI offered only
  the free tier's models. By 03:14 UTC on 12 November it offered Gemini 4 Argon,
  Claude Opus and Sonnet 5.5, with a five-hour limit and a separate Argon
  weekly limit. At 03:42 UTC, just after the thirty runs, it showed the
  free-tier list again. All thirty runs were made while Argon was offered;
  the two lead tests that followed failed at once ("model … is not
  recognized") and used nothing.
- **Quota:** the Argon weekly limit went from 99% to 81% over the thirty
  runs, about 0.6% a run; the five-hour figure did not move. Thirty runs
  were under half the weekly limit, so all were made, as the owner's rule
  allowed.
- **No skipping of permissions in the Argon runs.** `--mode auto` is still
  "not available for this account". The runs used `--mode accept-edits
  --sandbox` with session-only settings: a short allow list of shell
  commands, everything else refused (including commands outside the
  sandbox, web pages and MCP). Two task 5 runs were stopped by it. Details
  and the probes in `notes/test.md`.
- **The three earlier runs on Gemini 3.8 Flash** (task 1 plain, before the
  Pro plan reached Antigravity, with `--dangerously-skip-permissions
  --sandbox`) are kept as earlier evidence, labelled as such, in
  `example/results/flash-*`.
- **No connectors.** No MCP servers or plugins configured, re-checked before
  the first Argon run; MCP also denied in the session settings.
- **Permission rules already saved in the CLI's user settings still
  loaded;** session settings add to them rather than replace them.
- **Vendor pages were read as their own text:** Antigravity's docs in
  Markdown with `curl`, the terms as stripped HTML. The Gemini Apps privacy
  page, the Gems page and the Google One plans page through a summarising
  fetch.
- **No prices.** The Google One page showed no
  figures.
- **The Gemini chat app is covered from Google's pages only, untested.**

## What is here

| File | What it is |
|---|---|
| [`notes/2026-11-12-installed-agy.md`](notes/2026-11-12-installed-agy.md) | The installed CLI, account, models, quota, connectors, instruction file check |
| [`notes/2026-11-12-antigravity-cli.md`](notes/2026-11-12-antigravity-cli.md) | Antigravity and its CLI: rules, modes, sandbox, headless, migration, terms on scripting |
| [`notes/2026-11-12-plans-and-models.md`](notes/2026-11-12-plans-and-models.md) | Models by plan, limits, credits |
| [`notes/2026-11-12-data-and-gemini-app.md`](notes/2026-11-12-data-and-gemini-app.md) | Telemetry and terms; the Gemini app's training setting, retention, Gems |
| [`notes/leads.md`](notes/leads.md) | Twelve repeated tips; one failed by inspection |
| [`notes/test.md`](notes/test.md) | The run log, the permission probes, the quota |
| [`watch.md`](watch.md) | The addresses to read each month |
| [`example/`](example/) | The runner scripts and session settings; `results/` with each run, the probes and the quota log |

## Decisions

1. **Antigravity, tested through its command-line app,** stands in for
   Google's assistant; the Gemini chat app is covered from Google's pages
   and marked untested (owner, 12 November 2026).
2. **Gemini 4 Argon (Medium), the default once the Pro plan showed,** for
   the thirty runs (owner, 12 November 2026). The three Flash runs are kept
   but not mixed into the tables.
3. **Three runs per prompt,** because one run cost about 0.6% of the
   weekly Argon limit and thirty fitted well under half (owner's rule).
4. **No `--dangerously-skip-permissions` in the Argon runs** (lead's
   instruction); the narrowest mode that let task 3 rename files was used.
5. **Task 3 plain marked with `check_t3.py --plain`** (tasks v2.1); the
   strict result is kept beside it.
6. **No price in the article** until the owner reads it from the Google One
   page.

## For the owner

1. **Scripting and the terms.** Google's FAQ: headless mode "is intended
   for direct scripting and CI workflows. Wrapping `agy` inside third-party
   coding agents or applications … is not supported under consumer plans",
   and its terms call using third-party tools to access the service "a
   breach". The tests run `agy -p` from a shell script that Claude Code
   starts. **Decided 12 November 2026:** the owner is comfortable with the
   agent starting the runs (made on 12 November, once the Pro plan showed).
2. **Your plan.** **Answered 12 November 2026: Google AI Pro**, whose
   benefits page lists "Entry rate limits to advanced models, including
   Gemini 4 Argon and Opus 5.5, in Google Antigravity". But `agy models`
   offers neither: only Gemini 3.8 Flash, Claude 4.6 and GPT-OSS, the
   Free and Plus set. Google's Models page says Gemini 4 Argon and the
   Claude 5.5 models need a paid, non-trial Pro subscription. Checked
   in the browser: `agy` is signed in to the Pro account, and the plan is a
   paid membership, not a trial. So Antigravity is not seeing the Pro plan.
   To try: `/logout` in `agy` and sign in again (the owner, not the agent),
   then `agy models`; if Gemini 4 Argon still does not appear, ask Google
   support. Price in CAD still wanted.
   **12 November, later:** the owner ran `agy models` again and got the
   same six models. By 03:14 UTC the Pro models appeared (Gemini 4 Argon,
   Claude 5.5) and the thirty runs were made on Argon; at 03:42 UTC the
   free-tier list was back. Worth asking Google support why the plan comes
   and goes.
3. **Telemetry.** In `agy`, `/config` > Enable Telemetry: on or off, and was
   it on by default? The terms say Interactions are used to improve Google's
   products and may be reviewed by people unless you switch it off.
4. **Quota.** Done: the thirty runs used about 18 points of the weekly
   Argon limit (99% to 81%). Separately, the free tier's Gemini weekly
   figure, which the CLI shows when the Pro plan is not seen, fell from 72%
   at 01:50 UTC to 54% at 02:25 and 33% at 03:42 UTC with no run from here
   on that pool; other Antigravity use on the account shares it.
5. **The Gemini app.** Is Keep Activity on? Do you have Gems, and have they
   become "skills" yet? Is there a memory or "saved info" setting, and what
   does it hold?
6. **The Antigravity app.** Does the desktop app show the same quota bar,
   and does its Settings > Account have the same telemetry switch?
7. **Your own CLI permission rules.** The allow rules already saved in
   `~/.gemini/antigravity-cli/settings.json` apply to every `agy` run,
   tests included. Keep or trim them as you see fit.

## What the template and tasks got wrong

Nothing under `../2026-11-10-assistant-guides/` was edited. In addition to
the Grok guide's list:

1. **Free-tier quotas cannot carry thirty runs.** On Antigravity's free
   tier view one run of task 1 used about 6% of a week (Gemini 3.8 Flash);
   on Pro, Argon used about 0.6% a run. *Change:* the README
   should ask agents to read the quota before the first run (`agy -p
   /usage`, Settings > Usage elsewhere), estimate from one run, and agree a
   budget with the owner before running the rest.
2. **Parallel runs hit rate limits** (two of three returned a 429 error and
   retried). *Change:* run one at a time on free tiers.
3. **Terms on scripted use** differ by vendor. *Change:* add a step to read
   each vendor's terms on headless or scripted use, and put any doubt to
   the owner before testing.
4. **The plan assumed Gemini CLI still served individuals.** *Change:* the
   vendor-reading step should begin with "is this product still offered to
   individuals?", and the plan's table should say Antigravity for Google.
5. **Permission modes differ by account and the README assumed one.**
   Antigravity offers `auto` only to some accounts, and its headless default
   refuses every command. *Change:* name a per-app narrow set-up (here:
   `accept-edits`, `--sandbox`, a session allow list) and forbid
   skip-all-permissions flags unless the owner agrees.
