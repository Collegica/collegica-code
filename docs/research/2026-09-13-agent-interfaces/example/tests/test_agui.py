import json

from fastapi.testclient import TestClient

from onedoor.core import ScriptedAgent
from onedoor.doors.agui import app, translate

client = TestClient(app)


def test_translate_orders_events_the_agui_way():
    kinds = [e.type for e in translate(ScriptedAgent().run("a b"), thread_id="t", run_id="r")]
    assert kinds[:4] == ["TOOL_CALL_START", "TOOL_CALL_ARGS", "TOOL_CALL_END", "TOOL_CALL_RESULT"]
    assert kinds[4] == "TEXT_MESSAGE_START"
    assert kinds[-2:] == ["TEXT_MESSAGE_END", "RUN_FINISHED"]
    assert all(k == "TEXT_MESSAGE_CONTENT" for k in kinds[5:-2])


def test_endpoint_streams_sse_from_run_agent_input():
    payload = {
        "threadId": "t1", "runId": "r1", "state": {}, "tools": [], "context": [],
        "forwardedProps": {},
        "messages": [
            {"id": "m0", "role": "user", "content": "earlier"},
            {"id": "m1", "role": "assistant", "content": "ok"},
            {"id": "m2", "role": "user", "content": "one two three"},
        ],
    }
    with client.stream("POST", "/", json=payload, headers={"accept": "text/event-stream"}) as r:
        assert r.status_code == 200
        assert r.headers["content-type"].startswith("text/event-stream")
        events = [json.loads(l[6:]) for l in r.iter_lines() if l.startswith("data: ")]
    assert events[0] == {"type": "RUN_STARTED", "threadId": "t1", "runId": "r1"}
    assert events[-1]["type"] == "RUN_FINISHED"
    text = "".join(e["delta"] for e in events if e["type"] == "TEXT_MESSAGE_CONTENT")
    assert text == "Your message has 3 words. I have seen 2 earlier turns."
