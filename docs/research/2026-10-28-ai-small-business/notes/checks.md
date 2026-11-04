## Access and confidence

Checked 2026-10-28. Method: WebFetch of primary pages where they loaded; WebSearch result text where they did not, marked **[snippet]**.

- **Blocked (HTTP 403) this session:** every openai.com / help.openai.com / chatgpt.com page, manychat.com and help.manychat.com, crtc.gc.ca, merriam-webster.com, answerthepublic.zendesk.com, legisquebec.gouv.qc.ca. A curl fallback was refused as bot-check circumvention, so nothing was pulled from those sites.
- **Search budget ran out** partway through (session cap of 200 WebSearch calls). The ChatGPT connector/agent and pricing questions therefore have **no first-hand or snippet source**. They are marked UNVERIFIED below, and someone needs to check them in a normal browser before publishing.
- **Loaded first-hand:** blog.google, support.google.com (Gemini Notebook Help), answerthepublic.com/pricing(.md), developers.facebook.com (Meta messaging policy), support.claude.com, claude.com/pricing, platform.claude.com, developers.openai.com (API docs), laws-lois.justice.gc.ca (CASL), ised-isde.canada.ca, priv.gc.ca, cai.gouv.qc.ca, hubspot.com, calendly.com, cal.com.
- WebFetch passes each page through a summariser. Quotes from legislation were requested "word for word" and re-checked. One early paraphrase of CASL s.6(2) was wrong and has been replaced with the verbatim text.
- Prices are USD list prices unless stated. Canadian buyers may see CAD or regional pricing, and sales tax is extra.

---

## 1. NotebookLM vs "Gemini Notebook"

**Verdict: TRUE.** The name is correct, the basic tier is free, and YouTube videos can be added as sources (only the transcript is used).

- Google renamed it on **16 July 2026**: "We're renaming NotebookLM to Gemini Notebook." It stays "the same standalone product". https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/ (The URL is still notebooklm.google, per the same post.)
- Free tier: "Gemini Notebook Standard". "Sign up free of charge by using your gmail account." Limits are **100 notebooks** and **50 sources per notebook**. https://support.google.com/gemininotebook/answer/16213268?hl=en
- Paid tiers (same page): **AI Plus** 200 notebooks / 100 sources; **AI Pro** 500 / 300; **AI Ultra** 500 / 500 or 600, depending on the storage tier.
- YouTube: web and YouTube URLs are supported source types. The video must be **public with captions**, have been **uploaded at least 72 hours** earlier, and contain speech. Only the transcript is used: "only the text transcript of the video". Each source is capped at 500,000 words or 200 MB. https://support.google.com/gemininotebook/answer/16215270?hl=en
- Note: the video's "drop in a YouTube video" advice works only on the transcript. On-screen visuals are not read.
- Also new: code execution for data analysis ("secure cloud computer"). It went first to Ultra and Workspace business customers, with Pro "over the coming weeks" (blog.google post above).

## 2. AnswerThePublic: 3 free searches a day?

**Verdict: PROBABLY TRUE (snippet only).** Paid pricing is confirmed first-hand.

- The help article "Is There a Free Version of AnswerThePublic?" says free accounts get "up to 3 searches per day" **[snippet]**. The page itself returned 403. https://answerthepublic.zendesk.com/hc/en-us/articles/22617503900187-Is-There-a-Free-Version-of-AnswerThePublic
- Secondary sources agree: 1 search/day without registering, 3/day with a free account **[snippet]** (search results citing neilpatel.com and answerthepublic.com/ja/pages/free_limit). The free_limit page loaded but showed no limit text.
- Current paid plans, first-hand from https://answerthepublic.com/pricing.md, in USD:
  - **Starter** $20/mo, or $120/yr ($10/mo)
  - **Growth** $99/mo, or $594/yr
  - **Business** $199/mo, or $1,194/yr
  - Plans are now credit-based: Starter has "60 monthly credits".
  - The pricing page itself does not mention a free plan.

