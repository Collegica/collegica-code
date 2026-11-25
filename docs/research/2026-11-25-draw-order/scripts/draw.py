"""Which account to draw from, in which year: a small decumulation model.

Round numbers, real (inflation-adjusted) dollars, federal brackets only.
Run: python3 draw.py

Model, stated so it can be checked:
- Age 65 to 94 (30 years of withdrawals). CPP $10,300 and OAS $9,150 a year from
  65, in today's dollars (Canada.ca 2026: average CPP $858.34 a month, full OAS
  $762.50 a month).
- Tax: 2026 federal brackets only (Canada.ca), no provincial tax, no credits.
  Credits are fixed amounts that every strategy uses up, so they cancel in a
  comparison. OAS recovery tax: 15% of net income above $93,454 (the 2025
  figure on Canada.ca), capped at the OAS received. Brackets and thresholds are
  held constant in real terms (they are indexed).
- RRIF opened at 70; minimum withdrawals from 71 at the CRA 'all other RRIFs'
  prescribed factors; before 71 there is no minimum.
- Real return 2% a year in RRSP/RRIF and TFSA. A non-registered account earns
  the same 2% but 20% of the return is taxed each year (1.6% after tax).
- TFSA contributions capped at $7,000 a year (2026 limit, held real); any
  surplus withdrawal beyond that goes to the non-registered account.
- Result: the largest constant after-tax spending (real) that lasts to 95,
  found by bisection. Higher is better.
"""
BRACKETS = [(58523, .14), (117045, .205), (181440, .26), (258482, .29), (1e18, .33)]
CPP, OAS_AMT = 10300.0, 9150.0
CLAW_START = 93454.0
RRIF = {71:.0528,72:.0540,73:.0553,74:.0567,75:.0582,76:.0598,77:.0617,78:.0636,
        79:.0658,80:.0682,81:.0708,82:.0738,83:.0771,84:.0808,85:.0851,86:.0899,
        87:.0955,88:.1021,89:.1099,90:.1192,91:.1306,92:.1449,93:.1634,94:.1879}
TFSA_CAP = 7000.0

def tax(income):
    t, lo = 0.0, 0.0
    for hi, r in BRACKETS:
        if income > lo:
            t += (min(income, hi) - lo) * r
        lo = hi
    return t

def total_tax(income):
    """Income tax plus OAS recovery tax (income includes OAS)."""
    claw = min(OAS_AMT, max(0.0, 0.15 * (income - CLAW_START)))
    return tax(income) + claw

def net(w, age):
    inc = CPP + (OAS_AMT if age >= 65 else 0.0) + w
    return inc - total_tax(inc)

def solve_w_for_net(target, age, cap):
    """Smallest RRSP withdrawal w (<= cap) giving after-tax income >= target."""
    if net(cap, age) < target:
        return cap
    lo, hi = 0.0, cap
    for _ in range(60):
        mid = (lo + hi) / 2
        if net(mid, age) >= target: hi = mid
        else: lo = mid
    return hi

def simulate(S, strategy, rrsp, tfsa, nonreg=0.0, r=0.02, T=None, detail=False, end=95, parts=False):
    taxes = 0.0
    claw_years = 0
    for age in range(65, end):
        rmin = RRIF.get(age, 0.0) * rrsp if age >= 71 else 0.0
        if strategy == "last":
            w = rmin
        elif strategy == "first":
            w = solve_w_for_net(S, age, rrsp)
        else:  # meltdown to taxable income T
            fixed = CPP + OAS_AMT
            w = max(rmin, T - fixed)
        w = min(max(w, rmin), rrsp)
        n = net(w, age)
        rrsp -= w
        inc = CPP + OAS_AMT + w
        taxes += total_tax(inc)
        if inc > CLAW_START: claw_years += 1
        short = S - n
        if short > 0:
            # draw non-registered first, then TFSA, then more RRSP
            drawn = 0.0
            take = min(short, nonreg); nonreg -= take; short -= take; drawn += take
            take = min(short, tfsa); tfsa -= take; short -= take; drawn += take
            if short > 1e-6:
                extra = solve_w_for_net(n + short, age, rrsp + w) - w  # more RRSP
                extra = min(max(extra, 0.0), rrsp)
                n2 = net(w + extra, age)
                taxes += total_tax(CPP + OAS_AMT + w + extra) - total_tax(inc)
                rrsp -= extra
                if S - n2 - drawn > 1.0:
                    return (None, taxes, claw_years) if detail else None
        elif short < 0:
            surplus = -short
            put = min(surplus, TFSA_CAP); tfsa += put; surplus -= put
            nonreg += surplus
        rrsp *= 1 + r
        tfsa *= 1 + r
        nonreg *= 1 + r * 0.8
    if parts:
        return rrsp, tfsa, nonreg
    left = rrsp + tfsa + nonreg
    return (left, taxes, claw_years) if detail else left

