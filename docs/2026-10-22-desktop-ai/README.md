# AI on your own files — plan and research

Plan and notes for an AI article on using an assistant as a desktop or
terminal app working on local files, rather than a browser chat: Claude
Desktop and Claude Code, the ChatGPT desktop app and Codex, and Hermes
Desktop. Started 2026-10-22. Draft: `website/ai/desktop-agents/index.md`
(`draft: true` until reviewed).

Audience: non-programmers who use a chat assistant and have not yet given one
a folder. Follows [`2026-09-13-local-agent`](../2026-09-13-local-agent/README.md),
which set up the local-model path this article points to for private files.

## What was verified, and how

| Topic | Notes | Checked against |
|---|---|---|
| Claude Desktop, Cowork, Claude Code | [`notes/anthropic.md`](notes/anthropic.md) | Anthropic's docs and support pages, 2026-10-22 |
| ChatGPT desktop app, Codex | [`notes/openai.md`](notes/openai.md) | learn.chatgpt.com (Markdown), help.openai.com in a browser, the Codex repo |
| Hermes Agent and Desktop since v0.21.2 | [`notes/hermes.md`](notes/hermes.md) | v0.22.0 release notes (`gh`), Hermes docs |
| Why files beat pasting; standards; risk; privacy | [`notes/why-local-files.md`](notes/why-local-files.md) | Anthropic engineering and research posts, METR, Willison, Meta, agents.md, agentskills.io, modelcontextprotocol.io |

One task was run in all three terminal apps on a made-up receipts folder,
timed and graded against an answer key: [`notes/test.md`](notes/test.md),
with the generator, prompt, key and every output in [`example/`](example/).
Hermes providers and OpenRouter's pricing, logging and free-tier limits were
read on OpenRouter's own docs (added on request, 2026-10-22).

## Decisions

1. **Benefits first, products second.** The argument (context, files out,
   persistent instructions, MCP, the terminal) holds for all three; the
   products change monthly.
2. **"A folder is not a model" gets its own section.** It is the confusion
   that matters most for privacy, and both hosted vendors say it plainly.
3. **Say the evidence is from coding.** No study of non-programmers was found;
   the 79%/49% figure and METR's 19% are both from developers.
4. **Date the moving parts.** Cowork folding into Claude (16 Sept), cloud
   tasks for Pro/Max (6 Oct), the ChatGPT app merge (9 July), Hermes 0.22
   (13 Oct).

## Open

- Max's upper price and whether Claude's consumer training switch starts on
  or off: not confirmed from a primary source; the draft avoids both.
- Hermes telemetry: the FAQ says none; v0.22.0 adds opt-in metrics, default
  off. The draft says "only if you say yes".
- Hero: `hero.md` and `hero-original.png` (eight-dot mark fixed, as before).
- The desktop apps themselves were not timed, only their terminal twins.
