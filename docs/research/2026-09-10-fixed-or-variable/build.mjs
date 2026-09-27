#!/usr/bin/env node
// Generates the article's hindsight tables and rate-path chart from the same
// module the in-page calculator uses, so the two can never disagree.
//
//   node build.mjs           → tables (markdown) on stdout
//   node build.mjs --svg     → also writes ../../../website/static/img/finance/rate-path.svg

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..", "..", "..");
const lib = join(root, "website", "static", "js", "fixed-or-variable");
const { compare, replay, chartSvg, labelOf } = await import(join(lib, "mortgage.js"));
const rates = JSON.parse(readFileSync(join(lib, "rates.json"), "utf8"));

const money = (x) => "$" + Math.round(x).toLocaleString("en-CA");
const signed = (x) => (x > 0 ? "+" : "−") + money(Math.abs(x));

function table(title, c) {
  const rows = [
    [`5-year fixed at ${c.fixedRate.toFixed(2)}%`, c.fixed],
    [`Variable, adjustable payment (prime − ${c.offer.varDisc.toFixed(2)})`, c.arm],
    [`Variable, fixed payment (prime − ${c.offer.varDisc.toFixed(2)})`, c.vrm],
  ];
  if (c.term === 3) rows.splice(1, 0, [`3-year fixed at ${c.offer.fixed3.toFixed(2)}%`, c.fixed3]);
  if (c.locked) rows.push([`Variable, locked into 5-year fixed at ${c.lockIn.rate.toFixed(2)}% in ${labelOf(c.lockIn.month)}`, c.locked]);
  const base = c.term === 3 ? c.fixed5 : c.fixed;
  const out = [
    `### ${title}`, "",
    "| Contract | First payment | Highest payment | Interest charged | Owing at end of term | vs. 5-year fixed |",
    "|---|---:|---:|---:|---:|---:|",
  ];
  for (const [label, r] of rows) {
    const trig = r.triggerHit ? ` — trigger rate hit ${labelOf(r.triggerHit)}` : "";
    const d = r === base ? "—" : signed(r.interest - base.interest);
    out.push(`| ${label}${trig} | ${money(r.firstPayment)} | ${money(r.peakPayment)} | ${money(r.interest)} | ${money(r.endBalance)} | ${d} |`);
  }
  out.push("", `Variable rate over the term: low ${c.variableLow.toFixed(2)}%, high ${c.variableHigh.toFixed(2)}%, average ${c.variableMean.toFixed(2)}%.`);
  return out.join("\n");
}

// 2021: five-year term, plus any mid-term lock-ins we have sourced conversion
// rates for (rates.json "conversions"; omitted until those are pinned).
const a = compare(rates, { start: "2021-09", term: 5 });
const locks = (rates.conversions ?? []).map((k) =>
  ({ ...k, run: compare(rates, { start: "2021-09", term: 5, lockIn: { month: k.month, rate: k.rate } }) }));

// 2023: three-year term; 5-year fixed shown as the baseline people were choosing.
const b3 = compare(rates, { start: "2023-09", term: 3 });
const b5 = compare(rates, { start: "2023-09", term: 5 });
b3.fixed3 = b3.fixed; b3.fixed5 = b5.fixed; b3.fixedRate = b5.fixedRate;
b3.fixed = b5.fixed; b3.fixedTermLabel = "5-yr";

// today's offer, for the "how to decide now" section
const now = compare(rates, { start: rates.asOf, term: 5, until: rates.asOf });

console.log(`Principal $500,000, 25-year amortization, semi-annual compounding. Data through ${labelOf(rates.dataThrough)}.\n`);
console.log(table(`Signed ${labelOf("2021-09")}, five-year term (${a.months} payments)`, a));
if (locks.length) {
  console.log("\nLocked in mid-term (started variable, converted to a fixed rate):");
  for (const k of locks) {
    console.log(`- ${labelOf(k.month)} at ${k.rate.toFixed(2)}%: interest ${money(k.run.locked.interest)}, owing ${money(k.run.locked.endBalance)}, ${signed(k.run.locked.interest - a.fixed.interest)} vs staying fixed — ${k.src}`);
  }
} else {
  console.log("\n(no mid-term conversion rates pinned yet — see notes/historical-rates.md 3F)");
}
console.log("");
console.log(table(`Signed ${labelOf("2023-09")}, three-year term (${b3.months} payments)`, b3));
console.log("");
// The renewal comparison in "The row that is not finished": the Sept-2023
// three-year holder renews now at various rates; the five-year holder serves
// out 5.24% to Sept 2028. Both continue on the balance their own path reached.
{
  const c3 = compare(rates, { start: "2023-09", term: 3 });
  const c5 = compare(rates, { start: "2023-09", term: 5 });
  const amortLeft = (25 * 12 - 36) / 12;
  const tail = (bal, rate) => replay({
    principal: bal, amortYears: amortLeft, start: rates.asOf, months: 24,
    mode: "fixed", rateFor: () => rate,
  });
  const base = c5.fixed.interest + tail(c5.fixed.endBalance, c5.fixedRate).interest;
  console.log(`\nRenewal comparison — five-year total interest, both paths to Sep 2028`);
  console.log(`  stay in the ${c5.fixedRate.toFixed(2)}% five-year: ${money(base)}`);
  for (const r of [3.30, 3.94, 4.00, 4.09, 4.50]) {
    const t = c3.fixed.interest + tail(c3.fixed.endBalance, r).interest;
    const d = base - t;
    console.log(`  renew the three-year at ${r.toFixed(2)}%: ${money(t)} — ${d >= 0 ? "better" : "worse"} by ${money(Math.abs(d))}`);
  }
}

console.log(`Today (${labelOf(rates.asOf)}): 5y fixed ${now.fixedRate.toFixed(2)}%, variable ${now.variableStart.toFixed(2)}% (prime − ${now.offer.varDisc.toFixed(2)}), spread ${(now.fixedRate - now.variableStart).toFixed(2)} pts.`);

if (process.argv.includes("--svg")) {
  const dir = join(root, "website", "static", "img", "finance");
  mkdirSync(dir, { recursive: true });
  const svg = chartSvg(rates, [a, b3], {
    alt: "Bank of Canada prime rate, 2021 to 2026, against the five-year fixed rate and the variable rate available in September 2021 and September 2023",
  });
  writeFileSync(join(dir, "rate-path.svg"), svg);
  // Inlined into the article (so the page's theme tokens style it) via an include.
  const frag = join(root, "website", "finance", "fixed-or-variable", "_rate-path.md");
  mkdirSync(dirname(frag), { recursive: true });
  writeFileSync(frag, "```{=html}\n<figure class=\"fov-chart\">\n" + svg + "\n</figure>\n```\n");
  console.log(`\nwrote ${join(dir, "rate-path.svg")} and ${frag}`);
}
