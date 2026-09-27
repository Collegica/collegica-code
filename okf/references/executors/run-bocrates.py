#!/usr/bin/env python3
"""Executor for the bocrates computation (OKF §10.2).

Runs the sanctioned computation — annual averages of the Bank of Canada
overnight rate — against the bundled data and prints a receipt: enough for the
attester to confirm that exactly this code ran against exactly this data.

    python3 run-bocrates.py

Standard library only; Python 3.11 or later. The computation declares no
parameters, so there is nothing for an agent to supply and nothing to edit.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent / "computations" / "bocrates"
COMPUTATION = PROJECT / "src" / "bocrates" / "summary.py"
DATA = PROJECT / "data" / "overnight.csv"

sys.path.insert(0, str(PROJECT / "src"))
from bocrates import annual_average, read_rates  # noqa: E402  (after sys.path)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


observations = read_rates(DATA)
result = annual_average(observations)

receipt = {
    "computation": "references/computations/bocrates/src/bocrates/summary.py",
    "computation_sha256": sha256(COMPUTATION),
    "data_sha256": sha256(DATA),
    "parameters": {},
    "result": {
        "observations": len(observations),
        "first": observations[0][0],
        "last": observations[-1][0],
        # Full precision, deliberately: a receipt is evidence for the attester,
        # and rounding here would make an honest run fail a tight comparison.
        "annual_average": {str(year): mean for year, mean in result.items()},
    },
    "ran_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
}
json.dump(receipt, sys.stdout, indent=2)
sys.stdout.write("\n")
