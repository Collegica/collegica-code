# Social discourse: fixed or variable, Canada (Reddit, X, hindsight stories)

Research date: 2026-09-10. Scope: what Canadian borrowers and mortgage brokers are saying right now about fixed vs variable, and how the 2021 variable cohort and the 2023 fixed cohort feel in hindsight.

## Access and confidence

- **Reddit is blocked for every non-browser client.** `www.reddit.com` and `old.reddit.com` return "blocked due to a network policy" (403) to WebFetch, curl with a browser UA, `api.reddit.com`, and `r.jina.ai`. `api.pullpush.io` now returns 429 with an explicit "no free scraping for agents" message. Five redlib mirrors returned empty pages. `agent-reach` is not installed.
- **What worked:** the user's Chrome session (claude-in-chrome). Loading `old.reddit.com` in a tab, then running a same-origin `fetch()` of `/r/<sub>/search.json` and `<permalink>.json?sort=top` from page context returned full JSON (scores, comment counts, OP text, top comments). Cloudsearch `timestamp:` syntax works for year-bounded searches. Every Reddit item below marked **[fetched]** has OP text and the top 3–5 comments read verbatim with live scores; **[snippet]** means title/score/comment count only. Scores are live as of today and drift by a few points between calls.
- **X:** no authenticated access. WebSearch `site:x.com` to discover, then `api.fxtwitter.com/<user>/status/<id>` for full text and engagement (works; `api.vxtwitter.com` returned 403 today). Thread continuations are not retrievable, so multi-part Ron Butler threads are known only from their first post plus press coverage. `site:x.com` search is very noisy and surfaced almost nothing from June–September 2026; the most recent fetched broker post is 2026-05-30.
- **Web hindsight pieces:** CBC, Global, CMT, MPA, nesto, True North, Ratehub, NerdWallet fetched fine (some via `r.jina.ai`). Globe and Mail, canadianmoneyforum (now behind a TollBit paywall), and the Financial Post video page did not yield text.
- Reddit posters are private individuals: thread URL, subreddit and date only, no usernames. Brokers and commentators are named.

## 1. Reddit

### 1a. The 2026 decision threads (renewal wave)

1. **"Bank of Canada holds interest rate at 2.25%. Should I go fixed or variable for our mortgage this year?"** — r/PersonalFinanceCanada, 2026-03-18, 256 pts, 345 comments [fetched]
   https://old.reddit.com/r/PersonalFinanceCanada/comments/1rxd4bk/bank_of_canada_holds_interest_rate_at_225_should/
   OP: business owner with 3 years of runway, notes "a few years ago people all over reddit would say go variable" but sees preference shifting to fixed. Top comments: (603) going fixed "so I dont have to devote mental energy to worrying about it"; (389) "My crystal ball is in the shop"; (170) if you think the Iran war pushes inflation up, go fixed; (103) went variable because they may move and the break penalty is far smaller; (72) just took RBC 3-yr fixed 3.54% — "I just want some stability."
2. **"Why are banks now pitching 3-year vs 5-year mortgages?"** — r/PersonalFinanceCanada, 2025-11-28, 157 pts, 216 comments [fetched]
   https://old.reddit.com/r/PersonalFinanceCanada/comments/1p91x7s/why_are_banks_now_pitching_3year_vs_5year/
   OP: two banks both pushed a 3-year; "is 3 the new 5?" Top: (218) their broker also pushed 3-year until they insisted on 5; (103) it's just the yield curve, "nothing sinister"; (58) 3-year is cheaper and renews sooner into expected lower rates; (22) suspects lenders are steering to 3-year to limit their own rate risk.
3. **"Variable vs. Fixed in 2026-2027"** — r/PersonalFinanceCanada, 2026-01-09, 82 pts, 152 comments [fetched]
   https://old.reddit.com/r/PersonalFinanceCanada/comments/1q8ftbt/variable_vs_fixed_in_20262027/
   OP is a 2021 variable-taker ("one of those bone headed people... eating all the COVID hikes to the face"), renewing within 9 months. Top: (107) "over the long run variable tends to win out. If you can't [stomach it], go fixed"; (69) "standard fallacy of what was influences what will"; (23) choosing variable in 2021 "wasn't bone-headed... only a loss in retrospect"; (17) going fixed, "my peace of mind is more important than saving possibly 0-2%."
4. **"Mortgage renewal 500k (3.6 variable or 4.2 3yr fixed)"** — r/MortgagesCanada, 2026-09-05, 25 pts, 84 comments [fetched] — the freshest thread
   https://old.reddit.com/r/MortgagesCanada/comments/1w86ujn/mortgage_renewal_500k_36_variable_or_42_3yr_fixed/
   Top: (19) a 2021 variable-taker's post-mortem: 1.18% variable vs 2.2% fixed, "did the maths: 0.25 x 4... The maths was right, yours truly was wrong" — reached 6%, and the lender's "switch to fixed" was at posted rates; (18) took 3.8% 5-yr fixed, "the last 5 years on variable was a rollercoaster"; (14) "Projections are for 3 consecutive rate hikes come January. If you can handle it, stick with variable"; (9) "in 2021, the message from banks was that rates were low and would remain low... even the banks have no clue."
