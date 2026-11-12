"""Rebuild each test run's outputs from Claude Code's own session transcripts.

    python3 recover.py

The test folders were made in a temporary directory that was emptied before
their outputs had been copied here. Claude Code keeps a transcript of every
session under ~/.claude/projects/<folder-path>/, so the files each run wrote
(its Write and Edit calls) and its last reply can be rebuilt from those. This
script only reads the transcripts. Renames done with `mv` (task 3) are not
files written, so they appear in `_bash-commands.txt`, not as files.
"""
import glob
import json
import os
from pathlib import Path

P = Path.home() / ".claude/projects"
OUT = Path(__file__).parent / "results"


def main() -> None:
    for d in sorted(glob.glob(str(P / "*scratchpad-cg-runs-*-folder"))):
        label = d.split("scratchpad-cg-runs-")[1][: -len("-folder")]
        sessions = sorted(glob.glob(d + "/*.jsonl"), key=os.path.getmtime)
        out = OUT / label
        out.mkdir(parents=True, exist_ok=True)
        for n, s in enumerate(sessions, 1):
            files, last_text, prompt, models, t0, t1 = {}, "", None, set(), None, None
            for line in open(s):
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                ts = e.get("timestamp")
                if ts:
                    t0, t1 = t0 or ts, ts
                m = e.get("message") or {}
                if e.get("type") == "user" and prompt is None and isinstance(m.get("content"), str):
                    prompt = m["content"]
                if e.get("type") != "assistant":
                    continue
                if m.get("model"):
                    models.add(m["model"])
                for c in m.get("content") or []:
                    if c.get("type") == "text" and c.get("text", "").strip():
                        last_text = c["text"]
                    if c.get("type") != "tool_use":
                        continue
                    inp = c.get("input") or {}
                    if c.get("name") in ("Write", "Edit"):
                        fp = inp.get("file_path", "")
                        rel = fp.split("-folder/")[-1] if "-folder/" in fp else os.path.basename(fp)
                        if c["name"] == "Write":
                            files[rel] = inp.get("content", "")
                        elif rel in files:
                            files[rel] = files[rel].replace(inp.get("old_string", ""), inp.get("new_string", ""), 1)
                        else:
                            files[rel + ".edits"] = files.get(rel + ".edits", "") + (
                                "\n--- old\n" + inp.get("old_string", "") + "\n+++ new\n" + inp.get("new_string", ""))
                    if c.get("name") == "Bash":
                        files["_bash-commands.txt"] = files.get("_bash-commands.txt", "") + inp.get("command", "") + "\n----\n"
            pre = f"session{n}-" if len(sessions) > 1 else ""
            (out / f"{pre}prompt.txt").write_text(prompt or "")
            (out / f"{pre}reply.md").write_text(last_text)
            (out / f"{pre}run.txt").write_text(f"models: {sorted(models)}\nfirst event: {t0}\nlast event: {t1}\n")
            for rel, txt in files.items():
                (out / (pre + rel.replace("/", "__"))).write_text(txt)
            print(label, f"s{n}", sorted(models), t0, t1, sorted(files), "LIMIT" if "hit your" in last_text else "")


if __name__ == "__main__":
    main()
