from onedoor.core import (
    RunFinished, RunStarted, ScriptedAgent, TextDelta, ToolFinished, ToolStarted, final_text,
)


def test_stream_obeys_the_port_contract():
    events = list(ScriptedAgent(run_id="r1").run("one two three"))
    assert isinstance(events[0], RunStarted) and events[0].run_id == "r1"
    assert isinstance(events[-1], RunFinished)
    started = [e for e in events if isinstance(e, ToolStarted)]
    finished = [e for e in events if isinstance(e, ToolFinished)]
    assert [s.call_id for s in started] == [f.call_id for f in finished]
    deltas = "".join(e.text for e in events if isinstance(e, TextDelta))
    assert deltas == events[-1].text == "Your message has 3 words. I have seen 0 earlier turns."


def test_history_is_passed_not_kept():
    agent = ScriptedAgent()
    first = final_text(agent.run("hello"))
    second = final_text(agent.run("hello", history=[{"role": "user", "content": "hi"}]))
    assert first.endswith("0 earlier turns.") and second.endswith("1 earlier turns.")
    assert final_text(agent.run("hello")).endswith("0 earlier turns.")  # no state leaked
