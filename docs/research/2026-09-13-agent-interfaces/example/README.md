# onedoor — one agent core, four doors

The worked example from [One Agent, Four Doors](https://www.collegica.org/ai/agent-interfaces/).
A Python package whose core knows nothing about protocols, with four thin
adapters — CLI, REST, MCP, AG-UI — that each translate the same event stream
into one of them. The point is the shape, not the size: 12 source files.

## Run it

```bash
pixi run test          # every door, against the scripted agent — no key, no network
pixi run onedoor "how many words is this"     # the CLI door
pixi run rest          # REST on :8771  → POST /chat, POST /chat/stream
pixi run agui          # AG-UI on :8772 → POST /  (RunAgentInput in, SSE out)
pixi run mcp           # MCP over stdio — add it to Claude Code / Claude Desktop
```

By default the doors are served by `ScriptedAgent`, a deterministic stand-in
that emits every event the core can emit. To put Hermes behind them:

```bash
git clone https://github.com/NousResearch/hermes-agent.git && cd hermes-agent && uv sync
export PYTHONPATH=$PWD            # so `from run_agent import AIAgent` resolves
export OPENROUTER_API_KEY=...     # or the provider key your model needs
export ONEDOOR_AGENT=hermes ONEDOOR_MODEL=anthropic/claude-sonnet-4.6
```

Nothing in `doors/` changes. That is the claim the tests make.

## What is where, and why

| Path | What it is |
|---|---|
| `src/onedoor/core/events.py` | The six internal events. The only vocabulary a door may use. |
| `src/onedoor/core/agent.py` | The port: `Agent.run(message, history) -> Iterator[Event]`, and its contract. |
| `src/onedoor/core/scripted.py` | The deterministic agent the tests run against. |
| `src/onedoor/core/hermes.py` | The Hermes adapter: `AIAgent` callbacks → the event stream, on a worker thread. |
| `src/onedoor/config.py` | Which agent stands behind the doors (`ONEDOOR_AGENT`). |
| `src/onedoor/doors/cli.py` | Terminal: streams deltas; `--json` shows the raw events. |
| `src/onedoor/doors/rest.py` | FastAPI: `/chat` (the shape from Hermes's docs) and `/chat/stream` (SSE). |
| `src/onedoor/doors/mcp_server.py` | The agent as an MCP tool, `ask`. Request/response by nature. |
| `src/onedoor/doors/agui.py` | AG-UI: `translate()` maps core events to AG-UI events; the route streams them. |
| `tests/` | One file per door, one for the core, one for the Hermes bridge with a stand-in `AIAgent`. |

## What the tests prove, and what they do not

They prove that four protocol adapters work end-to-end against the port, that
the AG-UI door emits events in the order the protocol expects, that the MCP
door answers a real client over stdio, and that the Hermes bridge turns
callbacks into the stream and reports failure as an event.

They do not prove a run against a live model. The Hermes adapter is written
against the constructor signature and streaming code in
`NousResearch/hermes-agent` as of September 2026; the two tool callbacks'
argument shapes are undocumented and are passed through unparsed until you
have seen a real one.
