"""Run one common task in Codex, in a fresh folder, with no MCP servers.

    python3 run.py <run-dir> <prompt-file> [--agents <file>] [--model gpt-6.1-sol]
    python3 run.py <run-dir> <prompt-file> --resume <session-id> --tag turn2

Builds the made-up folder in <run-dir>/folder (unless --resume), optionally
copies a file in as AGENTS.md, and runs `codex exec` there. Every MCP server
and plugin named in the user's ~/.codex/config.toml is switched off for this
run with a `-c` override on the command line; the file itself is only read,
never edited. Connectors (`--disable apps`) and local memories
(`--disable memories`) are switched off too, so one run cannot see another.
Writes <tag>-run.json (command, times, session, token use), <tag>-events.jsonl
and <tag>-last-message.md beside the folder.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import tomllib
from datetime import datetime, timezone
from pathlib import Path

TASKS = Path(__file__).resolve().parents[2] / "2026-11-10-assistant-guides" / "tasks"


def overrides() -> list[str]:
    cfg = tomllib.loads((Path.home() / ".codex" / "config.toml").read_text())
    args = []
    for name in cfg.get("mcp_servers", {}):
        args += ["-c", f"mcp_servers.{name}.enabled=false"]
    args += ["-c", "plugins._default.enabled=false"]
    for name in cfg.get("plugins", {}):
        args += ["-c", f'plugins."{name}".enabled=false']
        # A disabled plugin's own MCP servers were still loaded in the first
        # check, so each one is also switched off by name.
        plugin, market = name.split("@", 1)
        cache = Path.home() / ".codex" / "plugins" / "cache" / market / plugin
        for mcp in cache.glob("*/.mcp.json"):
            for server in json.loads(mcp.read_text()).get("mcpServers", {}):
                key = f'plugins."{name}".mcp_servers.{server}.enabled=false'
                if key not in args:
                    args += ["-c", key]
    # Even so, a bundled plugin's MCP server stayed loaded until the plugins
    # feature itself was switched off (notes/test.md, "No MCP servers").
    args += ["--disable", "plugins", "--disable", "apps", "--disable", "computer_use",
             "--disable", "memories", "-c", "notify=[]"]
    return args


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("prompt_file")
    ap.add_argument("--agents")
    ap.add_argument("--resume")
    ap.add_argument("--model", default="gpt-6.1-sol")
    ap.add_argument("--tag", default="")
    ap.add_argument("--as-name", default="AGENTS.md",
                    help="file name for --agents (CLAUDE.md for one lead)")
    ap.add_argument("--effort", help="reasoning effort, for one lead")
    ap.add_argument("--reuse", action="store_true",
                    help="new session in the existing folder (third turn of a lead)")
    a = ap.parse_args()
    run = Path(a.run_dir)
    folder = run / "folder"
    if not a.resume and not a.reuse:
        if run.exists():
            sys.exit(f"{run} exists")
        folder.mkdir(parents=True)
        subprocess.run([sys.executable, str(TASKS / "make_folder.py"), str(folder)],
                       check=True, stdout=subprocess.DEVNULL)
        if a.agents:
            shutil.copy(a.agents, folder / a.as_name)
    prompt = Path(a.prompt_file).read_text()
    tag = a.tag or "turn1"
    cmd = ["codex", "exec"]
    if a.resume:
        cmd += ["resume", a.resume]
    cmd += ["-m", a.model, "--skip-git-repo-check", "--json",
            "-o", str(run / f"{tag}-last-message.md")]
    if a.resume:
        cmd += ["-c", 'sandbox_mode="workspace-write"']
    else:
        cmd += ["-s", "workspace-write", "-C", str(folder)]
    if a.effort:
        cmd += ["-c", f'model_reasoning_effort="{a.effort}"']
    cmd += overrides() + [prompt]
    start = time.time()
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(run / f"{tag}-events.jsonl", "w") as out:
        p = subprocess.run(cmd, cwd=folder, stdout=out, stderr=subprocess.PIPE, text=True)
    wall = round(time.time() - start, 1)
    (run / f"{tag}-stderr.txt").write_text(p.stderr)
    session, usage = None, None
    for line in (run / f"{tag}-events.jsonl").read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        session = session or ev.get("thread_id")
        if ev.get("type") == "turn.completed":
            usage = ev.get("usage")
    # The model, effort and version Codex itself recorded, from its session
    # log (only these fields are copied: the log also holds account ids).
    reported = {"models": [], "efforts": [], "cli_version": None, "tool_namespaces": []}
    for log in (Path.home() / ".codex" / "sessions").rglob(f"*{session}.jsonl"):
        text = log.read_text()
        for key, field in (("models", "model"), ("efforts", "effort")):
            reported[key] = sorted(set(re.findall(rf'"{field}":"([^"]*)"', text)))
        version = re.search(r'"cli_version":"([^"]*)"', text)
        reported["cli_version"] = version and version.group(1)
        reported["tool_namespaces"] = sorted(set(
            re.findall(r'"type":"namespace","name":"([^"]*)"', text)))
    shown = ["<prompt>" if c == prompt else c for c in cmd]
    (run / f"{tag}-run.json").write_text(json.dumps({
        "started_utc": started, "wall_s": wall, "exit": p.returncode,
        "session": session, "reported": reported, "usage": usage,
        "command": shown}, indent=1) + "\n")
    print(f"{run.name} {tag}: exit {p.returncode}, {wall}s, session {session}")
    return p.returncode


if __name__ == "__main__":
    sys.exit(main())
