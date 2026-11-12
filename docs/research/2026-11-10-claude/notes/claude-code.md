# Claude Code and the instruction file: notes

Claude Code's documentation at code.claude.com, read 2026-11-10 as the
pages' own Markdown (each page has a `.md` form), in full unless a section
is named. The changelog was read for the two newest versions only.

## What it is and where it runs

<https://code.claude.com/docs/en/overview>, read 2026-11-10 (opening and
install section only).

- "Claude Code is an agentic coding tool that reads your codebase, edits
  files, runs commands, and integrates with your development tools.
  Available in your terminal, IDE, desktop app, and browser."
- "Most surfaces require a Claude subscription or Anthropic Console
  account."

## The instruction file: CLAUDE.md

<https://code.claude.com/docs/en/memory>, read 2026-11-10 in full.

- "CLAUDE.md files are markdown files that give Claude persistent
  instructions for a project, your personal workflow, or your entire
  organization. You write these files in plain text; Claude reads them at
  the start of every session."
- Where they live, in load order: managed policy (on macOS
  `/Library/Application Support/ClaudeCode/CLAUDE.md`); user,
  `~/.claude/CLAUDE.md`, "Personal preferences for all projects"; project,
  `./CLAUDE.md` or `./.claude/CLAUDE.md`; local, `./CLAUDE.local.md`.
- "Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` from your current
  working directory and every directory above it." "All discovered files
  are concatenated into context rather than overriding each other."
  Subfolders' files load "once Claude reads, writes, or edits another file
  in that subdirectory".
- **It is advice, not a lock.** "Claude treats them as context, not enforced
  configuration. To block an action regardless of what Claude decides, use a
  PreToolUse hook instead." "CLAUDE.md content is delivered as a user
  message after the system prompt … there's no guarantee of strict
  compliance, especially for vague or conflicting instructions."
- What to write: "Treat CLAUDE.md as the place you write down what you'd
  otherwise re-explain." Add to it when "Claude makes the same mistake a
  second time" or "You type the same correction or clarification into chat
  that you typed last session".
- How to write: "concrete enough to verify"; "target under 200 lines per
  CLAUDE.md file. Longer files consume more context and reduce adherence";
  "if two instructions contradict each other, Claude may pick one
  arbitrarily".
- `/init` "generate[s] a starting CLAUDE.md"; `/memory` lists and opens the
  files; `/context all` shows which loaded; `/doctor prompt-audit` looks for
  "instructions written for older models, references to files or commands
  that don't exist, and files that contradict each other".
- "Project-root CLAUDE.md survives compaction: after `/compact`, Claude
  re-reads it from disk".

### AGENTS.md

Same page. "Claude Code can read `AGENTS.md` as your project instructions,
so a repository already set up for other coding agents works without adding
a `CLAUDE.md`, an import, or a setting." "By default, Claude reads
`AGENTS.md` only when you have no `CLAUDE.md` in your working directory or
above it." "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or
later." The older workarounds (a `CLAUDE.md` holding `@AGENTS.md`, a
symlink) still work and are no longer needed. Tested here: lead 7 in
[`test.md`](test.md).

### Auto memory (Claude Code's own, on your computer)

Same page. "Auto memory lets Claude accumulate knowledge across sessions
without you writing anything." "Auto memory is on by default in local
sessions." Stored at `~/.claude/projects/<project>/memory/`, a `MEMORY.md`
index plus one file per memory; "The first 200 lines of `MEMORY.md`, or the
first 25KB, whichever comes first, are loaded at the start of every
conversation." "Auto memory is machine-local." "Auto memory files are plain
markdown you can edit or delete at any time." Off: the toggle in `/memory`,
or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.

The toggle "doesn't turn it back on" in "a session that another Claude Code
session started, such as when Claude runs `claude` through its Bash tool".
The test runs here were started that way; whether auto memory was active in
them was not checked.

## Best practices page

<https://code.claude.com/docs/en/best-practices>, read 2026-11-10 in full.

- Opening: "in most cases, your first plain prompt in a fresh session
  already does the right thing, without any setup on your part."
- Two kinds of instruction: what the model reads and "decides what to do
  with" (prompt, CLAUDE.md, skills) and what Claude Code enforces (hooks,
  deny rules). "There's no *guarantee* that it'll follow your instructions."
- "Only write down what Claude can't find by reading the repo."
- "A specific prompt helps … because it gives Claude information it doesn't
  already have."
- "Interview me until you could write the spec, then write it to SPEC.md."
- "Give Claude something it can run that comes back pass or fail." "Ask
  Claude for *evidence*: the command it ran and its output … 'All tests
  pass' on its own tells you very little."
