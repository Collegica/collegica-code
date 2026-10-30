## Access and confidence

Researched 2026-10-27. Where I could, I read the primary text directly from the Justice Laws site. That covers ITA ss. 12.2, 20, 89, 123.3, 125, 129, 148, 211.1 and 248, and Income Tax Regulations 306, 307, 308 and 1401. The Regulations page says they are "current to 2026-09-30". I also used CRA Folios S3-F2-C1 (last updated 14 Jan 2025) and S3-F6-C1, the Budget 2013 and Budget 2018 documents, CRA's corporation rate page, Quebec Finance Bulletin 2026-3 and the Assuris site.

Some sources were blocked (HTTP 403 or 404): PwC's Ontario 2026 budget page, Revenu Québec's news page, Sun Life's Suncentral PDFs, Manulife's advisor pages and Investment Executive. For those points I fell back to secondary sources, and each one is flagged below.

Confidence by item:
- **High.** The statutory mechanics (items 1–5, 7). CDA, ACB and NCPI. The 10/8 rules. Federal rates. Assuris limits.
- **Medium.** Ontario's July 2026 small-business rate cut. I confirmed it on CRA's rate page and in several accounting-firm write-ups, but not in the Ontario budget text. Also medium: which provinces follow the federal passive-income grind (Quebec is confirmed from its bulletin, BC from secondary sources), and the industry term "MTAR".
- **Low / no source found.** Any CRA position that names "infinite banking". I could not find one.

Quotes are kept under 15 words. "Quote" means exact text from the cited page. Everything else is paraphrase.

---

## 1. The exempt policy test (ITR 306)

**What it is.** A life insurance policy is an "exempt policy" if, on each policy anniversary, its savings component stays at or below that of an imaginary benchmark policy. The Regulation calls the savings component the "accumulating fund" and the benchmark the "exemption test policy". In the Regulation's words, the accumulating fund "does not exceed the total of the accumulating funds" of the test policies. The test ignores policy loans.
- ITR 306: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-306.html

**Why it matters.** The annual accrual rule in ITA s. 12.2 taxes the growth inside a life policy each year. It does not apply to "an exempt policy" (s. 12.2(1)). So in an exempt policy the cash value grows without annual tax. Tax arises only when you dispose of the policy (item 2). A death benefit paid under an exempt policy is expressly *not* a disposition: s. 148(9) "disposition", para (j)(ii). So there is no income inclusion at death.
- s. 12.2: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.2.html
- s. 148(9): https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-148.html

**Mechanics that matter for a reader.**
- **New test policies.** If the death benefit rises by more than 8% in a year, a fresh exemption test policy is deemed issued. The threshold is "8% of the amount of the benefit on death" (ITR 306).
- **The 250% rule.** After the 10th anniversary, the policy is checked against its value three years earlier. If the accumulating fund exceeds 250% of that earlier value, the test policies are re-dated under s. 306(7). This stops late, heavy funding from riding on an old benchmark (ITR 306).
- **Correcting a breach.** If the policy fails the test, the insurer normally has until 60 days after the anniversary to fix it, for example by raising the death benefit or paying out the excess. This is in s. 306(1)(b) and is industry practice. I paraphrased it and did not re-quote it.

**The 2017 changes.** These were announced in Budget 2013 and 2014, enacted in December 2014, and apply to policies issued after 2016. Policies issued before 2017 are grandfathered unless they are materially changed. Canada Life Tax & Estate Planning Group, "A practical view of the exempt test changes effective 2017" (current Oct 2021): https://www.acp.canadalife.com/content/dam/advisors/documents/strategies/tepg/en_ca/articles/li-taxation/a-practical-view-of-the-2017-exempt-test-changes-cl-en.pdf

The changes:
- **New benchmark.** Old: a 20-pay endowment at age 85, priced on the insurer's own assumptions. New: "an eight-pay endowment at age 90 policy" using prescribed rates (Canada Life).
- **Prescribed interest rate.** ITR 1401(4)(a)(i): "an annual interest rate of 3.5% is to be used". Old floor: 4% (ITR 307(1)). Sources: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1401.html and https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-307.html
- **Mortality table.** "Proposed CIA Mortality Tables, 1986–1992" for standard lives (ITR 1401(4)). Old: CIA 1969–75.
- **Each coverage tested separately.** On multi-coverage policies, each coverage now gets its own test policy (ITR 306).
- **Surrender charges ignored.** Cash value is now measured without deducting surrender charges, which cuts universal life over-funding room (Canada Life).
- **Net effect.** You can deposit more in the first 8 years. But the long-run maximum tax-sheltered fund is lower, because the benchmark reaches the face amount at 90 rather than 85 (Canada Life).

