# Gemini CLI and Antigravity CLI: notes

Read 2026-11-11. Google's documentation pages were downloaded and read as
their own text (HTML stripped); the Antigravity pages, which are built in the
browser, were read through a summarising fetch and are marked so. Quotations
are exact unless marked as a summary.

## Gemini CLI no longer serves personal Google accounts

<https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals>
("Gemini Code Assist consumer accounts"), read 2026-11-11, page "Last updated
2026-10-09 UTC":

- "Starting June 18, 2026, Gemini Code Assist IDE extensions stopped serving
  requests for the Gemini Code Assist for individuals, Google AI Pro, and
  Google AI Ultra tiers. This also applies to usage of Gemini CLI. As part of
  the deprecation, you can no longer use the Login with Google option to
  access the IDE extensions or Gemini CLI."
- "Users of Gemini Code Assist consumer accounts on both Gemini Code Assist
  IDE extensions and Gemini CLI can migrate to the Antigravity family of
  products."
- Standard and Enterprise subscriptions "are subject to a separate
  deprecation schedule".

<https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/>,
dated 19 May 2026, read 2026-11-11:

- "On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will
  stop serving requests for Google AI Pro and Ultra, as well as those using it
  free of charge using Gemini Code Assist for individuals."
- "While there won't be 1:1 feature parity right out of the gate, we made sure
  Antigravity CLI keeps the most critical features of Gemini CLI: Agent
  Skills, Hooks, Subagents, and Extensions (now as Antigravity plugins)."
- Antigravity CLI is "Built in Go" and "shares the same agent harness as
  Antigravity 2.0, the new Antigravity desktop application".
- Standard and Enterprise licences: "your access remains unchanged … Gemini
  CLI will remain accessible via paid Gemini and Gemini Enterprise Agent
  Platform API keys."

The Gemini CLI README, <https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md>,
read 2026-11-11, opens with a box headed "Read before installing":

- "No free tier or Google AI plans: Free individual access and Google AI Pro /
  Ultra (Google One) moved to Antigravity CLI on June 18, 2026".
- "Not optimized for Gemini 4+: Not tuned for the Gemini 4 series".
- "Not for model benchmarks: Don't use Gemini CLI to benchmark Gemini
  models—its harness isn't tuned for Gemini 4+ and produces unrepresentative
  scores."
- Its table: Antigravity CLI (`agy`) for "free / Google AI Pro & Ultra
  accounts"; Gemini CLI for organisations with Code Assist Standard or
  Enterprise, "plus legacy paid API / Vertex keys".
- Sign-in options still listed: Google sign-in with a paid Code Assist
  licence, a Gemini API key (`GEMINI_API_KEY`), or Vertex AI.

Releases, read through the GitHub API on 2026-11-11: Gemini CLI latest
**v0.68.0** (published 2026-11-10); the Mac here has **0.38.2**.
Antigravity CLI (`google-antigravity/antigravity-cli`) latest **1.5.6**
(published 2026-11-11); the Mac here has 1.5.6 (`agy --version`).

## The instruction file: GEMINI.md

<https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md>,
read 2026-11-11:

- "Context files, which use the default name `GEMINI.md`, are a powerful
  feature for providing instructional context to the Gemini model."
- "Instead of repeating instructions in every prompt, you can define them once
  in a context file."
- Loaded from `~/.gemini/GEMINI.md` (all projects), from `GEMINI.md` in the
  workspace and its parent folders, and "just-in-time" from folders a tool
  touches. The CLI "concatenates the contents of all found files, and sends
  them to the model with every prompt."
- `/memory show` displays what was loaded; `/memory reload` re-reads.
- The name can be changed in `settings.json`, `context.fileName`, for example
  `["AGENTS.md", "CONTEXT.md", "GEMINI.md"]`.

Antigravity CLI migration guide, <https://antigravity.google/docs/cli/gcli-migration>,
read 2026-11-11 through a summarising fetch (the page is built in the
browser), no date on the page:

- On instruction files: "No modifications are needed to your existing rule
  documents"; the agent keeps applying `GEMINI.md` and `AGENTS.md` in the
  workspace, and `~/.gemini/GEMINI.md` globally.
- The command is `agy`. On first run it "automatically detects your existing
  profiles"; extensions are imported with `agy plugin import gemini`.
- MCP servers move out of `~/.gemini/settings.json` into
  `~/.gemini/config/mcp_config.json` (global) and `.agents/mcp_config.json`
  (workspace). Workspace skills move from `.gemini/skills/` to
  `.agents/skills/`.

## Headless mode (for the tests)

<https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/headless.md>,
read 2026-11-11: headless mode is "triggered when the CLI is run in a non-TTY
environment or when providing a query with the `-p` (or `--prompt`) flag";
`--output-format json` returns `response`, `stats` and `error`;
`stream-json` has an `init` event with "Session metadata (session ID,
model)".

`gemini --help` (0.38.2), read 2026-11-11: `-m/--model`; `-p/--prompt`;
`--approval-mode default|auto_edit|yolo|plan`; `--allowed-mcp-server-names`;
`-e/--extensions` ("If not provided, all extensions are used"); `-r/--resume`
("latest" or an index); `-o/--output-format text|json|stream-json`. There is
no flag to switch off agent skills.

`agy --help` (1.5.6), read 2026-11-11, for comparison: `-p/--print`,
`--model`, `--mode accept-edits|auto|plan`, `--conversation <id>` and
`-c/--continue`, `--output-format json`, `--settings` ("Settings for this
session only, never saved"), `--effort`, `agy models`, `agy mcp
… enable, disable`. No flag names MCP servers to exclude for one run; whether
`--settings` can do it was not checked.

## Antigravity pricing

<https://antigravity.google/pricing>, read 2026-11-11 through a summarising
fetch, no date on the page: "Individuals: $0/month" with "Basic weekly rate
limits"; Google AI Pro "More rate limits", Ultra "Even more rate limits", both
with a "Flexible AI credit pool"; business through Google Cloud,
"Standard/Plus plans starting at $30 USD per seat per month". Antigravity
itself is covered in the site's *One Repository, Three Agents*.
