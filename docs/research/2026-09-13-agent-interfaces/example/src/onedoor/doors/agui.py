"""The AG-UI door: the agent inside a frontend, as a stream of typed events.

AG-UI (ag-ui-protocol 0.1.22) is an event protocol: a run is a sequence of
typed events — RUN_STARTED, TOOL_CALL_START/ARGS/END/RESULT, TEXT_MESSAGE_
START/CONTENT/END, RUN_FINISHED — sent over SSE. That is why this door needs
the core's *stream* and could not be built on a request/response API: every
internal event maps to one or more AG-UI events, in order, as they happen.

The endpoint takes AG-UI's ``RunAgentInput`` and answers the latest user
message, with the earlier messages passed to the agent as history.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Iterator

from ag_ui.core import (
    EventType, RunAgentInput, RunErrorEvent, RunFinishedEvent, RunStartedEvent,
    TextMessageContentEvent, TextMessageEndEvent, TextMessageStartEvent,
    ToolCallArgsEvent, ToolCallEndEvent, ToolCallResultEvent, ToolCallStartEvent,
)
from ag_ui.encoder import EventEncoder
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

from onedoor.config import get_agent
from onedoor.core.agent import Message
from onedoor.core.events import (
    Event, RunFailed, RunFinished, TextDelta, ToolFinished, ToolStarted,
)

app = FastAPI(title="onedoor (AG-UI)", version="0.1.0")


def translate(events: Iterator[Event], *, thread_id: str, run_id: str) -> Iterator[object]:
    """Core events in, AG-UI events out. Pure — no I/O, easy to test."""
    message_id = uuid.uuid4().hex
    text_open = False
    for event in events:
        if isinstance(event, ToolStarted):
            yield ToolCallStartEvent(tool_call_id=event.call_id, tool_call_name=event.name)
            yield ToolCallArgsEvent(tool_call_id=event.call_id, delta=json.dumps(event.arguments, default=str))
            yield ToolCallEndEvent(tool_call_id=event.call_id)
        elif isinstance(event, ToolFinished):
            yield ToolCallResultEvent(
                message_id=uuid.uuid4().hex, tool_call_id=event.call_id,
                content=json.dumps(event.result, default=str),
            )
        elif isinstance(event, TextDelta):
            if not text_open:
                yield TextMessageStartEvent(message_id=message_id, role="assistant")
                text_open = True
            yield TextMessageContentEvent(message_id=message_id, delta=event.text)
        elif isinstance(event, RunFinished):
            if text_open:
                yield TextMessageEndEvent(message_id=message_id)
            yield RunFinishedEvent(thread_id=thread_id, run_id=run_id)
        elif isinstance(event, RunFailed):
            if text_open:
                yield TextMessageEndEvent(message_id=message_id)
            yield RunErrorEvent(message=event.error)


@app.post("/")
async def run(input_data: RunAgentInput, request: Request) -> StreamingResponse:
    encoder = EventEncoder(accept=request.headers.get("accept"))
    user_turns = [m for m in input_data.messages if m.role == "user"]
    prompt = user_turns[-1].content if user_turns else ""
    history: list[Message] = [
        {"role": m.role, "content": m.content}
        for m in input_data.messages[:-1] if getattr(m, "content", None)
    ]
    agent = get_agent()

    def body() -> Iterator[str]:
        yield encoder.encode(RunStartedEvent(thread_id=input_data.thread_id, run_id=input_data.run_id))
        for event in translate(agent.run(prompt, history=history),
                               thread_id=input_data.thread_id, run_id=input_data.run_id):
            yield encoder.encode(event)

    return StreamingResponse(body(), media_type=encoder.get_content_type())
