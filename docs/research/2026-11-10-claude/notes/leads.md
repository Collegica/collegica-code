# Leads: tips repeated about Claude, and what became of them

Collected 2026-11-10 and 2026-11-11 by generic web searches. Reddit threads
were read through archived snapshots (reddit.sentinel-team.org), because
reddit.com does not serve plain page text; the original thread address is
given where the snapshot shows it. GitHub issues were read through the
GitHub API. Nothing here is a source for the article on its own: a lead
counts only once it is *passed* in [`test.md`](test.md) or stated on a
vendor page (noted with the page).

| # | The tip | Where it is repeated | Status |
|---|---|---|---|
| 1 | Write rules in capitals, with IMPORTANT or YOU MUST, so Claude follows them | Common in instruction files shared on GitHub; GitHub issues such as [#17530](https://github.com/anthropics/claude-code/issues/17530) report rules "systematically ignored" even with "MUST/ALWAYS" wording | **Failed** (test.md, lead 1): plain wording already scored 10 of 10 in three runs out of three; capitals added nothing. The vendor's best-practice page now lists it under "What you can stop doing". |
| 2 | Claude Code ignores `AGENTS.md`; you need a `CLAUDE.md`, or a `CLAUDE.md` that imports it | Long-standing advice from 2025, when Claude Code read only `CLAUDE.md` | **Failed** (test.md, lead 2): read and followed in three runs out of three. The memory page says it reads `AGENTS.md` itself since v2.1.277. |
| 3 | After every correction, tell it "Update your CLAUDE.md so you don't make that mistake again" | Boris Cherny's ten tips, summarised on r/ClaudeAI: [snapshot, 1 Feb 2026](https://reddit.sentinel-team.org/posts/1qspcip/snapshots/2026-02-01T18%3A46%3A41.013311Z) (original on [X](https://x.com/bcherny/status/2017742741636321619)) | **Passed** (test.md, lead 3), on Sonnet 5.5: the next session followed every rule in three runs out of three. The memory page says the same: add to it when "Claude makes the same mistake a second time". |
| 4 | Say `ultrathink`, or "think hard", for a better answer | Widely repeated; r/ClaudeAI [snapshot, 8 Feb 2026](https://reddit.sentinel-team.org/posts/1qyrnti/snapshots/2026-02-08T00%3A46%3A08.892315Z) on effort | **Failed to show a difference** (test.md, lead 4), on a different model; inconclusive. The best-practice page: "think hard … be thorough" are "ordinary prompt text"; effort is the control; `ultrathink` "still works" for one turn. |
| 5 | Start every complex task in plan mode; review the plan before it writes anything | Cherny's tips (as lead 3); r/ClaudeAI [snapshot, 18 Apr 2026](https://reddit.sentinel-team.org/posts/1sn27yu/snapshots/2026-04-18T01%3A10%3A06.838236Z), [snapshot, 27 Feb 2026](https://reddit.sentinel-team.org/posts/1rfwmlh/snapshots/2026-02-27T22%3A56%3A52.470321Z); [Builder.io](https://site.builder.io/blog/claude-code-tips-best-practices) | Tested only through task 3's "tell me your plan, then stop": the result was the same as without; the plan made it say how it checked. Plan mode itself (`Shift+Tab`) is interactive and was not tested. |
| 6 | Put your project structure, stack and conventions in `CLAUDE.md` | r/ClaudeAI [snapshot, 27 Feb 2026](https://reddit.sentinel-team.org/posts/1rfwmlh/snapshots/2026-02-27T22%3A56%3A52.470321Z), [snapshot, 8 Feb 2026](https://reddit.sentinel-team.org/posts/1qyrnti/snapshots/2026-02-08T00%3A46%3A08.892315Z) | **Contradicted by the vendor**, untested: "Describe your architecture and file layout in `CLAUDE.md`" is in the best-practice page's "What you can stop doing": "Claude reads the repo itself. Only write down what isn't in there." |
| 7 | Run `/compact` when a session gets long; starting a new session is "way more disruptive" | r/ClaudeAI [snapshot, 8 Feb 2026](https://reddit.sentinel-team.org/posts/1qyrnti/snapshots/2026-02-08T00%3A46%3A08.892315Z) | Untested (interactive). The vendor says the opposite for unrelated work: "`/clear` between unrelated tasks", and after two failed corrections "run `/clear` and write a better prompt". |
| 8 | Ask Claude to interview you, or to ask clarifying questions until it is "95% confident" | Many blogs and threads, e.g. [a collected tip](https://claude-tips.pages.dev/tips/interview-me-first) | Untested: `claude -p` has no one to answer. The vendor page gives its own version: "Interview me until you could write the spec, then write it to SPEC.md." |
| 9 | Give it a role: "You are a senior accountant…" | Third-party prompt guides; Anthropic's prompting guide has "Give Claude a role" | Not run (cap of four). The vendor's advice is about the *system prompt*, which a chat user does not write. |
| 10 | Use subagents to keep the context clean, or for a better answer | Cherny's tips (as lead 3); r/ClaudeAI threads above | Untested. The best-practice page: "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help". |
| 11 | Ask for the first step only, review it, then the next | r/ClaudeAI [snapshot, 18 Apr 2026](https://reddit.sentinel-team.org/posts/1sn27yu/snapshots/2026-04-18T01%3A10%3A06.838236Z) | Untested. |
| 12 | End each session with "what did you learn?" and save it | r/ClaudeAI [snapshot, 18 Apr 2026](https://reddit.sentinel-team.org/posts/1sn27yu/snapshots/2026-04-18T01%3A10%3A06.838236Z) | Untested; close to lead 3, which passed. Note that Claude Code's auto memory now does part of this itself (memory page). |
| 13 | Claude Code "ignores" `CLAUDE.md` | Dozens of GitHub issues; the umbrella request [#13689](https://github.com/anthropics/claude-code/issues/13689) is open; [#27032](https://github.com/anthropics/claude-code/issues/27032) closed | Not borne out on this task: the house rules held in 12 runs out of 12 where they were in an instruction file (task 2 practice; leads 1, 2 and 3, step 3). The vendor says it is "context, not enforced configuration"; for a rule that must hold, use a hook or a deny rule. |

## Searches made

Generic, naming no person, site or project: "Claude Code tips reddit
r/ClaudeAI CLAUDE.md ultrathink plan mode"; "anthropics/claude-code github
issue CLAUDE.md instructions ignored"; "Claude prompt tips XML tags
IMPORTANT all caps role prompting"; "youtube Claude Code tips beginners
CLAUDE.md plan mode"; "Claude tip ask me clarifying questions interview me".
YouTube results came back only as third-party summaries of videos; no video
was watched, so none is listed.
