## Access and confidence

Checked **2026-10-31**. Every URL below was read on that date unless marked otherwise.

- **Method.** curl of the page, with HTML stripped to text, for Google, Yahoo, Apple, laws-lois.justice.gc.ca, ised-isde.canada.ca and priv.gc.ca. These pages served plain HTML with no bot check. WebFetch (which summarises the page) for facebook.com and linkedin.com, whose pages render with JavaScript. Quotes from WebFetch went through a summariser, so treat them as near-verbatim and re-check before quoting in print.
- **Blocked:** crtc.gc.ca returned **HTTP 403** to both curl and WebFetch (FAQ `https://crtc.gc.ca/eng/com500/faq500.htm`, bulletins 2012-548 and 2012-549). We did not try to get around it. **No CRTC guidance was read first-hand.** The social-media and "friendship" questions below rest on the statute and regulations only.
- **WebSearch was unavailable** (session budget used up). Pages were found from known URLs and from links on the pages themselves.
- **Not loaded / not found:** takeout.google.com itself (it needs a sign-in). Yahoo's data-download dashboard (`yahoo.mydashboard.oath.com` returned an error page without sign-in). No GitHub code search hit for LinkedIn's `Connections.csv` header.
- **Reused (already verified 2026-10-28):** `docs/2026-10-28-ai-small-business/notes/checks.md` §7 (CASL basics: CEM definition, consent, 6-month/2-year implied consent, s.6(2) content, penalties) and §8 (PIPEDA, cross-border transfers, OPC generative-AI principles, Quebec Law 25). They are not repeated here, only cited.
- **UNVERIFIED** marks anything we could not confirm from a primary page. It usually means "commonly reported, or from memory". Check those items in a normal browser before publishing.

---

## 1. Exports, per platform

### 1a. Google: Google Contacts export and Google Takeout

**Google Contacts export** (the quick route for contacts only). https://support.google.com/contacts/answer/7199294?hl=en
- The page says: "first download them as a CSV or vCard file."
- Steps: go to Google Contacts. Select one contact, several, or "Selection Actions" then All. Then "More actions" then **Export**.
- The steps text names only **Google CSV** ("To back up your contacts, select Google CSV"). vCard is mentioned in the intro line only. The Outlook CSV option is **UNVERIFIED** from this page.
- Limit: for work or school accounts, "you can't select all contacts in the Directory."

**"Other contacts"** (people you emailed but never saved). https://support.google.com/contacts/answer/1069522?hl=en
- Gmail saves them automatically: "Google Contacts automatically saves their email address in your 'Other contacts' group."
- You can see them on a computer only, under Contacts, then "Other contacts". "If you're on an iPhone, iPad, or Android device, you won't see Other Contacts."
- Why it matters for the article: this group is often the richest list of real correspondents. Whether a Contacts export or Takeout includes "Other contacts" is **UNVERIFIED**.

**Merging duplicates** (useful for upkeep). https://support.google.com/contacts/answer/7078226?hl=en
- Menu, then "Merge & fix". "You can't merge contacts that are saved in different Google Accounts."

**Google Takeout** (everything, including Gmail). https://support.google.com/accounts/answer/3024190?hl=en
- Steps: sign in, go to Google Takeout, select products, choose delivery method and format, then create the export.
- Delivery: an email link, or straight to Google Drive, Dropbox, OneDrive or Box.
- Archive format: .zip or .tgz. Large exports are split, and you can choose up to 50 GB per file.
- Timing: "this process could take from a few minutes to a few days." Also: "Most people get the link to their archive the same day."
- Links expire after about 7 days: "We only allow each archive to be downloaded 5 times".
- Schedule: a one-off export, or every 2 months for a year.
- Contacts format: "we export contacts as vCard, which is a very common format for email providers."
- Gmail labels: "each message's labels are preserved in a special X-Gmail-Labels header". There is no export by date range: "we don't support timeframe exports."
- **Gmail file format = MBOX: UNVERIFIED** on the pages we read. Neither 3024190 nor the Gmail export page below names the format. Takeout's own UI (sign-in required) is where it shows.

