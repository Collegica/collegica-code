# Leads: tips repeated about Gemini, and what became of them

Collected 2026-11-11 by generic web searches. Reddit threads were read
through archived snapshots (reddit.sentinel-team.org), because reddit.com does
not serve plain page text. Nothing here is a source for the article on its
own: a lead counts only once it is *passed* in [`test.md`](test.md) or stated
on a vendor page (noted with the page).

**None was tested.** The `gemini` command-line app could not sign in (see
`test.md`), so every lead is still *untested*. Where Google's own page says
the same or the opposite, that is noted; it does not change the status.

| # | The tip | Where it is repeated | Status |
|---|---|---|---|
| 1 | Write a prompt with four parts: persona, task, context, format | Google's *Prompting guide 101* for Workspace ([PDF](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf), 2024 edition, not read in full); repeated by [Android Authority](https://www.androidauthority.com/gemini-prompt-guide-3433163/) | Untested. Vendor-origin but from 2024, before the current models. Close to task 1's "brief" practice. |
| 2 | Keep prompts short: the "average successful prompt is about 21 words" | [Android Authority](https://www.androidauthority.com/gemini-prompt-guide-3433163/), quoting the same guide | Untested. The figure is from secondary coverage; the search did not find it in the PDF. It pulls against lead 1 and against task 1's brief. |
| 3 | Start a new chat for each new task, because Gemini uses the whole conversation | Workspace *Prompting guide 101* (as lead 1) | Untested. |
| 4 | Say "Using only the linked files" so it answers from your documents | [A productivity newsletter](https://www.jeffsu.org/newsletter-224/); the opposite reported on Google's forum: ["Gemini ignored constraints, injected external data, and failed to read file uploads"](https://discuss.ai.google.dev/t/gemini-ignored-constraints-injected-external-data-and-failed-to-read-file-uploads-google-sheets/110854) | Untested. This is task 5's practice; the planned test would have answered it. |
| 5 | Gemini skips large parts of a long uploaded document; split it into smaller files | r/GoogleGeminiAI, "Gem not sticking to knowledge" ([snapshot, 20 Mar 2026](https://reddit.sentinel-team.org/posts/1rx37ql/snapshots/2026-03-20T16%3A36%3A18.942598Z)), a commenter's observation | Untested. |
| 6 | Gemini CLI ignores `GEMINI.md`; override the system prompt (`GEMINI_SYSTEM_MD`) to fix it | r/GeminiAI, "Gemini CLI kept ignoring my repo docs" ([snapshot, 8 May 2026](https://reddit.sentinel-team.org/posts/1t2p5sk/snapshots/2026-05-08T20%3A30%3A05.637131Z)) | Untested. Task 2 practice would have tested the first half. |
| 7 | Point Gemini at `AGENTS.md` so one instruction file serves every assistant | Cheatsheets such as [Phil Schmid's](https://www.philschmid.de/gemini-cli-cheatsheet) | Untested. Vendor: Gemini CLI reads other names if `context.fileName` is set in settings; Antigravity reads `AGENTS.md` without a setting (migration guide). |
| 8 | Save standing preferences with `/memory add` | [Phil Schmid's cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet); [Addy Osmani's tips](https://addyosmani.com/blog/gemini-cli/) | Untested (interactive, and Gemini CLI only). |
| 9 | Turn on checkpointing, and undo with `/restore` | [Addy Osmani's tips](https://addyosmani.com/blog/gemini-cli/) | Untested. |
| 10 | Keep secrets out with a `.geminiignore` file | [Addy Osmani's tips](https://addyosmani.com/blog/gemini-cli/); [dev.to](https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b) | Untested. |
| 11 | Do not run in YOLO mode on a folder you care about | [dev.to](https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b); [Gemini CLI settings docs](https://geminicli.com/docs/cli/settings/) | Untested. `gemini --help`: `yolo` "auto-approve all tools"; `auto_edit` approves only edits. |
| 12 | Plan first: `/plan` or `--approval-mode plan` (read-only) before letting it change files | [Gemini CLI settings docs](https://geminicli.com/docs/cli/settings/); [cheatsheets](https://cheatsheets.zip/gemini-cli) | Untested. This is task 3's practice. `gemini --help` lists `plan (read-only mode)`; `agy` has `--mode plan`. |
| 13 | Keep the temperature at 1.0 with Gemini 3; do not lower it for "accuracy" | [Phil Schmid, "Gemini 3 prompting"](https://www.philschmid.de/gemini-3-prompt-practices); Google's Vertex AI Gemini 3 prompting guide (returned "Page Not Found" on 2026-11-11) | Untested. Only for people using the API; the app and the CLIs have no temperature setting for a beginner. |
| 14 | Put standing context in the Gem, not in Saved Info, so it applies only to that task | [geotoolbox.ai](https://geotoolbox.ai/blog/gemini-gems) | Untested, and overtaken: Gems become read-only on 17 November 2026 and are replaced by skills (Gemini Apps Help, read 2026-11-11). |
| 15 | Gemini CLI's free tier is gone; here are workarounds | [dev.to, "Gemini CLI free tier shut down: 6 fixes"](https://dev.to/owen_fox/gemini-cli-free-tier-shut-down-6-fixes-that-work-2026-26hc) | Not a practice. Confirmed by Google (deprecation page and transition post) and by the test attempt here. |

## Searches made

Generic, naming no person, site or project: "Gemini CLI 'no longer supported
for Gemini Code Assist for individuals' Antigravity"; "Gemini app tips reddit
Gems instructions saved info best practices 2026"; "gemini-cli github issue
GEMINI.md instructions ignored"; "Gemini prompting tips persona task context
format 'Gemini for Workspace prompt guide'"; "Gemini 3 prompting tips
temperature 1.0 shorter prompts 'be direct' developers"; "Gemini CLI tips
reddit /memory add plan mode checkpointing YOLO .geminiignore"; "Gemini app
makes up numbers from uploaded spreadsheet 'only use the file' tip
hallucination". No X post or YouTube video came back as a primary result; none
is listed.
