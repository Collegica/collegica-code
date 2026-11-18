# Code Mode in Claude Code: what it is

18 November 2026. Reading only: every claim below is from a page named in the
list at the end. **Nothing was run.** Trying it would set an environment
variable and answer a confirmation dialog that saves an answer to
`~/.claude.json` and restarts the session, so it was left for the owner to
approve (see "Not tested").

## What it is

Code Mode is an **experimental, off-by-default** feature of Claude Code, added
in v2.1.323 (12 November 2026). Without it, Claude asks for tool calls (Bash,
Read, Edit) one at a time and reads each result before deciding the next. With
it, Claude writes a piece of **JavaScript** that makes the tool calls, and
Claude Code runs that code in the session. One script can run commands in
parallel, feed one result into the next call, and return only the part of the
output Claude needs to read.

The documentation's example: find the file, edit it, run the tests, return the
path and test output.

```javascript
const files = await $`rg -l "function retryPolicy" src`.text();
const target = files.trim().split("\n")[0];
await edit(target, "maxAttempts: 3", "maxAttempts: 5");
({ edited: target, tests: $`npm test -- retryPolicy`.nothrow() });
```

You see the tool calls (the edit's diff), not the code; `Ctrl+O` opens the
transcript viewer where each script is a collapsed **Code** row. The docs
suggest it for changes repeated across many files, searches whose results need
filtering, and independent commands that can run at once.

## Turning it on

`CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1` in the shell or in the `env` block of
`~/.claude/settings.json`; Claude Code asks you to confirm before the first
session and restarts. A project's own settings files cannot turn it on, "so a
repository you clone can't turn on Code Mode for you". Setting the variable to
`0` in managed settings blocks it for an organisation; managed settings cannot
turn it on for users.

## Limits that matter

- **Interactive terminal sessions only.** Not `-p`, the Agent SDK, the VS Code
  panel, the Desktop app or cloud sessions. (So it cannot be used in the way the
  [computer-control trials](../2026-11-17-computer-control/README.md) used
  `claude -p`.)
- **Direct Anthropic API with a subscription or Console account.** Not a
  gateway, Bedrock, Google Cloud, Foundry, or a custom `ANTHROPIC_BASE_URL`;
  not with an API-key helper, OpenTelemetry export, `DISABLE_TELEMETRY`,
  HIPAA configuration or zero data retention.
- **Models:** Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2; native build.
- **Resume:** a Code Mode session can be resumed only in the terminal with the
  variable set to `1`; with it off Claude Code refuses to resume.
- **No** Remote Control, Claude in Chrome or computer use; the session cannot be
  moved to the Desktop app or turned into a background session.
- **Time:** waiting code stops after ten minutes; background code (auto or
  `bypassPermissions` mode) can run for up to two hours.
- **Agent teams:** needs v2.1.326 or later; teammates are in Code Mode in
  in-process display mode only.

## Permissions

Each tool call in a script still passes `deny` and `ask` rules and
`PreToolUse` hooks under its usual name (`Bash`, and so on). In **auto mode**
a classifier reviews the *code* before it runs, **not each tool call**, and
"doesn't see values computed at run time, such as a path taken from search
output", so the docs say to keep rules or hooks for calls you must control.
In other modes the code starts without review and you are prompted per call.
A hook can match the tool that runs the code, `REPL`, and read the script from
`tool_input.code`. The docs also warn that Bash rules match command text and
can be bypassed with or without Code Mode; sandboxing is the stronger limit.

## Changes in its first week (changelog)

- 2.1.323, 12 Nov: added.
- 2.1.325, 13 Nov: fixes: scripts ignoring a worktree entered with
  `EnterWorktree` and writing `~` paths into the project; words typed at a
  permission dialog not reaching Claude; Claude starting work by itself when a
  session that ended during a script was resumed.
- 2.1.326, 16 Nov: works with agent teams; the `$` shell helper refuses some
  values; permission checks tightened (more sandboxed commands ask or are
  refused); fixes for mods and for skills with inline `!` commands under auto
  mode.
- 2.1.327, 17 Nov: no longer refuses to start when a mod hooks tool calls; fix
  for a running script getting permission prompts and denials once a second
  script started in auto mode.

An experimental feature with permission fixes in each of four releases in six
days: the safe reading is "try it in a scratch folder, not on a repository you
cannot afford to break".

## Where the idea comes from

- **Cloudflare, "Code Mode: the better way to use MCP" (26 September 2025).**
  Convert MCP tools into a TypeScript API and let the model write code against
  it. Argued reasons: models have seen far more real code than tool-call
  examples, and chained calls need not pass each output back through the model.
  Code runs in V8 isolates on Cloudflare Workers with no general network
  access; each MCP server is a pre-authorised "binding", so the generated code
  never sees the keys. The post reports no benchmarks.
- **Anthropic engineering, "Code execution with MCP" (4 November 2025).**
  Present MCP tools as code files in a filesystem, load only the ones needed,
  and keep intermediate data in the execution environment. It reports a drop
  from about 150,000 tokens to 2,000 (98.7%) for one example without showing how
  it was measured, and notes that running model-written code needs sandboxing,
  resource limits and monitoring.
- **Claude API "programmatic tool calling".** The model calls your tools from
  code inside the code-execution container. Stable on the Claude API, Claude
  Platform on AWS and Foundry; needs the `code_execution_20260120` tool
  version; not zero-data-retention eligible (data kept up to 30 days). This is
  the API feature; Code Mode is the Claude Code feature.

## What is not established

- **No Anthropic figure** for Code Mode's token or time savings was found.
  Secondary coverage repeating "37%" traces it to the 2025 API article, not to
  Code Mode (that comparison comes from a third-party analysis, not read here).
- Whether Code Mode makes a given job faster or more reliable is unmeasured.
  The only quantitative claim anywhere in these sources is the 98.7% figure for
  a different design (tools as code in an MCP setting).

## Not tested

Not run here: enabling it, reading a script, resuming a session, hooks that
match `REPL`. To test it, someone must set the variable, answer the
confirmation dialog (which saves to `~/.claude.json`), and run an interactive
session in a scratch folder, ideally with a task like "list broken local
Markdown links" from the docs.

## Sources

- [Run tool calls from code with Code Mode](https://code.claude.com/docs/en/code-mode)
  (Claude Code docs, read 18 Nov 2026).
- [Claude Code changelog](https://code.claude.com/docs/en/changelog) (2.1.323
  to 2.1.327; only the first 100,000 characters of a very long page were read).
- [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
  (Anthropic Engineering, 4 Nov 2025).
- [Code Mode: the better way to use MCP](https://blog.cloudflare.com/code-mode/)
  (Cloudflare, 26 Sep 2025).
- [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)
  (Claude API docs; front-matter and summary read).
