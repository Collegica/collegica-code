# Rivera Renos: contacts database

Built 31 Oct 2026 from your exports, then **updated the same day with `exports/2026-10-31-update/`** (see "Update log" at the end). Everything ran on this computer. Nothing was sent and nothing connected to the internet.

> **This is not legal advice.** The CASL rules below are applied mechanically from the evidence in your exports. If a decision matters, for example before a big campaign, check it with the CRTC guidance (fightspam.gc.ca) or a lawyer.

## What I built

| File | What it is |
|---|---|
| `contacts.db` | SQLite database, one row per person in `people`. Open it with DB Browser for SQLite, TablePlus, or `sqlite3`. |
| `build_contacts.py` | Rebuilds the database from `./exports`. Safe to re-run. Python 3 standard library only, works offline. |
| `selftest.py` | Checks that a re-run keeps your notes, merge decisions, old emails and unsubscribes. It runs on a throwaway copy. |

I didn't read or use `make_exports.py` or `PROMPT.txt`.

**Sources read:** Google Contacts (15), Yahoo Contacts (8), iCloud vCards (10), LinkedIn Connections (14), Facebook friends (12), and the Gmail mailbox (23 emails, May 2024 to Oct 2026). That's 71 source records in total. The 31 Oct update added a second LinkedIn `Connections.csv` (4 rows) and a second Gmail `Mail.mbox` (1 email): 75 source records and 24 emails now.

### Useful tables and views
- `v_contacts`: the everyday view. Name, best email and phone, company and title, last email each way, how often you email, CASL status, and your notes.
- `v_can_email_today`: who you may send marketing email to today, and until when.
- `v_do_not_email`: your suppression list. Load it into any mailing tool you use.
- `merge_review`: the possible duplicates I didn't merge.
- `field_values`: **where every field came from**. Every value from every source is listed with its source file and record, and `chosen=1` marks the value used, with the reason.
- `source_records`: each raw record, which person it went to, and why (`same email`, `same phone`, `same full name`).
- `email_stats`: first and last email, last emailed by you, last email from them, counts, emails in the last 12 months, and the average gap between emails.
- `casl_status` and `casl_evidence`: the CASL decision and the dated evidence behind it.

## How many people

