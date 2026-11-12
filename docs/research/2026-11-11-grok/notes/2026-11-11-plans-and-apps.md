# Plans, apps, and the chat's own features

Read 11 November 2026.

| Page | How read |
|---|---|
| [x.ai/pricing](https://x.ai/pricing) | as rendered text in a browser (direct download refused with 403) |
| [docs.x.ai: Welcome to Grok](https://docs.x.ai/grok/overview.md) | Markdown, `curl` |
| [docs.x.ai: FAQ, Grok website and apps](https://docs.x.ai/grok/faq.md) | Markdown, `curl` |
| [docs.x.ai: Connectors](https://docs.x.ai/grok/connectors.md) | Markdown, `curl`, headings only |
| [The X Subscription: overview](https://docs.x.ai/x-subscription/overview.md), [pricing](https://docs.x.ai/x-subscription/pricing.md), [usage limits](https://docs.x.ai/x-subscription/usage-limits.md), [X Premium customers](https://docs.x.ai/x-subscription/x-premium.md), [Do I have to switch?](https://docs.x.ai/x-subscription/do-i-have-to-switch.md) | Markdown, `curl` |
| [grok.com/plans](https://grok.com/plans) | `curl`: the page is drawn by script and the text was empty. Not read. |

## The products

- Grok is "available on the web at grok.com and in the iOS and Android apps.
  Sign in once and your conversations, settings, and subscription stay in
  sync" (overview). It can chat, make images and video (Imagine), talk by
  voice, read uploaded files, and use **connectors** to email, files and
  calendar (overview; connectors page lists Google Drive, Gmail and Google
  Calendar, Outlook, SharePoint, OneDrive, Teams, Salesforce, custom MCP).
- **Grok in X**: the Grok icon in the X app or x.com; governed by X's terms
  and privacy policy, not xAI's (X help page, see `2026-11-11-data.md`).
- **Grok Build**: the command-line coding agent; see `2026-11-11-grok-build.md`.
  grok.com also has a "Build mode" (developer FAQ, security).
- **Grok Bot**: "AI teammates on a persistent cloud computer" (overview). Out
  of scope for this guide; noted only.
- No desktop app for Mac or Windows is listed on x.ai's product menu (Grok,
  Business, Government; Download: iOS, Android; Grok on X; Grok Bot). Not
  confirmed either way.

## Plans: The X Subscription

xAI now sells one subscription, **The X Subscription**, covering Grok,
Cursor and X. "Grok and Cursor share a weekly included usage pool."
Existing SuperGrok and X Premium plans "continue unless you change or
cancel them"; switching is optional and "permanent".

Prices from x.ai/pricing, shown as "$" with no currency named; the docs call
them "list prices" that "do not include sales tax". No Canadian price shown.

| Plan | Monthly | Annual (docs page) | Usage | Grok features named on the page |
|---|---|---|---|---|
| Free | $0 | $0 | Limited | "Limited Chat requests", "Limited agent requests" |
| Plus | $8 | $80 | "Shared AI usage pool" (Basic) | "Grok Chat, Voice, Imagine, and Build", "Grok API access", Cursor |
| Premium | $30 | $300 | 4× Plus | adds Grok Bot, "Latest Grok models" |
| Super | $100 | $1000 | 15× Plus | "Significantly higher usage across Chat, Imagine, Voice & Build" |
| Ultra | $200 | $2000 | 50× Plus | (comparison table only) |
| Teams | "$30+/user/month" | | 4–50× Plus, pooled | |

- The comparison table on x.ai/pricing has a "Grok Build" row with "Limited"
  in one cell; which column it belongs to was not clear from the page text.
  **For the owner to check.**
- Usage (grok FAQ): "one shared weekly usage pool that you can spend however
  you like across any Grok product", rolled out from June 2026. Settings >
  Usage shows a bar, "a percentage breakdown by product (API, Build, Chat,
  Imagine, Voice)", and the reset date. When it runs out, "paid features will
  pause until your weekly limit resets"; free Chat and Voice limits remain;
  Extra Usage Credits from $5, web only.
- X benefits by plan (X Premium customers page): Plus gets "a checkmark,
  creator tools, and fewer ads on X"; Premium and above "full X Premium+
  benefits".

## Projects, memory, custom instructions in the chat

**No xAI page read today describes them.** docs.x.ai's Grok section has
overview, FAQ, connectors and business pages only; the FAQ mentions
Projects once, in passing: "Some users on grok.x.ai or other hosts run into
missing features like Projects." Third-party pages describe memory,
"Workspaces" and custom instructions with conflicting details
([one](https://www.maginative.com/article/xai-upgrades-grok-with-personalized-memory-and-custom-workspaces/));
they are leads, not sources. The article says only what the vendor says and
sends the rest to *For the owner*.

## Files in the chat

From the FAQ: upload with **+**; up to about 100 files at once on the web,
20 on Android; "up to 150 MB per file"; very long files "may be summarized or
handled in sections". Delete files at grok.com/files.
