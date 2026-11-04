## Access and confidence

- Researched 2026-10-28 with WebSearch/WebFetch. Primary documents read in full text (PDF extracted locally): Bridgewater "Engineering Targeted Returns and Risks" (Dalio, Aug 2011 reprint of 2004), Bridgewater Daily Observations "Our Thoughts about Risk Parity and All Weather" (Dalio/Prince/Jensen, 16 Sep 2015), Asness/Frazzini/Pedersen FAJ 2012, Qian/PanAgora Sep 2005, AQR Alternative Thinking 2026 Issue 3 "Inflation Redux?", State Street ALLW Q3 2026 Quarterly Snapshot. Read as web pages (via summariser, so exact wording is near-verbatim, not guaranteed): Bridgewater "The All Weather Story" (2012), Finance Canada FES 2022 Annex 2, Bank of Canada 28 Oct 2026 press release, StatCan Daily 19 Oct 2026, Fed H.15, BoC selected bond yields, Man Group May 2025, LongPoint RGBM page, Return Stacked US site, C.D. Howe 2024, Fortune 2024.
- Paywalled/blocked (403): Bloomberg (Dalio 21 Aug 2026; BCOM 2026), CNBC (Dalio 21 Aug 2026), Global X HEQL page, WisdomTree NTSX page. Facts from those are marked **[snippet]** (search-result text only).
- Quotes are kept under 15 words. "Near-verbatim" quotes from summarised pages are marked (nv).
- Not covered here by design: the 2014 retail 30/40/15/7.5/7.5 mix and its evidence (see origins-and-evidence.md), and Canadian ETF tickers/tax placement (other researcher). Tickers below appear only where needed to explain a mechanism.
- Confidence: high on Part 1 principles (primary text); high on ALLW figures (issuer PDF, 30 Sep 2026); high on rates/CPI/BoC (official sources, 27–28 Oct 2026); medium on gold/commodity levels (secondary price sites, one Bloomberg snippet); medium on Bridgewater institutional All Weather returns (press only; Bridgewater does not publish them).

---

## Part 1 — First principles

### P1. Return = cash + risk premium + surprise vs what is discounted

- Dalio's building blocks: "return = cash + beta + alpha" (Engineering Targeted Returns and Risks, Aug 2011, reprinting a 2004 article) — https://bridgewater.brightspotcdn.com/fa/e3/d09e72bd401a8414c5c0bdaf88bb/bridgewater-associates-engineering-targeted-returns-and-risks-aug-2011.pdf
- Why assets beat cash: the system needs it; central banks keep cash below asset returns so borrowing to invest pays (2015 Daily Observations, p. ~6): if cash beats assets, "money will move from assets to cash and the economy will contract." — https://www.cmgwealth.com/wp-content/uploads/2015/10/Our-Thoughts-about-Risk-Parity-and-All-Weather-Bridgewater-Ray-Dalio-2015.pdf
- The surprise term: "returns of assets are driven by how conditions unfold in relation to what is discounted" (2015, same PDF). Stocks do well when growth beats expectations and/or rates come in below expectations.
- The All Weather Story (Jan 2012, Podolsky/Johnson/Jennings): "Markets move based on shifts in conditions relative to … what is priced in" (nv); the two drivers are growth (volume of activity) and inflation (its pricing). All you can be confident of: assets return above cash, and volatility comes from conditions vs expectations (nv) — https://www.bridgewater.com/research-and-insights/the-all-weather-story
- Implication for the article: expected return of a balanced portfolio ≈ cash + a modest premium; the *variance* is driven by growth/inflation surprises, which is what the structure tries to neutralise.

### P2. Asset biases to growth and inflation; four equal-risk environment sub-portfolios