**"MTAR line".** This is industry shorthand, not a term in the Act or the Regulations; I confirmed it does not appear in ITR 306. It stands for "maximum tax actuarial reserve". It is the curve traced by the exemption test policy's accumulating fund: the ceiling a policy's cash value may not cross. Medium confidence on the expansion. It is widely used by insurers but is not in the statute.

**Insurer-level tax (a nuance worth telling readers).** Growth in an exempt policy is not entirely untaxed. Life insurers pay Investment Income Tax under Part XII.3 at "15% of its taxable Canadian life investment income" (s. 211.1(1)). Insurers build that cost into pricing (Canada Life, above).
- https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-211.1.html

## 2. Tax on surrender, withdrawal and policy loans

**The rule (s. 148(1)).** When a policyholder disposes of an interest in a policy, it includes in income the proceeds of disposition minus the policy's **adjusted cost basis (ACB)**. That excess is the "policy gain". It is ordinary income, not a capital gain, so it is fully included. If the result is negative, it is ignored (Canada Life).

**What counts as a disposition (s. 148(9)).** It includes "a surrender thereof" and "a policy loan made after March 31, 1978". It does *not* include:
- assigning the policy "for the purpose of securing a debt or a loan other than a policy loan". This is why a bank loan secured by the policy (IRP, item 6) is not taxed as a disposition.
- a death benefit under an exempt policy.
- Source: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-148.html

**Policy loans.**
- The proceeds of a policy loan are the lesser of the loan and the cash surrender value net of other loans (s. 148(9) "proceeds of the disposition").
- The loan is taxed only on the part that exceeds the ACB.
- Repaying the loan later restores ACB, and allows a deduction for amounts previously taxed.
- Interest on a policy loan is deductible only if the borrowed money is used to earn business or property income. The insurer must also certify the interest on Form T2210 (s. 20(2.1); CRA Folio S3-F6-C1, ¶1.84–1.86): https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-3-property-investments-savings-plans/series-3-property-investments-savings-plan-folio-6-interest/income-tax-folio-s3-f6-c1-interest-deductibility.html
- Interest on money borrowed *to buy* a life policy is excluded from deduction (s. 20(1)(c)(i)–(ii); Folio ¶1.59–1.60).

**Partial surrenders and withdrawals.** These use a proportionate share of the ACB (Canada Life).

**ACB and NCPI.**
- ACB is a statutory formula, roughly premiums paid plus certain additions, minus several deductions (s. 148(9) "adjusted cost basis", items A–O).
- The key deduction is item L, the **net cost of pure insurance (NCPI)**. It is a prescribed annual "cost of insurance" set out in ITR 308. It is not what the insurer actually charges.
- Simplified, NCPI = mortality probability × (death benefit − reserve). Because it is subtracted every year, ACB usually rises in the early years while premiums are paid. It then falls, and often reaches zero in late life.
- For post-2016 policies, NCPI uses the CIA 1986–92 table and subtracts the accumulating-fund reserve rather than the cash surrender value. The result is lower NCPI, so ACB is higher and lasts longer. That means smaller taxable gains on loans and surrenders, but a smaller CDA credit at death (Canada Life).
- ITR 308: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-308.html

## 3. The capital dividend account (CDA) and why ACB matters

**The rule.** ITA s. 89(1), "capital dividend account", para (d). A private corporation's CDA is credited with life insurance proceeds received "in consequence of the death of any person". The credit is reduced by the ACB "immediately before the death". For deaths after March 21, 2016, that is the ACB of the "policyholder's interest in the policy".
- https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-89.html
- CRA Folio S3-F2-C1 ¶1.60–1.60.1 (last updated 14 Jan 2025): https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-3-property-investments-savings-plans/series-3-property-investments-savings-plan-folio-2-dividends/income-tax-folio-s3-f2-c1-capital-dividends.html

