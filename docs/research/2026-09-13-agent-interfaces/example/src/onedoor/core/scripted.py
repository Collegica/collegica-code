"""A deterministic agent for tests and demos. No model, no network, no key.

It exercises every event the port can emit: one tool call, then a reply
streamed word by word. Because it is the *same port* the real agent
implements, every door is tested end-to-end against it, and a door that
passes here needs no change to serve Hermes.
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator

from onedoor.core.agent import Message
from onedoor.core.events import (
    Event, RunFinished, RunStarted, TextDelta, ToolFinished, ToolStarted,
)


class ScriptedAgent:
    def __init__(self, *, run_id: str | None = None) -> None:
        self._fixed_run_id = run_id

    def run(self, message: str, *, history: list[Message] | None = None) -> Iterator[Event]:
        run_id = self._fixed_run_id or uuid.uuid4().hex
        yield RunStarted(run_id)

        call_id = f"{run_id}-tool-1"
        yield ToolStarted(call_id, "word_count", {"text": message})
        count = len(message.split())
        yield ToolFinished(call_id, "word_count", count)

        turns = len(history or [])
        reply = f"Your message has {count} words. I have seen {turns} earlier turns."
        words = reply.split(" ")
        for i, word in enumerate(words):
            yield TextDelta(word if i == len(words) - 1 else word + " ")
        yield RunFinished(run_id, reply)
