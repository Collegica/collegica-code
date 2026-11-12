"""agyplan.py <job> [<job> ...]

Runs jobs through agybatch.py in batches of three (two at a time), reading
`agy -p /usage` before the first batch and after each one. Stops if any
weekly figure falls below 30%; waits for the reset if the five-hour figure
for Gemini falls below 10%. Logs to $RUNS/usage-log.txt.
"""
import os, re, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = Path(os.environ.get("RUNS", "/tmp/agyruns"))
LOG = RUNS / "usage-log.txt"


def usage():
    out = subprocess.run(["agy", "-p", "/usage"], capture_output=True, text=True, cwd=RUNS).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) == 4:
            rows.append((parts[0], parts[1], int(parts[2].rstrip("%")), parts[3]))
    with LOG.open("a") as f:
        f.write(datetime.now(timezone.utc).isoformat(timespec="seconds") + "\n" + out + "\n")
    return rows


def check(rows):
    for group, kind, pct, reset in rows:
        if "Weekly" in kind and pct < 30:
            return "stop", f"{group} {kind} {pct}%"
    for group, kind, pct, reset in rows:
        if "Five Hour" in kind and group.startswith("Gemini") and pct < 10:
            return "wait", reset
    return "go", ""


def main(jobs):
    RUNS.mkdir(parents=True, exist_ok=True)
    rows = usage()
    for i in range(0, len(jobs), 3):
        state, info = check(rows)
        while state == "wait":
            reset = datetime.fromisoformat(info.replace("Z", "+00:00"))
            secs = max(60, (reset - datetime.now(timezone.utc)).total_seconds() + 60)
            print(f"five-hour limit low; waiting {secs/60:.0f} min until {info}", flush=True)
            time.sleep(secs)
            rows = usage()
            state, info = check(rows)
        if state == "stop":
            print(f"STOP: {info}", flush=True)
            return
        batch = jobs[i:i + 3]
        env = dict(os.environ, AGY_PAR="2", RUNS=str(RUNS))
        r = subprocess.run([sys.executable, str(HERE / "agybatch.py"), *batch], env=env, capture_output=True, text=True)
        print(r.stdout.strip(), flush=True)
        rows = usage()
        print("usage:", "; ".join(f"{g} {k} {p}%" for g, k, p, _ in rows), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
