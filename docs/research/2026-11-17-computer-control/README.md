# Directing Claude Code from another assistant: trials

Run 17 November 2026 on one Mac. Follows the research note
[`2026-11-12-computer-control`](../2026-11-12-computer-control/README.md),
which listed six trials. Four were run (parts of 1, 3 and 6, below); the rest
need accounts or machines this session could not use.

## What was run

One scratch folder per coordinator, each holding `sample.csv` (three rows,
total 78.25). Each coordinator was asked to have Claude Code (`claude`,
2.1.326) write `total.py`, run it, and report the command, Claude's words, the
output and the changed files. The briefs are in `example/`.

| Coordinator | Version and model | Result |
|---|---|---|
| Codex CLI | 0.166.0, `gpt-6.1-sol`, low effort | run 1 stopped: Claude "Not logged in". Run 2 (network and `~/.claude` writable) stopped: Claude's own permission check refused to write. Run 3 (brief adds `--permission-mode acceptEdits`): worked, 78.25 |
| Grok Build | 1.0.70, `grok-4.6-build` | headless stopped: "a headless run cannot ask for approval" (twice, once with `--allow` rules). With `--permission-mode auto`: worked, 78.25, about 2 minutes |
| Hermes Agent | v0.23.2, ChatGPT Terra (`gpt-5.6-terra`) | worked first time, 78.25, about 1 minute |
| Claude Code via `hc` to a new Antigravity terminal | Gemini 3.8 Flash, auto mode | stopped at the trust-folder dialog until the owner approved it; then worked, 78.25 (`example/results/antigravity/`) |
| Claude Code (this Mac) to Claude Code 2.1.325 on a second computer (Linux under WSL2), `hc exec --on`, `--permission-mode acceptEdits` | worked; the remote Claude could not run the program without approval and said so; I ran it there: 78.25 (`example/results/atlas/`) |

Independent check: each `total.py` was run by hand on `sample.csv` and printed
78.25 (12 x 2.50 + 2 x 14.00 + 3 x 6.75). All three files are in `example/results/`.

Continue or fresh (Hermes asked both): with `claude -p --continue` Claude
remembered writing `total.py`; as a new session it said it had no record, but
found the file in the folder and described it.

## Settings used, and why

- Codex: default `workspace-write` sandbox. Run 2 and 3 added
  `sandbox_workspace_write.network_access=true` and `~/.claude` as a writable
  root. I did not test which of the two cleared "Not logged in". `--dangerously-bypass-approvals-and-sandbox` was not used.
- Grok: `--always-approve` was not used. `--allow 'Execute(...)'` was rejected
  (`unknown tool prefix`); `--allow 'Bash(...)'` was accepted but did not
  match, because Grok ran several commands joined together.
- Hermes: empty data root with only the ChatGPT sign-in copied (refresh token
  blanked), deleted afterwards; `-t file,terminal,todo`; the same set-up as
  the Hermes guide. `--yolo` and `-z` not used.
- Claude Code: `--permission-mode acceptEdits` in a scratch folder only.
- One run per route. Each brief named the command to start Claude, so this
  shows the handoff works when the route is given, not that an assistant
  finds it alone.

## Not tested

Grok Bot, ChatGPT Work or Computer Use, connected hosts, SSH projects; a
the host going offline (not disconnected, since other work uses that machine);
local versus cloud marker file. The first group needs the owner's accounts.

## For the owner

- Claude's sign-in notice in the runs said the sign-in ends between 21 and 24
  November 2026; it was removed from the saved logs. Renew with `claude auth login`.
- The Codex and Hermes runs used your ChatGPT sign-in; Grok used its own
  sign-in; Claude used yours. Small runs (Codex about 200,000 input tokens,
  mostly cached; Grok reported a cost of 0.04 US dollars for the stopped run and 0.14 for the run that worked).
- Paths in the saved logs are neutralised: `<scratch>`, `<home>`.