- "Watch the first minute, press `Esc` the moment Claude drifts, and after
  two failed corrections run `/clear` and write a better prompt instead of a
  third."
- `/rewind`: "roll the code, the conversation, or both back to an earlier
  prompt". Warning: "a file that only a Bash command touched isn't
  restored."
- **"What you can stop doing"**, the page's own table of retired advice:

  | Old advice | The page's verdict |
  |---|---|
  | Manage the context window aggressively | "Most current models have a 1M-token window and compaction happens on its own" |
  | "Add IMPORTANT or ALL CAPS" | "Current ones follow a plainly worded line, and piling on emphasis mostly makes Claude over-apply the rule." |
  | Subagents to protect context, or for a better answer | "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help" |
  | "`think hard`, `think harder`, `be thorough`" | "Effort is the control for that … `ultrathink` still works" |
  | "keep going, loop until done, don't be lazy" | "more likely to cause over-work than fix a stall" |
  | Describe the file layout in CLAUDE.md | "Claude reads the repo itself. Only write down what isn't in there." |

## Models and effort

<https://code.claude.com/docs/en/model-config>, read 2026-11-10 (sections:
model aliases, Work with Fable, `default` model setting, Adjust effort
level).

- Default: "Pro, Max, Ultra, Team, Enterprise, and Anthropic API: defaults
  to Opus 5.5".
- "No Fable model is the account-type default on any plan or provider.
  Select one explicitly: Fable 5.2: run `/model fable`". "Choosing one with
  `/model` saves it as the selected model in your user settings, so later
  sessions start on it".
- On Fable: "They sustain long autonomous sessions, investigate before
  acting, and verify their work more often than smaller models." "Skip the
  verification reminders: it verifies its own work with less prompting".
- "Depending on your plan and seat tier, Fable usage can bill to usage
  credits instead of drawing on your plan's included limits."
- Effort: `low`, `medium`, `high`, `xhigh`, `max`; "Fable 5.2, Opus 5.5,
  Sonnet 5.5, and Haiku 5.5 default to `medium`".
- "Fable 5.2 requires Claude Code v2.1.321 or later".

**What this means for the tests:** every run here was on
`claude-fable-5-2`, because that is what the owner's account had selected. It is
not what a new subscriber gets by default (Opus 5.5).

## Permission modes

<https://code.claude.com/docs/en/permission-modes>, read 2026-11-10
(sections: available modes, which mode a session starts in, tool calls
denied in `claude -p`, plan mode, boundaries stated in conversation).

- Modes: Manual ("Reads only" without asking), `acceptEdits`, `plan`,
  `auto` ("Everything, with background safety checks"), `dontAsk`,
  `bypassPermissions` ("Isolated containers and VMs only").
- Interactive terminal sessions start in auto mode (built-in default since
  v2.1.228). "`claude -p` … runs with no permission mode set start in Manual
  mode", so a scripted run needs `--permission-mode auto` or allow rules.
- Plan mode: "Claude reads files, runs shell commands to explore, and writes
  a plan, but does not edit your source." `Shift+Tab`, or `/plan` before one
  prompt.
- "If you tell Claude 'don't push' or 'wait until I review before
  deploying', the classifier blocks matching actions … a boundary can be
  lost if context compaction removes the message that stated it. For a hard
  guarantee, add a deny rule instead."

## Checkpoints

<https://code.claude.com/docs/en/checkpointing>, read 2026-11-10 (first
sections). "Every prompt you send that starts a turn creates a new
checkpoint." `/rewind` or `Esc` twice opens the menu.

## Changelog

<https://code.claude.com/docs/en/changelog>, read 2026-11-10, top two
entries only.

- 2.1.322, 10 November 2026.
- 2.1.321, 9 November 2026: "Added Claude Fable 5.2 (`claude-fable-5-2`),
  now the default Fable model — 1M context, $8/$40 per Mtok with $0.20/Mtok
  cache reads". (API prices in US dollars per million tokens; they do not
  apply to subscription use.)

## Prompting guide (Claude Platform docs)

<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>,
read 2026-11-11 (General principles; the hallucination section).

- "Think of Claude as a brilliant but new employee who lacks context on
  your norms and workflows."
- "Providing context or motivation behind your instructions, such as
  explaining to Claude why such behavior is important, can give Claude more
  information about your goals". Example given: "NEVER use ellipses" against
  a sentence explaining that the text will be read aloud.
- "XML tags help Claude parse complex prompts unambiguously, especially when
  your prompt mixes instructions, context, examples, and variable inputs."
- "Setting a role in the system prompt focuses Claude's behavior and tone".
  This is written for developers setting a system prompt, not for a chat
  message.