**Paying it out.**
- The corporation elects under s. 83(2), filing Form T2054 with a CDA computation (Folio ¶1.17). Resident shareholders then receive the dividend tax-free.
- Over-electing triggers Part III tax "equal to 60% of the portion" that is not a capital dividend (Folio ¶1.87).

**Worked example (illustrative numbers, not sourced).** A $1,000,000 death benefit is paid to the corporation:
- ACB at death $150,000: CDA credit is $850,000, so $850,000 can be paid out tax-free and $150,000 goes out as a taxable dividend.
- ACB at death $0 (common in old age): the whole $1,000,000 can go out tax-free.

So a *declining* ACB is good for estate planning, because it raises the CDA credit. It is bad for living access, because loans and surrenders above ACB are taxed. The 2017 NCPI change moved the balance toward living access (Canada Life).

**Collateral-assigned policies.**
- If a policy is pledged to a lender (not absolutely assigned) and the corporation remains beneficiary, the net proceeds still go into the corporation's CDA (Folio ¶1.67).
- Proceeds paid straight to a creditor institution can also count, under conditions (¶1.68).
- Only *net* proceeds count. That is the death benefit minus ACB, not the full death benefit (¶1.70).
- Correction to a secondary claim: CRA TI 2012-0447171E5 is sometimes cited for "full death benefit credited". It actually allows no ACB reduction only for creditor's *group* insurance, and states the position "would not apply" to other products. https://taxinterpretations.com/cra/severed-letters/2012-0447171e5

## 4. Passive income rules (2018+) and why exempt-policy growth matters

**The rule.** Budget 2018, Ch. 1: "the amount of active business income eligible for the small business deduction would be reduced by $5 for every $1 of investment income above the $50,000 threshold". It is fully eliminated at $150,000. Budget 2018 equates the $50,000 threshold to about $1M of passive assets at 5%. https://www.budget.canada.ca/2018/docs/plan/chap-01-en.html

Enacted in s. 125(5.1), the business limit is reduced by $500,000 × 5 × (AAII − $50,000) ÷ $500,000, measured on the *prior* year's AAII of the corporation and its associated corporations. https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-125.html

**Does exempt-policy growth count as AAII? No, not while it accrues.**
- AAII (s. 125(7)) is built from "aggregate investment income" (s. 129(4)). It also adds "amounts in respect of a life insurance policy that are included in computing the corporation's income" (s. 125(7)).
- Annual growth inside an exempt policy is never included in income, because s. 12.2 does not apply. So it is outside AAII.
- Budget 2018 confirms the targeting. Investment income for this measure includes "income from non-exempt life insurance policies" (Ch. 1). I paraphrased this from the fetch summary and did not re-verify it word for word: medium confidence on the exact wording.
- **Caveat.** A *policy gain* on surrender, withdrawal or a policy loan above ACB *is* income, so it feeds AAII in the year it is realized.

**How much it matters (illustrative arithmetic on 2026 rates).** Take a CCPC with $500,000 of active income and a $2M portfolio yielding 5%:
- AAII = $100,000.
- Business limit falls by 5 × $50,000 = $250,000.
- The federal cost on that $250,000 is (15% − 9%) = **$15,000 a year**.
- If the province follows the grind (BC: 12% − 2% = 10% more), the cost becomes **$40,000**.
- Ontario does not follow the grind, so the cost is federal only: **$15,000**.
- At AAII ≥ $150,000 the whole $500,000 is ground: federal $30,000, plus BC $50,000 = $80,000.

If $1M of that portfolio instead sat inside an exempt policy, AAII would drop by about $50,000 and the grind would disappear. Two offsets:
- The policy's growth is reduced by cost of insurance, fees and the insurer's 15% IIT, and is less liquid.
- Income taxed at the general rate builds GRIP, so it can be paid out as *eligible* dividends taxed at lower personal rates. The grind is partly a deferral cost, not a pure loss. This is standard integration reasoning; I did not find a single primary quote for it.

**Which provinces follow the grind.**
- **Quebec does.** Its bulletin says the business limit is reduced when AAII "is between $50 000 and $150 000" (Bulletin 2026-3, fn. 1).
- **Ontario and New Brunswick do not.** Secondary sources, medium confidence; for example the RBC Wealth Management blog: https://wmc.rbcwealthmanagement.com/aaron-fennell/blog/small-business-deduction-grind:-the-impact-of-earning-passive-investment-income-in-a-private-corporation-8705261348316301447
- **BC and Alberta do.** Same RBC source, medium confidence.

