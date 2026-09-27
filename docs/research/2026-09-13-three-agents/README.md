# One repository, three agents — plan and research

Plan and notes for the first on-site Software Development article: setting
up git and GitHub for a project, and putting Antigravity, Claude Code (in
Claude Desktop) and ChatGPT (Codex) to work on the same repository. Started
2026-09-13.

Audience: a developer who has one of these tools and is being offered the
other two — and wants the setup that lets all three touch one repository
without stepping on each other or on the developer.

## What was verified, and how

| Claim | Checked against |
|---|---|
| Each tool's install, sign-in, project model, worktree support, permissions, instruction files | The vendors' own documentation, read in full — [`notes/tools.md`](notes/tools.md) lists the pages and what was not obtainable |
| What is installed here, and the versions | The machine: `/Applications`, `--version`, `gh auth status` |
| What happens when the three CLIs are asked the same read-only question about this repository | Run here — [`notes/run.md`](notes/run.md) |
| Ubuntu and Windows install steps, added in a follow-up session | Mixed confidence — see below |

Not verified: anything behind a GUI I cannot see this session — the
Antigravity 2.0 window, the Claude Desktop Code tab, the ChatGPT desktop
app's Codex pane. The article describes those from the vendors' pages and
says so; the CLIs, which share the engines, are what was run.

### Adding Ubuntu and Windows

The article as first published covered macOS only — every command was
`brew`, every path was `~/Library`-adjacent, the timed probe ran on one M4
Mac. A later session extended the install section to Ubuntu and Windows.
Its own network policy blocked `antigravity.google`, `learn.chatgpt.com` and
`cli.github.com` directly (403/407 at the egress proxy), so the two kinds of
new claims carry different confidence:

- **High.** `code.claude.com/docs/en/setup` was reachable and fetched in
  full — a single page with exact system requirements and install commands
  for macOS, native Windows, WSL, and Ubuntu/Debian/Fedora/RHEL/Alpine
  package repositories. Quoted directly. `apt-cache policy gh` /
  `apt-cache madison gh` and `claude --version` were run live on a stock
  Ubuntu 24.04 container in that session — the "Ubuntu's own `gh` is two
  years behind" claim and the Claude Code CLI version are first-hand.
- **Corroborated, not primary-sourced.** Antigravity's Windows/Linux system
  requirements, the `agy` Windows install path and its WSL/native-PATH
  split, and Codex's Windows-native install being labelled experimental all
  come from several independent secondary write-ups agreeing with each
  other, not from fetching the vendor page in that session. `notes/tools.md`
  flags exactly which sentences these are.

The empirical probe in [`run.md`](run.md) was **not** re-run on Ubuntu or
Windows — it is inherently a one-machine measurement (timings, exact CLI
output), and this repository's development machine is the M4 Mac the
article already names. The article says so explicitly rather than implying
the three-CLI test was repeated per platform.

## Decisions

1. **git and gh first, then the agents.** All three lean on the same two
   facts: a branch can be checked out in one place at a time (hence
   worktrees everywhere), and `gh` is the plumbing the desktop apps use to
   watch and merge pull requests.
2. **One section per agent, the same five headings each** — install, sign
   in, open the project, isolate (worktree), what it reads — so the reader
   can compare rather than be told.
3. **Instruction files are the interoperability layer.** `CLAUDE.md`,
   `AGENTS.md`, `.agents/`. The repository, not the tool, is where the rules
   live; the article recommends one file and pointers.
4. **Measure the boring thing.** Not benchmark quality — one read-only
   question, three CLIs, what each did and how long it took.
5. **The updates are the story.** Two of three CLIs refused the first
   probe until updated; that is the most honest thing to tell someone
   setting this up.

## Traps hit

- `codex exec` has no `--ask-for-approval` flag (that is an interactive-mode
  option); its non-interactive controls are `--sandbox` and the config.
- Codex 0.132.0 refused its own configured model — "'gpt-6-astra' requires a
  newer version of Codex" — and logged a model-list parse error. `codex
  update` is the fix; it is also the first line of any setup guide.
- `agy --version` printed 1.0.0 while `agy update` reported 1.2.2 and "already
  latest"; the first `--print` said "this version is no longer supported…
  /logout, then log in again." Two version strings, one product.
- macOS has no `timeout`; bound a possibly-interactive CLI with a background
  job and a kill.
- OpenAI's help centre and download pages refuse non-browser fetches; the
  documentation at `learn.chatgpt.com` serves Markdown and is the source used.
- Antigravity's docs site serves Markdown at `<page>/index.md`, but several
  sidebar entries (Rules, Skills, Hooks) resolve to no such page from the
  slugs I could guess; those features are named, not described.