5. **"Can't decide between variable or fixed… My broker insists going variable but I'm worried."** — r/MortgagesCanada, 2026-05-21, 32 pts, 220 comments [fetched]
   https://old.reddit.com/r/MortgagesCanada/comments/1tjrsbb/cant_decide_between_variable_or_fixed_my_broker/
   OP: 3-yr fixed 3.8% (RBC, cashback + points) vs 5-yr variable 3.30%; not selling for 10+ years. Top: (22) "you are worried, that shows your risk tolerance. So go fixed and sleep well at night"; (14) 3.8% for 3 years is good, BoC "caught between" US yields and weak employment; (13) a broker: "I would personally go variable" but warns RBC claws back cashback if you break; (9) "I don't think I could ever sleep easy choosing a variable rate."
6. **"3.45 variable vs. 3.69 fixed"** — r/MortgagesCanada, 2026-05-12, 50 pts, 125 comments [fetched]
   https://old.reddit.com/r/MortgagesCanada/comments/1tavumc/345_variable_vs_369_fixed/
   OP: TD 5-yr variable 3.45% vs RBC 3-yr fixed 3.69% with 30-yr amortization; "historically variable always saved me money." Top: (10) renewed variable, an unusually low fixed offer "looks like RBC is trying to make fixed attractive"; (9) "At these rates, fixed is no brainer... You are trying to time market"; (7) chose variable only because selling in 1–2 years (penalty).
7. **"Mortgage Rates!! So much uncertainty!"** — r/PersonalFinanceCanada, 2026-03-20, 151 pts, 340 comments [fetched]
   https://old.reddit.com/r/PersonalFinanceCanada/comments/1rz1kw6/mortgage_rates_so_much_uncertainty/
   OP: $640k uninsured, 6 months pregnant, offered 3.69% 3-yr fixed. Top: (357) "3.69 is great right now"; (295) "fixed rates under 4% are fantastic deals. People got spoiled by... 5 years ago but that is NOT normal."
8. **"Variable or fixed mortgage? Which would you choose today"** — r/MortgagesCanada, 2025-12-06, 21 pts, 113 comments [fetched]
   https://old.reddit.com/r/MortgagesCanada/comments/1pfitxi/variable_or_fixed_mortgage_which_would_you_choose/
   Top: (11) "I prefer fixed. 3yrs. Steady payments... No stress"; (9) "every bank is trying to sell you on var right now… my instinct would be fixed"; (8) "Variable, consistently... with fixed I'm paying for the fudge room the bank builds in"; (8) chose 3-yr fixed 3.74% over 3.65% variable, "difference is insignificant compared to peace of mind."
9. **"3 yr fixed vs 5 yr variable"** — r/PersonalFinanceCanada, 2025-11-20, 46 pts, 42 comments [fetched] — a 2023 fixed-taker renewing off 5.54%
   https://old.reddit.com/r/PersonalFinanceCanada/comments/1p2fc7p/3_yr_fixed_vs_5_yr_variable/
   Top: (66) "Option to switch to fixed is a sham. The fixed they let you switch to will always be like 1% higher"; (16) predictions are priced in, variable wins "more often than not" if you can absorb the risk; (9) "Historically, variable usually comes out on top."
10. **"Bond yields ripping. Better lock in those mortgage rates soon!"** — r/TorontoRealEstate, 2026-09-10 (today), 150 pts, 136 comments [fetched] and **"Canada's fixed mortgage rates surge higher as bond yields continue to rise"** — r/TorontoRealEstate, 2026-09-03, 85 pts, 89 comments [fetched]
    https://old.reddit.com/r/TorontoRealEstate/comments/1wck0k3/bond_yields_ripping_better_lock_in_those_mortgage/ · https://old.reddit.com/r/TorontoRealEstate/comments/1w6cuzu/canadas_fixed_mortgage_rates_surge_higher_as_bond/
    The Sept 3 OP quotes Ratehub's Jamie David: the fixed–variable spread has "widened noticeably", lowest 5-yr variable ~3.3% vs 5-yr fixed ~4.09%. Today's thread: (94) "RBC said the housing market had bottomed. Proof that nobody really knows"; (31) "Just go variable, the BoC might hike 25 basis points." The sub's mood is bearish on housing rather than analytical about terms.
11. **"Bank of Canada holds overnight rate at 2.25% — what it means for mortgages"** — r/canadahousing, 2026-06-10, 166 pts, 61 comments [fetched]
    https://old.reddit.com/r/canadahousing/comments/1u2bb5z/bank_of_canada_holds_overnight_rate_at_225_what/
    OP: 3.35% variable vs ~4.04% fixed is "about $182/month on a $500K mortgage." Top: (70) "Where are you seeing such low rates?" — friend offered 4.29%; (29) "There is no such thing as 3.35% right now"; (19) BMO went from 4.3% to 3.89% 3-yr fixed within 24 hours of being told the borrower would call a broker. Rate-shopping friction is a recurring sub-theme.