**Corporate rates in 2026.** Source: CRA, https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html

| Jurisdiction | Small business (combined) | General (combined) |
|---|---|---|
| Federal alone | 9% | 15% |
| Ontario | 2.2% → **11.2%** (cut from 3.2% effective **1 July 2026**, prorated for straddle years; was 12.2%) | 11.5% → **26.5%** |
| British Columbia | 2% → **11%** | 12% → **27%** |
| Quebec | 2.2% → **11.2%** for taxation years starting after 29 Apr 2026 (was 3.2% → 12.2%). Requires 5,500 paid hours or primary/manufacturing activity, with linear reduction between 5,000 and 5,500 hours | 11.5% → **26.5%** |

Sources for the rate changes:
- Ontario cut: CRA rate page (above) plus accounting-firm summaries, for example https://welchllp.com/insights/knowledge/ontarios-small-business-tax-rate-is-changing-what-business-owners-need-to-know/
- Quebec: Finance Québec Information Bulletin 2026-3 (29 Apr 2026), "the minimum tax rate … currently at 3.2%, will drop to 2.2%". https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/finances/publications-adm/Bulletins/EN/BULEN_2026-3.pdf

**Budget changes 2024–2026 (relevance check).**
- **Capital gains inclusion.** Budget 2024 proposed raising it from 1/2 to 2/3, first for gains from 25 Jun 2024, then deferred to 1 Jan 2026. It was **cancelled on 21 Mar 2025**, so the 50% inclusion stands. This matters here because the non-taxable half of a corporate capital gain also flows to the CDA, and the passive-portfolio comparison depends on it. https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase
- **Federal Budget 2025 (4 Nov 2025).** Per CALU: "does not propose any changes to … the tax rules governing life insurance products". https://calu.com/wp-content/uploads/2025/11/Budget-2025-1.pdf
- **Provincial.** I found no 2026 federal budget measure touching life insurance. The provincial small-business rate cuts in Ontario and Quebec are the only relevant 2026 changes.

## 5. Corporate ownership: shareholder benefits, premium deductibility, beneficiary

**Premiums are generally not deductible.** CRA treats them as "on account of capital" and so non-deductible under s. 18(1)(b). The exception is s. 20(1)(e.2) (TI 2012-0446491E5). https://taxinterpretations.com/cra/severed-letters/2012-0446491e5

**The s. 20(1)(e.2) collateral exception.** All of these conditions must hold:
- an interest in the policy is "assigned to a restricted financial institution", that is, a bank, trust company or credit union, not a private lender;
- the interest on the loan is deductible;
- the assignment is "required by the institution as collateral".

The deduction is the least of (i) premiums payable, (ii) NCPI for the year, and (iii) the portion of those relating to the debt outstanding. https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-20.html

Because post-2017 NCPI is lower, this deduction is smaller on newer policies (Canada Life).

**Shareholder benefit (s. 15(1)).**
- **Corporation owns the policy and is sole beneficiary.** Premium payments "would not ordinarily constitute a taxable benefit" (TI 2012-0446491E5).
- **A shareholder, or a person related to one, is beneficiary or owner while the company pays.** CRA assesses a s. 15(1) benefit equal to the *premiums paid*, not the death benefit. That is CRA's long-standing practice per insurer commentary, for example the Canada Life TEPG article on beneficiary designations: https://www.acp.canadalife.com/content/dam/advisors/documents/strategies/tepg/en_ca/articles/corporate-owned/beneficiary-designations-with-corporate-owned-life-insurance-cl-en.pdf (I did not open this one; it was a search result).
- **Split arrangements.** For shared or split-dollar setups between related companies, CRA (2024 CALU Roundtable, 2024-1007091C6) declined to confirm there is no benefit. Its answer: case-by-case only. https://taxinterpretations.com/cra/severed-letters/2024-1007091c6

**Who should be beneficiary.** In practice, the corporation that owns and pays for the policy should also be the beneficiary. That avoids a s. 15(1) benefit, and the proceeds come into the corporation and generate the CDA credit. If a family member is named instead, two things go wrong: the premiums become a taxable benefit, and the CDA mechanism is lost. Holdco vs Opco ownership is a further structuring question, involving creditor exposure and the cash value counting as a passive asset for the QSBC share tests. I found no primary source here, so this is flagged for professional review, not stated as fact.

