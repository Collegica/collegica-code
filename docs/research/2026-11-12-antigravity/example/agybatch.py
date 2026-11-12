"""batch.py <job> [<job> ...]   job = <task>-<plain|practice|lead name>-r<n>

Builds a fresh folder per job, runs it with run.sh (3 at a time), and copies
the folder to the research folder's example/results/<job>/ as soon as it ends.
"""
import json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SP = Path(__file__).parent
WT = Path(os.environ.get("REPO", Path(__file__).resolve().parents[4]))
TASKS = WT / "docs/research/2026-11-10-assistant-guides/tasks"
RESULTS = WT / "docs/research/2026-11-12-antigravity/example/results"
RUNS = Path(os.environ.get("RUNS", "/tmp/agyruns"))
P = TASKS / "prompts"
LEADS = SP / "leads"

def spec(job):
    task, kind, _ = job.split("-")
    files = {}
    turns = []
    if task == "t2":
        turns = [P / "t2.txt"]
        if kind == "practice":
            files["AGENTS.md"] = (TASKS / "house-rules.md").read_text()
        if kind == "claudemd":
            files["CLAUDE.md"] = (TASKS / "house-rules.md").read_text()
        if kind == "geminimd":
            files["GEMINI.md"] = (TASKS / "house-rules.md").read_text()
    elif task == "t3" and kind in ("practice", "plan"):
        turns = [P / "t3-practice-1.txt", P / "t3-practice-2.txt"]
    elif task == "t3" and kind == "planmode":
        turns = [P / "t3-plain.txt", LEADS / "t3-go.txt"]
    elif task == "t4" and kind == "grokignore":
        turns = [P / "t4-plain.txt"]
        files[".grokignore"] = "members.csv\n"
    elif task == "t1" and kind == "brief10":
        turns = [P / "t1-plain.txt"]
        files["AGENTS.md"] = (LEADS / "brief10-agents.md").read_text()
    else:
        turns = [P / f"{task}-{kind}.txt"]
    return files, turns

def run(job):
    files, turns = spec(job)
    d = RUNS / job
    o = RUNS / (job + ".out")
    for x in (d, o):
        if x.exists():
            shutil.rmtree(x)
    o.mkdir()
    subprocess.run([sys.executable, "-I", str(TASKS / "make_folder.py"), str(d)], check=True, capture_output=True)
    for name, text in files.items():
        (d / name).write_text(text)
    session = None
    for i, pf in enumerate(turns, 1):
        extra = []
        if session:
            extra = ["--conversation", session]
        tag = f"turn{i}"
        env = dict(os.environ)
        if job.startswith("t3-planmode") and i == 1:
            env["AGY_MODE"] = "plan"
        shutil.copy(pf, o / f"{tag}-prompt.txt")
        r = subprocess.run([str(SP / "agyrun.sh"), str(d), str(pf), tag, *extra], capture_output=True, text=True, env=env)
        try:
            session = json.loads((o / f"{tag}.json").read_text()).get("conversation_id")
        except Exception:
            session = None
    out = RESULTS / job
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(d, out / "folder", ignore=shutil.ignore_patterns(".grok", ".git"))
    for f in o.iterdir():
        shutil.copy(f, out / f.name)
    return job, " | ".join((o / f"turn{i}.time").read_text().strip() for i in range(1, len(turns) + 1))

if __name__ == "__main__":
    jobs = sys.argv[1:]
    with ThreadPoolExecutor(int(os.environ.get("AGY_PAR", "1"))) as ex:
        for job, t in ex.map(run, jobs):
            print(job, t, flush=True)
