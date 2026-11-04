"""The internal event vocabulary — the only thing a door is allowed to know.

Six shapes. They are deliberately smaller than any wire protocol, because a
door's job is to *translate outwards*: AG-UI has thirty-odd event types, MCP
has a request and a response, a terminal has stdout. The intersection of what
every door can carry is what the core emits.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Union


@dataclass(frozen=True)
class RunStarted:
    run_id: str


@dataclass(frozen=True)
class TextDelta:
    """One chunk of the assistant's reply, in order. Concatenate to get the text."""
    text: str


@dataclass(frozen=True)
class ToolStarted:
    call_id: str
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ToolFinished:
    call_id: str
    name: str
    result: Any = None


@dataclass(frozen=True)
class RunFinished:
    run_id: str
    text: str


@dataclass(frozen=True)
class RunFailed:
    run_id: str
    error: str


Event = Union[RunStarted, TextDelta, ToolStarted, ToolFinished, RunFinished, RunFailed]
