#!/usr/bin/env python3
"""Attester for the bocrates computation (OKF §10.2, §10.5).

Deterministic, no LLM. Takes a receipt from the executor and answers one
question: was this result produced by running the sanctioned computation
against the sanctioned data?

    python3 bocrates-attester.py receipt.json
    python3 run-bocrates.py | python3 bocrates-attester.py

Exit 0 on a passing verdict, 1 on a failing one, 2 on a malformed receipt.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent / "computations" / "bocrates"
COMPUTATION = PROJECT / "src" / "bocrates" / "summary.py"
DATA = PROJECT / "data" / "overnight.csv"
REL_TOL = 1e-9


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def close(a, b) -> bool:
    if a == b:
        return True
    try:
        return math.isclose(float(a), float(b), rel_tol=REL_TOL, abs_tol=1e-9)
    except (TypeError, ValueError):
        return False


try:
    raw = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    receipt = json.loads(raw)
except Exception as e:  # noqa: BLE001
    print(f"attester: could not read receipt: {e}", file=sys.stderr)
    sys.exit(2)
for k in ("computation_sha256", "data_sha256", "parameters", "result"):
    if k not in receipt:
        print(f"attester: receipt missing {k}", file=sys.stderr)
        sys.exit(2)

checks: list[dict] = []


def check(name: str, ok: bool, detail: str | None = None) -> None:
    entry = {"name": name, "ok": ok}
    if detail:
        entry["detail"] = detail
    checks.append(entry)


# 1. Provenance: the code and data that ran are the bundled ones.
comp_hash, data_hash = sha256(COMPUTATION), sha256(DATA)
check("computation is the sanctioned file", receipt["computation_sha256"] == comp_hash,
      None if receipt["computation_sha256"] == comp_hash
      else f"receipt {receipt['computation_sha256'][:12]}… bundle {comp_hash[:12]}…")
check("data is the sanctioned file", receipt["data_sha256"] == data_hash,
      None if receipt["data_sha256"] == data_hash
      else f"receipt {receipt['data_sha256'][:12]}… bundle {data_hash[:12]}…")

# 2. Parameters: the contract declares none, so none may be bound.
extra = sorted(receipt["parameters"].keys())
check("no undeclared parameters were bound", not extra,
      f"undeclared: {', '.join(extra)}" if extra else None)

# 3. Fidelity: re-run and compare every figure the receipt reports.
if all(c["ok"] for c in checks):
    sys.path.insert(0, str(PROJECT / "src"))
    from bocrates import annual_average, read_rates  # noqa: E402

    obs = read_rates(DATA)
    expect = annual_average(obs)
    got = receipt["result"].get("annual_average", {})
    mism = []
    if set(got) != {str(y) for y in expect}:
        mism.append(f"years: receipt {sorted(got)} vs re-run {sorted(str(y) for y in expect)}")
    for year, mean in expect.items():
        if not close(got.get(str(year)), mean):
            mism.append(f"{year}: receipt {got.get(str(year))} vs re-run {mean:.6f}")
    if receipt["result"].get("observations") != len(obs):
        mism.append(f"observations: receipt {receipt['result'].get('observations')} vs re-run {len(obs)}")
    check("result matches an independent re-run", not mism, "; ".join(mism[:5]) if mism else None)
else:
    check("result matches an independent re-run", False, "skipped: provenance or parameter check failed")

ok = all(c["ok"] for c in checks)
json.dump({"ok": ok, "verdict": "ATTESTED" if ok else "REJECTED", "checks": checks}, sys.stdout, indent=2)
sys.stdout.write("\n")
sys.exit(0 if ok else 1)
