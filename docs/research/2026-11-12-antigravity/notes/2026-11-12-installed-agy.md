# The installed `agy`, its account, and what loads

Checked 12 November 2026, about 01:30 to 01:50 UTC, on the owner's Mac, read
only. Paths shortened to `~/`.

| Check | Command | Result |
|---|---|---|
| Version | `agy --version` | `1.5.6` |
| What it is | `agy --help`; `agy changelog`; antigravity.google | Google's Antigravity CLI, the successor to Gemini CLI (see `2026-11-12-antigravity-cli.md`) |
| Signed in | `agy models` | lists models for the account, so signed in |
| Models offered | `agy models` | gemini-3.8-flash-high, -medium, -low; claude-sonnet-4-6; claude-opus-4-6-thinking; gpt-oss-120b-medium |
| Default model | `agy -p /model` | `gemini-3.8-flash-high`; `~/.gemini/antigravity-cli/settings.json` holds no `model` key, so this is the account's default, not a choice the owner made |
| Plan | owner, 12 November 2026 | **Google AI Pro** (benefits page pasted by the owner: "Entry rate limits to advanced models, including Gemini 4 Argon and Opus 5.5, in Google Antigravity"). The CLI's model list instead matches the "Free & Google AI Plus" column (Gemini 3.8 Flash, Claude 4.6, GPT-OSS; no Gemini 4, no Claude 5.5). Google's Models page reserves Argon and Claude 5.5 on Pro for paid, non-trial subscriptions. Checked in the browser at the owner's request (12 November, about 02:25 UTC): the Google One page of the account `agy` is signed in to shows "Current plan Google AI Pro (5 TB)", a long-standing paid membership, not a trial. `agy models` run again then still listed only the Free and Plus models, and `/usage` showed only weekly limits, not the five-hourly refresh the Plans page gives Pro. Unresolved: why Antigravity does not see the Pro plan |
| Quota | `agy -p /usage` | Gemini models 90% of the weekly limit remaining, resetting 2026-11-18T17:41:11Z; Claude and GPT models 100% |
| Auto mode | `agy -p … --mode auto` | stderr: "--mode auto is not available for this account; continuing in the default mode." |

## Connectors and instruction files

- `agy mcp list`: "No MCP servers configured."
- `agy plugin list`: "No plugins installed."
- `~/.gemini/config/mcp_config.json` and `~/.gemini/GEMINI.md`: empty files.
- Unlike Grok Build, Antigravity's docs mention no reading of Claude Code's
  or Cursor's files; its global rule files live under `~/.gemini/`.
- **Tools check** (headless, before any task): asked to list every tool it
  can call, it named 13 (`run_command`, `read_file`, `edit_file`,
  `write_file`, `ask_question`, `search_web`, `schedule`, `manage_task`,
  `invoke_subagent`, `manage_subagents`, `define_subagent`, `send_message`,
  `swarm`) and said "Direct MCP tools: None are currently registered or
  active". It added that a subagent could be given MCP tools
  (`EnableMCPTools`), but none are configured. Output:
  `../example/results/toolcheck/`.
- **Instruction file check:** in a fresh test folder with the house rules
  saved as `AGENTS.md`, a headless run asked to quote its project rules
  quoted them in full. Unlike Grok Build, no folder trust was needed. Output:
  `../example/results/rulescheck/`.

## Quota, measured

| When (UTC) | Gemini weekly remaining |
|---|---|
| Before anything | 90% |
| After the tools and rules checks | 89% |
| After three task-1 plain runs, run in parallel | 72% |

So about 6% of the weekly limit per run of the task (109,038 to 180,456
tokens each). Two of the three runs hit "RESOURCE_EXHAUSTED (code 429): You
have exhausted your capacity on this model" partway through, yet finished
with a full answer. Testing stopped there, with the owner's agreement: the
remaining 27 runs would have needed about 160% of a week.

At about 02:25 UTC the Gemini weekly remaining read **54%**, down from
72% at 01:50 UTC, with no run made from here in between. The quota is
shared with the Antigravity app and IDE on the same account.

## Later on 12 November: the Pro plan appears, then goes

- About 03:14 UTC: `agy models` listed Gemini 4 Argon (low, medium, high),
  Gemini 3.8 Flash, Claude Opus 5.5 and Sonnet 5.5 (low, medium, high) and
  GPT-OSS; `agy -p /model` gave `gemini-4-argon-medium`; `/usage` showed
  weekly and five-hour limits for Gemini and for Claude and GPT, and a
  "Gemini 4 Argon Weekly Limit", all at 100%.
- `--mode auto` still "not available for this account".
- 03:42 UTC, after the thirty runs: `agy models` listed the six free-tier
  models again, `agy -p /model` `gemini-3.8-flash-high`, and `/usage` one
  Gemini weekly line at 33% (reset 2026-11-18T17:41Z) and one Claude and
  GPT line at 100%.

