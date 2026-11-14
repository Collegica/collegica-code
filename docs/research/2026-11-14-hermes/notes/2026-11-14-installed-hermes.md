# The installed Hermes, read 14 November 2026

Read-only commands only (`--version`, `--help`, `hermes config get`,
`hermes tools list`, `hermes status`). Nothing in the tester's Hermes folder
was changed. The tests used a separate, empty data root; the only thing copied
into it was the sign-in for the provider under test (see `notes/test.md`),
deleted afterwards.

| What | Found |
|---|---|
| Version | Hermes Agent v0.23.1 (2026.9.24), stable, "Up to date"; installed from git; Python 3.14.9 |
| The tester's default model | a free model on OpenRouter, `nvidia/nemotron-3-ultra-550b-a55b:free` (`hermes config get model`). Used for the first set of runs, in `notes/test-free-model.md` |
| Default approvals | `mode: smart`, `single_query_mode: deny`, `cron_mode: deny`, `unattended_mode: deny`, `approvals.deny: []` |
| Terminal backend | `local` (not Docker or another sandbox), so the terminal runs as the tester's user |
| Toolsets enabled for the CLI by default | web, browser, terminal, file, code_execution, vision, image_gen, video_gen, tts, skills, todo, kanban, memory, context_engine, session_search, connections, clarify, delegation, cronjob, computer_use. Off by default: video, x_search, stt |
| Memory | `memories/MEMORY.md` and `USER.md` under the Hermes data root; limits 2,200 and 1,375 characters (memory page) |

## The command line

`hermes --help` lists, among others: `chat`, `model`, `setup`, `gateway`,
`send`, `cron`, `webhook`, `kanban`, `skills`, `tools`, `mcp`, `connectors`,
`sessions`, `memory`, `approvals`, `security`, `dashboard`, `serve`,
`desktop`, `acp`, `profile`, `update`, `uninstall`.

Flags used or relevant to the guide (from the installed `hermes --help` and
`hermes chat --help`; the online CLI page was not checked for the same text):

- `-z PROMPT` scripted one-shot: "Tools, memory, rules, and AGENTS.md in the
  CWD are loaded as normal; approvals are auto-bypassed." `--usage-file` works
  with `-z` only.
- `chat --oneshot -q` / `--query-file`: answer and exit; `--format
  stream-json` for events; `--in DIR`; `-m`, `--provider`; `-t TOOLSETS`;
  `-s SKILLS`; `--resume SESSION_ID`; `--yolo`; `--max-turns`;
  `--run-budget SECONDS`.
- `--ignore-user-config`: ignore `config.yaml`, "credentials in .env are still
  loaded".
- `--ignore-rules`: "Skip auto-injection of AGENTS.md, SOUL.md, .cursorrules,
  memory, and preloaded skills."
- `--safe-mode`: disable user config, AGENTS.md and memory, plugins and MCP
  servers.
- `HERMES_HOME` selects the data root (the installation page says so). A new
  one is prepared on first use: Hermes installed its own Python dependencies
  there (about 1.1 GB) and seeded `SOUL.md`, skills and an empty `memories/`.

## Model names

The model catalogue Hermes uses (`https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`,
fetched 14 November 2026) lists `openai/gpt-6.1-terra` for OpenRouter and Nous.
Hermes's own list of models for its `openai-codex` provider (ChatGPT sign-in),
in `hermes_cli/codex_models.py` of the installed copy, names **`gpt-5.6-terra`**
(also `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-luna`, `gpt-5.5`,
`gpt-5.4`, `gpt-5.4-mini`). The second is the one used for the Terra runs; a
test call with `--provider openai-codex -m gpt-5.6-terra` answered
"Model: gpt-5.6-terra" and the stream's first event reported the same name.
