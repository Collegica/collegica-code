# Hermes Agent and Hermes Desktop — checked at the source on 2026-10-22

Builds on `docs/research/2026-09-13-local-agent/notes/` (components, run, serving
options) and the article `website/ai/local-agent/index.md`. That work used
Hermes CLI v0.21.2 and a Desktop build (bundle 0.17.2) that `hermes desktop`
compiled inside the checkout. Facts already recorded there (64K context
minimum, Ollama custom endpoint, profiles, "same config, same keys…") are not
repeated except where they changed.

## Access and confidence

- **Read in full:** the v0.22.0 release notes, pulled as raw text with
  `gh release view v0.22.0 -R NousResearch/hermes-agent` (704 lines); the
  release list with dates (`gh release list`); licence and stars from
  `gh repo view`.
- **Read via a fetch-and-summarise tool (wording close, not guaranteed
  verbatim):** the Desktop docs page, the Desktop product page, the Security
  page, the work-machine guide, the Providers page, the FAQ, the Memory,
  Tools, Skills and Messaging pages, the GitHub README, the releases page,
  Nous Portal's pricing page. Quotes from these are as the tool returned them.
- **Conflict found, not resolved:** the FAQ and work-machine guide still say
  Hermes "does not collect telemetry"; the v0.22.0 notes add an *opt-in*
  shared-metrics switch (default off). See Telemetry below.
- **Stale doc content:** the Providers page still names Claude Opus 4.6 and
  GPT-4o as examples, while v0.22.0 notes mention "the Claude 5.5 / GPT-6
  model wave". The docs lag the code; treat model examples there as old.
- **Not verified:** a Nous blog post on Desktop (none found on the Nous
  site; coverage is press and X posts); anything run on this machine today.

## What it is

- Hermes Agent: Nous Research's open-source agent; README calls it
  self-improving, "creates skills from experience, improves them during use".
  https://github.com/NousResearch/hermes-agent
- Licence MIT (`gh repo view`: "MIT License"); 256,117 stars on 2026-10-22.
  https://github.com/NousResearch/hermes-agent
- Hermes Desktop: "a native app built around the **same** agent you get from
  the CLI and the gateway". https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- Desktop first shipped as a public preview on 2026-06-02 with v0.15.2
  (press, not primary): https://www.marktechpost.com/2026/06/03/nous-research-releases-hermes-desktop-a-native-cross-platform-front-end-for-hermes-agent-v0-15-2-with-streaming-tool-output/

## Price

- Product page: "free to download and use", MIT. https://hermes-agent.nousresearch.com/desktop
- FAQ: "You pay only for the LLM API usage from your chosen provider."
  https://hermes-agent.nousresearch.com/docs/reference/faq
- Nous Portal (optional provider) plans: Free (free models only, $0 credits);
  Plus $20/mo ($22 credits); Super $100/mo ($110); Ultra $200/mo ($220);
  top-ups $10–$200; can also "Use your ChatGPT plan". https://portal.nousresearch.com/
- New in v0.22.0: a first desktop install gets a free trial model,
  `nous/welcome`, "once per OS user", for onboarding only; CLI/TUI/gateway
  get no free model. Free-tier users see a Terms and Privacy notice.
  https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0

## Install (as of v0.22.x)

- Product page downloads: macOS DMG (page says macOS 12+), Windows installer,
  Linux via terminal install. https://hermes-agent.nousresearch.com/desktop
- **Changed in v0.22.0 (2026-10-13/14):** Desktop is now "a sealed, signed
  package that carries its own Python and Node", so "first launch builds
  nothing" — the Sept article's "`hermes desktop` builds the app on first
  launch" is out of date. Windows: signed MSIX (x64, ARM64) via App Installer
  or the Microsoft Store, **Windows 11 22H2 or newer**, NSIS/MSI installers
  gone. macOS: signed, notarized, **Apple Silicon only** in default builds.
  https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0
  (Note the product page's "Windows 10/11" and "macOS 12+" may be stale
  against this.)
- CLI: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
  (Linux, macOS, WSL2); Windows PowerShell `iex (irm
  https://hermes-agent.nousresearch.com/install.ps1)`; Termux on Android.
  https://github.com/NousResearch/hermes-agent
