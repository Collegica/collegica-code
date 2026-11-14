"""Summarise saved runs: wall time, tokens, tool calls, the first tool call, the
final reply, and the mechanical checks (task 2 word count, task 3 checker).

    python3 summarise.py <results-dir>      # example/results/<tag>/{folder,turnN.*}
    python3 summarise.py <workdir>          # live batch: <tag>/ beside <tag>.out/

Marking against the answer key is done by hand from this output.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

W = Path(sys.argv[1])
T = Path(__file__).resolve().parent.parent.parent / "2026-11-10-assistant-guides" / "tasks"


def load(path):
    res, tools, model = None, [], None
    for line in path.read_text().splitlines():
        try:
            j = json.loads(line)
        except ValueError:
            continue
        if j.get("type") == "system":
            model = j.get("model")
        elif j.get("type") == "tool_use":
            tools.append((j["name"], json.dumps(j.get("input"))[:160]))
        elif j.get("type") == "result":
            res = j
    return res, tools, model


runs = []
for d in sorted(W.iterdir()):
    if d.name.endswith(".out"):
        runs.append((d.name[:-4], d, W / d.name[:-4]))
    elif (d / "folder").is_dir():
        runs.append((d.name, d, d / "folder"))

for tag, out, folder in runs:
    print("=" * 70)
    print(tag)
    for turn in sorted(out.glob("turn*.jsonl")):
        res, tools, model = load(turn)
        wall = (out / (turn.stem + ".time")).read_text().strip()
        tok = res.get("tokens") if res else None
        print(f"-- {turn.stem}: {wall}; model {model}; tokens {tok}; tool calls {len(tools)}")
        for n, i in tools[:3]:
            print(f"   call: {n} {i}")
        print(res["text"] if res else "(no result)")
    if tag.startswith("t2") and (folder / "notice.md").exists():
        r = subprocess.run(["python3", str(T / "count_words.py"), str(folder / "notice.md")], capture_output=True, text=True)
        print("WORDS", r.stdout.strip())
        print(re.sub(r"\n{3,}", "\n\n", (folder / "notice.md").read_text()))
    if tag.startswith("t1") and (folder / "actions.md").exists():
        print(">> actions.md\n" + (folder / "actions.md").read_text())
    if tag.startswith("t3"):
        flag = ["--plain"] if "plain" in tag else []
        r = subprocess.run(["python3", str(T / "check_t3.py"), *flag, str(folder)], capture_output=True, text=True)
        print("CHECK_T3", "exit", r.returncode)
        print("\n".join(l for l in (r.stdout + r.stderr).splitlines() if not l.startswith("ok") or "index" in l))
        if "plain" in tag:
            r = subprocess.run(["python3", str(T / "check_t3.py"), str(folder)], capture_output=True, text=True)
            print("CHECK_T3 strict exit", r.returncode)