## 3. ManyChat: comment-to-DM, Meta partner, pricing, Meta's DM rules

**Comment-to-DM: TRUE (snippet).**
- ManyChat's own docs describe "Auto-DM links in comments", triggered by a keyword, any comment, or a specific reel **[snippet]**. https://manychat.com/blog/instagram-quick-automation-comment-to-dm-guide/
- Its Facebook product does the same for Page comments **[snippet]**. https://manychat.com/product/instagram

**Meta partner: TRUE per ManyChat (snippet).**
- ManyChat says it is an "official Meta Business Partner" in the messaging category **[snippet]**. https://manychat.com/blog/manychat-official-meta-business-partner/
- To verify yourself, use Meta's directory: https://www.facebook.com/business/partner-directory/search?solution_type=messaging (not loaded).

**Pricing: the video's "free / Pro" framing is out of date.** ManyChat changed its model on **2 March 2026** to plans billed by **monthly Active Contacts**. All figures below are **[snippet]**, from help.manychat.com plan articles (each returned 403):

| Plan | Monthly billing | Annual billing (per month) | Active contacts/month |
|---|---|---|---|
| Free | $0 | $0 | 25 |
| Essential | $17 | $14 | 250 (no AI) |
| Pro | $39 | $29 | 2,500 (includes AI) |
| Business | $99 | $69 | 7,500 |
| Advanced | $199 | $139 | 25,000 |

- Overage is about $0.10, $0.05 and $0.025 per extra contact on Essential, Pro and Business.
- Sources: https://help.manychat.com/hc/en-us/articles/25800323349020-Active-Contacts and https://help.manychat.com/hc/en-us/articles/25800228332572-Pro-plan
- Caution: one third-party article (chatarmin.com) says the public pricing page kept showing the older Free/Pro layout for weeks after the change. Check in a browser.

**Meta's rules for automated DMs.** All first-hand from https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy unless noted.
- **The user starts the conversation.** "Only after an Instagram user has sent your app user's Instagram professional account a message can your app send a message". Source: https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/messaging-api
- **24-hour window.** "For most user actions, it lasts 24 hours." Click-to-Direct ads open a 7-day window (Instagram messaging page above).
- **Promotions** are allowed inside the window only: "Messages sent within the standard messaging window may contain promotional content." Outside it, the business needs paid "Sponsored" messages.
- **Human Agent tag.** A person, not a bot, may reply manually within a 7-day period.
- **Private Replies** (the comment-to-DM mechanism): "allowed within 7 days of the referenced user action", and limited to "a single message" until the person replies.
- **Bot disclosure.** "Automated chat experiences must disclose that a person is interacting with an automated service". This applies at the start of a conversation, after a long gap, or when a human hands over to a bot.

## 4. "AI slop" word of the year

**Verdict: PARTLY RIGHT. Two different dictionaries are involved, both for 2025.**

- **Macquarie Dictionary (Australia)** chose **"AI slop"** as its **2025** Word of the Year, winning both the committee pick and the people's choice. Definition: "low-quality content created by generative AI which often contains errors and is not requested by the user". https://www.abc.net.au/news/2025-11-25/ai-slop-named-macquarie-dictionary-word-of-the-year-2025/106047682
- **Merriam-Webster** chose **"slop"** (the word alone) for **2025**, announced 15 Dec 2025. Its definition: "digital content of low quality that is produced usually in quantity by means of artificial intelligence". https://techcrunch.com/2025/12/15/merriam-webster-names-slop-the-word-of-the-year/ (merriam-webster.com returned 403.)
- **Collins** 2025 was **"vibe coding"**, not slop. https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/ **[snippet]**
- Suggested wording: "Australia's Macquarie Dictionary made 'AI slop' its 2025 word of the year; Merriam-Webster picked plain 'slop'."

