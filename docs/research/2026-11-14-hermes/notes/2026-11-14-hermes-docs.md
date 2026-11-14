# Hermes's own documentation, read 14 November 2026

Read from the copy installed with Hermes v0.23.1 (the `website/docs/` folder
of the install). The pages have the same names online under
<https://hermes-agent.nousresearch.com/docs/> and loaded (HTTP 200) on the same
day, but the online text was **not read or compared**: it may differ (for
example the sentence about `hermes -z` is in the installed `--help` and was
not found on the online CLI page). Quotations are from the installed copy.

## Context files

Page: `user-guide/features/context-files` and `user-guide/which-file-does-what`.

- "Only **one** project context type is loaded per session (first match wins):
  `.hermes.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` →
  `.cursorrules`." `SOUL.md` is always loaded separately, as the agent's
  identity (slot 1), and only from `HERMES_HOME`.
- `AGENTS.md` is loaded from the working directory at session start. Outside a
  git repository only the working directory is checked, "so an `AGENTS.md`
  planted in `/tmp` or `$HOME` can't leak into unrelated sessions". Inside a
  repository, the files from the git root down to the working directory are
  merged. Files in subfolders are picked up as the agent works there.
- Edits to these files mid-session take effect at the next session (the
  `which-file-does-what` page, not the context-files page).
- Context files are scanned for prompt injection (security page, layer 6).
- Tested: `AGENTS.md` in a fresh folder was read at once; `--ignore-rules`
  switched it off (`notes/test.md`).

## Memory

Page: `user-guide/features/memory`.

- Two files in `~/.hermes/memories/`: `MEMORY.md` (the agent's own notes, 2,200
  characters) and `USER.md` (a profile of you, 1,375 characters). Both are
  injected into the system prompt as a frozen snapshot at session start;
  changes appear next session. The agent writes them itself with the `memory`
  tool; `write_approval` can gate that.
- "Don't point two agent processes at the same Hermes home directory."
- It recommends `/new` at natural boundaries on messaging platforms (it names
  Telegram and Discord), where a chat is one long session.
- "Memory is scoped per profile by design — give a second agent its own
  profile" (the same page's caution about sharing one home).
- Not tested (the memory tool was off in the runs).

## Skills

Page: `user-guide/features/skills`.

- "Skills are on-demand knowledge documents the agent can load when needed",
  compatible with the agentskills.io standard. All live in `~/.hermes/skills/`;
  "The agent can modify or delete any skill."
- Format: a folder with `SKILL.md`, front matter (`name`, `description`,
  `version`, optional `platforms`, `metadata.hermes`) then Markdown.
- Every profile is seeded with a bundled catalogue; `hermes update` adds new
  ones. `hermes skills opt-out` and `hermes profile create --no-skills` give an
  empty set. Third-party installs go through a security scan.
- `-s NAME` preloads a skill for a session.
- Tested once: the house rules as a skill, in 1 of 3 runs a notice was written
  and it followed all six rules; in the other two the agent never read the
  notes (`notes/test.md`).

## Security and permissions

Page: `user-guide/security`.

- Eight layers: user authorisation, dangerous-command approval, file write
  safety, container isolation, MCP credential filtering, context-file scanning,
  cross-session isolation, input sanitisation.
- `approvals.mode`: `smart` (default; a second model judges risk, "genuinely
  dangerous commands are auto-denied", uncertain ones ask), `manual` (always
  ask), `off` (same as `--yolo`).
- `approvals.single_query_mode: deny` (default): a one-shot `-q` session
  refuses a dangerous command because nobody is there to answer. Same
  for cron (`cron_mode`) and webhook sessions (`unattended_mode`).
- A fixed "hardline blocklist" (`rm -rf /`, fork bombs, `mkfs` on a live
  root, writes to block devices) is refused even under `--yolo`. A user list,
  `approvals.deny`, does the same for patterns you choose, checked before
  `--yolo`.
- "Container bypass": under the Docker, Modal and similar backends,
  dangerous-command checks are skipped because the container is the boundary.
  The default `terminal.backend` is `local`.
- `HERMES_WRITE_SAFE_ROOT` (optional): confines `write_file` and `patch` to
  listed folders; credential files and system paths are always denied. It is
  set automatically in the official Docker image.
- An `execute_code` script can bypass the command patterns; messaging
  and API sessions ask once for the whole script.

## Models

Page: `user-guide/configuring-models` (listed, not read in full) and
`reference/cli-commands`. Hermes has no model of its own: `-m` and
`--provider` choose per run; `hermes model` sets the default. Which
provider sees your prompts is then the provider's matter.

## Official domains

Page: `getting-started/official-domains`. The documentation and installers
are served from `hermes-agent.nousresearch.com`; the source is the
`NousResearch/hermes-agent` repository (MIT licence, "Copyright (c) 2025 Nous
Research", per its `LICENSE` file). The page warns of fake "Hermes" sites and
lookalike accounts.

## Not found

No statement about telemetry from Hermes itself (the word appears only for
an unrelated plugin). Not claimed either way.

## OpenRouter (the provider the tested model ran through)

<https://openrouter.ai/docs/guides/privacy/logging>, read 14 November 2026:
each provider on OpenRouter has its own logging and retention policy; "you can
set whether you would like to allow routing to providers that may train on
your data (according to their own policies). There are separate settings for
paid and free models." OpenRouter's own handling of prompts is set out
separately in its privacy policy (<https://openrouter.ai/privacy>, not
read). `https://openrouter.ai/api/v1/models` listed the tested model as
`nvidia/nemotron-3-ultra-550b-a55b:free`, 1,000,000 tokens of context, price 0,
and a paid version `nvidia/nemotron-3-ultra-550b-a55b` at $0.60 per million
input tokens and $2.40 per million output.
