import anyio

from onedoor.doors.mcp_server import server


def test_ask_is_the_only_tool():
    tools = anyio.run(server.list_tools)
    assert [t.name for t in tools] == ["ask"]
    assert tools[0].input_schema["required"] == ["message"]


def test_ask_returns_the_final_text():
    result = anyio.run(server.call_tool, "ask", {"message": "a b c"})
    assert not result.is_error
    assert result.content[0].text == "Your message has 3 words. I have seen 0 earlier turns."
