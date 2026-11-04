"""The REST door: FastAPI, two routes.

``POST /chat`` is the request/response shape from Hermes's own docs — a
message in, ``{"response": ...}`` out. ``POST /chat/stream`` is the same call
as Server-Sent Events, one internal event per ``data:`` line. A fresh agent
is taken per request, so nothing is shared across concurrent calls.
"""

from __future__ import annotations

import dataclasses
import json
from collections.abc import Iterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from onedoor.config import get_agent
from onedoor.core.agent import Message, final_text

app = FastAPI(title="onedoor", version="0.1.0")


class ChatRequest(BaseModel):
    message: str
    history: list[Message] = []


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    agent = get_agent()
    return ChatResponse(response=final_text(agent.run(request.message, history=request.history)))


@app.post("/chat/stream")
def chat_stream(request: ChatRequest) -> StreamingResponse:
    agent = get_agent()

    def lines() -> Iterator[str]:
        for event in agent.run(request.message, history=request.history):
            record = {"event": type(event).__name__, **dataclasses.asdict(event)}
            yield f"data: {json.dumps(record, default=str)}\n\n"

    return StreamingResponse(lines(), media_type="text/event-stream")
