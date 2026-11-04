# A business wiki an AI keeps: worked example

The example behind the Collegica article *One Place for the Truth*. A small
(fictional) catering company keeps its raw material in `sources/` and lets an
AI assistant maintain `wiki/` by the rules in `AGENTS.md`: Andrej Karpathy's
"LLM wiki" pattern, with a few fields from the Open Knowledge Format so every
page says where its facts came from, who wrote it, and whether a person has
checked it.

| Folder or file | What it is |
|---|---|
| `sources/` | Raw material, never edited: an old FAQ, a price list, a supplier letter, meeting notes, a customer email |
| `wiki/` | What the assistant wrote from them (the run is described in `RUN.md`) |
| `AGENTS.md` | The rulebook: page format, ingest, answer, lint |
| `CLAUDE.md` | One line, so Claude Code reads `AGENTS.md` too |

## Try it

Copy the folder, delete `wiki/` except `index.md` and `log.md`, open it in an
assistant that can work on a folder (Claude Code, Claude Desktop, ChatGPT's
desktop app with a folder, Codex), and ask, one at a time:

1. "Ingest every file in sources/, oldest first."
2. "Answer the customer email in sources/2026-10-21-customer-email.txt."
3. "Lint the wiki."

Then read `wiki/open-questions.md`: that's the list of things only you can decide.