**27 rows. That becomes 26 people if you confirm the flagged merge below.** (After the update: Grace Li's two rows merged into one, and Hana Kim is new.)

How records were matched:
- **Merged automatically** when records share an email address, a phone number (formats like `416.555.0000` and `+1 416 555 0000` are treated as the same), or a LinkedIn URL, and the names fit (Ben/Benjamin, Kate/Katherine and Raj/Rajesh count as fitting).
- **Merged on exact full name** only when nothing contradicts it: no different emails, phones or companies. Facebook and most LinkedIn entries have no email, so they were linked by name. Each one is labelled `same full name` in `source_records`, so you can tell them apart from stronger links.
- **Flagged, not merged**, when the names are similar but not identical, or identical but something conflicts.

## Merges I wasn't sure about (please decide)

| # | Records | Why I didn't merge |
|---|---|---|
| 1 | **Ella MacDonald** (Yahoo + iCloud) vs **"Ella Mac"** on Facebook (friends since 2015) | "Mac" looks like a shortened MacDonald, but nothing else links them. |

To decide, run one of these. Your answer is saved and used on every future run:
```
python3 -I build_contacts.py --confirm-merge 1     # same person
python3 -I build_contacts.py --reject-merge 1      # different people
```
Review numbers are recounted on every run, so check `merge_review` for the current number first. (Ella was #2 before the update.)

*Resolved by the update:* the Grace Li question (Google/Yahoo Grace vs LinkedIn Grace at Harbour Lending). The new LinkedIn export shows the same email address on the same LinkedIn profile, so the two were merged automatically as one person (ID 20).

## Company and title: which source I trusted

The order is **LinkedIn first, then Google, then iCloud, then Yahoo.** LinkedIn is updated by the person themselves, so it's the most likely to be current. Google is the address book on the Gmail account you actually use. iCloud and Yahoo entries are undated and were typed in by you. Yahoo looks like your oldest list: it has "Benjamin", an all-caps email address, and "Li Mortgages" for Grace.

Conflicts are kept in `people.job_conflicts`, not thrown away:
- **Rajesh Kumar**: LinkedIn says *Operations manager*; Google says *Site supervisor*. I used LinkedIn, which suggests a promotion.
- **Grace Li**: LinkedIn says *Senior mortgage advisor, Harbour Lending*; Google says *Li Financial*; Yahoo says *Li Mortgages*. I used LinkedIn (merged in the 31 Oct update).
- **Ana Okafor**: the newer LinkedIn export says *Co-founder, Okafor & Bell Interiors*; the older LinkedIn export and Google say *Interior designer, Okafor Design*. I used the newer LinkedIn.

When the same source appears in more than one export (two LinkedIn files, for example), the **newer export wins**. "Newer" means a date in the folder or file name (`2026-10-31-update`, `google-2027-01`), or failing that the file's modified time. Older values stay listed in `job_conflicts` and `field_values`.
- **Ben Tremblay**: every source, including Ben's August 2026 email signature, says *Maple Property Mgmt*, so there's no conflict.

You can override any value and the override survives re-runs:
```sql
INSERT OR REPLACE INTO my_field_overrides (person_id, field, value, note)
VALUES (20, 'company', 'Harbour Lending', 'Told me in person');
```

## Who you can email about your business (CASL), as of 31 Oct 2026

The rules applied: express consent lasts until they withdraw it. A **purchase** gives implied consent for 2 years. An **inquiry** (a quote request, for example) gives implied consent for 6 months. An unsubscribe request is permanent and must be honoured within 10 business days. Being in your address book, or a LinkedIn or Facebook friend, is **not** consent.

### ✅ Can email today (5)
| Person | Why | Last day to send |
|---|---|---|
| **Farid Haddad** (Haddad Architects) | Express consent: *your own entry*, "Signed up for our newsletter on the paper form at the trade show", 25 Oct 2026. Keep that paper form. | No end date until Farid withdraws |
| **Ben Tremblay** (Maple Property Mgmt) | Purchase: you invoiced Unit 4B on 15 Oct 2026 | **14 Oct 2028** |
| **Victor Leclerc** | Inquiry: emailed 31 Oct 2026, "Could you send an updated quote for the bathroom?" | **29 Apr 2027** |
| **Katherine O'Brien** | Purchase: kitchen invoice sent 16 Jun 2025, paid 17 Jun 2025 | **16 Jun 2027** ⚠️ |
| **Olivia Martin** | Inquiry: asked for a basement quote on 20 Sep 2026 | **19 Mar 2027**. If Olivia hires you, this becomes a purchase and runs 2 years from then. |

⚠️ Katherine's invoice number is `#2024-117`. If that job was actually finished and paid in 2024, the window may already be over. Check your books.

These were found automatically by looking for words like "invoice", "paid", "quote" and "estimate", so check each one. If you add evidence of your own (signed contracts, paper consent forms), it goes in `my_casl_evidence`:
```sql
INSERT INTO my_casl_evidence (person_id, basis, evidence_date, note)
VALUES (12, 'express_consent', '2026-11-10', 'Ticked the newsletter box on the paper form at the Leslieville site');
-- basis: express_consent | purchase | contract | inquiry | personal_relationship | family_relationship | business_card | withdrawn
```

### ⛔ Do not email (1)
- **Uma Bose** asked on **20 Oct 2026**: *"please don't send me any more promotional emails."* The 10-business-day deadline is **3 Nov 2026**. Uma is on `v_do_not_email`, and the script never deletes that list, even if a future export no longer contains that email. The request says "any more", so promotional emails have reached Uma from *somewhere* that isn't in these exports. Find that list or tool and remove Uma there too.

### ❓ Your call (2): no consent on record, but one may apply
- **Devendra Patel**: your Google note says *"met at home show 2024."* If Devendra gave you a business card and didn't say "no emails", CASL implies consent, but **only for messages relevant to the job** (realtor). A referral-partner note fits that; a general promotion doesn't. (Farid had the same note and has moved up to "Can email" because of your express-consent entry.) Devendra also referred a Parkdale client to you (your 13 Apr 2026 thank-you email). That referral doesn't give you consent to email Devendra.
- **Sofia Rossi**: a Facebook friend since 2018 who invited your family to a BBQ (2 Jul 2026). If Sofia is a genuine friend or family member, the personal/family-relationship exemption applies.

If any of these apply, record it as `business_card`, `personal_relationship` or `family_relationship` in `my_casl_evidence` and re-run.

### ⌛ Consent has expired (2)
- **Maya Goldberg**: paid for the deck on 13 May 2024. That window ended after **12 May 2026**.
- **Quinn Taylor**: asked for a fence quote on 29 Nov 2024. That window ended after **28 May 2025**, and you never replied to that email.

### 🚫 No consent found (14)
Ana Okafor, Chloé Nguyen, Ella MacDonald, Grace Li, Hugo Silva, Inès Dubois, Jamal Ahmed, Liam Chen, Noah Fraser, Priya Sharma, Rajesh Kumar, Thomas Wright, Wen Zhao, Zoë Campbell.

Several of these people are trade partners. Ana is a designer you're working with; Liam (plumbing), Jamal (inspections) and Wen (tile) are suppliers who email *you*. Normal one-to-one work email with them is fine. Adding them to a promotional list isn't, unless they agree.

### No email address at all (3)
"Ella Mac" (Facebook), Yusuf Demir (Facebook only), and Hana Kim (LinkedIn only, new in the 31 Oct update).

## How often you email people (from the Gmail export)
- **Liam Chen**: 6 emails from Liam (plumbing schedules), about every 25 days. The last was 30 Sep 2026.
- **Ben Tremblay**: 3 emails Aug to Oct 2026. You last emailed Ben on 15 Oct (the invoice).
- **Ana Okafor**: you emailed on 10 Oct and got a reply on 11 Oct 2026.
- **Olivia Martin**: you sent a quote on 21 Sep 2026.
- You last emailed **Devendra Patel** on 13 Apr 2026, **Victor Leclerc** on 4 Jan 2026 and **Katherine O'Brien** on 16 Jun 2025.
- Inbound only: Uma (20 Oct 2026), Jamal (27 Jul 2026), Sofia (2 Jul 2026), Quinn (29 Nov 2024), Maya (13 May 2024).
- The other 15 people have no email in the export. Only Gmail mail was exported; Yahoo and iCloud mail weren't, so these counts only cover Gmail.

## Re-running when you add new exports

Put the new files anywhere under `./exports` (for example `exports/google-2027-01/`), then run:
```
python3 -I build_contacts.py
```
The format of each file is detected automatically: Google or Yahoo CSV, LinkedIn `Connections.csv`, `.vcf`, Facebook friends JSON, or `.mbox`.

**What a re-run keeps:** your notes (`my_notes`), overrides, CASL evidence, merge decisions, every email ever imported (so old purchases and unsubscribes still count when a newer export leaves them out), the suppression list, and person IDs. A person's ID stays the same, so notes stay attached. If two people later merge, their notes move to the surviving person.

**What a re-run rebuilds:** everything derived from the exports.

Add notes with:
```
python3 -I build_contacts.py --add-note 6 "Owns three buildings on Queen W"
```
or insert them straight into `my_notes`. To check the re-run logic still works: `python3 -I selftest.py`.

CASL dates are worked out as of the day you run the script. Re-run before every campaign, because Olivia's window ends in March 2027, Victor's in April 2027 and Katherine's in June 2027.

## What you should NOT do
1. **Don't email Uma Bose** anything promotional, from any address or tool, ever, unless Uma gives you new express consent.
2. **Don't export LinkedIn or Facebook contacts into a mailing list.** A connection isn't consent, and it breaks those platforms' terms.
3. **Don't send an email asking for consent** ("Can I add you to my newsletter?"). CASL treats that email as a commercial message too. Ask in person, by phone, or with a sign-up form, and record it in `my_casl_evidence`.
4. **Don't email past the "last day to send"** shown for each person.
5. **Don't send a commercial email without** your business name, a mailing address plus phone or email, and a working unsubscribe that you honour within 10 business days.
6. **Don't treat the auto-detected evidence as proof** without checking it. Under CASL, *you* have to prove consent. Keep the invoices and emails.
7. **Don't delete rows from `suppressions`.** If an entry is wrong (someone was not really unsubscribing), set `user_cleared = 1` and write the reason in `user_cleared_reason`.
8. **Don't share `contacts.db`.** It holds personal information (emails, phones, a birthday), and Canada's privacy law (PIPEDA) applies to it.

**This is fine without marketing consent:** replying to questions, sending quotes people asked for, invoices, warranty and safety notices, and scheduling with existing clients. CASL exempts these transactional messages from the consent rules.

## Update log

### 31 Oct 2026: `exports/2026-10-31-update/` (LinkedIn `Connections.csv`, 4 rows; Gmail `Mail.mbox`, 1 email)
Backup of the database before this update: `backups/contacts.before-2026-10-31-update.db`.

- **New person:** Hana Kim (ID 28), Project lead at Kim Heritage Restoration. LinkedIn connection made 28 Oct 2026. No email address, so not emailable.
- **Changed job:** Ana Okafor (ID 12), from *Interior designer, Okafor Design* to *Co-founder, Okafor & Bell Interiors* (newer LinkedIn export). Your note on Ana is unchanged.
- **Merge:** Grace Li. The LinkedIn-only Grace (old ID 27) merged into Grace Li (ID 20) on the same email address plus the same LinkedIn profile URL. ID 27 now points to 20 in `person_id_aliases`. Company and title are now *Harbour Lending, Senior mortgage advisor*.
- **CASL, caused by the new exports:** Victor Leclerc moved from *expired* to **can email until 29 Apr 2027** (new quote request, 31 Oct 2026).
- **CASL, caused by your own entry rather than the exports:** Farid Haddad moved from *your call* to **can email (express consent)**. This comes from the `my_casl_evidence` row you added (paper newsletter form, 25 Oct 2026). It had not been applied to the database before this run.
- **Kept:** your note on Ana, your consent record for Farid, Uma's unsubscribe, all 23 earlier emails, and every person ID.
- **Worth knowing:**
  - The new LinkedIn file has only 4 connections, but the old one has 14. It looks like a partial export, so the other 10 were **not** treated as removed. They're still in the database from the older file.
  - The new file gives different "Connected On" dates for two people: **Grace** (3 Mar 2021 vs 4 Jun 2021 before) and **Farid** (11 Jun 2019 vs 19 Feb 2020). The newer dates are used. This has no effect on CASL, because a connection isn't consent.
- **Script change:** when the same source appears in two exports, the newer one now wins (previously the order of folder names decided). The self-test now counts emails relative to the starting total, not a fixed 25. The self-test passes 8/8.
