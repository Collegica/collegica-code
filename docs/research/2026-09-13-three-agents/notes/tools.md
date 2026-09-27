# The four tools — checked at the source on 2026-09-13

## Access and confidence

- **Read in full:** Antigravity's getting-started, CLI install / execution
  modes / projects / permissions / sandbox, and 2.0 permissions, models,
  plans, subagents and remote-control pages (the docs site serves Markdown
  at `<page>/index.md`); its pricing and product pages; `agy --help` on this
  machine. Claude Code's desktop-app page, and — fetched directly this
  session — its [advanced setup page](https://code.claude.com/docs/en/setup),
  which covers system requirements and install on macOS, Windows (native and
  WSL), and Linux (apt/dnf/apk) in one place. OpenAI's ChatGPT/Codex docs
  (`learn.chatgpt.com`, Markdown at `<page>.md`): the ChatGPT desktop app,
  Codex CLI, cloud, IDE extension, worktrees, AGENTS.md, authentication,
  customization, code review, approvals and security, scheduled tasks. The
  GitHub CLI manual's command list and `gh auth login --help`.
- **Verified on this machine:** versions installed, `gh auth status`, and
  the read-only probe in [`run.md`](run.md).
- **Not obtained:** OpenAI's help-centre article on *Work with Apps* and the
  ChatGPT download page — both refuse non-browser fetches (403). The
  desktop app's developer features are taken from `learn.chatgpt.com`
  instead, which is OpenAI's own documentation.
- **Added later, for Ubuntu and Windows coverage, with a narrower session:**
  the article's original macOS-only setup steps were extended to Ubuntu and
  Windows in a follow-up session whose own network policy blocked direct
  fetches of `antigravity.google`, `learn.chatgpt.com` and `cli.github.com`
  (403/407 at the egress proxy — the same class of refusal as the OpenAI
  pages above, not a claim that these pages are unreachable in general).
  Two things were verified first-hand in that session instead: the
  Claude Code setup page above (a different host, not blocked, so fetched
  in full and quoted directly), and `apt-cache policy gh` / `apt-cache
  madison gh` run live on a stock Ubuntu 24.04 container, which is where the
  "2.45 in `universe`, two years behind" claim in the article comes from.
  Antigravity's Windows/Linux system requirements, the `agy` Windows
  installer path, the WSL packaging caveat, and Codex's native-Windows
  "experimental" status are corroborated across several independent
  secondary write-ups (LinuxCapable's Ubuntu install guide, ITECS's Windows
  setup guides for Antigravity and Codex, and others) rather than confirmed
  against the vendor page directly — lower confidence than everything above,
  and it is why the article states them as plain facts but does not quote
  vendor wording for them the way it does for macOS.

## What is installed here

| Tool | Version | Where it lives |
|---|---|---|
| git | 2.52.0 | Homebrew |
| GitHub CLI `gh` | 2.98.0 (2026-08-20) | signed in to github.com, SSH for git operations, token in the keychain |
| Antigravity 2.0 | 2.12.2 (docs: 2.13.0) | `/Applications/Antigravity.app` |
| Antigravity IDE | 2.5.5 | `/Applications/Antigravity IDE.app`; user data in `~/.antigravity/` — a VS Code-family editor, with the Claude Code extension installed inside it |
| Antigravity CLI `agy` | 1.0.0 (docs: 1.2.0) | `~/.local/bin/agy`; settings in `~/.gemini/antigravity-cli/settings.json` |
| Claude Desktop | 1.52386.3 | `/Applications/Claude.app`, the **Code** tab |
| Claude Code CLI | 2.1.266 | `claude` |
| ChatGPT desktop | 26.908.40834 | `/Applications/ChatGPT.app` |
| Codex CLI | 0.132.0 | `codex`; home `~/.codex/` with a global `AGENTS.md` |
| git (Ubuntu container, later session) | 2.43.0 | Ubuntu 24.04's own package |
| `gh` candidate (Ubuntu 24.04, `universe`) | 2.45.0 | not installed; `apt-cache policy gh` / `madison gh` |
| Claude Code CLI (Ubuntu container, later session) | 2.1.270 | `claude`; npm global manifest pinned `2.1.42`, native binary auto-updated past it |

## git and GitHub

`gh auth login` opens a browser flow and stores the token in the system
credential store; `--git-protocol ssh` (or the prompt) makes git push over
SSH with a key gh can upload for you (`gh ssh-key add`). Minimum scopes for a
pasted classic token: `repo`, `read:org`, `gist`. `gh` 2.98 has `repo create`,
`pr create/checks/merge`, `run watch`, `api`, and two agent-era commands:
`gh copilot` (runs the Copilot CLI, preview) and `gh agent-task`
(create/list/view tasks for GitHub's own coding agent).

Two facts every agent below leans on: **Git allows a branch to be checked
out in one place at a time**, which is why all three use worktrees for
parallel sessions; and **Claude Desktop's PR monitoring requires `gh` to be
installed and authenticated** — the CLI is the shared plumbing.

Cross-platform: `git` is Xcode's command-line tools on macOS, `apt install
git` (often already present) on Ubuntu, its own installer or `winget install
--id Git.Git` on Windows. `gh` is `brew install gh`, `apt install gh` or
`winget install --id GitHub.cli`, but Ubuntu's own `universe` package is
stale — `apt-cache policy gh` on a stock 24.04 container here shows 2.45.0,
against 2.98 on the macOS machine — and GitHub's own apt repository
(key at `cli.github.com/packages/githubcli-archive-keyring.gpg`, a `deb`
line pointed at `cli.github.com/packages`) is the documented fix.

## Antigravity (Google)

"Agentic development platform"; free for individuals (Gemini 3.8 / 3.7 /
3.6 Flash, Gemini 3.1 Pro, Claude Sonnet & Opus 4.6, gpt-oss-120b; unlimited
Tab; weekly rate limits), more quota on Google AI Pro / Ultra, no
bring-your-own-key. Four surfaces: **Antigravity 2.0** (the command centre:
Projects that span folders and repositories, agents in *Local Mode* or *New
Worktree Mode*, dynamic subagents, scheduled tasks by cron, artifacts —
plan, walkthrough, screenshots — Remote Control from a browser or phone),
**Antigravity IDE** (the editor: Tab, Command, agent side panel, browser
subagent), **Antigravity CLI** (`agy`; modes `default` → `accept-edits` →
`plan` with Shift+Tab; `--print` for headless; `--sandbox`; `/agents`,
`/diff`, `/permissions`, `/fork` between projects), and **extensions** for
VS Code, JetBrains, Zed, Xcode, Visual Studio.

Permissions are `action(target)` rules in three lists — deny > ask > allow —
for `read_file`, `write_file`, `read_url`, `execute_url`, `command`,
`unsandboxed`, `mcp`; the sandbox is `sandbox-exec` on macOS and namespaces
on Linux, no VM. Subagents can inherit the workspace, `branch` into a
worktree, or `share`; custom ones live in `.agents/agents/<name>.md` in the
repository or `~/.gemini/config/agents/`. The docs' requirement line: macOS
12 or newer, "X86 is not supported" — while the download page still lists an
Intel build; Windows 10 64-bit+ (x64 or ARM64); Linux glibc 2.28+ and
glibcxx 3.4.25+, i.e. Ubuntu 20.04+, Debian 10+, Fedora 36+, RHEL 8+ (Windows
and Linux requirements corroborated across secondary sources, not read
directly this session — see the note above).

`agy` installs the same way on macOS and Linux (`curl … | bash`, into
`~/.local/bin/agy`, working on WSL too); natively on Windows it is
`irm https://antigravity.google/cli/install.ps1 | iex`, no WSL required, into
`%LOCALAPPDATA%\agy\bin`. The two do not share a PATH: `agy` from the native
Windows installer is invisible to a WSL shell and needs a manual symlink to
reach from there, a friction several independent write-ups describe hitting.

## Claude Code, in Claude Desktop

The **Code** tab: sessions in sidebar tabs, each with a project folder, an
environment (Local, Cloud, SSH, WSL), a model, and a permission mode
(Manual, Accept edits, Plan, Auto, Bypass). The **worktree** option at
session start gives each session `<project>/.claude/worktrees/<name>`; a
`.worktreeinclude` file copies gitignored files such as `.env` in. Diff
review with line comments; **Review code**; when Claude opens a PR, a CI
status bar with **Auto-fix** and **Auto-merge** (squash), which needs `gh`.
Desktop and CLI read the same `CLAUDE.md` / `CLAUDE.local.md`,
`~/.claude/settings.json`, `.mcp.json`, `~/.claude/skills/`; `/desktop` moves
a CLI session into the app.

System requirements and platform install, from `code.claude.com/docs/en/setup`
(fetched in full this session): macOS 13.0+, Windows 10 1809+ or Windows
Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; 4 GB+ RAM. The native
installer (`curl … | bash` on macOS/Linux/WSL, `irm … | iex` in PowerShell,
or a documented CMD one-liner on Windows) auto-updates in the background;
Homebrew, WinGet (`winget install Anthropic.ClaudeCode`) and the Linux
package repositories (signed `apt`/`dnf`/`apk`, e.g.
`downloads.claude.ai/claude-code/apt/stable`) do not, and need a manual
`brew upgrade` / `winget upgrade` / `apt upgrade`. On native Windows, [Git
for Windows](https://git-scm.com/downloads/win) is optional but decides
which shell tool Claude Code uses: with it, the Bash tool via Git Bash; set
`CLAUDE_CODE_GIT_BASH_PATH` if it is not auto-detected; without it, the
PowerShell tool. WSL needs no Git for Windows — it runs the Linux installer
inside the distribution. Alpine and other musl distributions need `bash`,
`curl`, `libgcc`, `libstdc++` and `ripgrep` installed manually, plus
`USE_BUILTIN_RIPGREP=0` in settings.

## ChatGPT desktop, Codex

OpenAI's docs describe the **ChatGPT desktop app** as "your command center
for complex work": open a folder or project, choose **ChatGPT** or **Codex**
above the composer. Codex work on a local repository happens there or in the
**Codex CLI** (`curl -fsSL https://chatgpt.com/codex/install.sh | sh`, or
`npm i -g @openai/codex`; `codex exec` for scripts; `codex login` with a
ChatGPT plan or an API key) or the **IDE extension** (`openai.chatgpt`, for
VS Code, Cursor, Windsurf; Xcode and JetBrains have their own). **Worktrees**:
choose *Worktree* under the composer, pick the base branch, and Codex works
in a detached-HEAD worktree; **Handoff** moves a chat and its code between
Local and Worktree; **Create branch here** turns the worktree into a branch
to push and open a PR from. **Codex cloud** runs tasks in OpenAI containers
against a connected GitHub repository and opens PRs. **Code review**:
`/review` locally (against a base branch or uncommitted changes), and
`@codex review` on a GitHub PR, following `## Code Review Rules` in
`AGENTS.md`. Sandbox: no network by default, writes limited to the workspace;
`--sandbox read-only --ask-for-approval on-request` for a look-only run.

`AGENTS.md` discovery: `~/.codex/AGENTS.md` (or `AGENTS.override.md`), then
every directory from the Git root down to the working directory, later files
overriding earlier, 32 KiB in all by default.

The install script is identical on macOS, Linux and WSL. OpenAI shipped a
native Windows installer and a Windows-native sandbox (AppContainer / OS
access-control based, replacing the Landlock/seccomp sandbox Codex uses on
Linux) in early 2026, but multiple independent write-ups describe it as
still labelled experimental as of March 2026, with WSL — where Codex keeps
the Linux sandbox — recommended as the default until that changes. Not
confirmed against `learn.chatgpt.com` directly this session (blocked); see
the note above.

## The instruction files, side by side

| Agent | Reads | Global |
|---|---|---|
| Claude Code | `CLAUDE.md`, `CLAUDE.local.md`, `.claude/` (skills, settings, rules) | `~/.claude/CLAUDE.md` |
| Codex / ChatGPT | `AGENTS.md`, `AGENTS.override.md`, walked from the Git root | `~/.codex/AGENTS.md` |
| Antigravity | `.agents/agents/<name>.md` for custom subagents (confirmed); the docs list Rules, Skills, Hooks under *Customizations*, pages not fetched | `~/.gemini/config/` |

Codex reads `AGENTS.md`; Claude Code reads `CLAUDE.md`; a repository that
wants both to behave the same keeps one and points the other at it (this
site's `video/` projects carry both, identical).
