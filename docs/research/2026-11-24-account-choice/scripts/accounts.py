"""RRSP vs TFSA vs FHSA arithmetic. Round numbers, no real person's data.

Run: python3 accounts.py
"""

def rrsp(pretax, t_out, r, n):
    """Put `pretax` dollars of income straight into an RRSP: no tax now,
    tax at rate t_out on the way out. (The refund is just how you get there
    when the tax was already withheld; counting it again would double-count.)"""
    return pretax * (1 + r) ** n * (1 - t_out)

def tfsa(pretax, t_now, r, n):
    """The same pre-tax income, taxed now, the rest into a TFSA, tax-free out."""
    return pretax * (1 - t_now) * (1 + r) ** n

def fhsa(pretax, r, n):
    """Deductible going in, tax-free coming out for a qualifying home purchase."""
    return pretax * (1 + r) ** n

def taxable(pretax, t_now, t_gain, r, n):
    """Taxable account: taxed now, growth taxed at t_gain on the gain
    (simple: all gain realised at the end)."""
    after = pretax * (1 - t_now)
    g = after * ((1 + r) ** n - 1)
    return after + g * (1 - t_gain)

r, n = 0.05, 25
print(f"$1,000 of pre-tax income, {r:.0%} a year for {n} years (nominal, before fees)\n")

print("1. Ratio RRSP-without-refund / TFSA = (1 - t_out) / (1 - t_now)")
rates = [0.20, 0.30, 0.40, 0.50]
print("   t_now \\ t_out " + "".join(f"{x:>8.0%}" for x in rates))
for tn in rates:
    row = "".join(f"{(1-to)/(1-tn):>8.2f}" for to in rates)
    print(f"   {tn:>10.0%}    " + row)

print("\n2. Dollars at the end from the same $1,000 of pre-tax income")
cases = [
    ("same rate, 30% / 30%", 0.30, 0.30),
    ("rate falls, 40% / 25%", 0.40, 0.25),
    ("rate rises, 20% / 35%", 0.20, 0.35),
    ("OAS clawback year, 30% / 45%", 0.30, 0.45),
]
for name, tn, to in cases:
    a = rrsp(1000, to, r, n)
    b = tfsa(1000, tn, r, n)
    print(f"   {name:<32} RRSP {a:>7,.0f}   TFSA {b:>7,.0f}   RRSP-TFSA {round(a-b):>+7,}")

print("\n3. Break-even withdrawal rate: RRSP wins only if t_out < t_now")
for tn in rates:
    print(f"   t_now {tn:.0%}: RRSP ties TFSA at t_out {tn:.0%}")

print("\n4. FHSA, $1,000 of pre-tax income at 30%, qualifying home after 5 years")
t, r5 = 0.30, 0.05
print(f"   FHSA {fhsa(1000, r5, 5):,.0f}   RRSP (out at 30%) {rrsp(1000, t, r5, 5):,.0f}"
      f"   TFSA {tfsa(1000, t, r5, 5):,.0f}")
