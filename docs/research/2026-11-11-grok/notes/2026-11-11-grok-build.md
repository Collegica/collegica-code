# Grok Build: xAI's command-line app

Read 11 November 2026. Two sources, which mostly agree:

- **docs.x.ai**, the Markdown form of each page (`<page>.md`), fetched with
  `curl`: [overview](https://docs.x.ai/build/overview.md),
  [modes and commands](https://docs.x.ai/build/modes-and-commands.md),
  [AGENTS.md](https://docs.x.ai/build/features/project-rules.md),
  [headless and scripting](https://docs.x.ai/build/cli/headless-scripting.md),
  [MCP servers](https://docs.x.ai/build/features/mcp-servers.md),
  [permissions](https://docs.x.ai/build/features/permissions.md),
  [plan mode](https://docs.x.ai/build/features/plan-mode.md),
  [sessions](https://docs.x.ai/build/features/sessions.md),
  [settings](https://docs.x.ai/build/settings.md),
  [settings reference](https://docs.x.ai/build/settings/reference.md),
  [CLI reference](https://docs.x.ai/build/cli/reference.md),
  [enterprise](https://docs.x.ai/build/enterprise.md); and the index
  [llms.txt](https://docs.x.ai/llms.txt) with its full text `llms-full.txt`.
- **The user guide installed with version 1.0.70**, `~/.grok/docs/user-guide/`
  (27 files, dated 5 November 2026 on disk), read in full for files 01, 02,
  07, 12, 13, 14, and in part for 04, 05, 10, 22, 26. This guide is longer
  and newer in places than docs.x.ai.
- xAI's launch post, [Introducing Grok Build](https://x.ai/news/grok-build-cli),
  25 May 2026.

## What it is

- "Grok Build is a powerful and extensible coding agent. Use it via an
  interactive TUI, headlessly in scripts or bots, or through the Agent Client
  Protocol (ACP) in other apps." (overview)
- Launched 25 May 2026 as "an early beta for all SuperGrok and X Premium Plus
  subscribers" (launch post). On today's pricing page Grok Build is listed
  among the AI features of every paid plan from Plus up; see
  `2026-11-11-plans-and-apps.md`.
- Sign-in: "On first launch, Grok opens a browser for authentication. In
  non-browser environments, use an API key" (`XAI_API_KEY`). Credentials go
  in `~/.grok/auth.json`.
- Built-in tools (local guide 01): read and edit files, grep, list folders,
  run shell commands, web search and fetch, a to-do list, subagents.

## The instruction file

- **`AGENTS.md`** is the main one. Within each folder Grok reads any of
  `AGENTS.md`, `Agents.md`, `AGENT.md`, `CLAUDE.md`, `Claude.md` and
  `CLAUDE.local.md`, plus every `.md` in `.grok/rules/` (and `.claude/rules/`,
  `.cursor/rules/` for compatibility). Global rules live in `~/.grok/`.
  (docs.x.ai AGENTS.md page)
- Outside a git repository, only the working folder is read. Inside one,
  every folder from the root down; deeper files win on conflict.
- "Files are loaded in full, with no size cap; short, specific instructions
  are followed more reliably than long ones." (docs.x.ai)
- **Claude Code's files are read too, by default.** The local guide
  (12-project-rules.md): "When Claude compatibility is enabled (the
  default), Grok also scans your home-level `~/.claude/` directory for these
  filenames". The same holds for Claude's MCP servers, hooks, rules and
  skills (26-config-reference.md, `compat.claude.*`, all default on). Seen on
  the test machine: `grok inspect` listed the tester's global Claude file and
  the MCP servers from `~/.claude.json`.
- **Folder trust.** The local guide says: "Startup loading requires folder
  trust (`--trust` or an interactive grant)." The docs.x.ai page does not
  mention it, and `grok --help` for 1.0.70 lists no `--trust` flag. For
  hooks, the local guide says a headless run "counts the folder as trusted
  for your own hooks, but project hooks … still need the folder trusted".
  Whether a headless run loads a project `AGENTS.md` in an untrusted folder
  is **not clear from the docs**; `grok inspect` in the test folder would
  show it ("Project trusted: no" was shown in a scratch folder).
- Session-only rules: `--rules "<text>"` appends to the system prompt.
- `grok inspect` "lists each rules file Grok found, with its path and
  approximate token count."

## Memory (the command-line app)

- "Memory is experimental and disabled by default." (local guide 13).
  Turned on with `[memory] enabled = true`, `GROK_MEMORY=1` or
  `--experimental-memory`; notes are Markdown files, global and per
  repository; `/remember`, `/memory`, `/dream` manage them (llms-full,
  slash-command list).

## Plan mode, permissions, headless

- Plan mode: "For complex tasks, start Grok Build in plan mode. You can
  approve the plan, comment on individual steps, or rewrite it entirely
  before execution begins." (launch post). `--permission-mode plan` starts
  in it; a headless plan run "refuses every edit except the plan file"
  (local guide 22).
- Permission modes (docs.x.ai permissions; local guide 22): Ask (default),
  Auto (a classifier approves safe calls), Always-approve. Headless modes:
  `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`.
  "deny always wins over allow".
- A remembered "always allow" "still prompts for dangerous patterns such as
  `rm` and `git push`".
- Sandbox profiles (`off`, `workspace`, `read-only`, `strict`, `devbox`)
  limit what an approved call can do on disk and network (docs.x.ai sandbox,
  via llms-full).
- Headless: `grok -p "<prompt>"`, `--output-format json` gives the reply,
  session ID, usage and cost; `-r <session id>` resumes a session, so a
  second turn can continue the first (local guide 14).
- `web_fetch` is "Off by default for security" (`GROK_WEB_FETCH`, settings
  reference).

## Models

- The installed app, not signed in, reports "Default model: grok-4.6" and
  offers grok-4.6 and grok-4.5 (its built-in list; the online catalogue
  could not be fetched without sign-in).
- docs.x.ai settings page, example config: `default = "grok-build"  #
  recommended for coding / agent sessions`.
- docs.x.ai overview: "`grok-4.7`, SpaceXSI's latest model, is available
  directly on the xAI API."
- So **xAI's pages do not name one default model for Grok Build on a
  subscriber's account.** Signed in, `grok models` reported "Default model:
  grok-4.7" (also grok-4.7-build-fast, grok-4.6, grok-4.5). The tests pinned
  `-m grok-4.7`; every run reported `grok-4.7-build` in `modelUsage`.
- **Folder trust, tested:** in a fresh folder, `grok inspect` did not list
  `AGENTS.md` and a headless run said it had no project rules; with
  `--trust` (accepted by `grok -p`, though not in `--help`) or
  `GROK_FOLDER_TRUST=0` it was loaded. `--trust` records the folder in
  `~/.grok/trusted_folders.toml`.

## Data (the command-line app)

- docs.x.ai developer FAQ, security (via llms-full, section "Grok Build
  CLI"): "When using the Grok Build CLI without ZDR, privacy settings are
  available as a slash command (`/privacy`) and in settings (`/settings`).
  You can disable code data retention with these settings, even if ZDR is
  not enabled." And: "On using the Grok Build CLI, you will also see a
  screen to allow us to retain data to improve the product and model."
- Local guide 04: `/privacy` opens "Coding data, retention, and training",
  with **Opt in** or **Opt out**. Separate from telemetry, which is switched
  off with `DISABLE_TELEMETRY=1` or `[features] telemetry = false` (local
  guide 05).
- Sessions are saved on the computer under `~/.grok/sessions/` (local guide
  01).
