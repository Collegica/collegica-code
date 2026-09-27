import json

from fastapi.testclient import TestClient

from onedoor.doors.rest import app

client = TestClient(app)


def test_chat_is_the_hermes_docs_shape():
    r = client.post("/chat", json={"message": "a b c d"})
    assert r.status_code == 200
    assert r.json() == {"response": "Your message has 4 words. I have seen 0 earlier turns."}


def test_chat_with_history():
    r = client.post("/chat", json={"message": "x", "history": [{"role": "user", "content": "earlier"}]})
    assert r.json()["response"].endswith("1 earlier turns.")


def test_stream_is_sse_of_events():
    with client.stream("POST", "/chat/stream", json={"message": "a b"}) as r:
        assert r.headers["content-type"].startswith("text/event-stream")
        lines = [l for l in r.iter_lines() if l.startswith("data: ")]
    kinds = [json.loads(l[6:])["event"] for l in lines]
    assert kinds[0] == "RunStarted" and kinds[-1] == "RunFinished" and "TextDelta" in kinds
