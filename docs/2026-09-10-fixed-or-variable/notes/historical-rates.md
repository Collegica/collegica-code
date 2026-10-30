# Historical rate data for "Fixed or variable?" — research note

Research date: 2026-09-10 (all "today" values are as of this date unless stated).
Purpose: supply the inputs for two look-back simulations —
(A) 5-year term signed September 2021 → September 2026;
(B) 3-year term signed September 2023 → September 2026;
comparing 5-year fixed vs 5-year variable (and, for B, 3-year fixed). This note supplies data only; no payment arithmetic is done here.

## Access and confidence

| Source | Result | Notes |
|---|---|---|
| Bank of Canada Valet API (`V39079` overnight target, `V80691311` prime, `V80691335` 5-yr conventional mortgage, `BD.CDN.5YR.DQ.YLD` 5-yr benchmark bond) | fetched, full series 2020-12 → 2026-09-09 | https://www.bankofcanada.ca/valet/observations/V39079/json?start_date=2020-12-01 (same pattern for the others). This is the same data as the "Canadian interest rates and monetary policy variables: 10-year lookup" page. Highest-confidence source in this note. |
| Bank of Canada policy-rate page | fetched | https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/ — announcement table Apr 2025 → Sep 2026. |
| WOWA prime-rate history | fetched | https://wowa.ca/banks/prime-rates-canada — every prime change with effective date. |
| nesto BoC schedule / BoC rate pages | fetched | https://www.nesto.ca/mortgage-basics/bank-of-canada-interest-rate-schedule/ and https://www.nesto.ca/mortgage-basics/bank-of-canada-interest-rate/ |
| ilovemoney BoC tracker | fetched but **unreliable** | https://ilovemoney.net/calculators/canada/boc-rates — its 2025 rows put the last two cuts on Jun 4 and Jul 30 2025 (wrong; the BoC's own page and Valet show Sep 17 and Oct 29 2025) and its 2026 dates do not match the BoC schedule. Not used except as a negative cross-check. |
| WealthNorth rate history | fetched (both URLs) | https://wealthnorth.ca/mortgages/rates/mortgage-rate-history/ and https://wealthnorth.ca/mortgages/mortgage-rate-history/ |
| NerdWallet rate history | fetched | https://www.nerdwallet.com/ca/mortgages/mortgage-rate-history-in-canada |
| MyPerch rate history | fetched | https://myperch.io/homeowners/the-history-of-mortgage-rates-in-canada/ (page content is stale — it still says "current 5.00%") |
| LowestRates.ca | **403 ×3** (WebFetch twice, curl with browser UA once) → [snippet] only | https://lowestrates.ca/resource-centre/mortgage/historical-mortgage-rates-averages-trends |
| GlobalPropertyGuide | **403 ×3** → [snippet], no usable numbers surfaced | https://www.globalpropertyguide.com/north-america/canada/mortgage-interest-rate |
| ViewHomes | **403 ×3** → [snippet] | https://www.viewhomes.ca/blog/canadian-mortgage-statistics/ |
| Wayback Machine | WebFetch is blocked for web.archive.org; **curl to the CDX index and raw `id_` snapshots worked**. Every snapshot below is labelled with its true `Memento-Datetime`, because Wayback silently serves the nearest capture (e.g. the "Sept 2021" 3-year-fixed page is actually Oct 28 2021). | |
| Ratehub archived pages (Sept 2021, Sept 2023, June 2021, June 2023) | fetched via Wayback curl; 2023 pages parsed from embedded `__NEXT_DATA__` JSON, which carries an explicit `insuranceBucket` field | see section 3 |
| Canadian Mortgage Trends posts (Sept 18 2021, Sept 22 2023, Sept 28 2023) | fetched via Wayback curl (live site 403s) | see section 3 |
| BoC Staff Analytical Notes 2022-19, 2023-19, 2025-21; FSR 2023, FSR 2025, FSR 2026 (Households chapter) | fetched | see section 6 |
| Penalty sources (LoansCanada, nesto Jan 2026, Globe/McLister 2019) | fetched | see section 7 |
| CMT negative-amortization/OSFI article (Nov 2023) | 403 → Globe and Mail figures used from search [snippet] with URLs | see section 6 |

Confidence key used below: **[archived]** = read directly from an archived page or an official data series; **[article]** = a contemporaneous news post quoting a rate; **[snippet]** = search-result excerpt only; **[stale]** = a page whose visible date is later than the target date.

---

## 1. Bank of Canada target for the overnight rate — every change, Jan 2021 → Sep 2026

Sources cross-checked: (a) BoC Valet series V39079, business-daily, which records the *effective* date (since 2021 a change takes effect the day after the announcement); (b) BoC policy-rate page (Apr 2025 → Sep 2026 announcement table); (c) nesto's table (2020 → Jan 2026, announcement dates with prime). All three agree. WOWA prime table (section 2) gives a fourth implicit check since prime moved by the same amount the next day every time.

Rate entering 2021: **0.25%** (set 2020-03-27, effective 2020-03-30). No changes in 2021 (holds on Jan 20, Mar 10, Apr 21, Jun 9, Jul 14, Sep 8, Oct 27, Dec 8 2021, and Jan 26 2022).

| Announcement date | Effective date (Valet) | New target | Change |
|---|---|---|---|
| 2022-03-02 | 2022-03-03 | 0.50% | +0.25 |
| 2022-04-13 | 2022-04-14 | 1.00% | +0.50 |
| 2022-06-01 | 2022-06-02 | 1.50% | +0.50 |
| 2022-07-13 | 2022-07-14 | 2.50% | +1.00 |
| 2022-09-07 | 2022-09-08 | 3.25% | +0.75 |
| 2022-10-26 | 2022-10-27 | 3.75% | +0.50 |
| 2022-12-07 | 2022-12-08 | 4.25% | +0.50 |
| 2023-01-25 | 2023-01-26 | 4.50% | +0.25 |
| 2023-06-07 | 2023-06-08 | 4.75% | +0.25 |
| 2023-07-12 | 2023-07-13 | 5.00% | +0.25 |
| (holds: 2023-09-06, 10-25, 12-06; 2024-01-24, 03-06, 04-10) | | 5.00% | — |
| 2024-06-05 | 2024-06-06 | 4.75% | −0.25 |
| 2024-07-24 | 2024-07-25 | 4.50% | −0.25 |
| 2024-09-04 | 2024-09-05 | 4.25% | −0.25 |
| 2024-10-23 | 2024-10-24 | 3.75% | −0.50 |
| 2024-12-11 | 2024-12-12 | 3.25% | −0.50 |
| 2025-01-29 | 2025-01-30 | 3.00% | −0.25 |
| 2025-03-12 | 2025-03-13 | 2.75% | −0.25 |
| (holds: 2025-04-16, 06-04, 07-30) | | 2.75% | — |
| 2025-09-17 | 2025-09-18 | 2.50% | −0.25 |
| 2025-10-29 | 2025-10-30 | 2.25% | −0.25 |
| (holds: 2025-12-10; 2026-01-28, 03-18, 04-29, 06-10, 07-15, 09-02) | | 2.25% | — |

