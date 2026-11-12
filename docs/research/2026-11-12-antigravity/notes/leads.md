# Leads: widely repeated Antigravity tips

Collected 12 November 2026 from generic web searches (no names of the owner,
the site or the project). All *untested* unless marked. The owner's answer of
12 November allows at most two lead tests after the quota resets on
18 November; the two marked ★ are proposed.

| # | Lead | Where | Status |
|---|---|---|---|
| 1 ★ | Keep `GEMINI.md` from Gemini CLI: Antigravity reads it as well as `AGENTS.md`, no rename needed | [15 Antigravity CLI tips (Medium)](https://medium.com/google-cloud/15-antigravity-cli-tips-ddbc21c10a20); Google's migration page says the same | vendor-stated; test: task 2 with the house rules as `GEMINI.md` |
| 2 | Put instructions for every project in `~/.gemini/AGENTS.md` | [15 Antigravity CLI tips](https://medium.com/google-cloud/15-antigravity-cli-tips-ddbc21c10a20) | vendor-stated (rules page); not tested (would mean editing the owner's global file) |
| 3 | Run `agy inspect` first to see what context the agent has | [agentpedia: agy CLI errors](https://agentpedia.codes/blog/agy-cli-errors-troubleshooting) | **failed by inspection**: 1.5.6's `agy --help` lists no `inspect` subcommand (it is Grok Build's command) |
| 4 | Long instruction files burn quota up to three times faster | [agentpedia: GEMINI.md guide](https://agentpedia.codes/blog/antigravity-gemini-md-system-prompt-guide) | untested; no measurement given |
| 5 | The quota is shared across the app, CLI and SDK, so parallel agents drain it faster | [Google AI developer forum](https://discuss.ai.google.dev/t/antigravitys-usage-quota-is-very-restrictive/146716) | partly seen: three runs in parallel used 17% of a weekly limit and two hit 429 errors |
| 6 ★ | Plan with a stronger model, implement with a cheaper one | [Google AI developer forum: pro tips](https://discuss.ai.google.dev/t/pro-tips-for-using-google-antigravity/116201) | untested; the free tier has only Gemini 3.8 Flash among Gemini models. Alternative test: task 3 with `--mode plan` for turn 1 |
| 7 | Ask for a task list and implementation plan, edit it, then execute | [Google AI developer forum: pro tips](https://discuss.ai.google.dev/t/pro-tips-for-using-google-antigravity/116201) | vendor-stated ("Explore, plan, then execute"); this is task 3's practice |
| 8 | Allow routine build and test commands, block `ssh` and `sudo` | [Google AI developer forum: pro tips](https://discuss.ai.google.dev/t/pro-tips-for-using-google-antigravity/116201) | vendor-supported (`permissions.allow`); not tested |
| 9 | Keep the folder in git and commit working states, so a bad run is easy to undo | [Google AI developer forum: pro tips](https://discuss.ai.google.dev/t/pro-tips-for-using-google-antigravity/116201) | untested; general advice |
| 10 | Start in review mode rather than full auto | [Pasquale Pillitteri: complete guide](https://pasqualepillitteri.it/en/news/29239/how-to-use-google-antigravity-complete-guide) | untested; `auto` is not offered on this account anyway |
| 11 | Test each imported Gemini CLI extension before relying on it; parity is partial | [Google's migration page](https://antigravity.google/docs/cli/gcli-migration) ("Partial parity") | vendor-stated |
| 12 | Write a test first, then ask it to run the tests after each change | [Google's CLI best practices](https://antigravity.google/docs/cli/best-practices) | vendor-stated; close to task 4's practice ("how you checked") |
