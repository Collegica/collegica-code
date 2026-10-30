"""onedoor — one agent core behind four doors.

The core (:mod:`onedoor.core`) knows nothing about HTTP, terminals, MCP or
AG-UI. It defines one port, :class:`onedoor.core.Agent`, whose single method
turns a message into a stream of :mod:`onedoor.core.events`. Every door in
:mod:`onedoor.doors` is an adapter from that stream to one protocol.
"""

from onedoor.core.agent import Agent, final_text
from onedoor.core.scripted import ScriptedAgent

__all__ = ["Agent", "ScriptedAgent", "final_text"]
