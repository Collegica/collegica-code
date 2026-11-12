# Leads, 2026-11-11

What other people say about Herdr. Each is a lead, not a source: *untested*
until checked here or against `herdrdev/herdr` and herdr.dev, then *passed*
or *failed*. Found with generic web searches (no names of the owner, the
site or the project in any query); pages read with a fetch tool on
2026-11-11.

| Lead | Where | Status | How checked |
|---|---|---|---|
| Herdr is a single Rust binary that runs inside your existing terminal | [Better Stack](https://betterstack.com/community/guides/ai/herdr-ai-agent/) (updated 2026-06-08), [Bitdoze](https://www.bitdoze.com/herdr-agent-multiplexer/) (updated 2026-09-02), [Tecmint](https://tecmint.com/herdr-run-ai-coding-agents-in-linux-terminal) (updated 2026-07-10) | **passed** | GitHub: primary language Rust; ran it inside tmux here |
| Detection is by process name plus what is on screen, no configuration | Tecmint, Bitdoze | **passed** | Agents docs; here, with no integration installed, both agents were recognised and classified from the screen (`agent explain` names the screen rule) |
| Status colours: yellow working, red blocked, blue done, green idle | Tecmint | **partly passed** | Here: blocked red, done teal, idle green (theme catppuccin, default). Working not captured in colour |
| "idle" means no agent running or the shell is idle | Tecmint | **failed** | Concepts: idle is an agent that is "finished or waiting and has been seen". A pane with no agent shows no agent at all |
| `blocked` is what you see at a first-run permission prompt | Better Stack | **passed** | Claude's and Codex's folder-trust dialogs and Codex's update screen all showed blocked |
| Detach with `Ctrl+B` then `D` | Bitdoze | **failed** | README, Quick start and `prefix+?`: detach is `ctrl+b q`. (Could not press it here: see `test.md`) |
| `herdr session kill <name>` | Bitdoze | **failed** | 0.9.5 has `session stop` and `session delete`, no `kill` (`herdr session --help`) |
| `herdr wait --pane 2 --state done`, `herdr pane split --vertical`, `herdr pane split-right` | Bitdoze, Better Stack | **failed** | 0.9.5: `herdr agent wait <name> --until done`, `herdr pane split <id> --direction right`. Their syntax is older or invented |
| Licence AGPL-3.0, commercial licences on request | Bitdoze | **failed** (out of date) | Relicensed Apache-2.0 on 2026-07-22 (LICENSE history); README says Apache-2.0 |
| "No session resurrection yet" | Bitdoze | **failed** (out of date) | Session state docs: layout restore after restart, conversation resume through integrations, 48 snapshots |
| Install with `nix run github:ogulcancelik/herdr` | Tecmint, Bitdoze | **failed** (out of date) | The repository is now `herdrdev/herdr`; the old address redirects. Install docs use `herdrdev` |
| `herdr --remote ssh://you@server:2222` runs the server remotely and draws the UI locally with local keybindings | Tecmint, Better Stack, Bitdoze | **passed from docs**, not run | Persistence and remote access page. Remote use was out of scope (Mac only) |
| Remote mode handles pasted images better than SSH with tmux | Tecmint | **passed from docs**, not run | Docs: local clipboard images are bridged in `--remote`, not when you SSH in and run `herdr` |
| Closing the terminal does not stop running agents | Bitdoze's video notes | **passed** | Closed the client here; both agents kept running and one answered a prompt with nothing attached |
| No built-in sandboxing: agents run with your permissions | Bitdoze | **passed** | Docs and README: Herdr "doesn't wrap or replace" agents; nothing in the docs restricts them. Each agent's own permission prompts still apply (seen here) |
| Rendering slows with 10 or more panes | Bitdoze, citing Hacker News | **untested** | Only three panes here. 0.9.2 and 0.9.4 changelogs claim large CPU cuts |
| A new permission dialog can show as idle while it waits for you | blog roundup in search; Herdr's own docs | **passed from docs and issues** | Agents docs ("fall back to idle"); open issues #5221, #5490, #5593, #5741, #5775. Not reproduced here: every dialog met was recognised |
| Claude Code and Codex have their own parallel sessions; a multiplexer per tab adds little | Hacker News discussion, via a search summary | **untested** (opinion) | Used in the article's "when a plain terminal is enough" as a question, not a fact |
| Herdr M, a macOS desktop app wrapping the same sessions | Bitdoze | **failed** (out of date) | herdr.dev now offers the Herdr app on macOS, Windows and Linux, built on herdr-core; no "Herdr M" there |
| Moshi on iPhone works with Herdr | Bitdoze | **passed from docs**, not run | How to work page names moshi |
| NetworkChuck video: cross-machine and agent-to-agent examples | [summary page](https://www.ai.joaoqueiros.com/blog/herdr-networkchuck-terminal-ai-agents-ssh-worktrees-guide) | **untested** | Video not watched |
| Alejandro AO's "Herdr Crash Course" (2026-08-27) | search result | **untested** | Not watched |
| Reddit or X threads on Herdr itself | generic searches | **none found** | Searches returned blogs and the project's own pages; one Reddit result was about a different tool |