**What a Gmail export contains.** https://support.google.com/mail/answer/10016932?hl=en ("Export your data from Gmail")
- Your download includes "Message content", "Message headers", "Attachments" and labels, across inbox, sent, archived, spam and trash.
- Encrypted messages stay encrypted.
- Contact data you get from it: every From/To/Cc header in the mailbox. That is the raw material for "who have I actually corresponded with, and when".

### 1b. Yahoo

**Contacts export (New Yahoo Mail).** https://help.yahoo.com/kb/new-yahoo-mail/import-export-print-contacts-yahoo-mail-sln36726.html
- Steps: "click Contacts", then the More options icon, then "Export to CSV file or Print all".
- The format is **CSV only** on this page. vCard is not mentioned: **vCard from Yahoo is UNVERIFIED / likely not offered.**
- Cap: "save up to 5000 of your contacts in one place."
- Gotcha: "Special characters will prevent the import or export of Yahoo Contacts." You have to edit accents and dashes out first. That is a real problem for French-Canadian names.
- The older-version page (https://help.yahoo.com/kb/SLN28070.html) says the same: "Export (CSV)".

**Mail.** https://help.yahoo.com/kb/new-yahoo-mail/transfer-emails-contacts-accounts-yahoo-mail-sln36731.html
- "it's not possible to transfer your entire inbox from Yahoo Mail". Yahoo suggests forwarding, or backing up through a desktop app such as Outlook or Mac Mail (IMAP).

**"Download my data".** Yahoo Privacy Dashboard (https://guce.yahoo.com/privacy-dashboard?locale=en-CA, links to https://yahoo.mydashboard.oath.com/)
- "Download, delete, or manage your personal information", but "you must sign in"
- Steps, formats and timing **could not be read** without signing in: **UNVERIFIED.**
- The privacy policy (https://legal.yahoo.com/ca/en/yahoo/privacy/index.html, "Last updated: March 2026") points to the Privacy Dashboard for per-product data.

### 1c. Apple / iCloud

**iCloud Contacts as vCard.** https://support.apple.com/guide/icloud/import-export-and-print-contacts-mmfba748b2/icloud
- Go to icloud.com/contacts. Select one contact, several (Cmd/Ctrl-click, on a computer only), or "Select All Contacts". Then choose "Export vCard".
- "If you select multiple contacts, Contacts exports a single vCard containing all of them."

**Data & Privacy copy.** https://support.apple.com/en-us/102208 ("Get a copy of the data associated with your Apple Account")
- Steps: sign in at Apple's Data & Privacy page (privacy.apple.com), select "Request a copy of your data", pick the data, then Continue. "Access to this feature varies by country and region."
- What's included: "Data that you store with iCloud such as contacts, calendars, notes, bookmarks, reminders, email..."
- Formats: contacts, calendars, bookmarks and mail come "in formats such as .vcf, .ics, .html, and .eml."
- Timing: Apple verifies the request and then "notify you that it's available". **No processing time is stated** (a "up to 7 days" figure is UNVERIFIED). "You have 14 days to download your data".
- Caveats:
  - Data "stored in an end-to-end encrypted format that Apple cannot decrypt" is not provided. Contacts under Advanced Data Protection may fall here (**UNVERIFIED** for contacts specifically).
  - Apple masks some fields: "We mask certain information ... including ... email addresses". It is **unclear** whether that applies to addresses inside your contacts. Test it before relying on this route. The vCard export from icloud.com is the safer route for contacts.

### 1d. Facebook (Meta)

**Export ("Download your information").** https://www.facebook.com/help/212802592074644 (via WebFetch)
- Path: profile picture, then Settings & privacy, Settings, Meta Account (Accounts Center), "Your information and permissions", "Export your information", "Create export". Choose the profile and a destination (device or external service), then Start export.
- Formats:
  - HTML: "An easy to view format", delivered as a ZIP with an index file.
  - JSON: "A machine readable format ... to transfer your information more easily".
- Options: information types, date range, media quality.
- Availability: "you'll have 4 days to export your information in the Available downloads section". **Processing time is not stated.**

**Categories.** https://www.facebook.com/help/930396167085762
- The "Connections" category covers "friends and followers" ("Who and how you've connected with people on Facebook").
- The page does **not** itemise the fields. **UNVERIFIED (commonly reported):** the friends file lists each friend's **name and the date you became friends, with no email or phone**. Plan on Facebook giving you names and dates only.

### 1e. LinkedIn

**Download your data.** https://www.linkedin.com/help/linkedin/answer/a1339364 (via WebFetch)
- Steps: Me, then Settings & Privacy, Data Privacy, "Download your data". Select data, then "Request archive".
- Timing:
  - Specific categories: "we'll email you within minutes".
  - The full archive: "you'll receive an email within 24 hours".
  - Once ready: "available for download for 72 hours".
- Connections file contents: first and last name, profile URL, email address, company, position, and connection date.
- Email caveat: an email is "included only when authorized by the connection in their privacy settings." In practice most rows have no email (**the "most" is UNVERIFIED**).
- Exact `Connections.csv` column headers: **UNVERIFIED.** Commonly seen as `First Name, Last Name, URL, Email Address, Company, Position, Connected On`, with a few note lines above the header. Confirm against a real export.

---

## 2. Platform terms on automation and scraping

**LinkedIn User Agreement**, effective **3 Nov 2025**. https://www.linkedin.com/legal/user-agreement (via WebFetch). Section 8.2, "Don'ts":
- Scraping: "use software, devices, scripts, robots ... to scrape or copy the Services, including profiles".
- Copying: "Copy, use, display or distribute any information" from the Services "without the consent of the content owner". Note this covers what you got "through third parties (such as search tools or data aggregators or brokers)". That is relevant to enrichment tools.
- Bots: "Use bots or other unauthorized automated methods" to, among other things, "add or download contacts, send or redirect messages". This rules out auto-connect and auto-DM tools.
- Practical point: your own data download is the sanctioned route. Browser extensions that scrape profiles or automate messages break the terms.

**LinkedIn Professional Community Policies.** https://www.linkedin.com/legal/professional-community-policies (via WebFetch)
- "We don't allow untargeted, irrelevant, obviously unwanted, unauthorized, inappropriate commercial or promotional ... messages".
- do not use invitations "to send promotional messages to people you don't know".

**Meta Terms of Service**, last revised **1 Jan 2025**. https://www.facebook.com/terms.php (via WebFetch). Section 3.2:
- "You may not access or collect data from our Products using automated means" without prior permission. This applies whether or not you are logged in.
- Also: you may not "sell, license, or purchase any data obtained from us or our services".

**Meta Automated Data Collection Terms**, effective **7 Oct 2024**. https://www.facebook.com/legal/automated_data_collection_terms (via WebFetch)
- no Automated Data Collection "without first obtaining Meta's express written permission".

---

## 3. Canadian law for outreach from the database

Basics (CEM definition, s.6(2) content, implied-consent windows, s.13 onus, penalties) are in **checks.md §7**. PIPEDA scope, cross-border processing and the OPC generative-AI principles are in **checks.md §8**. This section adds what is specific to contacts gathered from your own accounts.

Sources:
- CASL S.C. 2010, c.23: https://laws-lois.justice.gc.ca/eng/acts/E-1.6/FullText.html
- Electronic Commerce Protection Regulations SOR/2013-221: https://laws-lois.justice.gc.ca/eng/regulations/SOR-2013-221/FullText.html

### 3a. Are social-media DMs and InMail "electronic messages" to an "electronic address"?

- **The statute.** CASL s.1(1) defines "electronic message" as "a message sent by any means of telecommunication". An "electronic address" covers "(b) an instant messaging account; ... or (d) any similar account". On the text, a LinkedIn message or Facebook DM is within scope.
- **ISED's plain-language summary** lists "email, social media and text messages". https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/understand-canadas-anti-spam-legislation/understand-canadas-anti-spam-legislation-sub/understanding-canadas-anti-spam-legislation
- **A narrow carve-out, ECPR s.3(d).** Section 6 does not apply to a CEM "sent and received on an electronic messaging service" if two conditions hold:
  - the sender ID and unsubscribe information "are conspicuously published and readily available on the user interface"; **and**
  - the recipient "consents to receive it either expressly or by implication".
- So even on a platform, **you still need consent**. The carve-out only relieves you of putting the ID/unsubscribe text in each message. Whether LinkedIn or Messenger meets the "conspicuously published ... on the user interface" test is **our interpretation, not CRTC-confirmed** (CRTC site blocked).

### 3b. Does a LinkedIn connection or Facebook friendship create consent?

**Personal or family relationship exemption, CASL s.6(5)(a).** Section 6 does not apply to a CEM "sent by or on behalf of an individual to another individual" with whom they have "a personal or family relationship".

ECPR s.2 defines both terms:
- **Family relationship:** related "through a marriage, common-law partnership or any legal parent-child relationship" **and** the two "have had direct, voluntary, two-way communication".
- **Personal relationship:** they "have had direct, voluntary, two-way communications" **and** it is "reasonable to conclude that they have a personal relationship". The factors include shared "interests, experiences, opinions and information evidenced in the communications", "the frequency of communication", time since they last communicated, and "whether the parties have met in person."

Our reading:
- A click-to-connect or friend request with no real back-and-forth does **not** meet this test.
- A friend you actually talk to might, but only for messages from you **as an individual** to them as an individual.
- A blast from your business to "all my friends" is a poor fit.
- The exact CRTC position on "friends/followers" is **UNVERIFIED** (FAQ blocked).

**Existing non-business relationship, s.10(13).** This is limited to three things, each within 2 years:
- (a) donations or gifts to a registered charity, political party or candidate;
- (b) volunteer work or meeting attendance for those same bodies;
- (c) membership in "a club, association or voluntary organization".
- It is **not** a general "we know each other" category. Social-network ties are not on the list.

**Existing business relationship, s.10(10).** Purchases within 2 years, inquiries within 6 months, and so on (see checks.md §7). Only contacts who are actually your customers or recent inquirers qualify, and they qualify through that relationship, not through the connection.

**Conspicuous publication, s.10(9)(b).** Consent is implied only if all three hold:
- the person "has conspicuously published" the address;
- the publication is not accompanied by a statement that the person does not want "unsolicited commercial electronic messages";
- the message is "relevant to the person's business, role, functions or duties".

ISED repeats the same two limits: no "don't contact" note, and relevance to their role. https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/getting-consent-send-email

So: a buyer's email on their company website can be pitched with a relevant B2B offer. A personal Gmail found in a friend list cannot.

**Disclosure to you, s.10(9)(c).** The same conditions apply where the person "has disclosed, to the person who sends the message, the electronic address" (e.g., handed you a business card). ISED: "Did they publish their contact information online or give you a business card?"
- Whether a LinkedIn connection letting you download their email counts as "disclosed to" you is **untested in anything we read**. Treat it as uncertain.

**Referral exemption, ECPR s.4(1).** The **first** CEM after a referral is exempt from the consent requirement if:
- the referrer has an existing business, non-business, family or personal relationship with **both** sender and recipient; and
- the message "discloses the full name" of the referrer(s) and says it "is sent as a result of the referral".

This is the cleanest legal route for warm introductions from your network.

**Asking for consent is itself a CEM (s.1(3), checks.md §7).** You cannot mass-email the whole database asking "may I email you?"

**Bottom line for CASL.**
- The database is fine to **build**. Each **commercial** message still needs a lawful basis per contact:
  - express consent;
  - customer (2 yr) or inquiry (6 mo);
  - conspicuous publication or disclosure plus relevance to their role;
  - a genuine personal or family relationship (one individual to another);
  - or a named referral (first message only).
- Store the basis and its date in a column. The onus of proof is on you (s.13).

### 3c. PIPEDA

PIPEDA FullText: https://laws-lois.justice.gc.ca/eng/acts/P-8.6/FullText.html

**Personal address book vs business use, s.4(2)(b).** PIPEDA does not apply to an individual who handles personal information "for personal or domestic purposes", and does not use it "for any other purpose".
- Our reading: once you turn your personal contacts into a prospecting list for a business, that exemption no longer covers the new use.

**Business contact information, s.4.01 and s.2(1).** The Act "does not apply ... in respect of the business contact information of an individual". The condition is that the organisation uses it "solely for the purpose of communicating" with the person "in relation to their employment, business or profession".
- Business contact information means name, "position name or title", work address, work phone, work fax, or "work electronic address".
- So emailing someone at work about their work is largely outside PIPEDA (CASL still applies).
- Personal emails, personal phone numbers, birthdays and notes about people are **not** business contact information.

**New purpose, Schedule 1, 4.2.4.** for a purpose "not previously identified, the new purpose shall be identified prior to use." Also: "the consent of the individual is required" before that use.
- **Principle 5 (4.5):** do not use or disclose for other purposes without consent. Keep it only "as long as necessary".
- **Principle 4 (4.4):** collect only what is needed, "by fair and lawful means". Also 4.4.1: "Organizations shall not collect personal information indiscriminately."
- **Principle 6 (4.6):** keep it "as accurate, complete, and up-to-date as is necessary". This is the legal hook for a maintenance and pruning routine.

**Publicly available information, Regulations SOR/2001-7, s.1(b).** https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-7/FullText.html
- Consent is not needed for a person's details in "a professional or business directory, listing or notice, that is available to the public". This holds only where the use relates "directly to the purpose for which the information appears".
- Social-media profiles are **not** on the s.1 list. Reading the list, (a) to (e) cover phone directories, business directories, public registries, court records, and publications "where the individual has provided the information". Whether a LinkedIn profile is a "publication" under (e) is **not settled in anything we read**.

**Sending contacts to a cloud AI service.** See checks.md §8.
- Transfers for processing keep you responsible, and you need comparable protection by contract.
- The OPC generative-AI principles (7 Dec 2023) say to use "anonymized or de-identified information within prompts" where possible.
- Practical: let the AI write the merge/clean script and run it locally on the CSV. Alternatively, send only the columns needed, not whole MBOX files.

---

## 4. Enrichment and scraping

**What enrichment services do.** This is our general description; no regulator text defines it.
- They take a name and company (or a LinkedIn URL) and return a likely work email, title, phone, company size and so on.
- The data comes from public web pages, partner data, pattern-guessing (`first.last@domain`) with verification pings, and in some cases scraped social profiles.
- Vendor sourcing practices vary and are **not verified here**.

**OPC + international regulators: Joint statement on data scraping**, **24 Aug 2023**. https://www.priv.gc.ca/en/opc-news/speeches-and-statements/2023/js-dc_20230824/
- publicly accessible personal information "is still subject to data protection and privacy laws".
- those who scrape it "are therefore responsible for ensuring that they comply".
- The listed harms include "Unwanted direct marketing or spam – scraped data may include contact information".
- Also: scrapers "may aggregate and combine scraped data" with "other personal information". That is essentially what enrichment does.
- Mass scraping "can constitute a reportable data breach".
- It was sent to Alphabet (YouTube), ByteDance, Meta, Microsoft (LinkedIn), Sina and X.

**Concluding joint statement**, **October 2024** (page dated 2024-10-28). https://www.priv.gc.ca/en/opc-news/speeches-and-statements/2024/js-dc_20241028/
- Platform permission is not enough. Contractual authorisation "cannot, in and of themselves, render such scraping lawful".
- "commercial data scrapers should take note": public personal data is "generally ... subject to" privacy laws.
- The obligation to protect against unlawful scraping "applies to both large corporations and Small and Medium Enterprises".
- It now has 16 co-signatories.

**Implications for the article (our synthesis):**
- Enrich from sources the person controls or published for business: their company site, email signatures, business cards. These fit the s.10(9)(b)/(c) and SOR/2001-7 s.1(b) logic.
- Avoid tools that scrape LinkedIn or Facebook. They breach platform terms (§2), and the regulators' position is that "public" does not mean "free to use".
- If you buy enriched data, you inherit the question of how it was collected. Under PIPEDA 4.4 collection must be "by fair and lawful means".
- Record a `source` and `basis_for_contact` for every enriched field, and refresh or prune per Principle 6 (accuracy) and Principle 5 (retention).