def max_spend(strategy, rrsp, tfsa, T=None, r=0.02):
    lo, hi = 10000.0, 200000.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if simulate(mid, strategy, rrsp, tfsa, T=T, r=r) is None:
            hi = mid
        else:
            lo = mid
    left, taxes, cy = simulate(lo, strategy, rrsp, tfsa, T=T, r=r, detail=True)
    return lo, taxes, cy

for name, rrsp, tfsa in (("Household A: RRSP 600,000, TFSA 100,000", 600000, 100000),
                         ("Household B: RRSP 1,200,000, TFSA 100,000", 1200000, 100000)):
    print(name)
    print(f"   {'strategy':<40}{'spend/yr':>10}{'tax 65-94':>12}{'clawback yrs':>14}")
    rows = [("Registered last (RRIF minimums only)", "last", None),
            ("Registered first (RRSP before TFSA)", "first", None),
            ("Meltdown, fill to 58,523 taxable", "melt", 58523.0),
            ("Meltdown, fill to 90,000 taxable", "melt", 90000.0),
            ("Meltdown, fill to 117,045 taxable", "melt", 117045.0)]
    for label, s, T in rows:
        sp, tx, cy = max_spend(s, rrsp, tfsa, T)
        print(f"   {label:<40}{sp:>10,.0f}{tx:>12,.0f}{cy:>14}")
    print()

def estate(S, strategy, rrsp, tfsa, T, death):
    """After-tax estate if death is at the start of age `death`: TFSA and
    non-registered pass untaxed (gains ignored); the RRSP/RRIF balance is added
    to that year's income and taxed at the federal brackets (no spouse rollover)."""
    out = simulate(S, strategy, rrsp, tfsa, T=T, end=death, parts=True)
    if out is None:
        return None
    r_, t_, n_ = out
    base = CPP + OAS_AMT
    extra_tax = total_tax(base + r_) - total_tax(base)
    return t_ + n_ + r_ - extra_tax

print("After-tax estate by age at death, spending held at a sustainable level")
print("(RRSP/RRIF balance taxed in the year of death, federal brackets, no spouse rollover)")
for name, rrsp, tfsa, S in (("Household A at 40,000 a year", 600000, 100000, 40000),
                            ("Household B at 60,000 a year", 1200000, 100000, 60000)):
    print(name)
    print(f"   {'strategy':<40}{'dies at 75':>12}{'dies at 85':>12}{'lives to 95':>13}")
    for label, st, T in (("Registered last (RRIF minimums only)", "last", None),
                         ("Registered first (RRSP before TFSA)", "first", None),
                         ("Meltdown, fill to 58,523 taxable", "melt", 58523.0)):
        vals = []
        for d in (75, 85, 95):
            v = estate(S, st, rrsp, tfsa, T, d)
            vals.append("fails" if v is None else f"{v:,.0f}")
        print(f"   {label:<40}{vals[0]:>12}{vals[1]:>12}{vals[2]:>13}")
    print()

print("Sensitivity: Household A, real return 0% and 4%")
for r in (0.0, 0.04):
    print(f"   real return {r:.0%}")
    for label, s, T in (("Registered last", "last", None), ("Registered first", "first", None),
                        ("Meltdown to 58,523", "melt", 58523.0), ("Meltdown to 90,000", "melt", 90000.0)):
        sp, tx, cy = max_spend(s, 600000, 100000, T, r=r)
        print(f"      {label:<24}{sp:>10,.0f}")
