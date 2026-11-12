# Test log: Herdr 0.9.5 with two agents, 2026-11-11

One session, on a Mac (Apple silicon, macOS), from about 20:19 to 20:47
UTC. Times below are UTC, or elapsed from the first prompt (T). Captured
screens are in [`../example/screens/`](../example/screens/), scrubbed of
paths, host name and account details. `$SCRATCH` stands for the temporary
folder the scratch repository lived in.

## Versions

| Program | Version | How read |
|---|---|---|
| Herdr | 0.9.5 (stable channel) | `herdr --version`, `herdr status --json` |
| Claude Code | 2.1.322, model reported "Opus 5.5" | its start-up banner |
| Codex CLI | 0.166.0 (0.167.1 offered), model reported "GPT-6.1-Sol low" | `codex --version`, its footer |

No Herdr integration was installed for the test, so every state below came
from Herdr reading the screen. The detection rules in use were the ones
Herdr downloads from herdr.dev: `agent explain` named a "remote" manifest,
version 2026.10.11.1, for both Claude Code and Codex.

## How it was driven

The test used a **new named session**, `scratch-herdr`, so nothing else on
the machine was touched. Herdr's TUI client was started in a **private tmux
server** of its own (`tmux -L herdrtest`), 200×50, so its screen could be
captured with `tmux capture-pane`. Everything else went through Herdr's own
CLI with `--session scratch-herdr`, which talks to that session's socket and
prints JSON. No keys were sent to any terminal other than this tmux server
and the panes of this session.

```sh
sh example/make_scratch_repo.sh "$SCRATCH/garden"
cd "$SCRATCH/garden"
tmux -L herdrtest new-session -d -s h -x 200 -y 50 "herdr --session scratch-herdr"
herdr --session scratch-herdr worktree create --workspace w1 --branch task-kind --label kind --no-focus
herdr --session scratch-herdr worktree create --workspace w1 --branch task-readme --label readme --no-focus
```

**Finding: worktrees go in your home folder by default.** `worktree create`
made each checkout at `~/.herdr/worktrees/garden/<branch>`, not beside the
repository, and opened each as its own workspace grouped under the
repository in the sidebar. (`--path`, or `[worktrees] directory` in the
config, changes this.) `~/.herdr` was removed at the end.

**Finding: the first-run welcome box.** A new session opened with a welcome
box ("↵ continue"). It was left open on purpose: continuing writes
`onboarding = false` to Herdr's `config.toml` and opens the integrations
settings (Configuration docs). While it was open, `ctrl+b q` did nothing;
no other keys were tried. The CLI worked normally throughout.

## Starting the agents

| When (UTC) | Command (through `herdr agent start <name> --kind <kind> --pane <pane> -- …`) | Herdr said | What the agent was doing |
|---|---|---|---|
| 20:20:39 | `kind`, Claude Code: `--model claude-opus-5-5 --strict-mcp-config` | `agent_not_ready`: "blocked during startup"; `agent get` → `blocked` | Claude's "Is this a project you trust?" dialog. **Right.** `agent explain`: rule `live_blocked_form` |
| 20:20:50 | (answered the dialog with `agent send-keys kind down`, `enter`) | `idle` after about 3 s | At its prompt. **Right** |
| 20:21:14 | `readme`, Codex, with MCP servers disabled by `-c` | `agent_not_ready`, `blocked` | Codex's "Trust this folder?" dialog, which would save the choice in Codex's config. **Right.** Rule `trust_directory`. Quit with `esc` rather than save |
| 20:21:40 | the same, plus `-c projects."<repo>".trust_level="trusted"` | `blocked` | Codex's "Update available" screen. **Right.** Rule `startup_update` (the 0.9.4 changelog's fix) |
| about 20:22 | (skipped the update) | `blocked` | The trust dialog again: the quoted key was not honoured |
| about 20:23 | the same with the key unquoted, `-c projects.<repo>.trust_level=trusted` | `blocked` (update screen), then **`done`** after `esc` | At its prompt; no trust dialog. **Wrong**: a fresh, never-used agent was called `done`, where the docs say start-up does not count as completed work. It stayed `done` until given work |

**Connectors.** The agents' MCP servers and built-in connectors were
disabled where possible, using command-line options only (no configuration
file was edited); one built-in server could not be, and stayed connected
for the run. Neither task used it. Each agent's `/mcp` view was checked
before any prompt.

- Claude Code: `--strict-mcp-config --no-chrome` (the second option was
  needed for a built-in connector that `--strict-mcp-config` alone does not
  turn off).
- Codex: `-c mcp_servers.<name>.enabled=false` for each server in its
  configuration, plus `--disable apps --disable plugins --disable
  computer_use` (shorthand for `-c features.<name>=false`). One built-in
  server is not defined in the configuration file, so `-c` could not reach
  it ("invalid transport").
