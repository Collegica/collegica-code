# Leads

Practices met while reading, not stated as a practice in the documentation and
not reproduced; each stays *untested* unless marked.

| Lead | Where it came from | Status |
|---|---|---|
| Run `/new` at natural boundaries so the memory snapshot refreshes | Memory page; stated by Hermes's documentation, so it can go in the guide as the vendor's advice | not tested (needs the interactive app) |
| Put personality and tone in `SOUL.md`, project rules in `AGENTS.md`, and let the agent write `USER.md` | `which-file-does-what` | the `AGENTS.md` half passed (probe, `notes/test.md`); the others untested |
| Set `approvals.deny` patterns so `--yolo` still cannot run, for example, `git push --force*` | Security page | untested |
| Run the terminal in Docker (`terminal.backend: docker`) to confine it to a container | Security page | untested |
| Use `--safe-mode` to tell whether a problem comes from your set-up or from Hermes | `hermes --help` | untested |
| A rules file makes a model more likely to give up without reading the files | seen on the free model (6 of 9 runs with a rules file or skill, 0 of 3 without); **not seen on Terra** (0 of 9 runs with a rules file or skill gave up) | not reproduced on Terra; the cause on the free model may be a Hermes search quirk (below) |
| `search_files` with pattern `.` and target `files` returns nothing in a non-empty folder | first call of every free-model give-up run | a possible tool quirk, not tested on its own |

No tips from X, Reddit or YouTube were collected for this guide.
