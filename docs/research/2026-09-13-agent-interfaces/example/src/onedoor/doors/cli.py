"""The CLI door: ``onedoor "a message"``.

Streams the reply as it arrives. ``--json`` prints every event as one JSON
object per line instead — the same stream the other doors translate, made
visible.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys

from onedoor.config import get_agent
from onedoor.core.events import RunFailed, RunFinished, TextDelta


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="onedoor", description="Ask the agent from a terminal.")
    parser.add_argument("message", help="what to ask")
    parser.add_argument("--json", action="store_true", help="print raw events as JSON lines")
    args = parser.parse_args(argv)

    agent = get_agent()
    status = 0
    for event in agent.run(args.message):
        if args.json:
            record = {"event": type(event).__name__, **dataclasses.asdict(event)}
            print(json.dumps(record, default=str))
        elif isinstance(event, TextDelta):
            sys.stdout.write(event.text)
            sys.stdout.flush()
        elif isinstance(event, RunFinished):
            sys.stdout.write("\n")
        if isinstance(event, RunFailed):
            print(f"error: {event.error}", file=sys.stderr)
            status = 1
    return status


if __name__ == "__main__":
    raise SystemExit(main())
