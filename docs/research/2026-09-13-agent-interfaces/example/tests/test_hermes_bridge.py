"""The Hermes adapter, with a stand-in AIAgent that behaves the way the real
constructor signature and ``stream_delivery.py`` say it does: callbacks fire
on the calling thread, ``run_conversation`` blocks and returns a dict."""

from onedoor.core import RunFailed, RunFinished, RunStarted, TextDelta, ToolFinished, ToolStarted
from onedoor.core.hermes import HermesAgent


class FakeAIAgent:
    seen: dict = {}

    def __init__(self, **kwargs):
        FakeAIAgent.seen = kwargs
        self.kw = kwargs

    def run_conversation(self, user_message, conversation_history=None, **_):
        self.kw["tool_start_callback"]("word_count", {"text": user_message})
        self.kw["tool_complete_callback"]("word_count", 3)
        for chunk in ("Three ", "words."):
            self.kw["stream_delta_callback"](chunk)
        return {"final_response": "Three words.", "messages": list(conversation_history or []) + [
            {"role": "user", "content": user_message}, {"role": "assistant", "content": "Three words."}]}


class ExplodingAIAgent(FakeAIAgent):
    def run_conversation(self, *a, **k):
        raise RuntimeError("provider down")


def test_bridge_turns_callbacks_into_the_event_stream():
    events = list(HermesAgent("any/model", factory=FakeAIAgent).run("a b c"))
    kinds = [type(e).__name__ for e in events]
    assert kinds == ["RunStarted", "ToolStarted", "ToolFinished", "TextDelta", "TextDelta", "RunFinished"]
    assert events[1].name == "word_count" and events[1].call_id == events[2].call_id
    assert "".join(e.text for e in events if isinstance(e, TextDelta)) == events[-1].text


def test_bridge_sets_the_embedding_flags_the_docs_insist_on():
    list(HermesAgent("any/model", factory=FakeAIAgent, max_iterations=7).run("x"))
    kw = FakeAIAgent.seen
    assert kw["quiet_mode"] is True and kw["skip_memory"] is True and kw["skip_context_files"] is True
    assert kw["max_iterations"] == 7 and kw["model"] == "any/model"


def test_bridge_reports_failure_as_an_event_not_an_exception():
    events = list(HermesAgent("any/model", factory=ExplodingAIAgent).run("x"))
    assert isinstance(events[0], RunStarted) and isinstance(events[-1], RunFailed)
    assert "provider down" in events[-1].error
