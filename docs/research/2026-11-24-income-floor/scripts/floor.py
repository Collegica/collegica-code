"""Guaranteed income floor arithmetic. Round numbers; official 2026 amounts.

Run: python3 floor.py
Sources (Canada.ca, read 2026-11-24): CPP maximum at 65 $1,507.65/month
(January 2026), average at 65 $858.34/month (July 2026); CPP -0.6%/month before
65 (max -36% at 60), +0.7%/month after 65 (max +42% at 70); OAS maximum
$762.50/month at 65-74 (October-December 2026), +0.6%/month deferred up to +36%.
"""
CPP_MAX, CPP_AVG, OAS = 1507.65, 858.34, 762.50

print("1. Public floor at 65, per month and per year")
for name, cpp in (("average CPP + full OAS", CPP_AVG), ("maximum CPP + full OAS", CPP_MAX)):
    m = cpp + OAS
    print(f"   {name:<24} {m:>8,.2f}/month  {12*m:>9,.0f}/year")

print("\n2. CPP by start age (monthly)")
for label, adj in (("60", -0.36), ("65", 0.0), ("70", 0.42)):
    print(f"   age {label}: average {CPP_AVG*(1+adj):>8,.2f}   maximum {CPP_MAX*(1+adj):>8,.2f}")
print(f"   OAS at 70 (full pension, +36%): {OAS*1.36:,.2f}  (Canada.ca shows 1,037.00)")

print("\n3. Break-even age for waiting from 65 to 70 on CPP (no tax, indexed)")
def breakeven(rate_real, boost=0.42, wait_years=5):
    """Age at which cumulative dollars (valued at 65 at a real rate) from the
    bigger pension overtake the smaller one that started 5 years earlier."""
    r = (1 + rate_real) ** (1 / 12) - 1
    pv = lambda start_m, amt, end_m: sum(amt / (1 + r) ** m for m in range(start_m, end_m))
    for end in range(61, 40 * 12):
        early = pv(0, 1.0, end)
        late = pv(wait_years * 12, 1 + boost, end)
        if late >= early:
            return 65 + end / 12
    return None
for rr in (0.0, 0.02, 0.04):
    print(f"   real return {rr:.0%}: break-even at age {breakeven(rr):.1f}")

print("\n4. What a dollar of floor replaces (25x rule, 4% withdrawal)")
need = 48000
for floor in (0, 19450, 27242):
    gap = max(need - floor, 0)
    print(f"   recurring need {need:,}, floor {floor:>6,}: gap {gap:>6,}, pot at 25x {25*gap:>9,}")

print("\n5. A hypothetical annuity (NOT a quote): payout rate p => premium per $1,000/yr = 1000/p")
for p in (0.05, 0.06, 0.07):
    print(f"   payout {p:.0%}: ${1000/p:>8,.0f} per $1,000/yr   (4% rule: $25,000)")

print("\n6. A non-indexed income loses buying power: value of $1,000 after n years at 2% inflation")
for n in (10, 20, 25, 30):
    print(f"   {n} years: ${1000/1.02**n:,.0f}")
