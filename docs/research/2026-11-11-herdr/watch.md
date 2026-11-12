# What to check each month

Last checked 2026-11-11, against Herdr 0.9.5.

| What | Where | What to look for |
|---|---|---|
| Releases feed | <https://github.com/herdrdev/herdr/releases.atom> | A stable release after v0.9.5 (ignore "Preview build" pre-releases unless the article mentions the preview channel) |
| Changelog | <https://github.com/herdrdev/herdr/blob/master/CHANGELOG.md> | Anything under *Unreleased* or a new version touching agent detection, blocked/idle, session restore, worktrees, remote, install commands |
| Current stable version | <https://herdr.dev/llms.txt> (first line) | "Current stable release: …" |
| Supported agents | <https://herdr.dev/tui/docs/agents/> | Agents added or dropped; "less tested" notes |
| Session restore table | <https://herdr.dev/tui/docs/session-state/> | Minimum integration versions for Claude Code and Codex |
| Remote use | <https://herdr.dev/tui/docs/persistence-remote/>, <https://herdr.dev/tui/docs/connecting-machines/> | Supported host platforms, `--remote` behaviour |
| Detection bugs | <https://github.com/herdrdev/herdr/issues?q=is%3Aissue+is%3Aopen+blocked> | Open reports of dialogs shown as idle for Claude Code or Codex |
| The app and herdr-core | <https://herdr.dev/>, <https://github.com/herdrdev/herdr-core>, <https://github.com/herdrdev/herdr-app> | Whether the terminal program (Herdr TUI) is still maintained, or is being replaced |
| Blog | <https://herdr.dev/blog/> | Announcements that change what the article says |
| Licence | <https://github.com/herdrdev/herdr/blob/master/LICENSE> | Still Apache-2.0 |
