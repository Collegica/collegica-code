# Apps, plans and models

Read on 11 November 2026. OpenAI's documentation for ChatGPT and Codex now
lives at learn.chatgpt.com; the older developers.openai.com/codex addresses
redirect there. Each page was read as its Markdown twin (the page address
with `.md` added), downloaded with `curl`, except where marked.

## Pages read

| Page | Address | How |
|---|---|---|
| Models | <https://learn.chatgpt.com/docs/models.md> | Markdown, whole page |
| Pricing (ChatGPT Work and Codex) | <https://learn.chatgpt.com/docs/pricing.md> | Markdown, whole page |
| Model selection | <https://learn.chatgpt.com/docs/model-selection.md> | Markdown, whole page |
| ChatGPT desktop app | <https://learn.chatgpt.com/docs/app.md> | Markdown, whole page |
| Use ChatGPT | <https://learn.chatgpt.com/docs/use-chatgpt.md> | Markdown, first half |
| ChatGPT pricing | <https://chatgpt.com/pricing> | HTML stripped to text; the prices are filled in by script and were **not** in the text |
| Changelog | <https://learn.chatgpt.com/docs/changelog> | HTML stripped to text, November 2026 entries |
| Codex releases | `gh api repos/openai/codex/releases` | Tag names and dates |
| Help Centre articles | help.openai.com | **Not read**: every article returned HTTP 403 to `curl` and to a summarising fetch |

## What they say

**Three ways to work, one app.** *Use ChatGPT*: "Use Chat for a question or
back-and-forth. Turn on Work in the switcher when you want ChatGPT to carry a
larger task through to a reviewable result. Select Codex when you want
developer views or more technical detail, especially for software
development." Its table: Chat to "Ask a question, search the web, brainstorm,
draft a message"; ChatGPT Work to "Create a deck, analyze files, draft a
report, build a project plan"; Codex to "Debug code, run tests, review a PR,
implement a feature".

**Desktop app.** *ChatGPT desktop app*: download for macOS or Windows, Linux
by a separate guide. "Start a chat, create a project, or open a folder.
ChatGPT can use the files and context in the location you choose." "Choose
ChatGPT or Codex. In ChatGPT, use the toggle above the composer to select
Chat or Work."

**Usage is shared.** *Pricing*: "ChatGPT Work usage inside ChatGPT uses the
same pricing, credits, and usage limits as Codex."

**Plans, as the Codex pricing page shows them** (the page writes "$"; the
Pro card says "$100, $200, or $500 USD per month", so these are US dollars;
no Canadian price is shown):

| Plan | Price | Codex models listed |
|---|---|---|
| Free | $0 / month | "GPT-6 Luna at Standard speed in the desktop app, subject to rollout" |
| Go | $8 / month | the same |
| Plus | $20 / month | "Codex on the web, in the CLI, in the IDE extension, and on iOS"; "GPT-6.1 Sol and GPT-6 Luna" |
| Pro | from $100 / month | "Plans at $100, $200, or $500 USD per month" |
| Business | $20 / user / month | "*2+ users, billed annually. $25 per user per month when billed monthly." "No training on your business data by default." |

**Usage limits.** "The estimates below show local messages per five-hour
period for Plus and Standard Business. Pro plans currently have no five-hour
limit." Plus: GPT-6 Astra 5–45, GPT-6.1 Sol 15–160, GPT-6.1 Terra 35–285,
GPT-6 Sol 15–150, GPT-6 Luna 350–3,000. "These estimates are not fixed
message limits." "Weekly limits may also apply." Usage dashboard:
<https://chatgpt.com/codex/settings/usage>; in the CLI, `/status`.

**ChatGPT pricing page** (chatgpt.com/pricing): plans Free, Go, Plus, Pro.
Model rows: GPT-6.1 Sol "No" on Free and Go, "Yes" on Plus; GPT-6 Luna on all
four. Feature rows include Codex ("Limited" on Free and Go, "Expanded" on
Pro), Memory ("Limited" / "Expanded"), Projects. Privacy row: "Content is
used to train our models — Opt-out available" on all four personal plans.
Plus card: "Projects, scheduled tasks, and custom GPTs". The prices themselves
are not in the page's text (filled in by script), so none is quoted from it.

**Which model Codex uses.** *Models*, "Configure your default local model":
"If you don't specify a model, the ChatGPT desktop app, Codex CLI, or IDE
extension uses a recommended model." No page read names that model for a
ChatGPT plan in one sentence. What the pages do say:

- The CLI section's examples all use `gpt-6.1-sol`: `codex --model
  gpt-6.1-sol`; `codex exec -m gpt-6.1-sol "Review the current changes"`.
- *Config basics*, "Default model": `model = "gpt-6.1-sol"`.
- *GPT-5.5 retirement*: "On Plus, Pro, Business, Enterprise, and Edu plans,
  choose **GPT-6.1 Sol** (`gpt-6.1-sol`) when available. On Free and Go plans,
  choose **GPT-6 Luna** (`gpt-6-luna`) in the desktop app when available."
- Reasoning effort: "For GPT-6.1 Sol, start with the reasoning effort
  available by default in your client".

So the tests pin `gpt-6.1-sol`, the model these pages give for a paid plan.
The effort was left unset, and `low` was reported in every run: that was the
test account's existing setting. No page read says what the default effort
is for GPT-6.1 Sol. A Free or Go user would get GPT-6 Luna, and only in the
desktop app.

**The four current models**, as *Models* describes them: GPT-6 Astra, "Our
most capable model for complex work"; GPT-6.1 Sol, "Near-Astra performance
for complex work at a lower cost than Astra"; GPT-6.1 Terra, "A fast,
efficient model for clear writing, visual understanding, and computer use";
GPT-6 Luna, "Our most efficient model for focused, high-volume tasks".
GPT-6.1 Sol: "a default context window of 500,000 tokens in Codex and ChatGPT
Work". GPT-5.5 retired from Codex with ChatGPT sign-in on 14 October 2026.

**Versions.** The changelog lists Codex CLI 0.167.1 (10 November 2026) and
0.167.0 (6 November). The tests used 0.166.0, the version installed; it was
not upgraded. GitHub release tags read the same day: `rust-v0.167.1`
(2026-11-10) and alphas of 0.169 and 0.170. Re-read in the evening: a
release `rust-v0.167.2` was published at 22:44 UTC on 11 November 2026,
after the tests.