- 2015 text (verbatim fragments): "stocks tend to perform better when the economy is stronger"; "bonds perform better when the economy is weaker or inflation falls"; "commodities perform better when growth is strong and inflation is rising". Bridgewater wants "25% of our risk" in each box (rising/falling growth × rising/falling inflation), with a further consideration for risk premia and discount rates.
- The 2026 ALLW snapshot restates this: the portfolio is "four separate and equal risk-weighted baskets of assets" each biased to one of rising/falling growth/inflation — https://www.ssga.com/library-content/products/fund-docs/etfs/us/insights-investment-ideas/spdr-allw-quarterly-snapshot.pdf
- Typical mapping (Bridgewater's logic, my tabulation): rising growth → equities, commodities, corporate credit, EM credit; falling growth → nominal bonds, inflation-linked bonds; rising inflation → ILBs, commodities, gold, EM credit; falling inflation → equities, nominal bonds. Assets appear in two boxes; that is why weights are solved for *risk*, not assigned one-asset-per-box.
- Academic corroboration: stocks and bonds have "opposite-sign sensitivities to growth news, but same-sign sensitivities to inflation news" (AQR 2026, p. 9) — https://www.aqr.com/-/media/AQR/Documents/Alternative-Thinking/AQR-Alternative-Thinking-Q3-2026---Inflation-Redux.pdf

### P3. Balance risk, not dollars; lever low-risk assets (or lengthen duration) to a target return

- Engineering (2011): since asset-class Sharpe ratios are "broadly similar (and not reliably known)", returns and risks "can be made similar … by using leverage or leverage-like techniques"; it only requires believing assets beat cash. Beta Sharpe ratios ~0.2–0.3; a traditional mix gets ~0.4 and is "about 95% correlated to the equity markets"; the repackaged balanced mix ~0.65; at 10% vol that is ~2.5%/yr more return.
- Engineering (2011): "a moderately leveraged, highly diversified portfolio is considerably less risky than an unleveraged, non-diversified one." (14 words)
- 2015: risk parity = "levering low risk assets and/or deleveraging high risk assets so that they have more parity". Balancing is approximate, "based on logical assessments of their durations and volatilities"; estimated return/risk ~0.6 vs 0.4 for 60/40, "at 10% risk, about 2% more return". Balanced portfolio matched global equities' return "with around one-third the risk" (backtest).
- Duration is the unlevered substitute: the 2014 retail mix gets bond risk by using long/intermediate Treasuries instead of futures leverage (cross-ref origins-and-evidence.md).
- Qian (PanAgora, Sep 2005) coined "Risk Parity": with 15%/5% vols, a 60/40 gets ~93% of its risk from stocks; 1983–2004 Russell 1000 vs Lehman Agg gave "stocks contributed 93% of risk" — https://www.panagora.com/assets/PanAgora-Risk-Parity-Portfolios-Efficient-Portfolios-Through-True-Diversification.pdf
- Why it should work (not just that it did): Asness, Frazzini & Pedersen (FAJ 68(1), 2012): "Safer assets must offer higher risk-adjusted returns than riskier assets" because many investors are leverage-averse; over 1926–2010 RP's Sharpe was 0.27 higher than the value-weighted market, ≈2.7%/yr at 10% vol — https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/Leverage-Aversion-and-Risk-Parity.pdf ; SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1990493
- Ilmanen, *Expected Returns* (Wiley 2011) frames returns by asset class, style premia and underlying factors (growth, inflation, illiquidity, tail risk) — https://www.aqr.com/Insights/Research/Book/Expected-Returns-An-Investors-Guide-to-Harvesting-Market-Rewards

### P4. Many uncorrelated return streams ("Holy Grail")

- Dalio (Principles, 2017; repeated on X): "find 15 good, uncorrelated return streams" to cut "about 80% of your risk" — https://x.com/RayDalio/status/2100981186902306972 **[snippet]** (tweet text from search result). Book chart discussion: https://acquirersmultiple.com/2018/01/ray-dalio-the-holy-grail-investing-strategy/ (secondary).
- Math check (mine): N equal-vol, zero-correlation streams → portfolio vol = σ/√N. N=15 → 25.8% of σ, i.e. 74% reduction, return/risk up √15 ≈ 3.9×, not 80%/5×. At ρ=0.6 diversification floors at √0.6 ≈ 77% of σ however many streams you add. Dalio's "80%" is approximate/rounded (likely assumes slight negative correlation or uses a chart reading). Secondary confirming the 74% figure: https://statoasis.com/post/the-holy-grail-by-ray-dalio
- Engineering 2011: once assets are levered to similar return/risk, "the main difference among these asset classes will be their correlations."
- Practical caveat for a retail investor: four-to-six asset classes is not 15 uncorrelated streams; correlations are regime-dependent (P7).

### P5. Don't predict; hold structurally; rebalance

- 2015: "All Weather is a strategic asset allocation mix, not an active strategy"; it rebalances, buying what fell relative to what rose (nearly verbatim, 2015 PDF).
- Origin story (2015): Dalio's 1990 family trust; he could not trust trustees' tactical calls, so built a mix for "all economic environments", tested against 1930s US deflation and 1920s German hyperinflation. Developed with Prince early-1990s, family invested 1996, institutional clients from 2003 (2015 PDF; All Weather Story says first institutional clients 2001–02 — minor discrepancy, flag it).
- The All Weather Story: goal was an allocation that "didn't rely on predicting" the shift (nv); "put equal risk on each scenario" (nv).
- "Biggest mistake" (Dalio, CNBC 17 Oct 2018): judging "what will be good by what has been good lately" — https://www.cnbc.com/2018/10/17/ray-dalio-this-is-the-biggest-mistake-that-most-investors-make.html **[snippet]**
- 2015 answer to "bonds will surely fall as rates rise": no systematic rate bias if balanced; Mar 1946–Sep 1981 (yields lowest→highest) the balanced mix earned 8.7%/yr vs 7.6% for 60/40 (backtest, Bridgewater).

### P6. Inflation-linked bonds, cash, currency

- ILBs: "Inflation-linked bonds do well in environments of rising inflation, whereas stocks and nominal government bonds do not" (All Weather Story, nv). They filled the rising-inflation/falling-growth gap. (Timing of when ILBs entered All Weather relative to the 1997 US TIPS launch: not verified; check the All Weather Story text before stating it.)
- But 2022 lesson: "Gold, TIPS and breakevens disappointed as real yields soared but long-term inflation expectations remained anchored" (AQR 2026, p. 6, paraphrase of a 26-word sentence). ILBs hedge *realised inflation over their duration*, not a real-yield shock; long-duration ILBs carry large real-rate risk.
- Cash as the hurdle and a regime: "Risk parity loses money when the diversified portfolio of assets has a lower return than cash" (2015). That happens when tightening raises discount rates and cash yields beat risk premia — exactly 2022, and the risk again in H2 2026 (BoC, Fed hiking). Cash today: BoC 2.50%, Fed funds eff. 3.88% (Part 2).
- Currency: Bridgewater's 2011 asset chart shows "hedged non-US bonds" (Engineering, Chart 1) — foreign bonds are held currency-hedged; ALLW's ILB sleeve is 100% US TIPS (snapshot). Bridgewater has no published retail rule for a non-USD base currency; for a Canadian, an unhedged USD sleeve adds USD/CAD risk, which historically has *diversified* Canadian equity (CAD tends to fall with oil/risk-off) — that last point is my inference; needs a source if used.

### P7. When the stock-bond correlation turns positive

- Driver: "the stock–bond correlation thus depends not on the level of inflation, but on the relative volatility of growth and inflation" (Brixton, Brooks, Hecht, Ilmanen, Maloney, McQuinn, JPM 49(4), 2023) — https://www.aqr.com/Insights/Research/Journal-Article/A-Changing-Stock-Bond-Correlation ; model explains ~70% of long-term US variation.
- Regimes (AQR 2026 Exhibit 1/8): positive 1973–1999, negative 2000–2019/21, "apparent regime change from 2022 onwards"; 36-month correlation "recently risen to multi-decade highs" (data to 31 Jul 2026).
- Man Group (Henry Neville, May 2025): below 3% inflation, correlation "negative 71% of the time"; above 3%, "negative 2% of the time" — https://www.man.com/insights/road-ahead-signs-of-the-times . Note Canada CPI is 3.1% (Sep 2026) and the BoC expects ~3.5% by year-end.
- Counterpoint: Man Group (Bloomberg, 6 Oct 2026) says moderate (2–4%) inflation has not hurt Treasury returns; 10y UST averaged 6.9% nominal / 4% real in such periods — https://www.bloomberg.com/news/articles/2026-10-06/man-group-disputes-view-that-high-inflation-is-bad-for-us-bonds **[snippet]**
- Secondary figures (not verified): 3-yr rolling S&P/UST correlation ~0.59 in 2025; +0.77 correlation of annual returns 2021–2025 — https://www.oxfordeconomics.com/resource/stock-bond-correlation-will-become-positive-again-in-2026/ (search snippet) **[snippet]**
- AQR's prescription: in inflation-dominant regimes "bonds are less diversifying to stocks, but commodities are strongly diversifying to both" (p. 10, 19 words → paraphrase); recommends strategic ILBs, commodities, trend following. Their inflation-dominant correlation matrix: trend vs equities −0.26, vs bonds −0.18; commodities vs bonds −0.53.
- AQR on late 2026: de-anchoring risks "seem real in late 2026" (Fed independence challenged, loose fiscal, trade policy); a "triple-whammy" on Treasury yields.

---

## Part 2 — What is different in 2026

### Bridgewater goes retail: ALLW (State Street Bridgewater All Weather ETF)

- Launched 5 Mar 2025 (NYSE Arca; originally "SPDR", now "State Street" branding). Actively managed; Bridgewater supplies a daily model portfolio, SSGA trades it. Gross = net expense ratio 0.85%. AUM $1,842.81M (27 Oct 2026) — https://www.ssga.com/us/en/intermediary/etfs/state-street-bridgewater-all-weather-etf-allw
- Notional exposure at 30 Sep 2026 (snapshot): nominal government bonds 70.7% (US 36.3, Europe 18.5, Australia 9.4, UK 6.5); equities 43.6% (US 13.6, Eurozone 9.5, Japan 4.9, EM 4.4, UK 4.0, Australia 3.8, China 3.4); inflation-linked bonds 36.5% (all US); commodities 32.7% (broad 23.1, gold 9.6). Total ≈ 183.5% → ~1.8× gross notional via futures/swaps. Note: no Canadian bonds or equities.
- Performance (NAV, 30 Sep 2026): Q3 −2.21%; YTD +3.91%; 1-yr +7.63%; since inception (cum.) +12.08%. MSCI ACWI IMI same periods: +1.08 / +12.97 / +16.61 / +21.24.
- 2025 (inception to 31 Dec): +15.1% **[snippet]** (https://www.fool.com/investing/2026/03/30/will-this-all-weather-etf-live-up-to-its-name/).
- Q3 2026 commentary (Bridgewater/SSGA): central banks hiked (Fed, ECB, BoJ, RBA); real yields +40 bp and breakevens +20 bp across DM; nominal and inflation-linked bonds "were the largest sources of losses"; oil gains and a small gold gain offset. "Commodities … the only asset class to post strong positive returns." 2026 saw oil above $100 several times, gold's record then "equally swift unwind", real yields at "decades-high levels".
- Institutional All Weather: lost ~22% in 2022 (vs ~−20% in 2008); risk-parity AUM industry-wide fell from ~$160B (2021) to ~$90B (end 2023), ~$70B withdrawn — https://fortune.com/2024/04/23/lackluster-returns-ray-dalio-investing-strategy-investors-pull-billions/ (Bridgewater does not publish fund returns; treat as press-reported). HFR Risk Parity 10% Vol index −19.5% in 2022 **[snippet]** (https://www.markovprocesses.com/blog/risk-parity-not-performing-blame-the-weather/). I did not find reliable published 2023–2025 annual returns or current AUM for the institutional All Weather fund.

### Dalio's latest public views (2025–2026)

- Book *How Countries Go Broke: The Big Cycle* (June 2025); "3% solution": cut US deficit to 3% of GDP via spending cuts, revenue and lower rates — https://raydalio.substack.com/p/how-countries-go-broke-in-a-5-minute ; House Budget Committee, 25 Mar 2025 — https://budget.house.gov/press-release/ray-dalio-to-house-gop-cut-the-budget-deficit-to-3-of-gdp
- LinkedIn post 21 Aug 2026 (reacting to Treasury Secretary Bessent's debt-buyback plan): underweight bonds, hold ~10–15% gold and "a bit" of bitcoin; US debt crisis possibly ~3 years away (±2) unless deficit cut from ~6% to 3% of GDP; revenue ~$5.5T vs spending ~$7.5T, interest ~$1T, ~$10T to refinance — Bloomberg https://www.bloomberg.com/news/articles/2026-08-21/dalio-says-sell-bonds-buy-gold-bitcoin-as-debt-crisis-looms **[snippet]**; CNBC https://www.cnbc.com/2026/08/21/ray-dalio-bessent-debt-crisis-bitcoin-gold.html **[snippet]**; Yahoo Finance https://finance.yahoo.com/markets/stocks/articles/bridgewater-founder-dalio-urges-investors-134826829.html (read; summariser): "tilt away from bonds and toward gold" (nv).
- Earlier: 5–15% gold as diversifier, "monetary order is breaking down" — https://seekingalpha.com/news/4540556-ray-dalio-the-monetary-order-is-breaking-down-recommends-5-15-allocation-in-gold **[snippet]**
- Article angle: Dalio's personal *tilt* (less bonds, more gold) departs from the strategic, no-prediction All Weather he co-designed; ALLW itself held only 9.6% gold notional and 107% notional in bonds (nominal + ILB) at 30 Sep 2026. Worth stating the tension plainly.

### Market levels (as of 27–28 Oct 2026)

| Item | Level | Date | Source |
|---|---|---|---|
| US 10y Treasury | 4.99% | 27 Oct 2026 | Fed H.15 https://www.federalreserve.gov/releases/h15/ |
| US 30y Treasury | 5.30% | 27 Oct 2026 | Fed H.15 |
| US 5y | 4.82% | 27 Oct 2026 | Fed H.15 |
| US 10y TIPS real yield | 2.64% | 27 Oct 2026 | Fed H.15 |
| US 30y TIPS real yield | 3.05% | 27 Oct 2026 | Fed H.15 |
| Fed funds effective | 3.88% | 27 Oct 2026 | Fed H.15 (FOMC meeting 27–28 Oct; ~82% odds of a December hike per USAGold) |
| GoC 2y / 5y / 10y | 3.36% / 3.57% / 3.83% | 27 Oct 2026 | BoC https://www.bankofcanada.ca/rates/interest-rates/canadian-bonds/ |
| GoC long bond | 4.12% | 27 Oct 2026 | BoC |
| GoC long Real Return Bond yield | 1.87% | 27 Oct 2026 | BoC |
| BoC policy rate | 2.50% (+25 bp, first hike in ~3 yrs) | 28 Oct 2026 | https://www.bankofcanada.ca/2026/10/fad-press-release-2026-10-28/ |
| Canada CPI | 3.1% y/y (ex-gasoline 2.2%; gasoline +27.8%, energy +19.0%) | Sep 2026, released 19 Oct | https://www150.statcan.gc.ca/n1/daily-quotidien/261019/dq261019a-eng.htm |
| Gold | ~$4,025–4,060/oz; YTD ≈ −6 to −7%; 2026 high ~$5,590–5,599 (28 Jan 2026) | 27 Oct 2026 | https://www.usagold.com/daily-precious-metals-market-report-october-27-2026/ ; https://fortune.com/article/current-price-of-gold-10-27-2026/ |
| Bloomberg Commodity Index | ~+33% in 2026 | Q3/Oct 2026 | https://www.bloomberg.com/professional/insights/commodities/what-is-driving-broad-commodities-33-rise-in-2026/ **[snippet]** |
| Oil | WTI ~$101, Brent ~$115 | Oct 2026 | same search result **[snippet]** |

- BoC rationale (verbatim fragment): to reduce the risk "that continuing high energy prices spread broadly"; CPI ~3% since April, ~3½% by year-end, 2027 avg ~3%, back to 2% by mid-2028; core near 2%; growth 1% in 2026.
- Gold run: 2024 +~25.5% (LBMA close $2,610.85); 2025 +~67% to $4,367.80 (LBMA PM 30 Dec 2025), best year since 1979 — https://www.visualcapitalist.com/charted-golds-annual-returns-2000-2025/ **[snippet]**; then record ~$5,590 in Jan 2026 and a ~28% fall to ~$4,030.
- Real yields: US 10y TIPS 2.64% vs Canadian long RRB 1.87%. Real yields at levels last common pre-2008 make the "cash + premium" maths for ILBs much better than in 2020–21 (when real yields were negative). Inference; worth one line in the article.
- Yield curve contrast: US 10y 4.99% vs GoC 10y 3.83% (≈116 bp gap). USD bonds held unhedged by a Canadian earn the gap but take FX risk; hedged, most of the gap is lost to the hedge cost (covered interest parity; my inference, not sourced).

### Capital efficiency / return stacking: getting the leverage without a margin account

- Mechanism: a fund holds $1 of one exposure in cash securities and uses futures/swaps (cheap embedded leverage at roughly cash rates) to add a second $1 (or $0.6) exposure. This is how ALLW reaches ~1.8× notional. Risk: you pay cash rate + spread on the levered sleeve; if both sleeves fall (2022), losses compound; counterparty/derivative and tracking risks; higher fees.
- Canada-listed:
  - RGBM — Return Stacked Global Balanced & Macro ETF (TSX), launched 5–6 Feb 2025; $1 global balanced + $1 systematic macro (trend + carry, long/short futures). Mgmt fee 0.85% + 10% performance fee over a 50/50 global equity / 10-yr GoC benchmark; MER 1.22% (audited, incl. perf fee); AUM C$38.36M (27 Oct 2026) — https://www.longpointetfs.com/etfs/rgbm ; first Canadian Return Stacked ETF — https://www.newsfilecorp.com/release/239778/Longpoint-Adds-Return-Stacked-Global-Balanced-Macro-ETF-RGBM ; Canadian family page lists only RGBM/RGBM.U — https://returnstackedetfs.ca/
  - "Enhanced" 1.25× funds (Global X HEQL etc., Hamilton): cash borrowing of 25% of NAV inside the fund, no daily reset; HEQL MER ~1.46% incl. borrowing (search snippet) **[snippet]** — https://www.globalx.ca/product/heql (403). These lever *equity*, i.e. the wrong side for risk parity; useful only as a contrast.
  - Auspice One Fund Trust (alternative mutual fund, not ETF): 100% stocks/bonds/gold + 100% managed futures **[snippet]** — https://pictureperfectportfolios.com/aoft-mutual-fund-review-auspice-one-fund-trust/
- US-listed (Canadians can buy in USD accounts; no Canadian tax-treaty relief in TFSA; other researcher covers tax):
  - RSSB 100% global equities + 100% US Treasuries (futures), ER 0.39%; RSBT 100% bonds + 100% managed futures, ER 1.01%; RSST 100% US equity + 100% trend, ER 0.99%; RSSY equity + carry; RSBA bonds + merger arb — https://www.returnstackedetfs.com/
  - NTSX (WisdomTree US Efficient Core) 90% S&P 500 + 60% Treasury futures, ER 0.20%; GDE 90% US large-cap + 90% gold futures, ER 0.20% **[snippet]** — https://etfdb.com/etf/NTSX/ ; https://www.wisdomtree.com/us/insights/blog/gold-in-the-age-of-efficient-capital
- For the article: these let a Canadian approximate "lever the low-risk assets" (P3) in a TFSA/RRSP where margin is not allowed. Key honest risk: in a positive-correlation, rising-cash-rate regime (2022, H2 2026) stacked bond exposure is the thing that hurts.

### Managed futures / trend following as a "fifth" diversifier

- 2022: SG Trend Index +27.3%, SG CTA Index +20.1% (best since 2000), from short bonds/rates and long USD and energy — https://www.hedgeweek.com/trend-followers-turn-leaders-ctas-deliver-record-returns-2022/
- AQR 2026: commodities, trend and L/S value were strongest in the 2022 bear market; trend "outperformed in both inflationary and disinflationary bear markets" (paraphrase; p. 17). Assumed long-run (SG Trend proxy) return 6.1%, vol 12.3%, Sharpe 0.25.
- 2026: US managed-futures ETFs DBMF ~+18% and KMLM ~+20% YTD, CTA ~+10% **[snippet]** (search result; https://finance.yahoo.com/markets/options/articles/3-managed-futures-etfs-made-122837848.html).
- Not part of Bridgewater's All Weather (which is static beta); adding it is a departure from "no prediction" toward "systematic reaction". Trend is long/short and reacts with a lag; it can lose in choppy, trendless years.
- Availability in Canada: earlier TSX managed-futures ETFs (Horizons Auspice HMF, iShares CMF) were delisted **[snippet]** — https://www.bloomberg.com/quote/HMF:CN . Current routes: RGBM (stacked macro incl. trend), Auspice alternative mutual funds, or US-listed DBMF/KMLM/RSBT/RSST. I found no plain, standalone Canada-listed trend ETF in Oct 2026 (absence not proven).

### Canada's Real Return Bonds and inflation protection

- Finance Canada, Fall Economic Statement, 3 Nov 2022, Annex 2: "cease issuance of Real Return Bonds (RRBs) effective immediately" (nv); reason: "low demand for this product" and to "promote liquidity by consolidating funding" in core sectors (nv) — https://budget.canada.ca/fes-eea/2022/report-rapport/anx2-en.html
- Pushback: C.D. Howe (22 Aug 2024): the government's own small issues and few maturities made a thin market; survey of 13 institutions ($2.6T) unanimously opposed cancellation — https://cdhowe.org/publication/cancel-rrb-cancellation/ . No reversal found as of Oct 2026 (Benefits Canada noted the budget silence — https://www.benefitscanada.com/canadian-investment-review/fixed-income/expert-says-lack-of-real-return-bonds-update-from-federal-budget-is-disappointing/).
- Existing RRBs still trade (long RRB yield 1.87%, BoC 27 Oct 2026); iShares XRB holds them: effective duration ~10.85 yrs, real yield ~2.38% (22 Oct 2026) **[snippet]** — https://www.blackrock.com/ca/investors/en/products/239490/ishares-canadian-real-return-bond-index-etf . Supply is shrinking as no new bonds are issued.
- Alternatives (mechanism only; other researcher covers tickers/tax): short US TIPS in CAD (iShares XSTH CAD-hedged, net assets ~C$2.58B on 23 Oct 2026 **[snippet]**; XSTP unhedged) — https://www.blackrock.com/ca/investors/en/products/319670/ishares-0-5-year-tips-bond-index-etf-cad-hedged ; short-term nominal bonds/cash (reprice quickly with rate hikes); broad commodities; gold. Caveat: US TIPS hedge US CPI, not Canadian CPI; the two diverged in 2026 (Canada 3.1% headline, ex-gasoline 2.2%).
- AQR's 2022 evidence ranks commodities and trend above TIPS/gold for an inflation *shock*; ILBs protect best against sustained realised inflation when bought at decent real yields.

---

## Threads for the article (my synthesis, not sourced)

1. The principles have aged well; the *2014 retail recipe* encodes 2000–2020 correlations (long Treasuries as the main hedge). The principle says balance growth *and* inflation risk; 2022 and H2 2026 are the inflation boxes showing up.
2. 2026 is the first year a retail investor could buy Bridgewater's own implementation (ALLW). Its weights (≈1.8× notional, ~107% bonds, 9.6% gold, 23% broad commodities, no Canada) are a useful reference point against the 30/40/15/7.5/7.5 mix.
3. For a Canadian: no new RRBs; BoC hiking; CAD-based investor faces USD real yields (2.64%) above Canadian (1.87%). Inflation box has to be filled with short TIPS, commodities, gold, possibly trend.
4. Dalio-the-commentator (cut bonds, 10–15% gold) vs All-Weather-the-design (don't predict, keep bonds balanced). The article should present both and say which one the reader is following.
5. Math honesty: "15 streams cut 80%" is ~74% at zero correlation; with real assets correlated, retail investors get maybe 3–5 effective bets.
