"""Writes website/events/monthly-budget/example.qmd from family.json.

family.json is produced by family.py from three Statistics Canada tables
(download URLs in the page's sources). Run from the repository root:
    python docs/research/2026-09-26-example-family/make_page.py
"""
import json
from pathlib import Path
here = Path(__file__).parent
d = json.loads((here / "family.json").read_text())
FORM, sav, taxes, ei, income = d["FORM"], d["savings"], d["taxes"], d["ei"], d["income"]
M = lambda x: f"${x:,.0f}" if x else "—"
total = sum(a for g in FORM.values() for _, a in g); s = sum(sav.values())
result = income - taxes - ei - total - s
NOTE = {"Municipal taxes": "property and school taxes together, as the survey counts them",
        "Car loan / Lease": "leases, plus vehicle purchases averaged over all households",
        "Other personal expenses": "charitable giving, plus everything else the survey counts with no line of its own on the form: household supplies, personal care products, household services",
        "Registered investments": "pension contributions (CPP and workplace plans), as the survey counts them"}
out = ["---", 'title: "What the output looks like"', 'subtitle: "An illustrative Toronto family of four, in the layout of an advisor\'s intake form"', "toc: false", "---", "",
 "::: {.callout-note}", "## Illustrative, not a real family",
 "Every figure is a Statistics Canada average: what an average couple with children spends, adjusted to Ontario. Your own output has your own figures, from your own statements. The sources and the caveats are at the end.", ":::", "",
 "## Summary", "", "| | Per year | Per month |", "|---|---:|---:|",
 f"| Income (average Toronto family) | {M(income)} | {M(income/12)} |",
 f"| Income taxes | {M(taxes)} | {M(taxes/12)} |",
 f"| Employment insurance premiums | {M(ei)} | {M(ei/12)} |",
 f"| Savings | {M(s)} | {M(s/12)} |",
 f"| **Total expenses** | **{M(total)}** | **{M(total/12)}** |",
 f"| **Results** | **{M(result)}** | **{M(result/12)}** |", "",
 "## Savings", "", "| | Per year | Per month |", "|---|---:|---:|"]
out += [f"| {k}{' ¹' if k in NOTE else ''} | {M(v)} | {M(v/12)} |" for k, v in sav.items()]
out += [f"| **Total savings** | **{M(s)}** | **{M(s/12)}** |", "", "## Expenses", ""]
for g, lines in FORM.items():
    gt = sum(a for _, a in lines)
    out += [f"### {g}", "", "| | Per year | Per month |", "|---|---:|---:|"]
    out += [f"| {ln}{' ¹' if ln in NOTE else ''} | {M(a)} | {M(a/12)} |" for ln, a in lines]
    out += [f"| **Total {g.lower()}** | **{M(gt)}** | **{M(gt/12)}** |", ""]
out += ["## Notes", ""] + [f"- ¹ **{k}**: {v}." for k, v in NOTE.items()] + [
 "- **Both mortgage and rent** appear because an average mixes homeowners and renters.",
 "- **Debt repayment** is empty: the survey does not count loan and credit card payments beyond the mortgage.",
 "- **Toronto:** Statistics Canada does not publish spending for Toronto on its own, so spending is adjusted to Ontario. Toronto's shelter costs are higher than Ontario's.",
 "- **Years:** spending is from 2023, income from 2024.", "",
 "## Sources", "",
 "- Statistics Canada, [Household spending by household type](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022401), table 11-10-0224-01, 2023: couples with children, Canada.",
 "- Statistics Canada, [Household spending, Canada, regions and provinces](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110022201), table 11-10-0222-01, 2023: each category scaled by Ontario ÷ Canada.",
 "- Statistics Canada, [Distribution of market, total and after-tax income by economic family type](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023701), table 11-10-0237-01, 2024: Toronto, economic families, average total income.", "",
 "How the figures were put together: [`docs/research/2026-09-26-example-family`](https://github.com/Collegica/collegica/tree/main/docs/research/2026-09-26-example-family).", "",
 "Back to [the event page](index.qmd).", ""]
(Path("website/events/monthly-budget/example.qmd")).write_text("\n".join(out))
print(f"wrote example.qmd: expenses {M(total)}, results {M(result)}")