- Herdr marked Claude Code's `/mcp` menu as **blocked**: a menu, not an
  approval. Blocked means "a dialog Herdr recognises is open", not only "it
  wants permission".

Final start commands:

```sh
herdr --session scratch-herdr agent start kind --kind claude --pane w2:p1 -- \
  --model claude-opus-5-5 --strict-mcp-config --no-chrome --permission-mode default
herdr --session scratch-herdr agent start readme --kind codex --pane w3:p1 -- \
  -c mcp_servers.<name>.enabled=false … \
  -c projects.<repo>.trust_level=trusted \
  --disable apps --disable plugins --disable computer_use
```

Claude Code was started with `--permission-mode default` so that it would
stop and ask before an edit, giving one deliberately blocked agent.

## Two agents, two tasks, at once

Prompts, sent within a second of each other with `herdr agent prompt`:

- `kind`: "Do task 1 in TASKS.md: add total_by_kind to seeds.py and print
  it. Keep it minimal. Do not touch anything else and do not commit."
- `readme`: "Do task 2 in TASKS.md: write README.md, at most five lines. Do
  not touch anything else and do not commit."

States polled once a second with `herdr agent list`, not read off the
sidebar ([`poll-run1.txt`](../example/screens/poll-run1.txt), UTC):

| Elapsed | kind (Claude) | readme (Codex) | What was actually happening |
|---|---|---|---|
| T−1 s (20:41:14) | idle | done | Both at their prompts. Codex's `done` is the start-up error above |
| T+1 s | working | working | Both reading the repository. **Right** |
| T+8 s | **blocked** | working | Claude showing "Do you want to make this edit to seeds.py?" with the diff. **Right**; rule `legacy_no_prompt_blocker` |
| T+17 s | blocked | **done** | Codex had written README.md and stopped ("Worked for 15s"). **Right** |
| T+2 min 0 s | — | — | Edit approved with `agent send-keys kind enter` |
| T+2 min 1 s | working | done | Claude editing, then running `python3 seeds.py; git status --short` (allowed without a prompt). **Right** |
| T+2 min 14 s | done | done | Claude finished ("Churned for 19s"). **Right** |

Every transition during the task matched what the agent was doing, to
within the one-second polling. The deliberately blocked agent was reported
blocked for the whole 1 min 52 s it waited, and the other agent's work
carried on and finished meanwhile.

The sidebar, captured separately with `tmux capture-pane -e` while Claude
waited and Codex had finished
([`04-tui.txt`](../example/screens/04-tui.txt)): Claude's marker red
(RGB 243,139,168), Codex's teal (148,226,213), default theme.

Results, checked by hand: `seeds.py` in the `task-kind` worktree gained
`total_by_kind` and prints "tomato: 12, bean: 38, squash: 5" (right);
`README.md` in `task-readme` has three lines (right; it describes only the
member totals, since the other change was on another branch). The main
checkout was untouched (`git status` clean). See
[`07-claude-diff.txt`](../example/screens/07-claude-diff.txt) and
[`07-codex-README.md`](../example/screens/07-codex-README.md).

## Detach and reattach

- 20:44:55: closed the client by killing its private tmux server (the
  documented "simply close your terminal window"; `ctrl+b q` was not
  available with the welcome box open). `herdr status`: server still
  running; `agent list`: both agents still there, `done`; both agent
  processes still alive (`ps`).
- 20:45:05: while no client was attached, `agent prompt readme "Reply with
  one word: ready. Do not run any commands." --wait` returned `done` in 2 s;
  Codex had answered "ready". Work carries on with nothing attached.
- 20:45:10: a new client, `herdr session attach scratch-herdr`, in a new
  private tmux session: the same workspaces, worktrees and both agents came
  back. The sidebar showed both agents with green hollow markers, while the
  CLI still said `done` for both: the new client did not carry the old
  client's unseen-completion badges, as the Concepts page says ("Each client
  tracks which completions it has displayed").

Not tested: a full server restart with integrations (which is what brings
conversations back after a restart), because installing an integration
writes into the agents' own configuration.

## Clean-up

Both agents exited (`ctrl+c` twice each), both worktrees removed with
`herdr worktree remove --workspace <id> --force` (which also closed their
workspaces), the private tmux server killed, `herdr session stop
scratch-herdr` and `herdr session delete scratch-herdr`, the scratch
repository and `~/.herdr` deleted. No process from the test was left
running.

Side effects of the test: Herdr created entries under `~/.config/herdr/`
for the session (removed by `session delete`) and a `.plugins.lock` file
there; it keeps downloaded detection manifests in `~/.local/state/herdr/`.
Neither agent's trust choice was saved.

## Cost

Three prompts in all: one to Claude Code (19 s of work plus the approval),
two to Codex (15 s and 1 s).
