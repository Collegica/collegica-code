# Projects and memory in the Claude apps: notes

Anthropic's support pages, read as the pages' own text on 2026-11-10 and
2026-11-11. None of this was tested: projects and memory live in the chat and
desktop apps, which the command-line app does not reach. See *For the owner*
in [`../README.md`](../README.md).

## Projects

<https://support.claude.com/en/articles/9517075-what-are-projects>, read
2026-11-10 ("Updated over a week ago"), and
<https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>,
read 2026-11-11 ("Updated this week").

- "Projects allow you to create self-contained workspaces with their own
  chat histories and knowledge bases."
- "Projects are available to all users, including those with free Claude
  accounts. Free users can create a maximum of five projects."
- Knowledge: "Anything you upload to this space will be used across all of
  your chats within that project."
- Instructions: "Click on 'Set project instructions.' … Claude will use
  these instructions for all the chats within the project."
- "Context is not shared across chats within a project unless the
  information is added into the project knowledge base."
- The name and description are for you: "note that Claude will not have
  access to these details".
- Paid plans: "When your project knowledge approaches context limits, Claude
  seamlessly enables RAG mode to expand capacity by up to 10x".
- Sharing a project is for Team and Enterprise only.

**A new version of projects is in beta.** "A new version of projects is now
available in beta, rolling out in stages starting with Claude Code." "In the
new version, a project is one conversation: you say what you need as it
comes to you, and Claude breaks the work into parallel threads that run in
the cloud." "Every thread starts with the project's files, repositories,
instructions, and memory". It is "available in beta to select Pro, Max, and
Ultra subscribers who use Claude Code", shown as "'Projects' in the sidebar
at claude.ai/code and in the Code tab of the Claude desktop app". Existing
projects are being moved: "Nothing is lost or deleted in the move." "Running
several threads at once uses [your plan's usage] faster."

## Memory and chat search

<https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>,
read 2026-11-10 ("Updated today").

- **Chat search**: "available to users on paid plans (Pro, Max, Ultra, Team,
  and Enterprise plans)". "Enabled by default." It searches "all chats
  outside of projects" and, inside a project, that project's chats only. Off
  switch: "Settings > Your Claude (or Settings > Memory in the older Settings
  layout)", "Search and reference chats".
- **Memory**: "Memory is on by default for Free, Pro, Max, and Ultra plans
  on the web, Claude Desktop, and Claude Mobile".
- "Claude saves memory as a set of individual topics as you chat, rather than summarizing conversations after they end. Mention that a deadline moved, and your next conversation already knows." (read 2026-11-10) "You can also tell Claude
  to 'remember this'."
- **Project memory**: "Each project has its own memory. While working in a
  project, Claude uses the project's memory alongside your memory from chats
  outside of projects, but not memory from other projects." To separate it
  fully: turn off "Use account memory" on the project's page.
- **Cowork**: memory is shared between chat and Cowork "when Cowork runs in
  the cloud; Cowork sessions that run locally on your computer don't use
  memory".
- **Switching it off**: "Settings > Your Claude", "Generate memory from
  chats". Two choices: "Pause memory" (kept, not used, nothing new saved) or
  "Reset memory" ("Permanently deletes all memories including project
  memories … this cannot be undone").
- **One chat without memory**: new chat, "+" in the message box, turn off
  "Memory", before the first message. "Unlike an incognito chat, the chat
  stays in your chat history."
- **Seeing it**: "Settings > Your Claude by selecting 'Manage' next to Your
  memory … Everything Claude remembers is listed under Topics." Each topic
  can be edited or deleted.
- **Sensitive topics**: "By default, Claude does not store topics related to
  personal or sensitive subject matter, like your health, race, ethnicity,
  religious beliefs, politics, gender identity". "Some information is never
  saved to memory, even if you ask. This includes government ID numbers,
  criminal history, financial account numbers, and immigration status."
- **Deleting a chat does not delete what was remembered from it**: "When a
  conversation is deleted, including under a retention period, memory
  entries generated from it aren't removed, but you can delete individual
  memories while memory is on."

## Moving memory between assistants

<https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude>,
read 2026-11-11. "Memory imports are available for Free, Pro, Max, Ultra,
Team, and Enterprise plans on the web and Claude Desktop." The page gives a
prompt to paste into the other assistant to list what it holds.

## Incognito chats

<https://support.claude.com/en/articles/12260368-use-incognito-chats>, read
2026-11-11. All plans. Not saved to history or memory, "not used for
training", but "retained for either 30 days (default)". "If you have the new
Claude experience, incognito chats open in the previous chat experience, so
Claude can't create files or run code in them."

## Memory in Claude Code is a different thing

Claude Code's "auto memory" is files on your own computer, not the apps'
memory. See [`claude-code.md`](claude-code.md).
