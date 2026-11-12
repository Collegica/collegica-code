# Claude apps and plans: notes

Anthropic's own pages, read 2026-11-10 and 2026-11-11 (the date is given for
each). All were downloaded whole and read as text, not through a summarising
tool, unless marked.

## Pricing page

<https://claude.com/pricing>, read 2026-11-10 (twice: once through a
summarising fetch, once as the page's own text; the two agree).

| Plan | Price as shown | What the page lists |
|---|---|---|
| Free | $0 | "Limited usage every 5 hours and every week"; chat on web, desktop and mobile; "Search the web, create files, and run code"; "Memory across conversations"; connectors; artifacts; Claude Design, Slides, Docs; projects "Up to 5" |
| Pro | $17 a month "with annual subscription discount ($200 billed up front). $20 if billed monthly." | Everything in Free, plus more usage; "Fable, paid with usage credits"; "Hand off and schedule tasks"; Claude Code; projects; "More Claude models"; Claude in Chrome and Microsoft 365 |
| Max | $100 a month | "5x Pro usage every 5 hours and every week"; "Fable included, up to half your weekly limit"; "$100 a month in API credits"; priority access |
| Ultra | $200 a month | "No 5-hour limit" (footnote: "for verified accounts"); "10x Pro usage every week"; $200 a month in API credits |
| Team | $20 a seat a month billed annually, $25 monthly; premium seat $100 / $125 | "No model training on your content by default" |
| Enterprise | "US$20/seat/month, billed annually, 20 seat minimum" plus usage at API rates | |

- **Currency.** The consumer prices carry a bare "$". Only the Enterprise
  line says "US$". The page was fetched from a Canadian address and showed
  no CAD figure. The article gives the figures as "$ as the page shows them"
  and does not call them CAD. What a Canadian card is actually charged is on
  the *For the owner* list.
- "Prices shown don't include applicable tax."
- Footnote on limits: "Usage limits apply. How fast you reach a limit depends
  on the model you use, how long your chats are, and how large your files
  are."
- Comparison table, row "Model training": **"Opt-out"** for Free, Pro, Max
  and Ultra. Row "Fable": Free "No", Pro "Usage credits", Max and Ultra "50%
  of weekly limits". Rows "Opus": Free "No", paid "Yes". "Sonnet" and
  "Haiku": all plans. "Context window": "Up to 1M, varies by model".
- Claude Code: "No" on Free, "Yes" on Pro, Max, Ultra.

## Desktop app

<https://support.claude.com/en/articles/10065433-install-claude-desktop>,
read 2026-11-11 ("Updated over a week ago").

- "Claude Desktop is available on macOS, Windows, and Linux (beta)."
- The availability table gives Chat on all six plans, and Claude Code and
  Claude Cowork on five (the Free column has no tick for either).
- macOS 13 or higher; Windows 10 or higher; Ubuntu 22.04+ or Debian 12+.
- On Linux: no computer use, no dictation.

## Cowork, and chat and Cowork becoming one

<https://support.claude.com/en/articles/13345190-get-started-with-cowork>,
read 2026-11-11.

- "Claude Cowork is available on paid plans (Pro, Max, Ultra, Team, and
  Enterprise)."
- "Claude Cowork uses the same agentic architecture that powers Claude Code,
  with no terminal required."
- "Cowork runs your sessions remotely in the cloud, so your sessions and
  files live with your Claude account and follow you across desktop, web,
  and mobile."
- "The new Claude experience, which combines chat and Cowork, is rolling out
  to Pro, Max, and Ultra plans." "If your message box no longer shows 'Chat'
  and 'Cowork' options, you have the new experience."
- "Cowork has unique risks due to its agentic nature and internet access."

The Free plan's "create files, and run code" on the pricing page and "paid
plans" here are not the same thing: the first is code execution inside a
chat, the second is the agent working on a task. Not tested; on the *For the
owner* list.

## Release notes

<https://support.claude.com/en/articles/12138966-release-notes>, read
2026-11-11 ("Updated this week"). Newest first, the entries that bear on the
guide:

- 5 Nov 2026: Personal Finance (beta, US only, Pro/Max/Ultra).
- 21 Oct 2026: Claude Duet research preview (Pro and Max).
- 7 Oct 2026: Claude Haiku 5.5; monthly API credits for Max and Team.
- 28 Sep 2026: Claude Sonnet 5.5.
- 22 Sep 2026: Claude Opus 5.5, "performs at the level of Claude Fable 5.1
  on most work and costs 40% less to run than Opus 5".
- 16 Sep 2026: "Claude Cowork comes to every conversation"; Design, Slides
  and Docs in any conversation, "available on every plan, including Free".
- 1 Sep 2026: Claude Fable 5.1 and Mythos 5.1.
- 25 Aug 2026: memory in Cowork, editable topics, sensitive-topics setting.

**Fable 5.2 is not in these release notes** as read. It is in the Claude
Code changelog (see [`claude-code.md`](claude-code.md)): v2.1.321, 9 November
2026.

## Usage limits

<https://support.claude.com/en/articles/9797557-usage-limit-best-practices>,
read 2026-11-11.

- What uses the limit faster: message length, attachment size, conversation
  length, tool use, model choice, effort level, artifacts, multi-step tasks.
- "Content in projects is cached and counts less against your limits when
  reused." "Caches expire after a period of inactivity."
- "Settings > Usage" shows "progress bars showing how much of your five-hour
  session and weekly usage limits you've consumed", with weekly limits "for
  all models, and for Fable (if included in your plan)".

No page read gives the limits as numbers of messages or tokens.