12. **"Anyone renew their mortgage lately after interest rates decreased?"** — r/PersonalFinanceCanada, 2025-09-29, 96 pts, 187 comments [fetched] — OP paying 5.34% on a 2022/23 3-yr fixed, offered 4.20% variable / 4.39% 3-yr / 4.59% 5-yr. Top: (129) those rates are "confusingly high", should get ~4% fixed; (52) Scotia 5-yr fixed 3.76% "coming from 1.89% so..."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/1ntms47/anyone_renew_their_mortgage_lately_after_interest/
- Also seen [snippet]: "Renewal is up in 5 months" (r/MortgagesCanada, 2026-04-20, 20 pts/59c); "Mortgage renewal in October 2026. Currently on variable (3.45%)... should I renew early to fixed?" (r/PFC, ~2026-04, 30 pts/21c, OP worried by oil and bond yields); "Would You Go Variable at 3.55% or Lock in Fixed at 3.90%?" (r/RealEstateCanada, 2026-06-18, 13 pts/53c [fetched]: top answer "Fixed given the tremendous disruption that Trump can and is willing to cause"); "Variable or Fixed Mortgage" (r/TorontoRealEstate, 2026-07-10, 25 pts/40c [fetched], top comments mock the OP's high quotes: "I'm 3.4 variable, renewed in June").

### 1b. The 2021 variable cohort: fixed-payment VRM fallout, still surfacing in 2026

13. **"Parents Can't Pay Off Deferred Interest (Ontario)"** — r/PersonalFinanceCanada, 2026-04-14, 141 pts, 298 comments [fetched]
    https://old.reddit.com/r/PersonalFinanceCanada/comments/1slemjz/parents_cant_pay_off_deferred_interest_ontario/
    A 21-year-old's parents took a CIBC fixed-payment variable in 2021, hit trigger, and now owe ~$22K deferred interest before CIBC will renew them into a 3-yr fixed; house bought at $1.1M, now ~$900K. Top: (449) pay the $300/month, the $10K "you probably will never get back"; (82) "Your parents need to sell the house that they can't afford."
14. **"(Update) PSA: CIBC is putting 'missing payment' strikes on variable rate mortgages from 2021 even if they're in good standing"** — r/PersonalFinanceCanada, 2025-12-26, 211 pts, 50 comments [fetched] (original: 2025-12, 76 pts/30c)
    https://old.reddit.com/r/PersonalFinanceCanada/comments/1pw7dqn/update_psa_cibc_is_putting_missing_payment/
    2021 CIBC variable; deferred interest accrued under the "designated amount" clause; credit score dropped ~150 points from two "missed payment" strikes reported right before renewal; CIBC: "not obligated to" notify. Escalating to FCAC. Concrete, citable example of the fixed-payment-VRM trap's long tail.
15. **"Millions of Canadians were bracing for a mortgage shock that never happened"** — r/TorontoRealEstate, 2026-01-22, 196 pts, 123 comments [fetched] — top comment (76): "Bought in 2021. Just renewed. Payment went up $82 a week." (58) "Canadians... will pay their mortgage no matter what. Second job, third job, rent out a room."
    https://old.reddit.com/r/TorontoRealEstate/comments/1qk605v/millions_of_canadians_were_bracing_for_a_mortgage/
16. **"Canadian Variable-Rate Mortgages Surge As BoC Recreates Renewal Trap"** — r/TorontoRealEstate, 2026-04-12, 124 pts, 112 comments [fetched] — OP mocks "True Peak FOMO bagholders who took variable rates during 2021/22 and paid tuition fees"; top reply (62): "Renewal rates are the biggest scam ever created by the banks instead of just having a 30 year mortgage at a fixed rate."
    https://old.reddit.com/r/TorontoRealEstate/comments/1sj1n3x/canadian_variablerate_mortgages_surge_as_boc/

### 1c. The "variable regret" genre, 2022–2023 (highest-voted)

17. **"No good options left - Locking in our mortgage today means my family will have to eat $600 into our savings every month for 4 years - do we do it?"** — r/PersonalFinanceCanada, 2022-10-17, 744 pts, 642 comments [fetched]
    https://old.reddit.com/r/PersonalFinanceCanada/comments/y61sm7/no_good_options_left_locking_in_our_mortgage/
    ~$800K GTA mortgage, family of five; "everywhere we turned we were advised not to lock in and that rates couldn't possibly exceed 5%"; about to lock 5.4% for 4 years and run $7,200/yr cash-flow negative; alternative was hitting trigger in early 2023. Top: (827) buckle in; (389) "$29,000 for peace of mind over 4 years is really cheap"; (348) "Lock it"; (193) "You'll sleep better."
18. **"Variable Vs Fixed Rate Hindsight & Interactions"** — r/PersonalFinanceCanada, 2022-10-29, 741 pts, 331 comments [fetched]
    https://old.reddit.com/r/PersonalFinanceCanada/comments/ygmqn3/variable_vs_fixed_rate_hindsight_interactions/
    A plea for civility: 2021 spreads were 1.25–1.75% ("5–7 hikes"), banks signalled low-for-long. Top: (210) fixed 3.29% in 2019 "looked on in sadness as we dropped to 1%"; (145) "I chose Variable because everyone said the rates won't go up this much this fast lol"; (128) "My options in Nov. 2021 were 1.45% ARM and 3.45% fixed"; (91) "I just can't sleep at night knowing it could change on a whim."
19. **"BMO tells us we owe $106,000 to get our mortgage 'back on track'"** — r/PersonalFinanceCanada, 2023-01-29, 1,043 pts, 657 comments [fetched]
    https://old.reddit.com/r/PersonalFinanceCanada/comments/10nx3ub/bmo_tells_us_we_owe_106000_to_get_our_mortgage/
    First-time owners, $960K variable at 1.35% (Dec 2021), rate 5.6% thirteen months later; payment stepped from $3,772 to ~$4,360+ month by month. Top (577) explains "back on track" means returning to the original amortization; (360) "Same thing happened to me... told 'You didn't do your homework'."
20. **"First time home buyers with variable, don't blame your broker"** — r/PersonalFinanceCanada, 2023-06-08, 438 pts, 817 comments [fetched]
    https://old.reddit.com/r/PersonalFinanceCanada/comments/14478bq/first_time_home_buyers_with_variable_dont_blame/
    OP bought spring 2021 at 1.22% variable vs 1.56% fixed; defends the choice on the information available. Top: (731) anxious husband insisted on 1.84% fixed in 2020 and "apologized for his anxiety costing us extra money... he's not apologizing anymore"; (709) "you're an adult capable of making your own decision"; (494) "1.22% to 1.56% is a spread of about one rate hike... fixed would still have been better."
21. **"Mortgage Rate from 1.2 to 5.8 in 1 year"** — r/PersonalFinanceCanada, 2023-06-09, 291 pts, 352 comments [fetched] — bought end-2021, "bleeding money"; (73) "Yes you can lock in, but no it won't be lower"; (66) "I am ride or die with my variable rate.. 7% here we come.."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/1455cag/mortgage_rate_from_12_to_58_in_1_year/
22. **"Mortgage amortization increased to 55 years"** — r/PersonalFinanceCanada, 2022-07-14, 454 pts, 307 comments [fetched] — 1.4% 5-yr variable, 30-yr amortization; after the July 2022 hike "original amortization is 360 months while my actual months remaining is 663." (222) "I went from 233 months left to 265 as of this morning."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/vyypg9/mortgage_amortization_increased_to_55_years/
23. **"Variable mortgage trigger rate!!"** — r/PersonalFinanceCanada, 2022-08-13, 426 pts, 459 comments [fetched] — $944K Vancouver variable at 3.69%, trigger 4.24%, bi-weekly $1,537 (top reply, 1,323: "Top thread: No one actually has a million dollar mortgage. Third thread: I have a million dollar mortgage.").
    https://old.reddit.com/r/PersonalFinanceCanada/comments/wnhbsl/variable_mortgage_trigger_rate/
24. **"Got the Trigger Rate courtesy call from RBC"** — r/canadahousing, 2022-07-26, 315 pts, 180 comments [fetched] — renewed 2020 at 2.70%, now 4.95%; lump sum or +$600/month; (64) TD fixed-payment variable, amortization "went from 30 years to 50 years."
    https://old.reddit.com/r/canadahousing/comments/w8twge/got_the_trigger_rate_courtesy_call_from_rbc/
25. **"1st time since 1990. Variable mortgage rates surpassing Fixed rates"** — r/PersonalFinanceCanada, 2022-11-09, 580 pts, 364 comments [fetched] — the I-told-you-so moment. (753) renewers "all plan on creating a new post asking the opinion of PFC"; (135) took 2.2% variable over 3.89% fixed, "up to 5% right now... And if it doesn't, then fuck me I guess."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/yqnh3t/1st_time_since_1990_variable_mortgage_rates/
26. **"Why did so many people go with variable when rates were sub 2%?"** — r/MortgagesCanada, 2023-09-07, 120 pts, 509 comments [fetched] — top replies: (30) "Why so many are going for fixed when rates are ATH? Answer for both: Nobody knew"; (26) "Tiff said rates would remain low for a long period"; (19) "a year from now people will ask 'Why people signed 5 years at 5.6% fixed in 2023?'" (prescient).
    https://old.reddit.com/r/MortgagesCanada/comments/16ck3ej/why_did_so_many_people_go_with_variable_when/
27. **"For those who have variable mortgages... do you regret your decision?"** — r/PersonalFinanceCanada, 2021-08-07, 96 pts, 169 comments [fetched] — the pre-hike consensus in amber. (229) "Nobody who has done it in the last 10-12 years has any reason to regret... This is a sampling problem"; (41) "I have never met anyone who was upset with variable for the past 15 years"; (68) locked in 5.29% in 2008 just before rates fell, "stuck with variable ever since."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/ozsked/for_those_who_have_variable_mortgages_in_the_past/
- Also: "Seen on Twitter — how many people that got a mortgage in the last 2/3 years are in the same spot now" (r/canadahousing, 2023-01-29, 194 pts/176c [fetched]; top (153): "Who doesn't lock in with a 1% rate, that is the real crime"); "45% with variable mortgages say they would have to sell in under 9 months: Yahoo/Maru poll" (r/canadahousing, 2023-02-02, 305 pts/235c [fetched]; (109) "when you have 'historic lows' and you're taking out a variable rate, one should assume it's going to go up"); "Variable Mortgage vs Fixed" (r/PFC, 2021-10-26, 66 pts/121c [fetched]: OP at 1.19% variable dismisses older friends' 1980s warnings, "Am I being stupid?" — top reply is about break penalties, not rate risk).

### 1d. The 2023 fixed cohort (locked at 4.2–6.6%) in hindsight

28. **"For those soon coming up on their mortgage renewal, here's what the bank just offered me."** — r/PersonalFinanceCanada, 2023-04-21, 593 pts, 279 comments [fetched] — variable 6.2%, 2-yr 5.55%, 3-yr 5.35%, 5-yr 4.19%. (367) "4.2 for 5 years doesnt seem to bad"; (66) "This is why I always go fixed."
    https://old.reddit.com/r/PersonalFinanceCanada/comments/12uc7c0/for_those_soon_coming_up_on_their_mortgage/
29. **"I am getting 6.6% for 3 year fixed. Is it a good deal?"** — r/MortgagesCanada, 2023-09-21, 24 pts, 103 comments [fetched] — variable at P-1.36 (5.84%), "these hikes... impacting my mental health"; commenters talk him out of it using the forward curve (implied 3-yr ~5.62%).
    https://old.reddit.com/r/MortgagesCanada/comments/16othpg/i_am_getting_66_for_3_year_fixed_is_it_a_good_deal/
30. The 2023 lockers now renewing: thread 9 (off 5.54%), thread 12 (off 5.34%), and **"Break current 5.09 3 year fixed term for a 3.70 5 year variable?"** (r/MortgagesCanada, 2026-03-01, 12 pts/18c [fetched]: penalty ~$6,500 + fee; replies say penalty exceeds savings and inflation could return). "Renewed Mortgage - Rates will probably Fall" (r/PFC, 2026-06-04, 233 pts/159c [fetched]) is a self-deprecating bad-timing post; top reply (131): "You could have bought at peak 2021 and went variable."
    https://old.reddit.com/r/MortgagesCanada/comments/1rhls7p/break_current_509_3_year_fixed_term_for_a_370_5/ · https://old.reddit.com/r/PersonalFinanceCanada/comments/1twxmw2/renewed_mortgage_rates_will_probably_fall/
- Notably, there is **no high-voted "I locked 5-year fixed at 5.5% in 2023 and regret it" thread**. The 2023 fixed cohort mostly took 2–3 year terms (per CMHC term data below) and is renewing in 2025–26 into lower rates, so their regret is muted and shows up as "should I break my 5.09%?" questions rather than confessionals. The regret genre is asymmetric: variable-2021 produced hundreds of posts; fixed-2023 produced almost none.

## 2. X: brokers and commentators

- **Ron Butler (@ronmortgageguy)** — the loudest broker voice; all [fetched] via fxtwitter:
  - 2024-09-18: "Stop taking 2-Yr & 3-Yr Fixed if we accept Fixed Rates bottom in 2025 — Consider Variable... lock in to Fixed next year — Consider 5-Yr Fixed if you can't handle Variable" (93 likes, 15.7k views). https://x.com/ronmortgageguy/status/1836395970734551251
  - 2025-08-15: "if some can get a 3.89% 5-Yr Fixed TAKE IT. People with Variable... will likely have 3.5% or even 3.25% next year. And they might end up with 5.50% in 2027" (120 likes). https://x.com/ronmortgageguy/status/1956350309992701960 — same argument on LinkedIn, Aug 2025, "Variable Rate Is NOT The Clear Best Choice Today... 90% of Borrowers who chose Variable in 2021 & 2022 found this out in 2023" (89 reactions). https://www.linkedin.com/posts/ron-butler-345531b_theres-some-terrible-mortgage-advice-out-activity-7362120032497098754-6Xrl
  - 2025-09-08: "Fixed Mortgage Rate Or Variable Mortgage Rate? The Debate Goes Red Hot" (447 likes, 46 replies, 67.6k views). https://x.com/ronmortgageguy/status/1965047786581504110
  - 2025-11-25: 2026 renewal shock "Should We Worry? The short answer is NO... 2021 mortgages that were 1.49% to 2.19%... will renew around 4%" (253 likes, 26.1k views). https://x.com/ronmortgageguy/status/1993329511027343523
  - 2025-12-05: "Make A Call To The Lender TODAY... 3 & 5 Year Bond Yields just BLEW UP" (364 likes, 62.4k views). https://x.com/ronmortgageguy/status/1996962070667932121
  - 2025-12-22: "borrowers choice of a Variable Rate Mortgage has risen from less than 15% in 2023 to over 40% of all new mortgages today. Is that a good idea?" (270 likes, 38.7k views). https://x.com/ronmortgageguy/status/2003171649647263802
  - 2026-03-19: "if you CAN lock in a 3 or 5 Yr Fixed Rate below 4%. I would do it" (151 likes, 23.8k views). https://x.com/ronmortgageguy/status/2034678655725527070
  - 2026-04-02: "Fixed Mortgage Rates Up 20%: DON'T PANIC... all the 3% rates are gone & every rate is in the 4% range" (516 likes, 78.5k views — his most-engaged 2026 post). https://x.com/ronmortgageguy/status/2039756699356062046
  - 2026-04-04: "It's The War In The Middle East... Don't lock in Variable at high rates. Wait & watch" (287 likes, 36k views). https://x.com/ronmortgageguy/status/2040506733781451140
  - 2026-04-24: "2026 is the highest number of Mortgage Renewals in the history of Canada, the majority... a 60% to 100% increase in Fixed Mortgage Rates (Variable Rate are lower than Fixed)" (84 likes; parent post 223 likes, 66.6k views). https://x.com/ronmortgageguy/status/2047668680893296822
  - Butler's arc, in one line: fixed under 4% is a gift, take it; once fixed is in the 4s (April 2026 onward) ride variable and wait. In CMT's April 2026 expert round-up he recommended the 5-year variable and called the war "entirely the driver of fixed mortgage rates."
- **Steve Saretsky (@SteveSaretsky)**, 2026-01-29 [fetched]: "Per Desjardins, the average 5 year fixed rate mortgage renewing this year will see a 20% payment increase. However, borrowers who renewed three year terms during the rate hike cycle will see payments FALL as much as 20%" (90 likes, 8.2k views). https://x.com/SteveSaretsky/status/2016987609281822971 · Substack "The Renewal Wall is Here" (2025-08-25): 10% of 2026 renewers face >40% increases; ~5% of fixed-payment variable borrowers have growing balances.
- **Daniel Foch (@danielfoch)**, 2026-04-26 [fetched]: "Everyone's a real estate investing genius until their mortgage comes up for renewal" (185 likes). https://x.com/danielfoch/status/2048254306889957586
- **Rob McLister (@RobMcLister)**: no 2026 X posts surfaced via search; his 2023-11-03 post "probabilities now favour variables" [snippet] and his Financial Post column of 2026-07-07, "Borrowers looking to duck rising mortgage risks are mostly grabbing three- and five-year fixed rates" [snippet via Muck Rack], bracket his position.
- **Ben Rabidoux**: nothing on fixed vs variable surfaced; his 2026 posts are about rents and appraisals.
- **Ratehub / Penelope Graham** (via CMT and Ratehub blog, not X): "the 5-year variable... offers great value... a great option for anyone looking to reduce the payment shock" (April 2026); "A common middle ground is to take out a shorter fixed rate, such as a two- or three-year term" (Globe, 2026-05-15). Jamie David (Ratehub VP) 2026-09-03: spread "quite large", 3.3% vs 4.09%.
- **Leah Zlatkin (LowestRates.ca)**, MPA 2026-06-24: "Most borrowers still prefer the certainty of fixed payments, especially after the sharp increases... in 2022 and 2023." **Victor Tran (Rates.ca)**, MPA 2026-03-02: "most households are still opting for fixed because it offers predictability." (Tran in Sept 2023: "Lots of regret in the market.")
- **David van Noppen (The Mortgage Advisors)**, CMT 2026-04-14: "For 45 of the last 50 years, variable rates were lower, so statistically there's a 90% chance of saving money" — recommends variable with a payment hedge (pay as if fixed).
- **TD's Steve Ng**, MPA 2026-04-30: "If they're looking for comfort, then fixed rates are where it's at"; 3- and 5-year terms "especially attractive."
- **nesto** (BoC page, 2026-09-02): 5-yr fixed 4.24%, 5-yr variable 3.45%, 3-yr fixed 4.29%; "The 3-year fixed's share of nesto commitments jumped from about 7.8% in February to 14.3% in April"; April 2026: 71% of applicants intended variable, 34% committed to it — "classic loss aversion."
- **Toronto Star (@TorontoStar)**, 2026-05-02 [fetched]: "Want a fixed-rate loan? Lock in now, mortgage experts say" (4.2k views). https://x.com/TorontoStar/status/2050440273126109351
- **WOWA (@WOWA_Canada)** weekly rate posts [fetched 2026-06-25]: 3-yr fixed insured 3.84%, 5-yr fixed insured 3.94%, 5-yr variable insured 3.30%, uninsurable 3.60%. https://x.com/WOWA_Canada/status/2070262610142839264
- **Canadian Mortgage Trends (@CdnMortgageNews)**, 2025-02-24 [snippet]: "@BMO says going variable could save borrowers over $6,000 on their next term."

**Broker consensus, September 2026:** there is no single answer, and the split is clean. The rate-comparison sites (Ratehub, Butler since April) say the ~75–90 bp spread makes 5-year variable the value play, with "pay it like a fixed" as the hedge. The broker-and-bank quotes (Zlatkin, Tran, TD) say most clients are choosing fixed anyway for certainty. What both camps converge on is the **short fixed term as the compromise**: the 3-year fixed is what banks are pitching, what nesto's data shows growing, and what CMHC's Q1 2026 numbers confirm as the plurality (uninsured: 49.5% fixed under 5 years, 35.5% variable, 14.9% fixed 5+ years; insured: 30.7% / 33.6% / 35.7%). The 5-year fixed is now a minority product outside insured first-time buyers. The one thing nobody recommends is breaking an existing term to switch.

## 3. Hindsight stories

**(a) Variable in 2021, rode it up**
- **CBC London, 2023-02-16** [fetched]: couple bought a $730K three-bedroom in London, Ont. in March 2022 on a variable; rate 5.6% by early 2023; payment $2,800 to $4,400/month; home value down ~$150K; "It's just been a nightmare for us." The most-cited mainstream profile of the cohort. https://www.cbc.ca/news/canada/london/ontario-couple-mortgage-nightmare-1.6750229
- **Global News, 2023-09-21** [fetched]: worked example, $500K insured from July 2021 — 1.25% variable vs 1.99% fixed; by Sept 2023 the variable borrower had paid 63% more interest, $23,579 extra. Eitan Pinsky (Pinsky Mortgages): a 2021–22 variable borrower "would not be better off even if rates go down in 2024, 2025." https://globalnews.ca/news/9976480/variable-rate-fixed-rate-mortgages-canada-interest/
- Reddit first-person: thread 19 (BMO $106K, 1.35% to 5.6%, payments stepped up in writing every hike); thread 4's top comment ("The maths was right, yours truly was wrong"; hit 6%; the convert-to-fixed option was at posted rates); thread 17 (locked 5.4% for 4 years, $600/month from savings); thread 13/14 (CIBC deferred interest and credit strikes surfacing at 2026 renewal); thread 15 (renewed 2026, "+$82 a week" — the soft landing). The dominant note in 2026 is not regret but *fatigue*: "the last 5 years on variable was a rollercoaster" (thread 4, 18 pts).
- CBC 2022-11-30 (broker Dani Hanna, London, Ont.): "is this keeping you up at night?... If the answer is 'yes,' then I strongly recommend locking into the fixed rate." Broker Mark Mitchell: "a lot of anticipatory selling because it's too high for them to lock in."

**(b) Fixed at 4.2–6.6% in 2023, watched variable fall**
- Thin. The 2023 fixed cohort skewed to 2–3-year terms (CMHC), so most are already renewing into 3.5–4.3% and their posts read as relief (thread 12: Scotia 3.76% "coming from 1.89%"; thread 9: off 5.54%, "we have been paying 5.54 for 2 years and have been comfortable"). The nearest thing to regret is the "should I break my 5.09%?" genre (thread 30), where the answer is always "penalty exceeds savings." Thread 26's 2023 comment predicted this exactly: "a year from now people will ask why people signed 5 years at 5.6%." The 5-year-fixed-at-peak regret story exists mainly in commenters' hypotheticals, not as a first-person genre.

**(c) Meme level**
- "Variable gang" as a phrase did not surface as a cohesive 2021 meme on X or Reddit; the 2021 sentiment is instead preserved in thread 27 (Aug 2021: "never met anyone upset with variable for the past 15 years") and thread 1c's "Variable Mortgage vs Fixed" (Oct 2021: 1.19% variable, older friends "worried about a repeat of the 80s," OP: "Am I being stupid?").
- The "I told you so" beat is thread 25 (Nov 2022, 580 pts: variable above fixed "1st time since 1990") and the r/canadahousing "Seen on Twitter" repost (Jan 2023, 194 pts: "Who doesn't lock in with a 1% rate, that is the real crime"). The 2026 echo is thread 16 ("True Peak FOMO bagholders... paid tuition fees"). Reddit's standing joke: "My crystal ball is in the shop" (389 pts) and PFC's self-parody about million-dollar mortgages (1,323 pts).
- Foch's "Everyone's a real estate investing genius until their mortgage comes up for renewal" (April 2026) is the broker-side version.

## 4. Recurring arguments (tally across ~30 threads, ~15 X/LinkedIn posts, ~12 articles)

| # | Argument | Count | Best-phrased instance |
|---|---|---|---|
| 1 | "Can you sleep at night" / peace of mind is worth the premium | ~14 | "going fixed so I dont have to devote mental energy to worrying about it" (603 pts, thread 1) |
| 2 | Rates are going back up (Iran war, oil, tariffs, deficits, US yields) | ~11 | Butler: variable "might end up with 5.50% in 2027"; Reddit: "Projections are for 3 consecutive rate hikes come January" |
| 3 | 3-year fixed is the sweet spot / compromise | ~11 | "is 3 the new 5?" (thread 2); nesto: 3-yr share 7.8% to 14.3% Feb–Apr 2026 |
| 4 | Variable wins historically | ~10 | van Noppen: "For 45 of the last 50 years, variable rates were lower" |
| 5 | Nobody has a crystal ball / can't time the market | ~10 | "My crystal ball is in the shop" (389 pts) |
| 6 | Fixed-payment VRM / trigger rate is a trap | ~10 | "original amortization is 360 months while my actual months remaining is 663" (thread 22) |
| 7 | IRD penalty: go variable if you might move or break | ~9 | "penalty for breaking a variable is significantly less than breaking a fixed" (103 pts) |
| 8 | Renewal shock for the 2021 cohort | ~8 | Saretsky/Desjardins: 5-yr fixed renewers +20%, 3-yr-term renewers down as much as 20% |
| 9 | The spread has to be X to justify variable | ~8 | "0.25 x 4... The maths was right, yours truly was wrong" (thread 4) |
| 10 | Brokers/banks push variable (or push 3-year) | ~7 | "every bank is trying to sell you on var right now… my instinct would be fixed" |
| 11 | Sub-4% fixed is historically great; stop anchoring to 2021 | ~5 | "fixed rates under 4% are fantastic deals... 5 years ago... is NOT normal" (295 pts) |
| 12 | The convert-to-fixed option is a sham (posted rates) | ~5 | "Option to switch to fixed is a sham" (66 pts, thread 9) |
| 13 | Take responsibility / don't blame the broker | ~4 | "you're an adult capable of making your own decision" (709 pts) |
| 14 | Stress test | ~1 | Essentially absent from the 2026 fixed-vs-variable debate |

## What the article can use

1. **The 2026 mood in one thread:** r/PFC "BoC holds at 2.25%, fixed or variable?" (March 2026, 256 pts, 345c) — top answer is peace of mind (603), second is "crystal ball is in the shop" (389); the OP's own observation that Reddit has flipped from "always variable" to fixed.
2. **The best single hindsight comment:** r/MortgagesCanada, Sept 2026 (thread 4): 1.18% variable vs 2.2% fixed in 2021, "did the maths... The maths was right, yours truly was wrong," plus the convert-to-fixed-at-posted-rates gotcha.
3. **The fixed-payment VRM long tail, still live in 2026:** r/PFC "Parents Can't Pay Off Deferred Interest" (April 2026, ~$22K owed before renewal) and the CIBC credit-strike PSA (Dec 2025). Concrete, recent, and not in the mainstream coverage.
4. **The most-upvoted regret thread of the cycle:** "No good options left" (Oct 2022, 744 pts, 642c) — "advised not to lock in and that rates couldn't possibly exceed 5%."
5. **The pre-hike consensus, dated:** r/PFC Aug 2021 "do you regret variable?" — "never met anyone who was upset with variable for the past 15 years" (41 pts) and the top reply already warning "This is a sampling problem" (229 pts).
6. **Broker split, quotable:** Butler March 2026 ("if you CAN lock in... below 4%. I would do it") vs Butler April 2026 ("Don't lock in Variable at high rates. Wait & watch"); van Noppen's "45 of the last 50 years"; Zlatkin's "most borrowers still prefer the certainty of fixed."
7. **Intent vs commitment:** nesto April 2026 — 71% wanted variable at application, 34% signed it. Pair with CMHC Q1 2026 term shares (short fixed 49.5%, variable 35.5%, 5-yr+ fixed 14.9% of uninsured).
8. **The asymmetry finding:** the variable-2021 regret genre is enormous; the fixed-2023 regret genre barely exists because that cohort took short terms and is now renewing down. That is itself an argument for the 3-year compromise the market has landed on.

Argument tally, ranked: peace of mind (14) > rates-going-back-up (11) = 3-year-fixed compromise (11) > variable-wins-historically (10) = no-crystal-ball (10) = VRM/trigger trap (10) > IRD/penalty (9) > renewal shock (8) = spread threshold (8) > brokers-push (7) > sub-4%-is-good (5) = convert-option-is-a-sham (5) > take-responsibility (4) > stress test (1).