- New `hermes pm` package manager: pinned, hash-checked environments; an
  update switches only once it passes its check. Python 3.14 for managed
  installs. Source installs follow tagged SemVer releases by default since
  v0.21.7 (2026-10-12). https://github.com/NousResearch/hermes-agent/releases
- macOS file access: the app prompts for Desktop/Downloads/Documents or needs
  Full Disk Access; `hermes doctor` reports permissions.
  https://hermes-agent.nousresearch.com/docs/user-guide/desktop

## Tools for local files

- Toolsets include `terminal`, `file`, `browser`, `web`, `vision`,
  `memory`, `session_search`, `skills`, `code_execution`, `delegation`,
  `clarify`, `cronjob`; enable per run with `hermes chat --toolsets
  "web,terminal"` or interactively with `hermes tools`.
  https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
- File tools: `read_file`, `write_file`, `patch`. Terminal backends: local,
  Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox. Browser:
  `browser_navigate`, `browser_snapshot`, `browser_vision`. Same page.
- Desktop UI: drag-and-drop attachments, a file browser for the working
  directory, an artifact gallery, a preview rail, a Git review pane and
  worktrees, a terminal pane. https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- v0.22.0: ~19 rarely used tools now load only on search, "roughly halving
  the desktop tool schema" — relevant to local models' context.
  `browser_exec` drives bundled Chromium. Browser can sign in via 1Password,
  Bitwarden or Hermes's vault and "the model never sees the password".
  https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0

## Memory and skills

- Memory: two files in `~/.hermes/memories/` — `MEMORY.md` (2,200 chars) and
  `USER.md` (1,375 chars) — injected "as a frozen snapshot at session start";
  no auto-compaction, a write over the limit errors. `session_search` gives
  full-text search over past sessions in SQLite. External providers (Honcho,
  Mem0, Supermemory, …) via plugins (moved to catalog plugins in v0.22.0).
  https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Skills: `SKILL.md` folders in `~/.hermes/skills/`, compatible with the
  agentskills.io standard; progressive loading; the agent creates and patches
  skills with `skill_manage`; hub sources include skills.sh, GitHub,
  `/.well-known/skills/index.json`; hub installs are security-scanned.
  https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- v0.22.0: "learnings and corrections go into the task's skill";
  `skills.auto_load` pins skills into every session; unused agent skills
  archive after 30 days (was 90); `hermes sync` removed.
  https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0

## Permission and approval model

- Three approval modes for dangerous commands: **Smart** (default — an
  auxiliary LLM auto-approves low-risk, escalates uncertain), **Manual**
  (always prompt), **Off** (= `--yolo`). A hardline blocklist (`rm -rf /`,
  fork bombs, block-device writes) applies even in YOLO.
  https://hermes-agent.nousresearch.com/docs/user-guide/security
- Writes blocked to `~/.ssh/`, `~/.aws/`, `/etc/sudoers`, Hermes `.env` and
  `auth.json`; optional `HERMES_WRITE_SAFE_ROOT` confines writes to chosen
  directories. Same page.
- Docker backend: `--cap-drop ALL`, no-new-privileges, pids limit; dangerous-
  command checks are skipped there because "the container itself serves as
  the security boundary" (paraphrase). Same page.
- Context files (AGENTS.md, .cursorrules, SOUL.md) are scanned for injection
  patterns; MCP subprocesses get credentials stripped from env. Same page.
- Work-machine guide: `approvals: mode: manual`; `approvals: deny` glob
  rules (e.g. `git push --force*`) override everything.
  https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
- v0.22.0: cloud-metadata fetches, zsh/dash pipe-to-shell and `deno eval`
  now need approval; `approvals.deny` works in sandboxes; owner-only file
  permissions on credentials and `state.db`. v0.22.4 (2026-10-21): the
  Desktop approval-mode chip follows the active profile.
  https://github.com/NousResearch/hermes-agent/releases

## Model providers

- Cloud: Nous Portal ("recommended", 300+ models, one OAuth login),
  OpenRouter, Anthropic (key, or OAuth only on Claude Max with extra
  credits), OpenAI/ChatGPT (key or OAuth), Google Gemini, GitHub Copilot,
  plus xAI, DeepSeek, Qwen, Kimi, Bedrock, NVIDIA NIM and 25+ others.
  https://hermes-agent.nousresearch.com/docs/integrations/providers
