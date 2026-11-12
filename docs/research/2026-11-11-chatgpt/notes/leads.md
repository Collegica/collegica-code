# Leads: tips repeated about ChatGPT and Codex, and what became of them

Collected 11 November 2026 by generic web searches naming no person, site
or project. Reddit threads appear as archived snapshots
(reddit.sentinel-team.org), because reddit.com does not serve plain page
text; none was opened beyond the search result. No YouTube video was
watched: searches returned written summaries only. Nothing here is a
source for the article on its own: a lead counts only once it is *passed*
in [`test.md`](test.md) or stated on a vendor page (noted with the page).

| # | The tip | Where it is repeated | Status |
|---|---|---|---|
| 1 | Write rules in capitals, with IMPORTANT, MUST, NEVER, so they are followed | Common in shared instruction files; the same advice is tested in the Claude guide | **Failed** (test.md, lead A): plain wording already scored 10 of 10 in three runs out of three; capitals added nothing. |
| 2 | Codex reads only `AGENTS.md`; a `CLAUDE.md` is ignored, so symlink `CLAUDE.md` to `AGENTS.md` or keep one file | [A gist on symlinking](https://gist.github.com/yurukusa/d36197848911f025add142abefcde685); [a write-up on cross-tool instruction files](https://codex.danielvaughan.com/2026/05/27/agent-instruction-files-agents-md-claude-md-cross-tool-portability-codex-cli/); [a pull request replacing CLAUDE.md with a symlink](https://github.com/jdx/usage/pull/618) | **Passed as stated, no difference here** (test.md, lead B): `CLAUDE.md` was not loaded as instructions in three runs out of three, but Codex opened it with the other files and followed it. The vendor page confirms only listed names are read. |
| 3 | After a mistake, have it update `AGENTS.md` so the next session knows | OpenAI's own best-practice page; [OpenAI community thread "Why does Codex repeat the same mistakes?"](https://community.openai.com/t/why-does-codex-repeat-the-same-mistakes/1383615) | **Passed** (test.md, lead D): the next session followed every rule in three runs out of three. |
| 4 | Turn the reasoning effort up (high, xhigh) for better answers | [A 26-task comparison of effort levels](https://www.stet.sh/blog/gpt-55-codex-graphql-reasoning-curve); [OpenAI community thread on choosing a level](https://community.openai.com/t/how-to-decide-a-level-of-reasoning/1374651); [Reddit snapshot](https://reddit.sentinel-team.org/posts/1sjuwux/snapshots/2026-04-18T00%3A03%3A06.91994Z) | **Failed to show a difference** (test.md, lead C): `high` gave the same answer as `low` on the fees question, slower and dearer. The vendor's own advice is "Low for faster, well-scoped tasks". |
| 5 | Plan first: use plan mode, or ask for a plan and approve it before it changes files | [Codex best-practice summaries](https://codex.danielvaughan.com/2026/04/12/codex-cli-best-practices-workflow-maturity-model/); OpenAI's best-practice page ("ask Codex to plan before it starts coding") | Tested only as task 3's "tell me your plan, then stop" (passed three of three; it said how it checked). Interactive `/plan` not tested. |
| 6 | `AGENTS.md` instructions "are not reliably followed across tasks" | [OpenAI community thread](https://community.openai.com/t/agents-md-and-project-markdown-instructions-are-not-reliably-followed-across-tasks/1404089) | Not borne out on this task: the house rules held in 9 runs out of 9 where they were in `AGENTS.md` (task 2 practice; lead A; lead D, turn 3). |
| 7 | A long `AGENTS.md` is silently cut off, so rules at the end are ignored | [openai/codex issue #13386](https://github.com/openai/codex/issues/13386) | Untested. The vendor page states the limit: `project_doc_max_bytes`, 32 KiB by default. |
| 8 | The global `~/.codex/AGENTS.md` is not loaded | [openai/codex issue #8759](https://github.com/openai/codex/issues/8759) | Untested: testing it means editing the owner's `~/.codex`, which is off limits. |
| 9 | Keep `AGENTS.md` short; delete any rule it already follows without being told | [A guide to lean instruction files](https://codex.danielvaughan.com/2026/06/15/agents-md-beyond-init-writing-project-instructions-that-reduce-token-spend-hooks-mcp-skills/); [OpenAI community tips thread](https://community.openai.com/t/tips-and-tricks-for-using-codex/1373143) | Untested as a tip. Vendor: "A short, accurate `AGENTS.md` is more useful than a long file full of vague rules." Task 2 plain shows which rules this model kept unasked (date in full, British spelling, length). |
| 10 | Start with `/init` to write the first `AGENTS.md` | Same tips thread; many blog guides | Untested (interactive). Vendor slash-command page: "Generate an `AGENTS.md` scaffold for the current project." |
| 11 | Custom instructions: keep them short, ask for a direct tone, no filler | Reddit snapshots, e.g. [May 2026](https://reddit.sentinel-team.org/posts/1t56yjy/snapshots/2026-05-08T18%3A10%3A01.312472Z), [March 2026](https://reddit.sentinel-team.org/posts/1rm0gdk/snapshots/2026-03-06T18%3A55%3A51.538717Z) | Untested: custom instructions live in the chat app's settings. |
| 12 | Ask it to interview you, or to ask clarifying questions, before it answers | [Martech](https://martech.org/want-better-answers-from-ai-tell-it-to-ask-questions/); [Tom's Guide](https://tomsguide.com/ai/local-ai-taught-me-a-better-way-to-use-chatgpt-and-it-starts-with-one-sentence) | Untested: `codex exec` has no one to answer. |
| 13 | Ask "What are you unsure about?" at the end | [TechRadar](https://www.techradar.com/ai-platforms-assistants/chatgpt/ask-chatgpt-what-are-you-unsure-about-its-the-simplest-trick-ive-found-for-getting-better-responses) | Close to task 1 practice ("list anything you were unsure about"), which brought out the 26 August heading and the unassigned soup. Not tested on its own. |
| 14 | Say "only from these files" so it does not guess | Widely repeated; OpenAI's prompting page has "Use only the supplied sources. Flag missing information instead of guessing." | Task 5: plain and careful both right in three runs out of three; the careful prompt added the figures the files do hold. |

## Searches made

"Codex CLI tips AGENTS.md reddit r/codex best practices 2026"; "ChatGPT
prompt tips custom instructions reddit r/ChatGPT 2026 what actually works";
"github openai/codex issue AGENTS.md instructions ignored"; "Codex reasoning
effort high vs low better results reddit codex tip"; "symlink CLAUDE.md
AGENTS.md Codex Claude Code same instructions file tip"; "ChatGPT tips ask
me questions before answering prompt trick youtube 2026"; and, limited to
openai.com, the training switch (see `2026-11-11-data.md`).
