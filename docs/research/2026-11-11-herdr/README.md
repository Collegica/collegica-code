# Many Agents, One Terminal: research

Notes for [the Herdr article](https://topics.pages.dev/software/herdr/),
drafted 2026-11-11 alongside the site's guides to the AI assistants. A
tool, not an assistant: it does not use the guides' template or common
tasks.

## Access and confidence

- **Vendor material, read 2026-11-11:** the `herdrdev/herdr` repository
  through the GitHub API (metadata, README, CHANGELOG 0.9.2 to 0.9.5, LICENSE
  history, releases, 451 open issues searched by keyword); the herdr.dev
  documentation for 0.9.5 through its `llms.txt` index, which serves each
  page's source at the `v0.9.5` tag; herdr.dev's front page, `/tui/`,
  `/core/` and blog index; the installed binary's own help and skill file.
  What was read is in [`notes/2026-11-11-vendor.md`](notes/2026-11-11-vendor.md)
  and [`notes/2026-11-11-issues.md`](notes/2026-11-11-issues.md).
- **Hands-on, one session on a Mac, 2026-11-11:** Herdr 0.9.5 with Claude
  Code 2.1.322 (Opus 5.5) and Codex CLI 0.166.0 (its default model, reported
  as GPT-6.1-Sol low) on a made-up scratch repository, each agent in its own
  Herdr-made git worktree. Logged in [`notes/test.md`](notes/test.md);
  screens in [`example/screens/`](example/screens/). **High confidence** in
  what was observed: driven through Herdr's JSON CLI, states polled once a
  second, every screen captured.
- **Small evidence.** One session, two agents, three prompts, no Herdr
  integration installed. The states matched what the agents were doing every
  time here; open issues show dialogs that other people see misread. The
  article says "in this test", not "always".
- **Not run here:** remote use (described from the docs; the test was kept to
  one machine); a server restart with conversation resume (needs an integration,
  which writes into `~/.claude` and `~/.codex`); pressing `ctrl+b q` (the
  first-run welcome box took the keyboard and dismissing it writes to
  Herdr's config file; the client was closed instead, which the docs treat
  as the same); the mouse; Linux and Windows.
- **Leads** from Tecmint, Better Stack, Bitdoze and others: 23 in
  [`notes/leads.md`](notes/leads.md); several are out of date (licence,
  detach key, command names, repository owner).
- **No connectors, mostly.** The agents' MCP servers and built-in
  connectors were disabled where possible, by command-line options only;
  one built-in Codex server could not be, and stayed connected. Neither
  task used it. Details in [`notes/test.md`](notes/test.md).

## Decisions

- **Scope is the terminal program.** On 2026-11-11 herdr.dev leads with a
  new desktop app built on herdr-core (separate repositories, created
  2026-10-16), and calls the terminal program *Herdr TUI*. The article
  covers the TUI, v0.9.5, which is what the proposal named and what is
  installed; it says the app exists and leaves it alone.
- **A new named session, not the default one,** so nothing else on the
  machine was touched; driven through the CLI with `--session`, plus a private
  tmux server (`tmux -L`) to host the TUI client and capture its screen.
- **Worktrees made by Herdr** (`herdr worktree create`), one per agent, as
  *One Repository, Three Agents* advises.
- **Claude Code in `--permission-mode default`** for the test, so it would
  stop and ask before an edit, giving one deliberately blocked agent.
- **No integration installed**, so the states seen are Herdr's screen
  reading alone, which is how Claude Code and Codex are detected even with
  their integrations (the integrations only report session identity).
- **Codex's folder trust passed on the command line**
  (`-c projects.<repo>.trust_level=trusted`, unquoted) rather than accepted
  in the dialog, which would have saved it in `~/.codex/config.toml`.
- **Volatile facts in one section** of the article ("What changes"):
  version, agents, the app.

## For the owner

1. **Press `ctrl+b q` yourself** in a new Herdr session, after dismissing the
   welcome box, and confirm the client detaches and `herdr` reattaches.
2. **Try a restart with an integration.** `herdr integration install claude`
   (it edits `~/.claude/settings.json` and adds a hook script), start Claude
   Code in a pane, `herdr server stop`, `herdr`, and see whether the
   conversation comes back. Uninstall afterwards if you do not want it.
3. **Watch the sidebar in a real terminal**, with the mouse: the colours for
   working, blocked, done and idle, and the notification sound or banner
   when an agent needs you. The test read the colours from captured
   terminal codes only.
4. **Decide about remote use.** The article describes `ssh` + `herdr`,
   `herdr --remote` and saved machines from the docs only. Testing it needs
   a second machine you can SSH into; it was out of scope.
5. **Decide whether the desktop app deserves its own article** or a section
   here. It was not opened.
6. **Codex's last built-in MCP server** could not be turned off from the
   command line. Find a switch for it before the next test, if one exists.
7. **Herdr talks to herdr.dev** for detection-rule updates and release
   checks; the privacy page was not read. Worth a look before the article
   says anything about privacy.

## Checker's report

A fresh checker reviewed the draft on 2026-11-11. Each finding, and what
changed:

| # | Finding | Change |
|---|---|---|
| 1 | "Right every time" contradicted the log: a fresh, unused Codex was marked `done` | Article says every state *during the task* was right and one at start-up was not; new bullet under "What the states tell you"; comment in the timeline table; `test.md` marks the row **Wrong** |
| 2 | The timeline was called "what the sidebar showed", but was polled with `herdr agent list` | Said so; the red/teal markers kept as a separate sidebar observation |
| 3 | (Code export manifest) | Left to the lead, as asked |
| 4 | Research README linked to repository paths missing from the public export, and named internal workflow | Links the published article; plan link and agent references removed |
| 5 | The research folder described the test machine's own set-up | Removed: other software and sessions on the machine, its agents' settings, the names and counts of MCP servers and connectors; local clock times replaced by UTC and elapsed time; the install command cropped from the Codex update screen. Generic wording for the connectors |
| 6 | "+2 min … I approved" and "the whole two minutes" against 1 min 52 s in the log | "+2 min 1 s … Claude Code's edit was approved"; "nearly two minutes" |
| 7 | `ctrl+b q` was never pressed | Marked "per the docs; in this test the window was closed instead" in all three places |
| 8 | "Takes every key": only `ctrl+b q` was tried; continuing opens the integrations settings | Reworded from the Configuration docs |
| 9 | Recognition of a hand-typed `claude`/`codex` was not tested | Said so; the test used `agent start --kind` |
| 10 | "Several third-party guides" was one | "One third-party guide (Bitdoze)" |
| 11 | `~/.herdr/worktrees/` is a default | "By default"; `--path` and `[worktrees] directory` mentioned |
| 12 | Herdr also checks for releases; `manifest_check` stops only rule checks | Both checks and both settings named; rules version 2026.10.11.1 |
| 13 | "Claude Code, Codex and most others" overstated screen reading | Reworded, with the agents that report their own state |
| 14 | Vendor apps' parallel worktree sessions came from an untested opinion | Now sourced to *One Repository, Three Agents* and framed conditionally |
| 15 | Desktop app date inferred from repository creation | "By November 2026 herdr.dev offers…" |
| 16 | Issue #5888 (first-run screens shown idle) missing | Added to `notes/2026-11-11-issues.md` and to the article after the trust-question sentence |
| 17 | Codex integration's changes understated | Hook script, `hooks.json`, `[features] hooks = true`, and the "Hooks need review" screen (#5888) |
| 18 | "About twenty"; licence history; Windows ARM64 | "More than twenty"; AGPL-3.0 from March, AGPL or commercial from 26 May, Apache-2.0 from 22 July 2026; "(ARM64 best-effort)" |
| 19 | Reboot and conversation resume inconsistent | A reboot brings conversations back only with the integration, squared with the 0.9.4 changelog |

## Files

| File | What it is |
|---|---|
| [`watch.md`](watch.md) | Feeds and pages to check each month |
| [`notes/2026-11-11-vendor.md`](notes/2026-11-11-vendor.md) | Repository, docs and site, what each says |
| [`notes/2026-11-11-issues.md`](notes/2026-11-11-issues.md) | Open issues on detection and restore |
| [`notes/leads.md`](notes/leads.md) | Third-party claims, passed or failed |
| [`notes/test.md`](notes/test.md) | The hands-on run |
| [`example/make_scratch_repo.sh`](example/make_scratch_repo.sh) | Builds the made-up scratch repository |
| [`example/screens/`](example/screens/) | Captured screens, `agent explain` output, the state poll, both agents' results |