- Local: Ollama (`http://localhost:11434/v1`), vLLM (`:8000/v1`), llama.cpp
  server (`:8080/v1`, needs `--jinja` for tool calls), LM Studio (first-class
  provider), SGLang (`:30000/v1`); all need 64K+ context. Same page.
- **New in v0.22.0 — built-in local runtime:** "run open models entirely on
  your machine with nothing leaving it: no account, no API key". Hermes
  installs and maintains llama.cpp (CPU, CUDA, Metal, Vulkan, ROCm), rates
  catalog models against your GPU and RAM, picks the best fit. Settings →
  Providers → Local Models, or `hermes model` → Local models. Catalog: Qwen3.8
  27B, Qwen3.8 Flash Next, Qwen3.6 35B-A3B, DeepSeek V4 Flash, any Hugging Face
  GGUF. (No Gemma 4 named in the catalog list; any GGUF works.)
  https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0
- v0.22.2 (2026-10-15): long local-model turns "survive on laptops" via
  stall-timer and compression fixes. https://github.com/NousResearch/hermes-agent/releases

## Telemetry and privacy

- FAQ: "Hermes Agent does not collect telemetry, usage data, or analytics";
  data in `~/.hermes/`; API calls go "only to the LLM provider you
  configure". https://hermes-agent.nousresearch.com/docs/reference/faq
- **But** v0.22.0 adds "Opt-in shared metrics — daily usage stats reach Nous
  only with consent"; both `telemetry.shared_metrics` switches default off,
  each profile asks once, Enter = "No thanks". Failure reasons are recorded
  "with opt-in telemetry". https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0
  → For the article: say telemetry is off unless you say yes at the prompt.
- Data does go to Nous when you use Nous services: Portal models, the free
  `nous/welcome` trial, and Connectors (Linear, Notion via "the Nous tool
  gateway"; first use creates "a free connectors-only identity"; connector
  tools "can also send your local files as attachments"). Off switches:
  `nous.guest: false`, `tools.connectors.enabled: false`. Same release.

## Messaging gateway

- 25+ platforms: Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email,
  Home Assistant, Mattermost, Matrix, iMessage (BlueBubbles), Microsoft
  Teams, LINE, Google Chat, IRC and others.
  https://hermes-agent.nousresearch.com/docs/user-guide/messaging
- Default deny: "the gateway denies all users who are not in an allowlist or
  paired via DM"; pairing codes expire after an hour. Same page.
- v0.22.0: "One gateway per machine is the default"; idle/daily session
  resets removed (use `/new`). Bot Screen streams a Linux gateway bot's
  desktop into Hermes Desktop so you can take over at a login or CAPTCHA.

## What changed since 2026-09-13 (v0.21.2 → v0.22.4)

Releases: v0.21.3 (09-14), v0.21.4 (09-21), v0.21.5 (09-24), v0.21.6 (10-08),
v0.21.7 (10-12), **v0.22.0 "The Threshold Release" (10-13/14)**, v0.22.1
(10-14), v0.22.2 (10-15), v0.22.3 and v0.22.4 (10-21). (`gh release list`)

1. Signed, self-contained Desktop packages; no build on first launch; Windows
   11 22H2+ MSIX and Microsoft Store; macOS Apple Silicon only.
2. Guided onboarding chat on a free `nous/welcome` trial model.
3. One-click local models via a managed llama.cpp runtime — the local path
   no longer needs Ollama at all.
4. Connectors (Linear, Notion…) through a Nous gateway; Connectors page
   replaces the MCP tab.
5. Opt-in telemetry prompt (default off).
6. v0.21.5: Simple/Advanced UI modes; French, German, Spanish catalogs;
   RTL/LTR text direction. v0.21.6: security fixes (dashboard auth, git
   filter programs in untrusted repos blocked), live transcription.
7. Codebase cut about a third (1.06M → 698K lines); tool renames
   (`todo` → `todo_list`, etc.; old names still work).
https://github.com/NousResearch/hermes-agent/releases
