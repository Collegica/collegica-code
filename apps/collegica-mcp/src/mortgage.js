// The calculator half. Same simulator as the article and the WebMCP tools:
// compare() from the site's own mortgage.js, results shaped by the site's own
// summarize(). Rates are fetched live so a data update needs no redeploy; the
// copy bundled at deploy time is the fallback.

import { compare, monthIndex, ymOf, labelOf, offersOn } from "../../../website/static/js/fixed-or-variable/mortgage.js";
import { summarize } from "../../../website/static/js/fixed-or-variable/tools.js";
import bundledRates from "../../../website/static/js/fixed-or-variable/rates.json" with { type: "json" };

let cache = { at: 0, rates: null, source: "bundled" };

export async function loadRates({ base, fetchFn = fetch, now = Date.now() }) {
  if (cache.rates && now - cache.at < 3600_000) return cache;
  try {
    const res = await fetchFn(`${base}/references/data/rates.json`, { cf: { cacheTtl: 3600 } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    cache = { at: now, rates: await res.json(), source: "live" };
  } catch {
    cache = { at: now, rates: bundledRates, source: "bundled" };
  }
  return cache;
}
export const resetRatesCache = () => { cache = { at: 0, rates: null, source: "bundled" }; };

/** Signing months the calculator accepts: archived offers with at least a year of rate path after them. */
export function signingMonths(rates) {
  const lastStart = ymOf(monthIndex(rates.dataThrough) - 11);
  return Object.keys(rates.offers).sort().filter((m) => m <= lastStart);
}

export function listMonths(rates) {
  return {
    dataThrough: rates.dataThrough,
    terms: [3, 5],
    months: signingMonths(rates).map((m) => {
      const o = offersOn(rates, m);
      return { month: m, label: labelOf(m), fixed5: o.fixed5, fixed3: o.fixed3, variableDiscountOffPrime: o.varDisc };
    }),
  };
}

export function compareMortgage(rates, { start, term, variablePayment = "adjusts", principal = 500000, amortizationYears = 25 }) {
  const months = signingMonths(rates);
  if (!months.includes(start)) return { error: `No archived rates for ${start}. Valid months: ${months.join(", ")}.` };
  if (term !== 3 && term !== 5) return { error: "term must be 3 or 5." };
  if (!(principal >= 1000)) return { error: "principal must be at least 1000." };
  if (!(amortizationYears >= 1 && amortizationYears <= 40)) return { error: "amortizationYears must be between 1 and 40." };
  const vmode = variablePayment === "fixed" ? "vrm" : "arm";
  return summarize(rates, { start, term, vmode, principal, amortYears: amortizationYears });
}