## 6. Leveraged strategies: IRP, 10/8, LIAs, "infinite banking"

**Insured Retirement Program (personal or corporate IRP).**
- An exempt policy accumulates cash value. Later, a *bank* lends against it under a collateral assignment, which is not a disposition (s. 148(9) para (f)).
- The cash is therefore received without a policy-gain inclusion.
- Interest is often capitalized, and the death benefit repays the loan.
- **Manulife Bank terms (example of market practice).** Lends "up to 75% of the net cash surrender value" (basic) or 90% (custom). Applicants must be "age 50 or older to apply". If the loan grows past the margin, "the bank may require additional collateral or a principal paydown". https://www.advisor.ca/partner-content/expert-advice/expert-insurance-lending-advice-from-manulife-bank/what-are-the-most-common-questions-about-the-insured-retirement-program-line-of-credit/
- **Corporate IRP variant.** The *shareholder* borrows personally and the corporation guarantees the loan by pledging its policy. CRA says the shareholder-benefit question needs "a review of all of the circumstances". If the shareholder pays "a reasonable fee", the guarantee alone gives no benefit. If the corporation's security is realized to pay the bank, that payment is "generally" a benefit to the shareholder (2006 CTF Roundtable, 2006-0174011C6, an old view). https://taxinterpretations.com/cra/severed-letters/2006-0174011c6 The guarantee fee is taxable income to the corporation.
- **Interest deductibility.** Only if the borrowed money is used to earn income (s. 20(1)(c)). Money spent on retirement living is not deductible. Borrowing to pay premiums is barred (Folio S3-F6-C1).
- **Risks.**
  - Rising interest rates compound the capitalized balance.
  - Weak policy dividends or returns lower the cash value.
  - Either can trigger a collateral call, a forced paydown, or a forced surrender. A forced surrender would trigger a policy gain *and* lose the insurance.
  - Lenders may change terms.
  - The lower CDA credit at death, after the loan is repaid, leaves less for heirs.
  - CRA challenge if the arrangement looks like a 10/8 or a LIA.

**10/8 arrangements (eliminated by Budget 2013).**
- The structure: a policy's investment account earns, for example, 8% tax-free. An equal loan is taken at 10%, secured by the policy, and the borrowed money is invested so the interest is deductible.
- Budget 2013 denied:
  - interest deductions on such borrowing "that relates to a period after 2013";
  - the s. 20(1)(e.2) premium deduction for the same period;
  - the CDA credit, which is reduced by the borrowing.
- It allowed tax-favoured withdrawals to unwind before 1 Jan 2014.
- Budget 2013 Annex 2: https://www.budget.canada.ca/2013/doc/plan/anx2-eng.html
- **Statutory definition.** "10/8 policy" (s. 248(1)) means a policy where a borrowing or policy loan is secured by an interest in the policy or its investment account, and the return credited to that account is tied to the loan's interest rate, or the account's size is capped by reference to the loan. https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html
- s. 20(2.01) blocks the interest deduction.
- **Distinction for readers.** An ordinary IRP is *not* a 10/8, because the loan rate and the policy return are not linked.

**"LIRA?" in the brief should read LIA: leveraged insured annuity.**
- Budget 2013 also targeted LIAs. An "LIA policy" is accrual-taxed, its premiums are not deductible, and its death benefit gives no CDA credit. The s. 89(1)(d) text excludes an "LIA policy".
- On 26 Aug 2020 CRA warned about *offshore* LIA schemes. It said they abuse the CDA rules and it would consider GAAR. https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2020/watch-out-offshore-leveraged-insured-annuity-schemes.html
- Globe and Mail summary (29 Oct 2020): https://www.theglobeandmail.com/investing/personal-finance/taxes/article-cra-takes-offence-with-leveraged-insurance-products/
- A LIRA, a locked-in retirement account, is unrelated.

**Recent CRA warning.** 4 Dec 2025, on "aggressive tax schemes involving critical illness insurance policies" that create artificial shareholder-loan accounts. Penalties and possible criminal charges were flagged. Summarized by the Canadian Tax Foundation: https://www.ctf.ca/EN/EN/Newsletters/Canadian_Tax_Focus/2026/1/260110.aspx

