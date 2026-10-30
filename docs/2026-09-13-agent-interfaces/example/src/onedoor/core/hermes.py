"""The Hermes adapter: ``run_agent.AIAgent`` behind the same port.

Hermes's Python API is callback-driven and blocking: ``run_conversation()``
returns when the whole tool loop is done, and streams by calling back on the
same thread. This adapter runs it in a worker thread and turns the callbacks
into the event stream every door already consumes.

What is verified against the source (``run_agent.py`` and
``agent/stream_delivery.py``, NousResearch/hermes-agent, September 2026):

- the constructor accepts ``quiet_mode``, ``skip_memory``, ``skip_context_files``,
  ``max_iterations``, ``enabled_toolsets``/``disabled_toolsets``, and the callbacks
  ``stream_delta_callback``, ``tool_start_callback``, ``tool_complete_callback``;
- ``stream_delta_callback`` is called with one positional argument, the text chunk;
- ``run_conversation(user_message, conversation_history=...)`` returns a dict with
  ``final_response`` and ``messages``.

What is *not* documented and therefore passed through unparsed: the argument
shapes of the two tool callbacks. They land in ``ToolStarted.arguments`` /
``ToolFinished.result`` as ``{"args": [...], "kwargs": {...}}``. Tighten that
once you have seen a real payload; do not guess it.

Hermes is not on PyPI. Install it the way its docs say (clone, ``uv sync``) and
run from that checkout, or point ``PYTHONPATH`` at it. The import is lazy so the
rest of this package works without it.
"""

from __future__ import annotations

import queue
import threading
import uuid
from collections.abc import Callable, Iterator
from typing import Any

from onedoor.core.agent import Message
from onedoor.core.events import (
    Event, RunFailed, RunFinished, RunStarted, TextDelta, ToolFinished, ToolStarted,
)

_DONE = object()


def _import_aiagent() -> type:
    from run_agent import AIAgent  # type: ignore[import-not-found]
    return AIAgent


class HermesAgent:
    def __init__(
        self,
        model: str,
        *,
        max_iterations: int = 25,
        enabled_toolsets: list[str] | None = None,
        disabled_toolsets: list[str] | None = None,
        factory: Callable[..., Any] | None = None,
    ) -> None:
        self.model = model
        self.max_iterations = max_iterations
        self.enabled_toolsets = enabled_toolsets
        self.disabled_toolsets = disabled_toolsets
        # ``factory`` exists so the bridge can be tested with a stand-in AIAgent.
        self._factory = factory

    def run(self, message: str, *, history: list[Message] | None = None) -> Iterator[Event]:
        run_id = uuid.uuid4().hex
        events: queue.Queue[Any] = queue.Queue()
        calls: dict[int, str] = {}

        def on_delta(text: str) -> None:
            events.put(TextDelta(text))

        def on_tool_start(*args: Any, **kwargs: Any) -> None:
            call_id = f"{run_id}-tool-{len(calls) + 1}"
            calls[len(calls)] = call_id
            name = _guess_name(args, kwargs)
            events.put(ToolStarted(call_id, name, {"args": list(args), "kwargs": kwargs}))

        def on_tool_complete(*args: Any, **kwargs: Any) -> None:
            index = max(len(calls) - 1, 0)
            call_id = calls.get(index, f"{run_id}-tool-?")
            events.put(ToolFinished(call_id, _guess_name(args, kwargs), {"args": list(args), "kwargs": kwargs}))

        def worker() -> None:
            try:
                make = self._factory or _import_aiagent()
                # One AIAgent per run: the docs are explicit that an instance holds
                # state and must never be shared across threads or tasks.
                agent = make(
                    model=self.model,
                    quiet_mode=True,
                    skip_memory=True,
                    skip_context_files=True,
                    max_iterations=self.max_iterations,
                    enabled_toolsets=self.enabled_toolsets,
                    disabled_toolsets=self.disabled_toolsets,
                    stream_delta_callback=on_delta,
                    tool_start_callback=on_tool_start,
                    tool_complete_callback=on_tool_complete,
                )
                result = agent.run_conversation(message, conversation_history=list(history or []))
                events.put(RunFinished(run_id, str(result.get("final_response", ""))))
            except Exception as exc:  # noqa: BLE001 — the door decides how to report it
                events.put(RunFailed(run_id, f"{type(exc).__name__}: {exc}"))
            finally:
                events.put(_DONE)

        yield RunStarted(run_id)
        threading.Thread(target=worker, name=f"hermes-{run_id[:8]}", daemon=True).start()
        while True:
            item = events.get()
            if item is _DONE:
                return
            yield item


def _guess_name(args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
    for key in ("tool_name", "name", "tool"):
        if isinstance(kwargs.get(key), str):
            return kwargs[key]
    for value in args:
        if isinstance(value, str):
            return value
        name = getattr(value, "name", None)
        if isinstance(name, str):
            return name
    return "tool"
