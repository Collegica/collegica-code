# One agent, four doors — plan and research

Plan and working notes for the first on-site article in the [AI
section](https://www.collegica.org/ai/). Started 2026-09-13. Audience: engineers who
have an agent working in one place — a script, a CLI, a notebook — and are
being asked to make it available in several.

Prompted by a two-minute screencast, *Hermes Agent: Use Hermes as a Python
Library* (ActionableOps, [youtu.be/X13ZtyNKB0I](https://youtu.be/X13ZtyNKB0I)),
and by a question it raised: **can one Python package expose an agent as a CLI,
a REST endpoint, an MCP server, an AG-UI backend and "AGP", written once?**

## What was verified, and how

Everything the article asserts about the four systems was checked against the
systems, not against memory. Details in [`notes/hermes.md`](notes/hermes.md)
and [`notes/protocols.md`](notes/protocols.md). The short form:

| Claim | Checked against |
|---|---|
| Hermes's library API: `AIAgent`, `chat()`, `run_conversation()`, the embedding flags | The official guide, fetched and read in full |
| `AIAgent.__init__` accepts ~25 callbacks the guide never mentions | `run_agent.py` on `main`, read directly |
| `stream_delta_callback` receives one positional string | `agent/stream_delivery.py`, line 35 |
| Hermes is an MCP *client*, not a server | Its MCP guide, in full |
| `mcp` 2.x renamed `FastMCP` to `MCPServer` | Installed package 2.2.0; the import error names the migration guide |
| AG-UI has 36 event types (its README still says "~16") | `ag_ui.core.EventType` in ag-ui-protocol 0.1.22 |
| "AGP" was renamed to SLIM in June 2025 | agntcy/slim PR #293, merged 2025-06-03 |

Two things that were **not** verified and are said to be unverified wherever
they appear: the argument shapes of Hermes's `tool_start_callback` and
`tool_complete_callback` (undocumented; the adapter passes them through), and
a run of the example against a live Hermes (no model key was spent — the
bridge is tested with a stand-in that behaves the way the source says the
real one does).

## Decisions

1. **One port, six events.** The core's vocabulary is the intersection of what
   every door can carry, not the union. AG-UI's thirty-six types are a target,
   not a source.
2. **The scripted agent is the test fixture for every door.** It implements the
   same port as the real adapter, so a door that passes against it needs no
   change to serve Hermes. That is the whole claim, made testable.
3. **The Hermes adapter is a thread and a queue.** `run_conversation()` blocks
   and streams by callback on the same thread; the only way to turn that into
   an iterator without touching Hermes is to run it on a worker.
4. **The MCP door returns final text only**, deliberately. MCP tools are
   request/response; pretending otherwise would misrepresent the protocol.
5. **SLIM is a section, not a door.** It is a transport under MCP and A2A, so it
   is described as where you would run the other doors' traffic, not built.
6. **The article says "AGP" once**, to explain the rename, then says SLIM.

## What the worked example verifies

`example/` — `pixi run test`, 14 tests, no network:

- the port contract (first/last event, deltas concatenate, tool pairs match, no state kept);
- CLI: streamed reply and `--json` event dump;
- REST: `/chat` matches the shape in Hermes's docs; `/chat/stream` is SSE of events;
- MCP: `ask` is the only tool; in-process `call_tool` returns the final text;
- AG-UI: `translate()` emits events in protocol order; the endpoint accepts a
  camel-cased `RunAgentInput` and streams SSE, with earlier messages as history;
- the Hermes bridge: callbacks become the stream; the embedding flags are set;
  a provider failure becomes `RunFailed`, not an exception.

Then over real transports, by hand, on 2026-09-13:

- MCP over stdio, driven by the SDK's own client: server `onedoor`, protocol
  `2025-11-25`, `ask` → the expected text;
- REST under uvicorn, `curl`: `/chat` JSON; `/chat/stream` 15 SSE events;
- AG-UI under uvicorn, `curl`: 19 events, `RUN_STARTED … RUN_FINISHED`, text reassembled.

## Traps hit

- **Port 8765 was taken** on the writing machine by an unrelated `http.server`,
  whose 501 page looked like a failing door for one confusing minute. The
  example serves on 8771/8772 and the readiness check now matches the app's
  own `openapi.json` title, not any 200.
- **`from mcp.server.fastmcp import FastMCP` is gone** in 2.x. Anything written
  against the 1.x SDK — including most tutorials — breaks on import.

## Open

- Run the example against a live Hermes and pin down the tool-callback shapes.
- AG-UI's `STATE_SNAPSHOT`/`STATE_DELTA` and human-in-the-loop events have no
  counterpart in the six core events. Adding shared state to the port is the
  obvious next article.
