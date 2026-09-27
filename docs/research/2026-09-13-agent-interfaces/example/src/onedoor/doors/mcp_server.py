"""The MCP door: the agent as a tool another agent can call.

This is the reverse of what Hermes's MCP guide covers. There, Hermes is the
*client* consuming tool servers. Here the agent is the *server*, and whoever
speaks MCP — Claude Code, Claude Desktop, another Hermes — can ask it.

MCP tools are request/response, so this door drains the stream and returns
the final text. The tool calls and the token-by-token reply that the other
doors surface are not visible here; that is the protocol's shape, not a
shortcoming of the adapter. ``python -m onedoor.doors.mcp_server`` serves it
over stdio; ``server.streamable_http_app()`` gives an ASGI app for HTTP.
"""

from __future__ import annotations

from mcp.server.mcpserver import MCPServer

from onedoor.config import get_agent
from onedoor.core.agent import final_text

server = MCPServer(
    "onedoor",
    instructions="One tool, `ask`. Send a message; get the agent's final reply.",
)


@server.tool(description="Ask the agent a question and get its final reply as text.")
def ask(message: str) -> str:
    return final_text(get_agent().run(message))


def main() -> None:
    server.run("stdio")


if __name__ == "__main__":
    main()
