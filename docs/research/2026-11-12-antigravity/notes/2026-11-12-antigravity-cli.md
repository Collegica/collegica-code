# Antigravity and its command-line app

Read 12 November 2026, from Google's Antigravity documentation in its
Markdown form (each page's address with `.md` added), downloaded with
`curl`. Index: <https://antigravity.google/llms.txt>.

Pages read: [overview](https://antigravity.google/docs/overview),
[models](https://antigravity.google/docs/models),
[plans](https://antigravity.google/docs/plans),
[rules](https://antigravity.google/docs/rules),
[MCP](https://antigravity.google/docs/mcp) (configuration part),
[terminal sandbox](https://antigravity.google/docs/sandbox) (first part),
[settings](https://antigravity.google/docs/settings) (data and CLI parts),
[FAQ](https://antigravity.google/docs/faq),
[CLI migration](https://antigravity.google/docs/cli/gcli-migration),
[headless mode](https://antigravity.google/docs/cli/headless),
[execution modes](https://antigravity.google/docs/cli/modes),
[CLI AI credits](https://antigravity.google/docs/cli/credits),
[model quotas (/usage)](https://antigravity.google/docs/cli/commands/usage),
[CLI best practices](https://antigravity.google/docs/cli/best-practices),
the [changelog](https://antigravity.google/docs/changelog) (CLI 1.5.3 to
1.5.6, through `agy changelog`), and Google's blog post
[An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
(19 May 2026).

## What it is

- Antigravity comes as an app (a desktop "command center"), an IDE, editor
  extensions, a CLI (`agy`) and a Python SDK (overview, llms.txt).
- The blog post: Gemini CLI is folded into Antigravity. "On June 18, 2026,
  Gemini CLI and Gemini Code Assist IDE extensions will stop serving
  requests for Google AI Pro and Ultra", and for those using it free through
  Gemini Code Assist for individuals. Enterprise access and paid API keys
  continue. Antigravity CLI "is available to everyone".
- Migration page: "Both CLI platforms use identical workspace context
  rules": `GEMINI.md` and `AGENTS.md` in the folder, `~/.gemini/GEMINI.md`
  globally. Gemini CLI extensions become plugins (`agy plugin import
  gemini`); MCP servers move to `mcp_config.json`.

## The instruction file

- "You can place an `AGENTS.md` or `GEMINI.md` file—or a `.agents/rules/`
  directory—in your workspace folder and in any parent folder up to the
  repository root." Global: `~/.gemini/AGENTS.md`, `~/.gemini/GEMINI.md`,
  and two more under `~/.gemini/config/` (rules page).
- `AGENTS.md` and `GEMINI.md` "do not use frontmatter" and are always
  active. Files in `.agents/rules/` need YAML frontmatter with a `trigger`,
  or are "silently" discarded.
- All always-on rules share a "20,000-token aggregate rules budget"; past
  it, the largest files are demoted to pointers the agent reads on demand.
- Best practices page: "Create a `GEMINI.md` or `AGENTS.md` file at your
  workspace root to outline specific directory standards, styling
  paradigms, test command parameters, and deprecation warnings."

## Practices Google recommends (CLI best practices)

- "The single most effective way to ensure reliable, correct modifications
  from an autonomous agent is to provide the agent with a local
  verification mechanism (such as unit tests, build commands, or formatting
  scripts)."
- "Explore, plan, then execute": ask how it works, ask for an
  implementation plan, approve, then apply.
- `@` to point at a file; paste a screenshot for visual problems.
- `Esc` to interrupt early; `/rewind` and `/fork` to go back or branch.

## Modes and permissions

- Modes (execution modes page): default; `accept-edits` ("still asks before
  running terminal commands"); `auto` (edits approved, commands in the
  terminal sandbox, commands outside it evaluated, "requires the terminal
  sandbox and a personal account"); `plan`.
- On this account `auto` is "not available" (see
  `2026-11-12-installed-agy.md`).
- Headless: `permission_mode` is `request-review` by default;
  `--dangerously-skip-permissions` "approves all tool calls, including file
  writes and command execution. Prefer scoped `permissions.allow` rules
  unless you fully trust the prompt and environment."
- Terminal sandbox: "Sandboxed commands can write to your project folders,
  temporary directories, and common build caches, and read system
  directories … Sensitive files such as `~/.ssh` and `.env` are blocked." On
  macOS it uses `sandbox-exec`. The CLI flag is `--sandbox` ("Run in a
  sandbox with terminal restrictions enabled", `agy --help`). How
  `--sandbox` combines with `--dangerously-skip-permissions` is not spelled
  out; the permissions page says `always-proceed`
  (`--dangerously-skip-permissions`) "take[s] precedence over `auto` mode".
- `toolPermission: "proceed-in-sandbox"` runs sandboxed commands without
  asking and asks for the rest (best practices page): the narrower choice
  for a person at the keyboard.

## Headless mode

- `agy -p "<prompt>"`; `--output-format json` gives `conversation_id`,
  `status`, `response`, `duration_seconds`, `num_turns`, `usage`.
- Second turn: `--conversation <id>` (or `-c` for the latest).
- `agy -p /usage` and `agy -p /model` print the quota and the model.

## Terms that matter for scripting

- FAQ: "Antigravity CLI headless mode (`agy -p`) is intended for direct
  scripting and CI workflows. Wrapping `agy` inside third-party coding
  agents or applications, or automating account rotation, is not supported
  under consumer plans."
- FAQ: "Using third-party software, tools, or services to access
  Antigravity is a violation of our Terms of Service … Such actions can
  result in suspension or termination of your account."
- The tests here call `agy -p` from a shell script; the script was started
  by Claude Code. Whether that counts as "wrapping `agy` inside [a]
  third-party coding agent" is for the owner to judge (README, *For the
  owner*).