Today (2026-09-10): **2.25%**, unchanged since 2025-10-30; Sep 2 2026 was the seventh consecutive hold. Next announcement 2026-10-28 (with MPR). Sources: https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/ ; https://www.bankofcanada.ca/2026/09/fad-press-release-2026-09-02/ ; Valet V39079.

Peak-to-trough summary useful for the article: 0.25% → 5.00% in ten hikes over 16 months (Mar 2022 – Jul 2023); 5.00% held 11 months; 5.00% → 2.25% in nine cuts over 17 months (Jun 2024 – Oct 2025).

## 2. Big-bank prime rate — every change, same period

Sources: WOWA prime history (effective dates) https://wowa.ca/banks/prime-rates-canada ; BoC Valet V80691311 (weekly Wednesday observations, so its dates lag the effective date by up to 6 days — used to confirm levels, not dates); nesto's table (prime column). All agree on levels.

Prime entering 2021: **2.45%** (since 2020-03-30). Spread over the overnight target was **+2.20 at every single point from Jan 2021 to Sep 2026** — verified against every row above (2.45−0.25, 2.70−0.50, … , 7.20−5.00, … , 4.45−2.25). Banks moved prime the day after each BoC announcement, by the full amount, every time.

| Effective date | Prime | Change |
|---|---|---|
| 2022-03-03 | 2.70% | +0.25 |
| 2022-04-14 | 3.20% | +0.50 |
| 2022-06-02 | 3.70% | +0.50 |
| 2022-07-14 | 4.70% | +1.00 |
| 2022-09-08 | 5.45% | +0.75 |
| 2022-10-27 | 5.95% | +0.50 |
| 2022-12-08 | 6.45% | +0.50 |
| 2023-01-26 | 6.70% | +0.25 |
| 2023-06-08 | 6.95% | +0.25 |
| 2023-07-13 | 7.20% | +0.25 |
| 2024-06-06 | 6.95% | −0.25 |
| 2024-07-25 | 6.70% | −0.25 |
| 2024-09-05 | 6.45% | −0.25 |
| 2024-10-24 | 5.95% | −0.50 |
| 2024-12-12 | 5.45% | −0.50 |
| 2025-01-30 | 5.20% | −0.25 |
| 2025-03-13 | 4.95% | −0.25 |
| 2025-09-18 | 4.70% | −0.25 |
| 2025-10-30 | 4.45% | −0.25 |

Today: **4.45%** (WOWA, nesto, Ratehub all show 4.45% after the Sep 2 2026 hold).

Note on WOWA's dates: WOWA lists a few 2022–2025 changes one day earlier than the Valet effective date (e.g. "March 3, 2022" vs Valet 2022-03-03 — same; but "October 29, 2025" vs Valet 2025-10-30, "September 17, 2025" vs 2025-09-18, "January 25, 2023" vs 2023-01-26, etc.). WOWA is recording the *announcement* date for those rows. For a simulation, use the effective date = announcement date + 1 business day; the one-day difference is immaterial to interest totals.

