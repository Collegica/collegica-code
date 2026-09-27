"""Which agent stands behind the doors. One place, read from the environment.

``ONEDOOR_AGENT=scripted`` (default) needs nothing. ``ONEDOOR_AGENT=hermes``
needs a Hermes checkout on the path, a provider key in the environment, and
``ONEDOOR_MODEL`` (OpenRouter-style, e.g. ``anthropic/claude-sonnet-4.6``).
"""

from __future__ import annotations

import os

from onedoor.core.agent import Agent


def get_agent() -> Agent:
    kind = os.environ.get("ONEDOOR_AGENT", "scripted")
    if kind == "scripted":
        from onedoor.core.scripted import ScriptedAgent
        return ScriptedAgent()
    if kind == "hermes":
        from onedoor.core.hermes import HermesAgent
        model = os.environ.get("ONEDOOR_MODEL")
        if not model:
            raise SystemExit("ONEDOOR_AGENT=hermes needs ONEDOOR_MODEL, e.g. anthropic/claude-sonnet-4.6")
        return HermesAgent(model)
    raise SystemExit(f"unknown ONEDOOR_AGENT={kind!r}; use scripted or hermes")
