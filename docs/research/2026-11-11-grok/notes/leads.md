# Leads: widely repeated Grok tips

Collected 11 November 2026 from generic web searches (no names of the owner,
the site or the project in any query). Each is a lead under the source rule:
*untested* until run here, then *passed* or *failed*. The four marked ★
were tested on 11 November 2026, three runs each, in Grok Build 1.0.70 on
grok-4.7 (reported `grok-4.7-build`); details in `test.md`, *Leads*.

| # | Lead | Where | Status |
|---|---|---|---|
| 1 ★ | Put your standing rules in `AGENTS.md`; it carries across Grok, Codex and Claude "better than people expect" | [Reddit, a Grok Build starter repo thread (mirror), May 2026](https://reddit.sentinel-team.org/posts/1tnrbmv/snapshots/2026-05-29T21%3A52%3A51.006629Z) | task 2's practice, `AGENTS.md`: rules held 10/10 in 3 of 3, but so did the plain prompt; notices shorter |
| 2 ★ | Grok reads your `CLAUDE.md` as well, so one file serves both | [docs.x.ai AGENTS.md page](https://docs.x.ai/build/features/project-rules) | **passed**: house rules as `CLAUDE.md` only, 10/10 in 3 of 3, and `grok inspect` lists the file |
| 3 ★ | Start multi-file work in plan mode and approve the plan before it edits | [xAI launch post](https://x.ai/news/grok-build-cli); [mer.vin](https://mer.vin/2026/05/grok-build-cli-xai-terminal-coding-agent-with-plan-mode-subagents-and-headless-ci/) | **passed, with a caveat** (re-marked 11 November 2026 under v2.1): plain prompt in plan mode, then "go ahead": `check_t3.py --plain` passed 3 of 3 and it said how it checked in 2 of 3 (plain without plan mode: 0 of 3). It follows its own plan: `notes/README.md` as the index in 2, a change to the folder's `README.md` in 1, both announced in the plan |
| 4 ★ | Grok 4.6 is wordy; rein it in with a line in `AGENTS.md` | [Cursor forum thread](https://forum.cursor.com/t/managing-output-verbosity-in-grok-4-6-vs-gpt-models-best-practices-for-agents-md-and-openspec/169862) | **passed** for length: "Keep every reply to ten lines or fewer" held in 3 of 3 and roughly halved the words (123–152 against 215–266); marks 8, 8, 8 against 9, 9, 9 |
| 5 | Run `grok inspect` before trusting a run, to see which rules and servers loaded | [layer3labs guide](https://www.layer3labs.io/guides/how-to-use-grok-build) | vendor-stated (docs.x.ai); not run as a test, but it was what showed Claude Code's files loading and `AGENTS.md` not loading in an untrusted folder |
| 6 | Keep secrets and build output out with a `.grokignore` file | [awesome-grok-build best practices](https://raw.githubusercontent.com/DominikTobureto/awesome-grok-build/9125e026dddc2c3e5884f2db5cc56436c7e71665/docs/best-practices.md) | **failed**: with `members.csv` in `.grokignore`, Grok read it and gave the total in 3 of 3. No `.grokignore` appears in xAI's docs or the 1.0.70 user guide |
| 7 | Talk to Grok directly and conversationally; it does best zero-shot with plain requests | [grok-prompting skill page](https://skillselion.com/skills/duyet/claude-plugins/grok-prompting) | untested |
| 8 | Put instructions in a Project's instructions rather than global custom instructions | [r/LoveGrok summary](https://go.tabbit.ai/model/grok-4-6/prompts/reddit-lovegrok-project-instructions-and-positive-constraints) | untested; chat only |
| 9 | Workspace instructions override your global custom instructions | [Arsturn guide](https://arsturn.com/blog/how-to-write-the-best-custom-instructions-for-grok-4-a-deep-dive) | untested; chat only; no xAI page found |
| 10 | Ask for confident answers, "no hedging language" | [Skillademia cheat sheet](https://skillademia.com/cheat-sheets/grok/) | untested; risks the opposite of task 5's practice |
| 11 | Use Think for logic and maths, DeepSearch for research, and ask it to cite sources | [Skillademia cheat sheet](https://skillademia.com/cheat-sheets/grok/); [Ruben's Substack](https://ruben.substack.com/p/how-to-better-use-ai-before-prompting) | untested; chat only, and mode names may be out of date |
| 12 | Start a fresh chat when switching into Think mode; it forgets the switch mid-chat | [r/grok thread, March 2025 (mirror)](https://redlib.ssps.io/r/grok/comments/1j6ywh8/grok_3s_think_mode_is_terrible) | untested; about Grok 3, likely out of date |
| 13 | Grok has no custom-instructions box; it uses memory for personalisation | [MemoryPlugin blog](https://blog.memoryplugin.com/how-grok-memory-works/) | untested; contradicts lead 9; for the owner to check in the app |
| 14 | The `grok` command may not be xAI's: an open-source `grok-cli` installs the same name | [issoh.co.jp](https://www.issoh.co.jp/tech/details/8078/) | **checked**: the installed `grok` is xAI's Grok Build (`notes/2026-11-11-installed-grok.md`) |