**TD deviation.** TD is the only Big 6 bank with a separate "TD Mortgage Prime Rate", set 0.15 above its regular prime since November 2016, when it raised mortgage prime to 2.85% without a BoC move (CBC, https://www.cbc.ca/news/business/td-bank-mortgage-prime-rate-1.3830878). It has kept the +0.15 through every move since; as of Sep 2026 TD mortgage prime is **4.60%** vs prime 4.45% (WOWA, https://wowa.ca/td-prime-rate and https://wowa.ca/banks/prime-rates-canada). So for a TD variable, the path above is +0.15 throughout (2.60% in Sep 2021, 7.35% at the Jul 2023 peak, 4.60% today). TD's advertised discounts are quoted off TD mortgage prime, so the *contract rate* is comparable to other banks' (e.g. Ratehub Sept 2021 shows TD at 1.40% = "Prime − 1.05" off 2.45, equivalently TD-mortgage-prime 2.60 − 1.20). No other Big 6 bank deviated from prime = overnight + 2.20 in this period.

## 3. Best available rates at the two signing dates (and mid-year checks)

All Ratehub pages below were captured from the Wayback Machine as raw snapshots and parsed locally; the 2023 pages embed a JSON rate table with an `insuranceBucket` field, so the insured/uninsured split is explicit for 2023. The 2021 pages predate that JSON; Ratehub's 2021 tables are the default "buying a home" scenario, which for the lowest broker rates is the insured (high-ratio) product; uninsured 2021 rates come from Canadian Mortgage Trends (quoting RateSpy data) and WOWA. Snapshot URLs are of the form `https://web.archive.org/web/<timestamp>/<original URL>`.

### 3A. September 2021 (term A signing)

Context: overnight 0.25%, prime 2.45%, TD mortgage prime 2.60%, BoC posted 5-yr conventional 4.79%, GoC 5-yr bond 0.79% (Sep 1) / 0.83% (Sep 15) / 0.80–0.90% range through the month (Valet BD.CDN.5YR.DQ.YLD; CMT). Fixed rates were at or near their all-time lows and started rising in October 2021 (Ratehub: "fixed rates started to climb again in October of 2021").

| Product | Best rate | Expressed as | Source and status |
|---|---|---|---|
| 5-yr variable, insured (best market) | **0.98%** | Prime − 1.47 (CanWise Financial) | Ratehub Big-5 page, captured 2021-09-18 (`web.archive.org/web/20210918053159/https://www.ratehub.ca/banks/bank-mortgage-rates`) and Ratehub 5-yr variable page captured 2021-09-18 (`.../20210918155700/https://www.ratehub.ca/best-mortgage-rates/5-year/variable`, "Rates updated: September 18, 2021"). Ratehub's prime-rate page in the same period shows "Best variable rates 0.95% Prime − 1.50". **[archived]** |
| 5-yr variable, uninsured (best) | not pinned to a single number | Ratehub's Sept 18 2021 variable table (mixed scenarios) lists MCAP 1.35% (P−1.10), First National 1.35% (P−1.10), HSBC 1.39% (P−1.06), TD 1.40% (P−1.05), BMO 1.42% (P−1.03), CIBC 1.44% (P−1.01), RBC 1.55% (P−0.90), Scotiabank 1.75% (P−0.70), Desjardins 1.60% (P−0.85). CMT Sept 18 2021: CIBC 5-yr variable 1.35%. Ratehub's June 16 2021 page shows best 5-yr variable 1.10% = P−1.35 (CanWise) and CIBC 1.54% = P−0.91. | **Recommendation for the simulation:** use P−1.47 (0.98%) as the insured best, and P−1.10 (1.35%, First National/MCAP, both offered uninsured) as a documented uninsured monoline rate; treat anything between P−1.10 and P−1.35 as plausible for a well-qualified uninsured borrower. **[archived] for the listed rates; the insured/uninsured labelling of the 2021 table is inferred, not stated.** |
| 5-yr fixed, insured (best) | **1.69%** (CanWise) | — | Ratehub main page captured 2021-09-15 21:22 UTC, "Rates updated: September 15, 2021, 4:20 p.m." (`.../20210915212231/https://www.ratehub.ca/best-mortgage-rates`); same 1.69% on the 5-yr fixed page updated Sept 20 2021. Full Sept 15 list: 1.69 CanWise, 1.84 Duca, 1.99 Equitable, 1.99 Meridian, 2.04 First National, 2.04 MCAP, 2.09 motusbank, 2.09 CMLS, 2.09 Simplii, 2.14 Tangerine, 2.19 Laurentian, 2.24 HSBC, 2.29 Scotiabank, 2.29 Desjardins, 2.31 BMO, 2.37 CIBC, 2.44 Alterna, 2.44 TD, 2.44 National Bank, 2.44 RBC. By Sept 20: 1.89 Meridian, 1.89 First National, 1.89 TD. **[archived]** |
| 5-yr fixed, uninsured (best) | **≈1.99%** (TD special, from Sept 16) ; monolines 2.04–2.09% | — | CMT, Sept 18 2021 (https://www.canadianmortgagetrends.com/2021/09/latest-in-mortgage-news-big-banks-lowering-their-5-year-fixed-rates/): "TD … lowering its rates by 45 bps … its insured (high ratio) 5-year fixed to 1.89% (from 2.34%) and its uninsured 5-year fixed to 1.99% (from 2.44%)"; RBC cut uninsured 5-yr fixed 25 bps to 2.19% (weekend of Sept 18); CIBC special-offer uninsured 5-yr fixed 2.39% (Sept 17) → 2.24% (Sept 21), CIBC insured 1.99% (Sept 21); HSBC insured 1.89%, uninsured 2.19% (Sept 21). WOWA snapshot (true capture Oct 24 2021 — **[stale]** by 5 weeks) lists uninsured-scenario 5-yr fixed: DUCA 2.04, Alterna/First National/motusbank/Peoples 2.09, ATB 2.14, Laurentian/Equitable 2.19, Meridian 2.29, CIBC/BMO 2.32, Tangerine 2.34, TD 2.39, HSBC 2.39, National/CMLS 2.44, MCAP/Scotia/Simplii 2.49, RBC 2.59. **[article] + [stale archived]** |
| 3-yr fixed, insured (best market) | **1.53%** (CanWise) | — | Ratehub Big-5 page captured 2021-09-18 ("Best market rate … 3 Year fixed 1.53%"); same 1.53% on Ratehub's June 16 2021 page. **[archived]** |
| 3-yr fixed, uninsured / general | 2.04–2.08% on Ratehub's 3-yr page — but that capture is **Oct 28 2021 [stale]** (Tangerine 2.04, CanWise 2.08, Alterna 2.09, motusbank 2.09, BMO 2.14, CMLS 2.14, Desjardins 2.14, MCAP 2.19, Equitable 2.24, First National 2.29, TD 2.34, Scotiabank 2.39, CIBC 3.49). Big-5 page Sept 18 2021 lists 3-yr fixed at TD 2.14, BMO 2.14, Scotia 2.24, RBC 2.24, CIBC 3.49. | No clean Sept 2021 uninsured 3-yr best was found; the Sept Big-5 rates (2.14–2.24) bracket it. Not needed for term A. |
| Big-bank "special" 5-yr fixed (not posted) | Ratehub Big-5 table, Sept 18 2021: **TD 1.89%**, Scotiabank 2.29%, BMO 2.31%, CIBC 2.37%, RBC 2.44%; 5-yr variable: TD 1.40% (P−1.05), BMO 1.42% (P−1.03), CIBC 1.44% (P−1.01), RBC 1.55% (P−0.90), Scotiabank 1.75% (P−0.70). CMT (Sept 18–21): TD uninsured special 1.99%, RBC uninsured 2.19%, CIBC uninsured 2.39→2.24%. | | **[archived] + [article]** |
| Posted 5-yr (BoC V80691335) | **4.79%** | — | Valet; unchanged from 2020-12 through 2022-04-13. |

Ratehub's own retrospective (5-yr fixed page, Sept 2023): "On January 1, 2022 the best high-ratio, 5-year fixed rate in Canada was 2.34%." Nesto claims the 2021 lows were 0.99% (insured 5-yr variable) and 1.34% (insured 5-yr fixed) (https://www.nesto.ca/mortgage-basics/mortgage-rates-history-canada/); Ratehub's current pages claim 2020–21 lows of 1.39% fixed and 0.85% variable, with 5-yr variable "as low as 0.88%" in late 2021 [snippet]. NerdWallet: lowest monthly average 5-yr fixed 1.9% (insured, Feb 2021), lowest variable 1.45% (Oct 2021).

### 3B. September 2023 (term B signing)

Context: overnight 5.00% (since Jul 13 2023; held Sep 6 2023), prime 7.20%, TD mortgage prime 7.35%, BoC posted 5-yr conventional 6.84% (Sep 6–27; 7.04% from Oct 4), GoC 5-yr bond 3.83% (Sep 1) / 4.02% (Sep 15) / intraday >4.41% on Sep 28 (a 16-year high) / 4.42% (Oct 3). Fixed rates were rising through the month; CMT Sept 22: "most mortgage rates now above 6%".

| Product | Best rate | Expressed as | Source and status |
|---|---|---|---|
| 5-yr variable, insured (best) | **5.95%** | **Prime − 1.25** ("Canadian Lender", Ratehub's anonymised lender) | Ratehub main page captured 2023-09-15 11:37 UTC (`.../20230915113703/https://www.ratehub.ca/best-mortgage-rates`), JSON `insuranceBucket: insured`, `primeRate: 7.2`; FAQ text: "As of September 7, 2023, the best high-ratio, 5-year variable mortgage rate in Canada is 5.95%". Same 5.95% on the 5-yr variable page captured Oct 1 2023 ("As of September 20, 2023, the lowest 5-year variable rate available in Canada is 5.95%"). Rest of the insured table (Oct 1 capture): CanWise 6.10, CMLS 6.25, First National/Equitable/ICICI 6.30, HSBC 6.40, MCAP 6.50, CIBC 6.70, "Big 6 Bank" 6.75, BMO 6.80, RBC 6.95, TD 7.00, Scotiabank 7.10, National Bank 7.24. **[archived]** |
| 5-yr variable, uninsured (best) | **5.90%** (P−1.30, Butler Mortgage) per WOWA — but capture is **Oct 10 2023 [stale]**; Ratehub Big-5 page Sept 22 2023 shows "Best market rate" 5.95% P−1.25 with no insured/uninsured split | — | WOWA (`.../20231010171017/https://wowa.ca/mortgage-rates`): "The best 5-year variable conventional mortgage rate is 5.90%, which is offered by Butler Mortgage"; same 5.90% insured (Citadel). **Recommendation:** use P−1.25 (5.95%) for both insured and uninsured in Sept 2023; the archived evidence does not show uninsured variable pricing worse than insured that month. |
| 5-yr fixed, insured (best) | **5.24%** ("Canadian Lender") | — | Ratehub main page Sept 15 2023 (JSON: term 60, fixed, 5.24, insured) and 5-yr fixed page captured Sept 20 2023: "As of September 7, 2023, the best high-ratio, 5-year fixed rate in Canada was 5.24%". Full insured table Sept 20: 5.24 Canadian Lender, 5.39 CanWise, 5.54 Alterna, 5.59 "Big 6 Bank", 5.59 Equitable, 5.64 CMLS, 5.64 Meridian, 5.69 RBC, 5.69 ICICI, 5.74 TD, 5.74 CIBC, 5.74 BMO, 5.84 First National, 5.84 MCAP, 5.89 Desjardins, 5.94 HSBC, 6.19 Simplii, 6.34 Tangerine, 6.39 Scotiabank, 6.84 National Bank. **[archived]** |
| 5-yr fixed, uninsured (best) | **5.54%** | — | Two independent readings: (i) Ratehub's "5.54% Best fixed rate in Canada" call-out on the Sept 20 and Sept 28 2023 pages (this widget sits outside the insured table; Ratehub does not label it, so the uninsured attribution is an inference); (ii) WOWA Oct 10 2023 [stale]: "The best 5-year fixed conventional mortgage rate is 5.54%, which is offered by Butler Mortgage" vs insured 5.39% (Citadel). CMT Sept 22 2023 (https://www.canadianmortgagetrends.com/2023/09/fixed-mortgage-rates-expected-to-surge-as-bond-yields-reach-16-year-high/): "The average nationally available deep-discount rate for high-ratio 5-year fixed mortgages is currently 5.79% … For uninsured rates … the average rate is currently 6.34%" (MortgageLogic.news data). **[archived]/[article]** |
| 3-yr fixed, insured (best) | **5.94%** on Sept 15 → **5.99%** by Sept 28 ("Canadian Lender"/CanWise) | — | Ratehub main page Sept 15 2023 (JSON: term 36, fixed, 5.94, insured); 3-yr fixed page captured Sept 28 2023: 5.99 CanWise, 5.99 Canadian Lender, 6.14 "Big 6 Bank", 6.29 HSBC, 6.29 ICICI, 6.39 Desjardins, 6.44 Alterna, 6.44 BMO, 6.54 MCAP, 6.59 Tangerine, 6.64 Scotiabank, 6.69 Equitable, 6.70 RBC, 6.71 TD, 6.86 First National, 6.89 motusbank, 6.94 CIBC, 7.04 National Bank. **[archived]** |
| 3-yr fixed, uninsured (best) | **5.84%** per WOWA Oct 10 2023 [stale] (MortgagePal); insured 5.64% (Citadel) on the same page | — | Note WOWA's Oct 10 insured 3-yr (5.64%) is *below* Ratehub's Sept 28 insured 3-yr (5.99%); the two sites survey different lender sets. For term B use 5.94–5.99% (Ratehub, Sept) for insured and treat 5.84–6.14% as the uninsured range; the "Big 6 Bank" 3-yr insured special was 6.14%. |
| Big-bank "special" (not posted) | Ratehub Big-5 page captured 2023-09-22: 5-yr fixed **RBC 5.69%**, TD 5.74%, BMO 5.74%, CIBC 5.74%, Scotiabank 6.39%; 3-yr fixed BMO 6.39%, TD 6.51%, RBC 6.50%, Scotiabank 6.64%, CIBC 6.94%; 5-yr variable CIBC 6.70% (P−0.50), BMO 6.78% (P−0.42), RBC 6.85% (P−0.35), TD 6.90% (P−0.30), Scotiabank 7.10% (P−0.10). Ratehub FAQ Sept 7 2023: "the average 5-year fixed mortgage rate available from the Big 5 Banks is 5.86%. Rates from the Big 5 Banks currently range from 5.69% to 6.39%." | | **[archived]** |
| Posted 5-yr (BoC V80691335) | **6.84%** (week of Sep 6 – Sep 27 2023) ; 7.04% from Oct 4 2023 | — | Valet. |

### 3C. Mid-year checks

**June 2021** (Ratehub main page captured 2021-06-16, "Last updated: June 16, 2021"): best 5-yr fixed 1.74% (CanWise), 3-yr fixed 1.53%, 1-yr 1.84%, 4-yr 1.74%, 10-yr 2.99%, 5-yr variable **1.10% = Prime − 1.35** (CanWise), 3-yr variable 2.45% (P−0.00). Big 5: 5-yr fixed Scotiabank 2.29%, 3-yr TD 2.14%, 5-yr variable CIBC 1.54% (P−0.91). So the insured variable discount deepened from P−1.35 in June to P−1.47 in September 2021, and the best 5-yr fixed fell from 1.74% to 1.69%. **[archived]**

**June 2023** (Ratehub main page captured 2023-06-15, FAQ "As of June 8, 2023"): best high-ratio 5-yr fixed **4.64%** (FAQ) / 4.83% in the JSON table at capture; best high-ratio 5-yr variable **5.80% = Prime − 1.15** (prime 6.95% after the Jun 8 hike); 3-yr fixed insured 5.39% (Desjardins), 5.44% (BMO); Big 5 5-yr fixed average 5.21%, range 5.04% (CIBC) – 5.74%; RBC 5-yr variable 6.45% (P−0.50), CIBC 6.70% (P−0.25), ICICI 6.60% (P−0.35). So between June and September 2023 the best insured 5-yr fixed rose ~60 bps (4.64→5.24) and the best variable discount deepened from P−1.15 to P−1.25 while prime rose 25 bps. **[archived]**

### 3D. Today (Sep 2026), for the "what would renewal look like" endpoint

- Ratehub (Sept 2026, live page [snippet]): best 5-yr fixed (high-ratio) **4.09%**, best 5-yr variable **3.30%** (= P−1.15 off 4.45). https://www.ratehub.ca/best-mortgage-rates
- WealthNorth (Aug 2026): 5-yr fixed posted 6.09%; discounted 5-yr fixed 3.9–4.3%; discounted variable 3.3–3.8%. https://wealthnorth.ca/mortgages/mortgage-rate-history/
- nesto (live): 3-yr fixed 4.29%, 5-yr fixed 4.24%, 5-yr variable 3.45% (these are nesto's own insured rates). https://www.nesto.ca/mortgage-basics/mortgage-rates-history-canada/
- CalculatorsCanada [snippet]: May 2026 big-bank best 5-yr fixed 3.99% (insured) to 4.44% (conventional).
- BoC posted 5-yr conventional: **6.09%** (since 2025-05-14). GoC 5-yr bond: 3.35% (Sep 1 2026), 3.48% (Sep 9 2026).


### 3E. Signing-date grid (insured / high-ratio basis)

Built the same way as the Sept 2021 and Sept 2023 anchors: raw Wayback snapshots of Ratehub pulled with curl and parsed locally. Two Ratehub surfaces are used and they agree where they overlap: the **rate table** (from 2022 on, the embedded `__NEXT_DATA__` JSON carries an explicit `insuranceBucket: insured` / `downPaymentBucket: <20` on every row, so the high-ratio basis is stated, not inferred) and the **"Best big bank rates in Canada"** table, whose "Best market rate" row gives the market-best 5-yr variable (with its prime-minus), 5-yr fixed and 3-yr fixed together. The 3-year column for 2022 comes from that second table, because Ratehub's 3-year term page has no captures in 2022 or 2024.

Prime in the last column is the prime in force on the capture date (section 2) and is the prime Ratehub itself quotes in the JSON (`primeRate`), so the prime-minus arithmetic is internally consistent.

| Month | Capture used (true Memento-Datetime) | Best 5-yr fixed (insured) | Best 3-yr fixed (insured) | Best 5-yr variable | Prime | Variable as |
|---|---|---|---|---|---|---|
| 2022-01 | main page 2022-01-13 12:30 UTC; Big-5 page 2022-01-16 ("Rates updated: January 12, 2022") | **2.34%** (CanWise) | **2.34%** (best market rate) | **0.85%** (CanWise) | 2.45% | **P − 1.60** |
| 2022-06 | main + Big-5 page 2022-06-12 22:23 UTC ("Rates updated: June 12, 2022, 4:19 p.m.") | **3.69%** (Canadian Lender) | **4.09%** (best market rate) | **2.40%** (CanWise) | 3.70% | **P − 1.30** |
| 2022-10 | main + Big-5 page 2022-10-13 16:25 UTC ("Rates updated: October 13, 2022, 4:19 p.m.") | **4.44%** (Canadian Lender) | **4.89%** (best market rate) | **4.25%** (Canadian Lender / CanWise) | 5.45% | **P − 1.20** |
| 2023-01 | main page 2023-01-13 22:27 UTC; 3-yr page 2023-01-18 05:25 UTC | **4.54%** (Canadian Lender) | **4.89%** (Alterna Savings; next 4.94% Canadian Lender) | **5.30%** (Canadian Lender) | 6.45% | **P − 1.15** |
| *2023-09 (anchor, §3B)* | *2023-09-15 / 09-20* | *5.24%* | *5.94%* | *5.95%* | *7.20%* | *P − 1.25* |
| 2024-01 | main page 2024-01-13 08:49 UTC (FAQ "as of January 9, 2024") | **4.89%** national / 4.84% Quebec-only ⚠ | **5.29%** ("Big 6 Bank") ⚠ | **5.95%** (Canadian Lender) | 7.20% | **P − 1.25** |
| 2024-06 | main page 2024-06-14 03:49 UTC (FAQ "as of June 7, 2024") | **4.74%** national / 4.64% Quebec-only ⚠ | **4.84%** ("Big 6 Bank") ⚠ | **5.70%** (Canadian Lender) | 6.95% | **P − 1.25** |
| 2025-01 | main page 2025-01-14 23:52 UTC (FAQ "as of January 14, 2025"); 3-yr page 2025-01-19 06:09 UTC | **4.04%** | **4.04%** ("Big 6 Bank"; next 4.19% Meridian) ⚠ | **4.45%** (Canadian Lender) | 5.45% | **P − 1.00** |
| 2025-06 | main page 2025-06-10 15:48 UTC (FAQ "as of June 10, 2025"); 5-yr variable page 2025-06-19 | **3.84%** (Canadian Lender) | **3.99%** (Canadian Lender) | **3.95%** (Canadian Lender) | 4.95% | **P − 1.00** |
| 2026-01 | main page 2026-01-04 22:08 UTC (FAQ "as of January 2, 2026"); 5-yr variable page 2026-01-04 | **3.94%** ("Big 6 Bank") | **3.89%** (Meridian Credit Union) | **3.45%** (Canadian Lender) | 4.45% | **P − 1.00** |
| 2026-06 | main page 2026-06-18 21:06 UTC (FAQ "as of June 18, 2026"); 3-yr page 2026-06-14 13:05 UTC | **4.04%** (Canadian Lender / "Big 6 Bank") | **4.04%** ("Big 6 Bank"; next 4.14% Scotiabank, 4.24% Meridian) ⚠ | **3.35%** (Canadian Lender) | 4.45% | **P − 1.10** |

Per-cell flags:

- **⚠ "Big 6 Bank"** — Ratehub's anonymised big-bank listing. It is a real offered rate sitting at the top of Ratehub's table, but the lender is not named, so it cannot be attributed to a specific bank. Affects: 2024-01 and 2024-06 3-yr, 2025-01 3-yr, 2026-01 5-yr, 2026-06 5-yr and 3-yr.
- **⚠ 2024-01 and 2024-06 5-yr fixed** — Ratehub's FAQ explicitly splits these: the table-topping rate (4.84% Jan, 4.64% Jun) was "available in Quebec only", with the best nationally available rate 5 bps / 10 bps higher (4.89% Jan, 4.74% Jun). The national figure is the one to use for a Canada-wide calculator; both are given.
- **2022-01 3-yr (2.34%)** and **2022-06 / 2022-10 3-yr (4.09% / 4.89%)** come from the "Best market rate" row of the Big-5 comparison table rather than a 3-year term page, because Ratehub's 3-year page has no 2022 captures. The row is undated beyond the page's own "Rates updated" stamp and does not carry the JSON `insuranceBucket` flag, so the **insured basis for these three cells is inferred** from the fact that the same row's 5-yr fixed and variable match the insured table exactly (2.34/0.85, 3.69/2.40, 4.44/4.25).
- **2026-01** — the Jan 4 capture reports Ratehub's Jan 2 2026 data. A second capture, **2026-01-28 14:42 UTC**, shows the month ending lower: 5-yr fixed **3.84%**, 3-yr fixed **3.79%** (Meridian), 5-yr variable **3.35% = P − 1.10**. Use Jan 2 for a "start of January" convention; the Jan 28 figures are the better "end of January" reading. Both are archived facts.
- **2025-01, 2025-06, 2026-01, 2026-06 captures** were served gzip/brotli-compressed by Wayback and had to be re-fetched with decompression; the earlier truncated reads were discarded. All dates above are the server-reported `Memento-Datetime`, not the requested timestamp.
- **No capture was missing for any requested month.** The thinnest coverage is 2025-06 (a single main-page capture, 2025-06-10) and 2026-06 (2026-06-18); neither required substitution.
- Every figure is **[archived]**. None of the grid is reconstructed from articles.

Shape of the series worth noting for the article: the variable discount is deepest exactly when variable was about to become the wrong bet (P−1.60 in Jan 2022, the widest in the whole window), compresses to P−1.15/−1.25 through the high-rate years, and only returns to P−1.00/−1.10 once cuts were underway. And the 3-yr/5-yr fixed relationship inverts: 3-yr is *above* 5-yr from mid-2022 through 2024 (4.09 vs 3.69; 4.89 vs 4.44; 5.29 vs 4.89), then converges and crosses back to level or below from 2025 on.

### 3F. Mid-term conversion rates, 2022 (the "panicked and locked in" case)

A Sept-2021 variable holder who converted mid-term did **not** get the market-best broker rate. Three things constrain the rate on offer, and they are documented separately from the rate itself:

1. **It is the existing lender's own rate, priced at or near posted.** Ratehub's own guide is explicit: on conversion "the rate you're likely to receive will be far from the best on the market", and will be "closer to their posted five-year fixed rate, rather than a discounted option" — the lender already has the business, so there is no acquisition discount. Its worked scenario puts conversion at **6.64%** against **5.79%** for refinancing away to a new lender, an **85 bp** gap. https://www.ratehub.ca/blog/as-variable-rates-rise-is-it-time-to-lock-into-a-fixed-rate-mortgage-term/ (article dated 2023-07-31 — **later than the 2022 events**, quoted for the mechanic, not for a 2022 rate). NerdWallet Canada states the same rule flatly: "You'll be charged the posted rate for that product, which will generally be higher than the special rates offered to entice borrowers." https://www.nerdwallet.com/ca/p/article/mortgages/switch-to-fixed-rate-mortgage (updated 2025-01-23). This corroborates the r/MortgagesCanada folk wisdom that conversions are priced off posted — **but note neither source names a bank or shows a 2022 rate sheet**, and in practice the big banks have discretion to convert at something between posted and their special rate.
2. **The term is constrained to be no shorter than the time remaining.** NerdWallet: the new fixed rate "will be based on your current lender's two-year fixed mortgage rates" if two years remain. Victor Tran (RATESDOTCA), Wealth Professional, 2022-11-23: a borrower who signed variable in 2020 with three years left "should choose a three-year fixed-rate mortgage term at the shortest to avoid incurring a penalty"; converting to a shorter term triggers "a penalty of three months' interest at the prime rate". https://www.wealthprofessional.ca/news/industry-news/dont-take-the-fixed-rate-conversion-decision-lightly-urges-mortgage-expert/371744 — so a Sept-2021 borrower converting in June 2022 had ~3¼ years left and would be quoted a 4-year or 5-year fixed, not the cheapest term on the board.
3. **The relevant comparison rates at the two conversion dates** (all **[archived]** unless marked):

| | June 2022 | October 2022 |
|---|---|---|
| (a) **Market-best 5-yr fixed, insured** (what a broker could get a *new* borrower) | **3.69%** (Ratehub, captured 2022-06-12) | **4.44%** (Ratehub, captured 2022-10-13) |
| (a′) Market-best 5-yr fixed per Ratehub FAQ | — | 4.29% "as of September 8, 2022" (stale FAQ text on the Oct 13 page) ⚠ |
| (b) **Big-5 *special* (not posted) 5-yr fixed** — the floor a bank might match on conversion | BMO 4.59, CIBC 4.62, TD 4.74, RBC 4.79, Scotiabank 4.84 (2022-06-12) | CIBC 5.17, BMO 5.30, TD 5.44, RBC 5.54, Scotiabank 5.64 (2022-10-13). Ratehub FAQ: Big-5 average 5.32%, range 5.17–5.54 (Sept 8 2022) |
| (c) **Posted 5-yr conventional** (BoC V80691335, chartered-bank average) — the ceiling if converted strictly at posted | 5.39% (Jun 1) → **5.64%** (Jun 15) → 6.04% (Jun 22) | **6.14%** (through Oct 12) → **6.49%** (from Oct 19) |
| (d) **Broker-reported actual lock-in pricing** | not found for June | **≈4.7%**, ranging as high as **5.39%** — Global News, 2022-09-17/19, brokers describing what variable holders were being offered to lock in five years at 80% LTV, with one named client offered **4.69%** for five years. https://globalnews.ca/news/9135060/variable-mortgage-fixed-conversion-interest-rate-canada/ **[article]** |

How to use this in the simulation. The honest bracket for a mid-2022 conversion is **(b) at the low end and (c) at the high end**: a borrower with a broker and some leverage got something near the bank's special rate; a borrower who simply phoned the branch and accepted got something near posted. The single best-documented real number is the Global News figure — a lock-in "often offered around 4.7 per cent" in mid-September 2022, with 5.39% at the high end, against a posted rate of 6.14% and a market best of 4.29–4.44% at the same moment. That ≈4.7% sits roughly at the Big-5 special level, i.e. about **40–100 bp worse than the market best** and about **1.4 pp better than posted** — which argues the "conversion = posted rate" rule of thumb is the pessimistic bound rather than the typical outcome, at least in 2022 when banks were competing hard for the converting cohort.

**Explicitly not found:** no archived Big-5 *conversion* rate sheet from 2022 (as distinct from new-business special rates), and no June 2022 equivalent of the Global News figure. Searches of Canadian Mortgage Trends' Sept–Nov 2022 archive surfaced trigger-rate and OSFI coverage but no post pricing conversions. Anything stated about June 2022 conversion pricing beyond the (b)/(c) bracket would be an estimate, so none is given.

## 4. Bank of Canada 5-year conventional mortgage rate (posted), V80691335

Weekly series (Wednesday). Every change, Dec 2020 → Sep 2026 (Valet):

| Effective (obs. date) | Posted 5-yr |
|---|---|
| ≤2020-12-02 → 2022-04-13 | 4.79% |
| 2022-04-20 | 4.99% |
| 2022-05-25 | 5.39% |
| 2022-06-15 | 5.64% |
| 2022-06-22 | 6.04% |
| 2022-07-27 | 6.14% |
| 2022-10-19 | 6.49% |
| 2023-08-02 | 6.79% |
| 2023-08-30 | 6.84% |
| 2023-10-04 | 7.04% |
| 2024-01-17 | 6.89% |
| 2024-02-07 | 6.79% |
| 2024-02-14 | 6.84% |
| 2024-07-03 | 6.79% |
| 2024-08-21 | 6.59% |
| 2024-09-11 | 6.79% |
| 2024-09-18 | 6.49% |
| 2025-05-14 → 2026-09-09 | 6.09% |

Monthly (first observation of each month), 2021-01 → 2026-09: 2021 all months 4.79; 2022: Jan–Apr 4.79, May 4.99, Jun 5.39, Jul 6.04, Aug–Oct 6.14, Nov–Dec 6.49; 2023: Jan–Jul 6.49, Aug 6.79, Sep 6.84, Oct–Dec 7.04; 2024: Jan 7.04, Feb 6.79, Mar–Jun 6.84, Jul–Aug 6.79, Sep 6.59, Oct–Dec 6.49; 2025: Jan–May 6.49, Jun–Dec 6.09; 2026: Jan–Sep 6.09.

Posted vs best-offered at the three dates: Sept 2021 4.79% posted vs 1.69% (insured) / ~1.99% (uninsured) best → 280–310 bp gap; Sept 2023 6.84% posted vs 5.24% / 5.54% → 130–160 bp gap; Sept 2026 6.09% posted vs 4.09% → 200 bp gap. (The posted rate matters for the big-bank IRD penalty, section 7, and was the stress-test floor 5.25% until the OSFI/MOF floor was superseded by contract+2% in the 2023 environment — Ratehub Sept 2023: "the stress test used is the contract rate + 2%".)

5-year GoC benchmark bond yield (BD.CDN.5YR.DQ.YLD), first business day of month, for the fixed-rate story: 2021: Jan 0.39, Apr 0.97, Jul 0.96, Sep 0.79, Oct 1.07, Nov 1.50, Dec 1.35; 2022: Jan 1.39, Mar 1.48, Apr 2.46, Jun 2.86, Sep 3.37, Nov 3.43, Dec 3.05; 2023: Jan 3.34, Mar 3.59, Jun 3.41, Jul 3.74, Aug 3.98, Sep 3.83, Oct 4.42, Nov 3.98, Dec 3.50; 2024: Jan 3.25, May 3.81, Jul 3.60, Sep 2.94, Oct 2.74, Dec 2.94; 2025: Jan 2.96, Mar 2.50, Jun 2.82, Sep 2.92, Dec 2.81; 2026: Jan 3.00, Mar 2.76, May 3.18, Jul 3.06, Sep 3.35 (Sep 9: 3.48).

## 5. Long-run context (1975–2026)

WealthNorth (https://wealthnorth.ca/mortgages/rates/mortgage-rate-history/ ; year-end posted 5-yr fixed, Bank of Canada data):
- All-time high 5-yr fixed posted **21.75% in August 1981**; variable peaked 19.20% the same year.
- Year-end 5-yr fixed: 1975 12.00; 1979 13.25; 1980 16.00; 1981 17.75; 1982 14.75; 1985 11.50; 1990 12.50; 1991 9.90; 1993 7.75; 1994 10.50; 1995 8.45; 1996 6.95; 1999 8.25; 2000 7.95; 2004 6.05; 2007 7.54; 2008 6.75; 2009 5.49; 2010 5.19; 2014 4.79; 2015 4.64 (lowest posted); 2016 4.64; 2017 4.99; 2018 5.34; 2019 5.19; 2020 4.79; 2021 4.79; 2022 6.49; 2023 7.04; 2024 6.49; 2025 6.09; 2026 6.09.
- Variable vs fixed selected years: 1980 13.45 vs 16.00; 1990 13.95 vs 12.50 (fixed lower); 2000 7.20 vs 7.95; 2009 1.95 vs 5.49; 2020 2.15 vs 4.79; 2023 6.65 vs 7.04; 2024 6.65 vs 6.49 (fixed lower); 2026 4.15 vs 6.09.
- "The long-term average since 1975 is approximately 8.5%"; variable was below 5-yr fixed in "approximately 90% of years (47 of 52 years)". Pandemic discounted fixed rates "1.5–2.0%"; variable low 2.15% (2020–21) — note these are WealthNorth's summary numbers and are higher than the archived best rates in section 3.

NerdWallet (https://www.nerdwallet.com/ca/mortgages/mortgage-rate-history-in-canada):
- Since 1980: 5-yr fixed average 8.27%; peak 21.75% (Aug–Oct 1981); low 4.64% (Apr 2015–Jun 2016; Sep 2016–Jul 2017). Prime: average 6.8%; peak 22.75% (Aug–Sep 1981); low 2.25% (Apr 2009–May 2010).
- 2013–2023 monthly averages: 5-yr fixed average 3.19%, high 6% (uninsured, Nov 2023), low 1.9% (insured, Feb 2021); 3-yr fixed average 3.07%, high 6.14% (Nov 2023), low 1.82% (Feb 2021); variable average 3.23%, high 7.7% (insured, Jul 2023), low 1.45% (Oct 2021).
- Payment table (25-yr amortization, 20% down): 1985 $80,294 home @12.14% → $686/mo; 1995 $150,773 @9.14% → $1,010; 2005 $248,915 @5.98% → $1,272; 2015 $441,605 @4.67% → $1,989; 2025 $679,543 @6.22% → $3,550.

MyPerch (https://myperch.io/homeowners/the-history-of-mortgage-rates-in-canada/): overnight rate 2.50% at inception (1935), 12.89% in 1980, peak **17.93% in 1981**, lowest ever 0.25% (2020–21), average since 1990 ≈5.78%; 5-yr fixed ≈11.38% (1975), 14.2% (1980), "just over 21%" (Sept 1981); inflation peaked 12.9% in 1981. (Page is stale: "current 5.00%".) Search snippet adds: 21.75% held Aug 12 – Oct 7 1981, then 13.5% by Jan 1983 and 12.5% by Nov 1983.

LowestRates.ca [snippet only]: 5-yr fixed peaked in 1981; spikes in the early 1990s (inflation) and 1995 (defence of the dollar); downtrend after 2007; "rates bottomed out at the 1s" in 2020; hikes from March 2022. URL: https://www.lowestrates.ca/resource-centre/mortgage/historical-mortgage-rates-averages-trends

nesto (https://www.nesto.ca/mortgage-basics/mortgage-rates-history-canada/): "the 5-year fixed uninsured rate skyrocketed to 18.35% as an average in 1981", prime 20.03% average that year.

What a 1975–2026 chart shows: a single spike to ~21–22% in 1981; a secondary peak ~12.5–13% in 1990; the 1994–95 bump to 10.5%; a 25-year glide from ~8% (2000) to ~4.6–4.8% posted (2015–2021); the 2022–23 jump from 4.79% to 7.04% posted — the sharpest one-year rise since 1981 in absolute posted-rate terms (WealthNorth: +1.70 in 2022, +0.55 in 2023); then 6.09% since mid-2025. The 2021 trough in *offered* rates (0.98% variable, 1.69% fixed) is far below anything the posted series shows.

## 6. Variable-rate mechanics that changed the 2021 story

**Two kinds of "variable".** Bank of Canada Staff Analytical Note 2022-19 (Nov 2022, https://www.bankofcanada.ca/2022/11/staff-analytical-notes-2022-19/): lenders offering *fixed-payment* variable-rate mortgages only: **Bank of Montreal, CIBC, RBC, TD, Desjardins, HSBC Bank Canada**; lenders offering *variable-payment* (adjustable) only: **Scotiabank, National Bank of Canada** (most monolines also adjust the payment). "About three-quarters of variable-rate mortgages have fixed payments." Variable-rate mortgages were "about one-third of total outstanding mortgage debt (up from 20% in late 2019)". For a fixed-payment product, a rising prime leaves the payment unchanged but shifts it toward interest; the **trigger rate** is where the payment no longer covers the interest (Ratehub: "the point at which your regular payment is no longer enough to pay all of the interest you've accrued since your last payment", https://www.ratehub.ca/blog/trigger-rate-what-you-need-to-know/). Past the trigger, TD, BMO and CIBC let the unpaid interest capitalise (negative amortization; amortization stretches); RBC does not allow negative amortization and raises payments instead (Globe and Mail, https://www.theglobeandmail.com/business/article-mortgage-borrowers-td-bmo-cibc-homeowners/).

**How many hit trigger.**
- SAN 2022-19 (Nov 2022): as of October 2022, with variable rates around 5.1%, "about 50%" of variable-rate fixed-payment mortgages had reached their trigger rate — "approximately 13% of all Canadian mortgages"; a further 50 bp of hikes would take it to 65% of VRFP (~17% of all mortgages) by mid-2023. Median payment increase for triggered mortgages ≈5%; pandemic-era 30-year-amortization originations ≈20%.
- SAN 2023-19 (Dec 2023, https://www.bankofcanada.ca/2023/12/staff-analytical-note-2023-19/): by November 2023 "up to 80%" of VRFP mortgages had reached their trigger rate; at most one-quarter had reached the point requiring mandatory payment changes; 45% of mortgages outstanding in Feb 2022 had already seen payments rise, 80% expected by end-2025; VRFP median payment +54% by end-2027 vs Feb 2022 (to $2,190); variable-payment mortgages were already +70% by Nov 2023; negative amortization adds ~6% to total cost over a 30-year amortization — "$600,000 mortgage = additional $70,000 in interest". (Ratehub and Global News attribute an "up to 80%" figure to a BoC report of February 2023; the citable BoC document with that number is the Dec 2023 note.)
- FSR 2023 (May 2023, https://www.bankofcanada.ca/2023/05/financial-system-review-2023/, Box 1): "the median payment increase over the 2023–26 period will be about 20%"; VRFP borrowers renewing 2025–26 "will need to increase their payments by approximately 40%"; roughly one-third of mortgages had already seen higher payments vs Feb 2022; "by the end of 2026, nearly all mortgage holders will have seen their payments increase"; median DSR on new mortgages rose 16% → >19% during 2022, share above 25% from 12% → 29%.

**Negative amortization at the banks (Q3 fiscal 2023, from bank filings via the Globe and Mail).** BMO $32.8B negatively amortizing = 22% of its Canadian residential book; TD $45.7B = 18%; CIBC $49.8B = 19%; "roughly one fifth of the mortgages on the books at BMO, TD and CIBC … nearly $130 billion" (https://www.theglobeandmail.com/business/article-mortgage-negative-amortizations-cibc/ ; https://www.theglobeandmail.com/business/article-canada-banks-mortgages-negative-amortization/). OSFI added capital requirements for negatively amortizing mortgages (Nov 2023; CMT https://www.canadianmortgagetrends.com/2023/11/four-big-banks-to-be-impacted-by-osfis-new-capital-requirements-for-negative-amortization-mortgages/ — 403 for fetch, cited from search) and CIBC reported 13,000 clients had exited negative amortization by Dec 2023 (CMT, https://www.canadianmortgagetrends.com/2023/12/13000-cibc-mortgage-clients-have-come-out-of-negative-amortization/).

**Renewal wall.**
- FSR 2025 (May 8 2025, https://www.bankofcanada.ca/2025/05/financial-stability-report-2025/) and SAN 2025-21 (Jul 2025, https://www.bankofcanada.ca/2025/07/staff-analytical-note-2025-21/): "About 60% of all outstanding mortgages in Canada are expected to renew in 2025 or 2026"; "about 60% of mortgage holders renewing in 2025 and 2026 are expected to see a payment increase"; vs December 2024 payments, average monthly payment "10% higher for those renewing in 2025 and 6% higher for those renewing in 2026"; **5-year fixed holders renewing in 2025 or 2026: average increase "around 15%–20%"** (2026 renewers: 20%); shorter-term fixed: decreases; variable-rate variable-payment: "average payment decline of around 5%–7%"; VRFP renewers in 2026: 10% face increases >40%, a quarter see decreases of ≥7%; "more than 90% of mortgage holders with a five-year fixed-rate mortgage will face payment increases at renewal that are smaller than they were stress-tested for".
- FSR 2026 (May 28 2026, Households chapter, https://www.bankofcanada.ca/publications/financial-stability-report/financial-stability-report-2026/households/): pandemic-era fixed-payment mortgages renewing in the next 12 months ≈ **12% of all outstanding mortgages**, with payments expected to "increase by about 15%"; another ≈14% of mortgages (variable and shorter-term) renew with no payment change; the Bank expects the renewal risk to have fully passed by H2 2027; arrears (60+ days) "only slightly above the 2018–19 average"; borrowers unable to refinance in 2027 ≈4% nationally / ≈9% in the Toronto area (7% / 12% if prices fall a further 10%); high-LTI borrowers ≈17% of balances; 2022–23 Toronto originations ≈2% of balances. Opening statement: https://www.bankofcanada.ca/2026/05/opening-statement-20260528/

## 7. Penalty facts

**Fixed-rate prepayment charge = greater of 3 months' interest and the Interest Rate Differential (IRD).** Variable-rate mortgages at essentially all federally regulated lenders charge only **3 months' interest** (LoansCanada: "how much interest you would have paid over 90 days on the amount you want to prepay, using your current annual rate"; https://loanscanada.ca/mortgage/interest-rate-differential/).

**Big-bank ("posted-rate") IRD.** LoansCanada's statement of the formula: IRD = (your contract rate − the bank's *posted* rate for a term matching your remaining time, sometimes less the discount you originally received) × balance × remaining months ÷ 12. Because the comparison rate is a posted rate (currently 6.09% for 5-yr, but the *shorter-term* posted rates are what apply, and banks have cut those aggressively), the differential is inflated. Worked example on that page: $400,000 balance, 3 years left, contract 5%, comparison 4% → 1% × $400,000 × 3 = **$12,000**. Monoline/"fair-penalty" lenders compare the contract rate to the rate they currently *offer* new customers for the remaining term, so the IRD is much smaller. Robert McLister, Globe and Mail (Nov 13 2019, https://www.theglobeandmail.com/investing/personal-finance/household-finances/article-big-banks-prepayment-charges-give-reason-to-consider-fair-penalty/): $300,000 5-yr fixed at 3.19%, broken after 1 year — major-bank IRD ≈ **$16,800** vs fair-penalty lender ≈ **$2,400** (3 months' interest); "Unlike Big Six banks, fair-penalty lenders don't use arbitrarily inflated rates ('posted rates') in their calculations."

**Representative 2023-vintage example.** nesto, "Mortgage Penalties Surge at the Big Banks" (Jan 22 2026, https://www.nesto.ca/featured-articles/mortgage-prepayment-penalties-surge-after-big-banks-cut-posted-rates/): a TD client who took a **3-year fixed at 4.30% in August 2023** on $500,000 faced a penalty of "around $5,400, based on a standard 3-month interest charge" before TD cut its 2-year posted rate by 195 bps; after the cut, the posted-rate IRD is "more than $22,000" (+≈$17,000). Same borrower at RBC: ≈$7,000 → "more than $16,000" after RBC's posted-rate cuts. Pegasus Lending [snippet] gives a matching stylised pair: $450,000 at 5.20% with 2 years left at a monoline → IRD ≈$9,000 vs 3-month interest ≈$5,850; $380,000 at 5.45% with 3 years left at a Big-6 bank → posted-rate IRD ≈$22,800 vs 3-month interest ≈$5,180 (https://pegasuslending.com/blog/mortgage-prepayment-penalty-canada/).

Relevance to the two look-backs: a Sept 2021 5-year fixed at ~1.99% broken in 2022–23 would have carried *no* IRD (rates had risen, so the differential was negative — only 3 months' interest applied); a Sept 2023 5-year fixed at ~5.24–5.54% broken in 2025–26 at a big bank faces the posted-rate IRD as rates fell, while the variable alternative was capped at 3 months' interest throughout.

---

### Quick reference for the parent's simulation

- Overnight/prime path: section 1/2 tables (prime = overnight + 2.20 throughout; TD mortgage prime +0.15 on top).
- Term A (Sept 2021): 5-yr fixed 1.69% insured / ≈1.99% uninsured (TD special; monolines 2.04–2.09%); 5-yr variable P−1.47 = 0.98% insured / P−1.10 = 1.35% documented uninsured monoline. Posted 4.79%.
- Term B (Sept 2023): 5-yr fixed 5.24% insured / 5.54% uninsured; 3-yr fixed 5.94–5.99% insured / ≈5.84–6.14% uninsured; 5-yr variable P−1.25 = 5.95% (P−1.30 = 5.90% on WOWA, Oct 10). Posted 6.84%.
- Endpoint (Sept 2026): prime 4.45%; best 5-yr fixed ≈4.09%; best variable ≈P−1.15 = 3.30%; posted 6.09%.
