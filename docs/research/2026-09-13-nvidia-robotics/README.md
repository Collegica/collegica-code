# Train the robot before you build it — plan and research

Plan and notes for the first on-site Robotics article: a map of NVIDIA's
robotics and simulation stack — Warp and Newton, Isaac Sim and Isaac Lab,
Cosmos and GR00T, Isaac ROS and Jetson — read from the outside, with the
same four questions asked of each piece: what it is, what it runs on, what
it costs to try, what was verified. Started 2026-09-13.

Audience: someone who knows some Python and wants to learn robotics in
simulation — the Robotics course this site was started for runs in a
browser — and keeps meeting NVIDIA's names without a map of how they fit,
what is free, what is open, and what needs an RTX card.

## What was verified, and how

| Claim | Checked against |
|---|---|
| Every version, release date, Python requirement, wheel platform and PyPI licence field | PyPI's JSON API, queried from this machine — [`notes/stack.md`](notes/stack.md) |
| What each piece is, its requirements, its licence, its install commands | The projects' GitHub READMEs and licence files, read in full (raw `main`); the Isaac Sim 6.0 and Isaac Lab 3.0 announcements on GitHub |
| Warp and Newton run without a GPU, and how fast | Run here on a 4-vCPU container — [`notes/cpu-run.md`](notes/cpu-run.md) |
| Isaac Sim's RAM/disk/driver lines and "no RT cores" rule, the licence FAQ, the WebRTC client, Jetson and DGX Spark prices and specs, GTC 2026, Isaac ROS platforms | Search-result snippets of the vendor's pages, corroborated by retailers and trade press — the vendor's own domains were blocked by this session's egress policy. Marked *(search)* in the notes; lower confidence |

Not verified: anything Isaac Sim, Isaac Lab, GR00T or Cosmos does when it
runs — none of them will start without an NVIDIA GPU, and Isaac Sim has no
macOS build. The article says which sections are documented and which were
run, and does not quote a benchmark it could not reproduce.

## Decisions

1. **The same four questions for every piece**, so the stack reads as a
   table rather than a brochure: what it is, what it runs on, what it costs
   to try, what was verified.
2. **Licences are the story under the story.** Two open engines at the
   bottom (Apache-2.0, Linux Foundation for Newton); a simulator whose
   source is Apache-2.0 but whose wheels are proprietary; models whose code
   is Apache-2.0 and whose weights are the NVIDIA Open Model License; Isaac
   ROS under its own licence. Said plainly, once, in a table.
3. **Date everything.** Isaac Sim, Isaac Lab and Newton ship monthly;
   three version lines are in flight; the article names the day.
4. **Run what can be run.** Warp and Newton on a CPU, timed, with the
   commands — and the honest reading that 10 frames/s is for learning, not
   training.
5. **Write from the machine the reader probably has.** No RTX card, maybe
   a Mac. The last section is the four ways in from there: CPU, rent,
   stream, buy.
6. **No hero yet.** The image was generated (`hero.md`) but its CDN was
   blocked from this session; the article ships without the banner until
   the file is added.

## Traps hit

- `pip index versions isaacsim` under Python 3.11 says 5.1.0.0 is the latest.
  It is not; the 6.x wheels are `==3.12.*` and pip hides what it cannot
  install. PyPI's JSON API tells the whole story.
- Warp refuses a kernel defined in code piped to `python -` ("Directly
  evaluating Warp code defined as a string using `exec()` is not
  supported"); it needs a file.
- GitHub's release pages, read through a summarising fetch, came back with
  the wrong years on their relative dates; every date in the notes is from
  PyPI or from a dated announcement post instead.
- Isaac Lab's `main` README still wears the Isaac Sim 5.1 badge and the
  2.x compatibility table; the 3.0 beta line is a tag and a branch, and its
  requirement (Isaac Sim 6.0) is in the release notes, not the README.
- Isaac ROS is not Apache-2.0; its `LICENSE` is NVIDIA's own. Easy to
  assume otherwise from the rest of the stack.
- `newton[examples]` pulled `mujoco-warp 3.12.0` while PyPI's latest was
  3.13.0 — the pin belongs to Newton, and the notes say so rather than
  quoting the newest number.
- Every NVIDIA domain — docs, developer, newsroom, nvidia.com — plus Hugging
  Face and Wikipedia were blocked by the session's network policy. GitHub
  and PyPI were not, and carry most of what matters; the rest is marked.
