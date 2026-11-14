# Watch list: Hermes Agent

Addresses to read at each monthly check. Last read 14 November 2026
(Hermes Agent 0.23.1). The docs are also installed with Hermes, under
`~/.hermes/hermes-agent/website/docs/`; `hermes --version` and `hermes update`
say whether the installed copy is current.

| What | Address | Why |
|---|---|---|
| Docs index | <https://hermes-agent.nousresearch.com/llms.txt> | new pages |
| Releases | the `releases` page of the `NousResearch/hermes-agent` repository on GitHub | version number, new flags, changed defaults |
| Security and approvals | <https://hermes-agent.nousresearch.com/docs/user-guide/security> | approval modes, `single_query_mode`, `HERMES_WRITE_SAFE_ROOT`, the hardline blocklist |
| Context files | <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files> | which instruction files are read, priority order |
| Which file does what | <https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what> | SOUL.md, USER.md, MEMORY.md, AGENTS.md |
| Memory | <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory> | limits, where memory lives, write approval |
| Skills | <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills> | skill format, preloading with `-s` |
| CLI reference | <https://hermes-agent.nousresearch.com/docs/reference/cli-commands> | `-z`, `chat --oneshot`, `--ignore-rules`, `--safe-mode` |
| Official domains | <https://hermes-agent.nousresearch.com/docs/getting-started/official-domains> | where to download from; impersonation warnings |
| Models and providers | <https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models> | which providers are built in |
| Hermes model catalogue | <https://hermes-agent.nousresearch.com/docs/api/model-catalog.json> | model names per provider (the Terra runs used `gpt-5.6-terra` from the `openai-codex` list in the installed copy, `hermes_cli/codex_models.py`) |
| OpenRouter, data policy | <https://openrouter.ai/docs/guides/privacy/logging> | the free-model comparison ran through OpenRouter; training settings |
| OpenRouter model page | <https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free> | whether the free comparison model is still offered |