## 5. "Training it on you": ChatGPT and Claude features

### Claude (first-hand)

- **Plans** (https://claude.com/pricing): Free $0; **Pro $20/mo** ($17/mo billed annually); Max from $100/mo. The Free tier already includes "Memory across conversations", Projects (up to 5), Skills and Connectors, and file creation with code execution. Pro adds unlimited Projects, more usage, Claude Code, and Claude in Chrome.
- **Memory** is on by default for Free, Pro and Max. Searching past chats requires a paid plan. https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- **Personalisation**: account-wide "Instructions for Claude", Project instructions (free users get five projects), and Skills, which "adjust the tone and format of Claude's responses". All are on every plan. https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
  - Note: the separate "Styles" feature now appears under Skills in this help article.
- **Skills** are "folders of instructions, scripts, and resources" that Claude loads when relevant. They are on Free, Pro, Max, Team and Enterprise, and need code execution switched on. https://support.claude.com/en/articles/12512176-what-are-skills
- **Gmail / Google Calendar connectors** ("Use Google Workspace connectors"). https://support.claude.com/en/articles/10166901-using-the-gmail-and-google-calendar-integrations
  - Gmail: "Send, reply to, and forward emails".
  - Calendar: "Create, update, and delete events".
  - **Claude asks first:** "By default, Claude asks for your approval before each of these actions". On Team and Enterprise, the owner decides whether members may switch that prompt off.
  - **So yes, Claude can now send email and add calendar events for the user, with a confirmation step.** The article does not say clearly whether Free accounts get every write action.

### ChatGPT (UNVERIFIED: all OpenAI pages returned 403)

- **Custom instructions** are on all plans. Free and Go accounts get up to 1,500 characters; Plus and above get 5,000 **[snippet]**. https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions
- **Memory:** Free users have "Saved memories". Plus and Pro also get "reference chat history" **[snippet]**. https://help.openai.com/en/articles/8590148-memory-faq
- **Projects** are on the Free tier, with up to 5 files per project, and can be set to project-only memory **[snippet]**. https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- A **ChatGPT Go** tier exists **[snippet]**. https://help.openai.com/en/articles/11989085-what-is-chatgpt-go
- **NOT VERIFIED this session; check before publishing:**
  - Plus price (widely reported as US$20/mo).
  - Which plans get the Gmail and Google Calendar apps/connectors, and whether those can *write* (send mail, create events) in chat.
  - Whether only ChatGPT agent mode can take those actions, and whether it asks for confirmation.
  - Background, not cited: Wikipedia says OpenAI launched ChatGPT Agent in July 2025 and added Gmail connectivity in Sept 2025. https://en.wikipedia.org/wiki/ChatGPT
  - Pages to check: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt and https://openai.com/chatgpt/pricing/

## 6. "40, 50 bucks a month"

Monthly list prices in USD, at monthly billing unless stated:

| Item | Price used | Source |
|---|---|---|
| ChatGPT Plus | ~$20 (UNVERIFIED) | see §5 |
| Claude Pro | $20 ($17 annual) | claude.com/pricing |
| ManyChat Pro | $39 ($29 annual), 2,500 active contacts | [snippet], §3 |
| HubSpot | Free: $0 (2 users, 1,000 contacts). Starter: "$20/month per seat", or "starting at $7" on an annual commitment | https://www.hubspot.com/pricing/crm |
| Calendly | Free: 1 event type, 1 calendar. Standard: $10/seat/mo billed yearly | https://calendly.com/pricing |
| Cal.com | Free forever for 1 user | https://cal.com/pricing |
| Gemini Notebook / AnswerThePublic | $0 on free tiers | §1, §2 |

- **Minimal stack** (one AI subscription, ManyChat Pro, free CRM, free scheduler): about **$59/mo**, or $49/mo with annual billing.
- **Both AIs**, ManyChat Pro, and free CRM and scheduler: about **$79/mo**.
- **Add HubSpot Starter and Calendly Standard:** about **$110 to $120/mo**.
- **Verdict:** "$40 to $50" works only with **one** AI subscription, ManyChat on annual billing or its $17 Essential tier (which has no AI), and free CRM and scheduling. A more realistic figure is **$50 to $80 USD a month**, before CAD conversion and tax.

---

## 7. CASL (Canada's Anti-Spam Legislation)

Statute: S.C. 2010, c. 23, https://laws-lois.justice.gc.ca/eng/acts/E-1.6/ (pages 1 to 3 loaded first-hand). The CRTC FAQ (https://crtc.gc.ca/eng/com500/faq500.htm) returned 403.

- **What counts as a commercial electronic message (CEM)**, s.1(2): a message where "it would be reasonable to conclude has as its purpose ... to encourage participation in a commercial activity". Profit motive is irrelevant: the s.1(1) definition of "commercial activity" applies "whether or not ... in the expectation of profit".
- **Channels covered.** The Act's "electronic address" means an address for "(a) an electronic mail account; (b) an instant messaging account; (c) a telephone account; or (d) any similar account" (s.1(1)). That covers email, SMS, and DMs on Instagram, Facebook or WhatsApp.
  - The Government of Canada's plain-language summary lists "email, social media and text messages". https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/understand-canadas-anti-spam-legislation/understand-canadas-anti-spam-legislation-sub/understanding-canadas-anti-spam-legislation
- **Asking for consent is itself a CEM**, s.1(3): "An electronic message that contains a request for consent ... is also considered to be a commercial electronic message." So you **cannot email or DM old leads to ask "can I keep emailing you?"** once implied consent has lapsed.
- **Consent**, s.6(1). You need express or implied consent.
  - **Express consent** does not expire unless withdrawn.
  - **Implied consent** is "generally time-limited". https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/getting-consent-send-email
  - **Inquiry or application:** consent runs "within the six-month period immediately before the day on which the message was sent", s.10(10)(e).
  - **Purchase or lease:** "within the two-year period immediately before the day on which the message was sent", s.10(10)(a). A written contract also qualifies while it is current or within 2 years of expiry, s.10(10)(d).
  - **Conspicuous publication** of an address can also imply consent, s.10(9)(b).
  - **Burden of proof:** the sender "has the onus of proving it", s.13. In practice, keep records of how and when each lead gave consent.
- **Exception:** a message that only "provides a quote or estimate ... if the quote or estimate was requested by the person" is exempt from the consent rule, s.6(6)(a). The identification and unsubscribe rules still apply.
- **Required content**, s.6(2). Each CEM must:
  - "(a) set out prescribed information that identifies the person who sent the message ..."
  - "(b) set out information enabling the person to whom the message is sent to readily contact one of the persons ..."
  - "(c) set out an unsubscribe mechanism".
  - Unsubscribes must take effect "no later than 10 business days" (s.11(3)). Contact information must stay valid for at least **60 days** after sending, per the regulations as summarised in the CASL text fetch. Verify that against SOR/2012-36 if quoted.
- **Penalties.** Administrative monetary penalties of up to **$1,000,000 for an individual and $10,000,000 for any other person** per violation, s.20(4). The Government summary: "can reach $1 million for individuals and $10 million for businesses".
- **What this means for "reactivating" old inbox leads** (the video's tip):
  - A lead who only *inquired* more than 6 months ago, and never bought, has no implied consent left.
  - An AI-drafted "just checking in, are you still looking?" email or DM that promotes your service is a CEM, and so is a message asking for consent (s.1(3)).
  - Safe to message: past *customers* within 2 years, people with express consent, and leads whose inquiry falls within 6 months. Every message must include sender ID, contact details and an unsubscribe.
  - A reply to someone who has *just* messaged you (for example, Instagram's 24-hour window) is usually fine on implied consent from the inquiry, but must still meet the s.6(2) requirements if commercial.
  - Interpretation note: this is our reading of the statute. CRTC enforcement guidance (e.g. Compliance and Enforcement Information Bulletin 2012-548) could not be loaded.

## 8. Privacy: PIPEDA, Quebec Law 25, OPC on generative AI

- **PIPEDA scope.** It applies to private-sector organisations handling personal information in "commercial activity". Its 10 fair information principles include accountability, identifying purposes, consent, limiting collection, limiting use/disclosure/retention, safeguards and openness. Quebec, BC and Alberta have substantially similar private-sector laws. https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/
- **Sending customer data to a US AI service or CRM** counts as a transfer for processing. https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/
  - The business stays responsible: "An organization is responsible for personal information in its possession or custody, including information that has been transferred to a third party for processing."
  - It must use "contractual or other means to provide a comparable level of protection".
  - It must tell customers their information "may be processed in a foreign country". In practice, read the vendor's data-processing terms and update your privacy notice.
- **OPC generative-AI principles** ("Principles for Responsible, Trustworthy and Privacy-Protective Generative AI Technologies", **7 Dec 2023**, issued jointly by the federal, provincial and territorial commissioners). https://www.priv.gc.ca/en/privacy-topics/technology/artificial-intelligence/gd_principles_ai/
  - The nine principles: legal authority and consent, appropriate purposes, necessity and proportionality, openness, accountability, individual access, limiting collection/use/disclosure, accuracy, safeguards.
  - Consent must be "valid and meaningful".
  - Those *using* the tools should put personal information into prompts only where authorised, and should prefer "anonymized or de-identified information within prompts".
  - "Safeguard any personal information ... with measures commensurate to the sensitivity".
  - Practical takeaway: strip names, phone numbers and emails before pasting a lead list or inbox export into a chatbot, unless your privacy notice and the vendor terms cover it.
- **Quebec Law 25** (main provisions in force Sept 2023), per the Commission d'accès à l'information. https://www.cai.gouv.qc.ca/protection-renseignements-personnels/sujets-et-domaines-dinteret/principaux-changements-loi-25
  - A named person must be in charge of personal information, with contact details published.
  - A **privacy impact assessment** ("évaluation des facteurs relatifs à la vie privée") is required **before** personal information is communicated outside Quebec, plus a written agreement. This applies to US AI and CRM vendors.
  - Consent must be "manifeste, libre, éclairé et donné à des fins précises".
  - Confidentiality incidents with "un risque de préjudice sérieux" must be reported, and an incident register kept.
  - People must be notified when a decision is based solely on automated processing.
  - (legisquebec.gouv.qc.ca returned 403, so these points come from the CAI summary, not the statute text.)

## 9. AI arithmetic on spreadsheets

- **Claude:** for data files it can "write and run code (for example Python or Javascript)" in a sandbox. This is on all plans and uses more of the usage allowance. https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
  - API docs: Claude can "perform complex calculations" by running code in "a secure, sandboxed environment". https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool
- **OpenAI:** the code-interpreter tool runs Python in a sandbox. "a model that writes code that fails to run can keep rewriting and running that code until it succeeds". https://developers.openai.com/api/docs/guides/tools-code-interpreter
  - The ChatGPT consumer help page on data analysis (https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) returned 403.
- **Limits, from the vendor:** "Claude can occasionally produce responses that are incorrect or misleading". Users "should not rely on Claude as a singular source of truth". https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on
- **Practical rule for the article:**
  - Totals, averages and "which listing/product sold best" are reliable only when the assistant visibly ran code (a code block or analysis step is shown).
  - A number written straight into prose without running code is a prediction, not a calculation.
  - Ask it to "use code and show the formula", then spot-check one row by hand.
  - No vendor publishes an error rate for in-text arithmetic. This is general guidance, not a measured figure.