**"Infinite banking" / "be your own bank".**
- A marketing label for an over-funded participating whole-life policy whose cash value is borrowed against, through policy loans or bank loans.
- **No CRA document addressing "infinite banking" by name was found.**
- The tax treatment is simply the general rules above:
  - policy loans are dispositions, taxable above ACB: "Any policy loan in excess of the policy's ACB … will be taxable" (MoneySense, J. Chevreau, 21 Nov 2023, https://www.moneysense.ca/columns/retired-money/infinite-banking-in-canada/);
  - interest is deductible only for income-earning use, with Form T2210;
  - premiums are non-deductible.
- Critics quoted there call it "almost all vendor-push or broker-push".

## 7. The real comparison: a passive portfolio inside a CCPC vs exempt-policy growth

**How passive income in a CCPC is taxed.** EY 2026 corporate investment income rates, which include changes to 15 Jan 2026: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-ca/services/tax/tax-calculators/2026/ey-tax-rates-corporate-investment-2026-01-15-v1.pdf
- **Federal rate on CCPC investment income (interest, rent, foreign income, taxable capital gains): 38.67%.** That is 28% base plus the 10 2/3% refundable tax (s. 123.3), with no general rate reduction. https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-123.3.html
- **Combined rates.** Ontario 50.17%, Quebec 50.17%, BC 50.67%, Alberta 46.67%.
- **Refundable portion.** 30 2/3% of aggregate investment income goes to non-eligible RDTOH (s. 129(4) "non-eligible refundable dividend tax on hand"). It is refunded at 38 1/3% of taxable dividends paid (s. 129(1)). https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-129.html
  - Net corporate tax after the refund is about 19.5% in Ontario. The refund only arrives when dividends are paid, and the shareholder then pays personal dividend tax.
- **Capital gains.** Half is taxable at about 50%, giving an effective ~25%. The other half goes to the CDA tax-free. The cancelled 2/3 inclusion would have changed this (item 4).
- **Canadian portfolio dividends.** Part IV tax applies (38 1/3%), fully refundable. Not separately fetched; standard rule.

**Exempt policy.**
- No annual corporate tax on the growth.
- But the return is net of cost of insurance, insurer expenses, the insurer's 15% IIT, commissions and early surrender charges.
- No contribution to AAII, so no SBD grind (item 4).
- At death, the death benefit less ACB passes through the CDA tax-free.
- Living access is either through policy gains, taxed as income and counted in AAII, or through a collateral loan (item 6).

**Framing.** The fair comparison is not "taxed investment vs untaxed insurance". It is a corporate portfolio taxed at about 50% with partial refund and CDA on half of capital gains, *plus* any SBD grind, against a policy whose internal return is lower before tax, illiquid early on, and tax-advantaged mainly *at death*. The policy wins mostly when the insurance need is real, the time horizon reaches to death, and the corporation would otherwise trip the $50k AAII line.

**Integration note.** CCPC refundable taxes aim to make income earned in a corporation and paid out as dividends cost roughly the same as income earned personally. The CDA is the channel that lets tax-free items, including insurance proceeds net of ACB, come out tax-free.

## 8. Policyholder protection: Assuris

Assuris is the industry-funded protector if a member life insurer fails. Whole life limits: https://assuris.ca/how-am-i-protected/assuris-protection/life-insurance/individual/whole-life/
- **Death benefit.** "Up to $1,000,000 or 90% of your death benefit, whichever is higher."
- **Cash value.** "Up to $100,000 or 90% of your cash value, whichever is higher."
- **Associated investment account** (prepaid premiums or dividends on deposit). Same $100,000 or 90% rule.
- Universal life page: https://assuris.ca/how-am-i-protected/assuris-protection/life-insurance/individual/universal-life/

Practical point: a corporate policy with $3M of cash value is protected for 90% ($2.7M), not 100%. The page gave no date for when these limits were set.

---

### Open items to verify before publication
1. Ontario 2026 budget primary text for the 2.2% rate and its 1 July 2026 effective date. PwC's page was blocked.
2. BC's and Alberta's adoption of the AAII grind, from a primary provincial source.
3. The exact Budget 2018 wording on "non-exempt life insurance policies".
4. CRA's current position on corporate guarantee fees for corporate IRPs. The 2006 view is old; look for a recent CALU Roundtable.
5. Holdco vs Opco ownership, and the effect of cash value on the QSBC asset tests. No source gathered.
