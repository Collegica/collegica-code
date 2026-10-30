# collegica-code

The code, examples and research notes behind the articles on
[collegica.org](https://www.collegica.org): the scripts that were run, the
examples you can clone and run yourself, and the notes that say what was
checked and how.

Each folder keeps the path it has in the site's own repository, so the links
between files work here as they do there.

## By article

| Article | Folder |
|---|---|
| [Fixed or Variable](https://www.collegica.org/finance/fixed-or-variable/) | [`docs/2026-09-10-fixed-or-variable`](docs/2026-09-10-fixed-or-variable), and the simulator in [`website/static/js/fixed-or-variable`](website/static/js/fixed-or-variable) |
| [Environments Are Not Packages](https://www.collegica.org/python/environments-and-packages/), [Python for Reproducible Research](https://www.collegica.org/python/reproducible-research/) | [`docs/2026-09-12-python-reproducibility`](docs/2026-09-12-python-reproducibility) — the `bocrates` example is in `example/` |
| [One Agent, Four Doors](https://www.collegica.org/ai/agent-interfaces/) | [`docs/2026-09-13-agent-interfaces`](docs/2026-09-13-agent-interfaces) — the `onedoor` example is in `example/` |
| [An Agent in Your Pocket](https://www.collegica.org/ai/edge-agent/) | [`docs/2026-09-13-edge-agent`](docs/2026-09-13-edge-agent) — the Android example is in `example/` |
| [An Agent on Your Own Machine](https://www.collegica.org/ai/local-agent/) | [`docs/2026-09-13-local-agent`](docs/2026-09-13-local-agent) |
| [A Voice in the Room](https://www.collegica.org/ai/voice-agents/) | [`docs/2026-09-13-voice-agents`](docs/2026-09-13-voice-agents) |
| [Sixteen Times Smaller](https://www.collegica.org/ai/turbovec/) | [`docs/2026-09-14-turbovec`](docs/2026-09-14-turbovec) |
| [Videos from HTML](https://www.collegica.org/ai/video-from-html/) | [`docs/2026-09-13-video-from-html`](docs/2026-09-13-video-from-html), and the four explainers' sources in [`video/`](video) |
| [One Repository, Three Agents](https://www.collegica.org/software/three-agents/) | [`docs/2026-09-13-three-agents`](docs/2026-09-13-three-agents) |
| [Train the Robot Before You Build It](https://www.collegica.org/robotics/nvidia-robotics/) | [`docs/2026-09-13-nvidia-robotics`](docs/2026-09-13-nvidia-robotics) |
| [Words In, Joints Out](https://www.collegica.org/robotics/vla-models/) | [`docs/2026-09-13-vla-models`](docs/2026-09-13-vla-models) |
| [A Session You Can Keep](https://www.collegica.org/aging-well/exercise-sessions/) | [`docs/2026-09-13-exercise-sessions`](docs/2026-09-13-exercise-sessions), and the clips' record in [`apps/owl-sessions`](apps/owl-sessions) |
| [The example family](https://www.collegica.org/events/monthly-budget/example) | [`docs/2026-09-26-example-family`](docs/2026-09-26-example-family) |
| [Let It Open the Folder](https://www.collegica.org/ai/desktop-agents/) | [`docs/2026-10-22-desktop-ai`](docs/2026-10-22-desktop-ai) — the receipts test is in `example/` |
| [Whole Life, Inside the Company](https://www.collegica.org/finance/corporate-whole-life/) | [`docs/2026-10-27-corporate-whole-life`](docs/2026-10-27-corporate-whole-life) |
| [All Weather, Rebuilt for Canada](https://www.collegica.org/finance/all-weather/) | [`docs/2026-10-28-all-weather`](docs/2026-10-28-all-weather) — the backtest is in `backtest/` |
| [Train It Before You Use It](https://www.collegica.org/ai/small-business-ai/) | [`docs/2026-10-28-ai-small-business`](docs/2026-10-28-ai-small-business) |
| [Rich, or Just Acting Rich?](https://www.collegica.org/finance/stop-acting-rich/) | [`docs/2026-10-29-stop-acting-rich`](docs/2026-10-29-stop-acting-rich) |
| [The Notebook That Holds the Truth About Your Business](https://www.collegica.org/ai/business-notebook/) | [`docs/2026-10-30-single-source-of-truth`](docs/2026-10-30-single-source-of-truth) — the example business's folder, rulebook and the assistant's wiki are in `example/` |

## For agents

[`okf/`](okf) is the site's knowledge in the
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md),
the same bundle served at [collegica.org/okf/](https://www.collegica.org/okf/index.md).
[`apps/collegica-mcp`](apps/collegica-mcp) serves it, and the mortgage
simulator, over MCP.

## How this repository is made

It is exported from the site's repository on every change there, so its
history is a record of what was published, not of how it was written.
Issues are welcome; a pull request is read and, if taken, carried across by
hand.

## Licence

MIT, in [`LICENSE`](LICENSE). Vendored code keeps its own licence beside it
(three.js, in `docs/2026-09-13-exercise-sessions/example/vendor/three/`).
