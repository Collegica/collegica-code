## Access and confidence

- Researched 2026-10-29. WebSearch was exhausted for the session (200/200), so everything below comes from WebFetch on known URLs, or from StatCan tables pulled straight from the official WDS/CSV endpoints and computed locally. No figure here comes only from a search snippet; the [snippet] tag is unused.
- **High confidence (primary data, computed by me from raw StatCan CSVs):** debt-to-income, CPI inflation of $1M, average new-vehicle price, SFS 2023 net worth by age and decile, DHEA Q4 2025 wealth quintiles.
- **Medium confidence (read through WebFetch's summariser, so wording may be paraphrased; check before quoting):** TransUnion Q2 2026 figures, AutoTrader Q2 2026 percentages, FCAC car-loan and credit-card examples, the Cox/KBB US ATP.
- **Read verbatim from the PDF:** the Ramsey State of Personal Finance Q3 2025 press release (2025-11-05).
- **Not obtained:** Equifax Canada Market Pulse (newsroom 404; a later fetch attempt was blocked by the permission system), J.D. Power Canada (403), Edmunds (403), Bank of Canada FSR 2026 household figures (only overview text came back), any Canadian BNPL usage statistic, any Canadian share of 84–96-month loans or negative-equity rate, and the Ramsey "Toyota is the top millionaire car brand" claim (no Ramsey page that could be fetched confirmed it).

---

## 1. Household debt and credit cards

### Debt-to-disposable-income (StatCan Table 38-10-0238-01, seasonally adjusted)
Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810023801 (CSV: https://www150.statcan.gc.ca/n1/tbl/csv/38100238-eng.zip)

| Quarter | Credit market debt to disposable income | Total household credit market debt |
|---|---|---|
| Q4 2009 | 163.62% | $1.48 trillion |
| Q3 2022 (series peak) | 188.22% | n/a |
| Q4 2025 | 178.69% | $3.22 trillion |
| Q1 2026 | 178.55% | $3.25 trillion |
| **Q2 2026 (latest)** | **176.37%** | **$3.28 trillion** (mortgages $2.45T; consumer credit $679B) |

- Plain English: in Q2 2026 households owed about **$1.76 for every $1 of disposable income**, against $1.64 when *Stop Acting Rich* came out (2009).
- Consumer credit (non-mortgage) was $441B in Q1 2009 and $679B in Q2 2026, about 54% higher in nominal terms.

### Consumer debt per person (TransUnion Canada, Q2 2026, published 2026-08-25)
Source: https://newsroom.transunion.ca/canadian-consumer-debt-reaches-record-264-trillion-as-financial-realities-differ-across-households/
- Total consumer debt was **$2.64 trillion**, up $116.7B (+4.6%) year over year.
- **Average non-mortgage debt per consumer was $28,118**, up 7.6% year over year.
- Consumer-level 90+ day delinquency was **1.81%** (1.77% a year earlier). Ontario was 1.96% and Alberta 2.41%.
- Credit card balances grew 5.1% and auto loans 7.9%, the fastest-growing non-mortgage product.
- The release gives no separate card-only or auto-only delinquency rate (as summarised).

### Survey of Financial Security 2023 (StatCan Table 11-10-0016-01, 2023 dollars)
Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110001601
- 36.0% of family units carried credit card and installment debt in 2023, with a **median of $4,500** among those who had it. In 2019 it was 37.3% with a median of $3,500.
- 58.4% carried some non-mortgage debt (median $21,000).

### Credit card rates and minimum-payment math
- FCAC example rates: "you may pay 19% interest on regular purchases and 22% on cash advances". The 21-day minimum grace period applies only to purchases. https://www.canada.ca/en/financial-consumer-agency/services/credit-cards/credit-card-work.html
- FCAC's minimum-payment definition: usually a flat amount (about $10 plus interest and fees), or the higher of $10 or 3% of the balance. In FCAC's worked example, **$2,000 at 18%, paying only the minimum, takes 3 years 11 months and costs $793 in interest**. Adding $100 a month cuts that to 1 year 2 months and $231. https://www.canada.ca/en/financial-consumer-agency/services/credit-cards/pay-off-credit-card.html (medium confidence; this is FCAC's own scenario)
- **My own calculation** (monthly compounding, minimum = greater of $10 or 3% of the current balance, no new spending), for a **$5,000 balance**:

| APR | Minimum only (3%) | Fixed $150/mo | Fixed $250/mo |
|---|---|---|---|
| 19.99% | 244 months (~20 yrs), $5,773 interest | 50 months, $2,357 | 25 months, $1,132 |
| 20.99% | 257 months (~21 yrs), $6,434 interest | 51 months, $2,568 | 25 months, $1,207 |
| 22.99% | 290 months (~24 yrs), $8,034 interest | 54 months, $3,045 | 26 months, $1,366 |

  The lesson: when the minimum is a shrinking percentage of the balance, payoff takes decades. Freezing the payment at its first-month amount ($150) cuts payoff to about 4 years. FCAC's shorter example reflects a different minimum formula, so say which formula an example uses.
- I did not fetch issuers' current posted rates. The 19.99–22.99% band is the convention, consistent with FCAC's 19%/22% example.

---

## 2. Cars

### Average new-vehicle price (StatCan, New motor vehicle sales, dollars ÷ units, Canada, unadjusted)
Sources: Table 20-10-0085-01 (current) https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2010008501 and the archived Table 20-10-0001-01 for 2009.

| Year | Average dollars per new vehicle sold |
|---|---|
| 2009 | $31,611 |
| 2019 | $43,567 |
| 2024 | $56,393 |
| **2025** | **$55,827** |
| **Jan–Aug 2026** | **$57,142** (Aug 2026: $56,661) |

- Caveat: this divides total retail sales dollars by units, so it includes fleet sales and is not a transaction-price survey. It is still a clean, primary, like-for-like series.
- New-car prices rose about **81% from 2009 to 2026**, while CPI rose about 49% (see section 4).

### AutoTrader Price Index, Q2 2026
Source: https://www.autotrader.ca/editorial/price-index/
- The average new-vehicle price **fell 2.2%** and the average used-vehicle price **fell 2.6%** year over year. EV prices rose. The page text gave no dollar levels (those are in linked PDFs I could not read).

### Long loans, depreciation and negative equity (FCAC)
Source: https://www.canada.ca/en/financial-consumer-agency/services/loans/financing-car/risks.html (medium confidence; read through the summariser)
- FCAC: "Long-term loans come with terms of 72 months (6 years) or more."
- Interest example on a $25,000 car at 5%: **36 months costs $1,974 in interest and 84 months costs $4,681**, about $2,707 more.
- Depreciation: a new car loses about **25% in year one**, then roughly 15–25% a year in years 2–5.
- Negative-equity example: after 2 years of an 8-year, $35,000 loan, negative equity is **$8,520**.
- FCAC's advice: choose the shortest term you can afford, make a down payment, and don't trade in while underwater.
- Federal loan/lease calculator: https://ic.gc.ca/app/scr/oca-bc/ssc/vehicle.html?lang=eng
- **Gap:** I found no fetchable Canadian source for the share of loans at 84–96 months, the average Canadian auto-loan size, or negative-equity prevalence. J.D. Power Canada was 403 and Equifax was unavailable.

### US comparators
- Cox Automotive/KBB: average new-vehicle transaction price **$50,562 (US$) in September 2026**, from the "Auto Market Snapshot" updated 2026-10-19. https://www.coxautoinc.com/insights-hub/ (medium confidence; this is a dashboard figure)
- Ramsey State of Personal Finance Q3 2025 (US, press release 2025-11-05, read verbatim): **89% of buyers who paid cash for a car report being happy with it, against 55% of those who financed**. "Almost half of car buyers take on payments." https://cdn.ramseysolutions.net/media/company/pr/press-releases/2025/2025-11-05%20SOPF%20Q3.pdf

---

## 3. How millionaires live

### Ramsey National Study of Millionaires (US)
Source: https://www.ramseysolutions.com/retirement/the-national-study-of-millionaires-research (page last updated Oct 3, 2024)
- It is still the **2017–18 study** (fielded Nov 2017 to Jan 2018), with 10,000+ US millionaires. I could find **no 2024/2025 re-run**; the 2024 date is only a page refresh.
- 79% received no inheritance, and only 3% inherited $1M or more.
- One-third never earned six figures in any single working year.
- "nearly three-quarters of the millionaires have never carried a credit card balance"
- 93% use coupons at least some of the time, and 85% shop with a grocery list.
- 62% attended public state schools.
- **Cars:** the page has no car data. The often-repeated claim that Toyota is the top brand among millionaires, followed by Honda and Ford, comes from Ramsey's *Everyday Millionaires* (2019). I could **not verify** it from a fetchable Ramsey page. Attribute it to the book, or drop it.
- The *Baby Steps Millionaires* release (2022-01-11) calls the study "the largest study of millionaires ever done in North America." https://cdn.ramseysolutions.net/media/company/pr/press-releases/2022/2022-01-11%20BSM%20Launch.pdf

### Sarah Stanley Fallaw / DataPoints
- https://datapoints.com/ and https://datapoints.com/the-next-millionaire-next-door/
- *The Next Millionaire Next Door* (2018, Stanley and Fallaw) stresses "living below your means" and "Understanding how those around you influence your financial behaviors".
- DataPoints' assessments use a "six-dimension framework" grounded in *The Millionaire Next Door*.
- The pages fetched gave no car-price or home-value numbers. Those figures are in the book itself.

### Canadian millionaire habits
- I found no Canadian survey of millionaires' consumption habits. A Canadian angle has to come from StatCan wealth data (section 4).

---

## 4. Canadian wealth and the inflated "millionaire"

### Survey of Financial Security 2023 (StatCan Table 11-10-0016-01, median net worth by age of major income earner, 2023 dollars)
| Age | 2019 median | 2023 median |
|---|---|---|
| All | $381,100 | **$519,700** |
| Under 35 | $56,400 | **$159,100** |
| 35–44 | $270,800 | **$409,300** |
| 45–54 | $602,000 | **$675,800** |
| 55–64 | $797,000 | **$873,400** |
| 65+ | $627,500 | **$738,900** |

### How many Canadian family units are millionaires (SFS 2023, Table 11-10-0075-01)
Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110007501
- There were 16.85M family units. The 7th net-worth decile had a median of $910,000, the 8th $1,270,700, the 9th $1,917,000 and the top decile $3,435,000 (average $4.38M).
- **My interpolation:** the $1M line falls near the top of the 7th decile, so **roughly 30–33% of Canadian family units (about 5–5.5 million) had net worth of $1M or more in 2023**. StatCan does not publish this count directly; label it as an estimate. Much of it is home equity.

### DHEA, Q4 2025 (StatCan Table 36-10-0660-01, average net worth per household)
Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610066001
- All households averaged **$1,078,642**. The average is skewed upward; the SFS median is about half of it.
- By wealth quintile: lowest −$4,608; second $167,907; third $526,185; fourth **$1,160,145**; highest **$3,543,579**. The top 20% hold **65.7%** of net worth and the bottom 40% about 3%.
- By age: under 35 averaged $455,453 and 55–64 averaged $1,597,113. Owners averaged $1,407,787 and renters $355,473.

### Inflating the threshold since 2009 (StatCan CPI, all items, v41690973, 2002=100)
- The 2009 annual average CPI was 114.43 and September 2026 was 170.0, a ratio of **1.486**.
- **$1,000,000 in 2009 dollars is about $1.49 million in September 2026 dollars.** The Bank of Canada calculator uses the same CPI series, but I computed this rather than running the calculator.
- Equivalently, a 2026 "millionaire" with exactly $1M has about $673,000 of 2009 purchasing power.
- CPI series: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401. BoC calculator: https://www.bankofcanada.ca/rates/related/inflation-calculator/

### Registered-account limits, 2026 (CRA)
Source: https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html
- The TFSA annual limit for 2026 is **$7,000** and the RRSP dollar limit is **$33,810**.
- Cumulative TFSA room for someone eligible since 2009 is **$109,000** in 2026. I summed the annual limits myself: 4×5,000 + 2×5,500 + 10,000 + 3×5,500 + 4×6,000 + 6,500 + 3×7,000.

---

## 5. Consumer behaviour, 2025–2026

- **TransUnion Q2 2026 Consumer Pulse** (2026-07-22): 51% cut discretionary spending, 26% cancelled subscriptions, and 18% paid down debt faster. Only 11% increased discretionary spending (+3 pts year over year). 50% say income is not keeping pace with inflation, and 86% rank inflation in their top three concerns. https://newsroom.transunion.ca/canadians-show-signs-of-financial-improvement-but-continue-to-feel-the-cost-of-living-squeeze-transunion-canada-study/
- **FCAC, "Budgeting over time and why it matters"** (Jan 2026; two-year longitudinal study with the Optimity app): consistent budgeters had greater savings, lower credit card debt and lower stress. About a third budgeted only intermittently but still gained. https://www.canada.ca/en/financial-consumer-agency/programs/research/budgeting-time.html
- **FCAC financial well-being dashboard** (July 2025): "Fewer Canadians had a budget in 2025 than in 2024." Most other indicators showed no change. https://fcac-research-recherche-acfc.canada.ca/en/financial-well%E2%80%91being-bien%E2%80%91etre-financier/
- **BNPL (FCAC guidance):** the rate "may go from 0% to 35% if you miss the minimum payment", and FCAC warns BNPL may "encourage you to spend beyond your means". https://www.canada.ca/en/financial-consumer-agency/services/loans/buy-now-pay-later.html. **Gap:** I found no Canadian BNPL usage rate from FCAC, BoC or StatCan.
- **Bank of Canada FSR 2026** (May 28, 2026): "Overall, Canadian households have proven resilient. But debt levels are elevated". https://www.bankofcanada.ca/publications/financial-stability-report/financial-stability-report-2026/. Detailed household-stress figures were not retrieved.
- **US comparator, Ramsey SOPF Q3 2025:** 41% would "rather enjoy life now than save for the future", and one in three spend more when stressed or emotional. (Same PDF as in section 2.)
- **"Loud budgeting", social-media spending, lifestyle inflation:** I found no credible Canadian (FCAC/BoC/StatCan/major-survey) source. Treat these as cultural framing only, or leave them out.

---

## Gaps to fill if search returns
1. Equifax Canada Market Pulse Q2/Q3 2026: average card balance, card and auto delinquency, auto-loan average balance.
2. A Canadian source for the share of auto loans at 84+ months and for negative-equity trade-ins (J.D. Power Canada, Canadian Black Book, DesRosiers).
3. Dollar levels from the AutoTrader Price Index (new and used average).
4. A Canadian BNPL usage rate (FCAC or BoC survey).
5. A primary source for the Ramsey/Everyday Millionaires car-brand claim.
