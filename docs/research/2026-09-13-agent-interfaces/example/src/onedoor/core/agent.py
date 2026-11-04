"""The port. One method, one direction: a message in, a stream of events out."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Protocol

from onedoor.core.events import Event, RunFinished

Message = dict[str, Any]  # {"role": "user" | "assistant" | ..., "content": str}


class Agent(Protocol):
    def run(self, message: str, *, history: list[Message] | None = None) -> Iterator[Event]:
        """Answer ``message`` in the context of ``history``, yielding events as they happen.

        Contract every implementation and every door relies on:

        - the first event is ``RunStarted`` and the last is ``RunFinished`` or ``RunFailed``;
        - ``TextDelta`` events arrive in order and concatenate to ``RunFinished.text``;
        - a ``ToolStarted`` is always followed, eventually, by a ``ToolFinished`` with
          the same ``call_id``;
        - the iterator is single-use, and the implementation holds no state between
          calls — a caller that wants memory passes ``history`` back in.
        """
        ...


def final_text(events: Iterator[Event]) -> str:
    """Drain a run and return the reply — for doors that cannot stream (MCP, ``/chat``)."""
    text = ""
    for event in events:
        if isinstance(event, RunFinished):
            text = event.text
    return text
