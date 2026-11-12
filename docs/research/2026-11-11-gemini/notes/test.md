# Test log: not run

**No run of the common tasks was completed.** The `gemini` command-line app
on this Mac is signed in with the owner's Google account, and Google refuses
that sign-in: Gemini CLI stopped serving personal Google accounts, free or on
Google AI Pro and Ultra, on 18 June 2026 (see
[`cli-and-antigravity.md`](cli-and-antigravity.md)). The shared README says
to stop testing when the app is not signed in; this is the same case, so
testing stopped after the attempt below. Nothing was installed, upgraded or
reconfigured.

## What was tried, 2026-11-11

| | |
|---|---|
| App | Gemini CLI 0.38.2 (`gemini --version`), installed with Homebrew |
| Sign-in | `security.auth.selectedType` is `oauth-personal` in the owner's `~/.gemini/settings.json` (read, not edited). `~/.gemini/.env` is empty; no `GEMINI_API_KEY` or `GOOGLE_API_KEY` is set in the environment. No other sign-in is configured. |
| Non-interactive form | `-p "<prompt>"` (headless docs), with `-o json` |
| Writing in the folder | `--approval-mode auto_edit` (auto-approve edits) would have been used; `yolo` was not needed for the tasks |
| Task 3, second turn | `--resume latest` from the same folder (`gemini --help`: "Resume a previous session") was the plan; never reached |
| Model pin | Not chosen. Google's pages give no default model for Gemini CLI on a personal sign-in, because there is none any more. |
| MCP servers | The owner's `settings.json` defines one MCP server. Excluded per run with `--allowed-mcp-server-names none` (an allow-list naming a server that does not exist). Not verified: the run failed before tools were loaded. |
| Extensions | `-e none`. No `~/.gemini/extensions` folder exists, and `gemini -l` failed on sign-in before listing. |
| Agent skills | Loaded regardless: the run printed 16 "Skill conflict detected" warnings for the owner's skills in two skill folders. `gemini --help` (0.38.2) has no flag to switch skills off. A run free of them would need a settings change, which the brief forbids. |

### Run 0: list the tools

- **Folder:** a fresh copy from `make_folder.py` in the session's temporary
  folder, outside any git repository.
- **Command:** `gemini -p "List every tool you have available, by name, and
  say which come from MCP servers or extensions." --allowed-mcp-server-names
  none -e none --approval-mode auto_edit -o json`
- **Started:** 2026-11-11T20:21:21Z. **Wall time:** 4.00 s. **Exit code:** 1.
- **Model reported:** none.
- **Result:** stdout empty; stderr:

  > Error authenticating: IneligibleTierError: This client is no longer
  > supported for Gemini Code Assist for individuals. To continue using
  > Gemini, please migrate to the Antigravity suite of products:
  > https://antigravity.google

  with `reasonCode: 'UNSUPPORTED_CLIENT'`, `tierId: 'free-tier'`. The same
  error came from an earlier identical attempt without `--approval-mode` and
  from `gemini -l`. The error is thrown in `_doSetupUser`, during sign-in,
  before any model or tool is set up, so a different `-m` would not change it.
- **Kept:** [`../example/results/t0-tools-list/`](../example/results/t0-tools-list/)
  (`prompt.txt`, `run.txt`, `stderr.txt` with home paths and skill names
  removed).

## What would make the tests possible

Each needs the lead's or the owner's decision; none was tried.

1. **Antigravity CLI (`agy`), Google's named successor.** Version 1.5.6 is
   installed and is the latest release. It has a non-interactive mode
   (`-p`), `--model`, `--mode accept-edits`, `--conversation <id>` to continue
   a session, and reads `GEMINI.md` and `AGENTS.md` unchanged (migration
   guide). Two things to settle first: it keeps MCP servers in
   `~/.gemini/config/mcp_config.json`, and its help shows no per-run flag to
   leave them out (`--settings`, "Settings for this session only, never
   saved", may do it; not checked); and it is a different app from the one
   the plan names, already covered in *One Repository, Three Agents*.
2. **A paid Gemini API key** with Gemini CLI. The README says it still works,
   but also says Gemini CLI is "Not for model benchmarks" and "Not optimized
   for Gemini 4+". No key is configured, and making one means a new billing
   account.
3. **The Gemini app by hand** (web or Mac app): upload the folder's files and
   paste each prompt. Not scriptable, so three runs each would be slow, and
   the folder-writing tasks (2 and 3) cannot be marked the same way.
