# What the installed `grok` is, and whether it can run the tests

Checked 11 November 2026, 20:05 to 20:20 UTC, on the test machine,
read only. Nothing under `~/.grok` was edited. Paths below are shortened to
`~/`.

## It is xAI's own Grok Build, not a third-party tool

| Check | What it showed |
|---|---|
| `grok --version` | `grok 1.0.70 (f50904eaee6c)` |
| `grok --help`, first line | `Grok Build TUI` |
| `which -a grok` | `~/.grok/bin/grok`, and `~/.local/bin/grok`, which is a link to the same file |
| `~/.grok/bin/grok` | a link to `~/.grok/downloads/grok-macos-aarch64`, a native arm64 program |
| `~/.grok/README.md` and `~/.grok/docs/user-guide/01-getting-started.md` | install with `curl -fsSL https://x.ai/cli/install.sh \| bash`; "Grok Build is a terminal-based AI coding assistant from SpaceXAI"; sign-in "with grok.com" |
| xAI's launch post, [Introducing Grok Build](https://x.ai/news/grok-build-cli), dated 25 May 2026, read 2026-11-11 | the same install command; "a new coding agent that runs right from your terminal", "early beta for all SuperGrok and X Premium Plus subscribers" |
| [docs.x.ai/build/overview](https://docs.x.ai/build/overview.md), read 2026-11-11 | the same install command and `grok -p` for headless use |

So the installed program is **Grok Build, xAI's official command-line coding
agent**, installed by xAI's own script. A different, unofficial open-source
project (`grok-cli` from superagent-ai) also installs a command called
`grok`; third-party guides warn of the clash
([one example](https://www.issoh.co.jp/tech/details/8078/)). That is not what
is installed here.

The company name has changed on xAI's pages. Page titles on x.ai read
"SpaceXSI"; the privacy policy (27 October 2026) names "SpaceX Super
Intelligence LLC ("SpaceXSI")"; the local docs say "SpaceXAI"; docs.x.ai's
index says "SpaceXSI (xAI)". The article says xAI, with the new name once.

## It was not signed in (at first)

**Update, 21:17 UTC:** the owner signed in. `grok models` then
printed "You are logged in with grok.com.", "Default model: grok-4.7", and
the list grok-4.7 (default), grok-4.7-build-fast, grok-4.6, grok-4.5. The
runs followed; see `test.md`. The checks below are as made before that.

| Check | What it showed |
|---|---|
| `grok models` | "You are not authenticated." Then "Default model: grok-4.6", "Available models: * grok-4.6 (default), - grok-4.5" |
| `~/.grok/auth.json` | does not exist |
| `XAI_API_KEY` in the environment | not set |
| `~/.grok/logs/unified.jsonl`, every `auth` line since the first entry on 2026-11-10 | `"has_current":false` and `"auth_mode":null` in all 52; `"has_cached_token":false`; one sign-in method on offer, `grok.com` |
| the same log at 20:10 UTC | "model catalog refresh failed", so the model list above is the program's built-in list, not the account's |

Per the brief ("If the app is not signed in, stop testing and report") **no
test was run.** Signing in would mean the owner's browser sign-in to grok.com
(or an API key), which only the owner can do.

## What would load in a run: `grok inspect`, in an empty folder outside any repository

Summarised; the names and counts of the tester's skills, plugins, rules and
servers are left out because this folder is exported publicly.

- **Project trusted:** no.
- **Project instructions:** the tester's global `Claude.md` from `~/.claude/`,
  marked `[claude]`: Grok Build reads Claude Code's files by default.
- **Permissions:** rules loaded from `~/.claude/settings.json`.
- **Skills:** many, most of them from `~/.claude/` and Claude Code plugins.
- **Plugins:** some, carrying skills or an MCP server.
- **MCP servers:** one from a plugin, the rest from `~/.claude.json`
  (`[claude]`).

### Excluding the MCP servers without editing configuration

With two environment variables set for the one command,
`GROK_CLAUDE_MCPS_ENABLED=false GROK_CURSOR_MCPS_ENABLED=false grok inspect`,
the servers from `~/.claude.json` are listed as `[disabled]`. The one
that comes with a plugin stays listed. These variables are documented in
`26-config-reference.md` (the `compat.claude.mcps` and `compat.cursor.mcps`
rows) and in `07-mcp-servers.md`.

For the plugin's server, the planned per-run flags are `--deny MCPTool` (a
permission rule that refuses every MCP tool call; `14-headless-mode.md`,
"Permission Rules") and `--disallowed-tools CallMcpTool,GetMcpTools,FetchMcpResource,ListMcpResources`
(removes the MCP tools from what the model is offered, on the daemon route;
same page, "Tool Filtering"). Whether that leaves the model with no MCP tool
at all can only be checked by asking a signed-in Grok to list its tools,
which the brief requires before the first run. **Verified after sign-in,
with one change:** `search_tool` and `use_tool` also had to be removed;
see `test.md`, *Why each part is there*.

`grok mcp list` printed "No MCP servers configured": it lists only Grok's own
`config.toml`, not the Claude-compatible sources or plugins. `grok inspect`
is the command that shows them all.
