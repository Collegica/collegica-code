// WebMCP tools for the calculator: the reader's own browser agent can drive
// the same simulator the page shows, and the page shows what the agent did.
//
// Progressive enhancement. calculator.js only imports this module where
// `document.modelContext` exists (Chrome 149+ behind the WebMCP origin trial
// or the chrome://flags/#enable-webmcp-testing flag, Edge 150+, and agents
// that speak the same API). Everywhere else the calculator is unchanged.
//
// Spec: https://github.com/webmachinelearning/webmcp — imperative API,
// `document.modelContext.registerTool()`. Tool results are plain objects;
// the same arithmetic is attested for headless agents in the OKF bundle at
// /okf/finance/computations/mortgage.md, and every result points there.

import { compare, labelOf, offersOn } from "./mortgage.js";

const ATTESTED = "https://www.collegica.org/okf/finance/computations/mortgage.md";
const round = (x) => Math.round(x);
const pct = (x) => Math.round(x * 100) / 100;

// The structured result an agent gets back. Same numbers as the table the
// reader sees; `note` carries the same caveats the page prints.
export function summarize(rates, o) {
  const vmode = o.vmode;
  const c = compare(rates, o);
  const v = c[vmode];
  const d = v.interest - c.fixed.interest;
  return {
    inputs: {
      start: c.start,
      startLabel: labelOf(c.start),
      term: c.term,
      variablePayment: vmode === "vrm" ? "fixed" : "adjusts",
      principal: o.principal,
      amortizationYears: o.amortYears,
    },
    monthsReplayed: c.months,
    termComplete: c.complete,
    dataThrough: rates.dataThrough,
    offer: { asOf: c.offer.asOf, source: c.offer.src },
    fixed: {
      rate: pct(c.fixedRate),
      firstPayment: round(c.fixed.firstPayment),
      peakPayment: round(c.fixed.peakPayment),
      interest: round(c.fixed.interest),
      endBalance: round(c.fixed.endBalance),
    },
    variable: {
      rateAtSigning: pct(c.variableStart),
      discountOffPrime: c.offer.varDisc,
      rateLow: pct(c.variableLow),
      rateHigh: pct(c.variableHigh),
      rateMean: pct(c.variableMean),
      firstPayment: round(v.firstPayment),
      peakPayment: round(v.peakPayment),
      interest: round(v.interest),
      endBalance: round(v.endBalance),
      triggerRateHit: v.triggerHit ? labelOf(v.triggerHit) : null,
    },
    verdict: {
      winner: d > 0 ? "fixed" : "variable",
      interestSaved: round(Math.abs(d)),
      over: c.complete ? `the ${c.term}-year term` : `the ${c.months} months so far`,
    },
    note:
      "An illustrative simulation, not a quote: best broadly available insured rates archived for the signing month, " +
      "prime = Bank of Canada rate + " + rates.primeSpread.toFixed(2) + ", semi-annual compounding on every product, " +
      "no fees, penalties or prepayments. Changing the mortgage size or amortization changes the size of the gap, not the winner.",
    attestedComputation: ATTESTED,
  };
}

/**
 * Register the calculator's tools. Returns true when registered, false when
 * the browser has no model context (nothing happens on the page either way).
 * @param {object} ctx
 * @param {object} ctx.rates       the loaded rates.json
 * @param {string[]} ctx.months    signing months the calculator offers
 * @param {HTMLFormElement} ctx.form
 * @param {() => object} ctx.readInputs   current form values as compare() inputs plus vmode
 * @param {() => void} ctx.render  redraw the table and chart from the form
 * @param {HTMLElement} ctx.root   the calculator, scrolled into view after a tool runs it
 */
export async function registerTools({ rates, months, form, readInputs, render, root }) {
  const mc = document.modelContext;
  if (!mc || typeof mc.registerTool !== "function") return false;

  await mc.registerTool({
    name: "list_signing_months",
    description:
      "List the mortgage signing months this calculator can replay, with the fixed and variable rates on offer in each. " +
      "Only months with archived rate offers are valid inputs to compare_mortgage.",
    inputSchema: { type: "object", properties: {} },
    annotations: { readOnlyHint: true },
    execute() {
      return {
        dataThrough: rates.dataThrough,
        terms: [3, 5],
        months: months.map((m) => {
          const o = offersOn(rates, m);
          return { month: m, label: labelOf(m), fixed5: o.fixed5, fixed3: o.fixed3, variableDiscountOffPrime: o.varDisc };
        }),
      };
    },
  });

  await mc.registerTool({
    name: "compare_mortgage",
    description:
      "Replay a Canadian mortgage signed in a given month as both a fixed-rate and a variable-rate contract against the " +
      "Bank of Canada's actual rate path, and show the comparison on the page. Returns rates, payments, interest charged, " +
      "balance owing and which product won. Call list_signing_months for the valid months.",
    inputSchema: {
      type: "object",
      properties: {
        start: { type: "string", enum: months, description: "Signing month, YYYY-MM. Must be one of the archived months." },
        term: { type: "number", enum: [3, 5], description: "Term in years." },
        variablePayment: {
          type: "string",
          enum: ["adjusts", "fixed"],
          description: "How the variable-rate payment behaves: 'adjusts' re-sets the payment when the rate changes (adjustable-rate); 'fixed' keeps the payment set at signing (variable-rate with a trigger rate).",
        },
        principal: { type: "number", minimum: 1000, description: "Mortgage amount in CAD. Default 500000." },
        amortizationYears: { type: "integer", minimum: 1, maximum: 40, description: "Amortization in years. Default 25." },
      },
      required: ["start", "term"],
    },
    annotations: { readOnlyHint: false, consequentialHint: false },
    execute({ start, term, variablePayment = "adjusts", principal = 500000, amortizationYears = 25 }) {
      // Return errors as results rather than throwing: the browser reports a
      // thrown error to the agent only as "the invocation failed" and keeps the
      // message in the console, so the agent would never see how to recover.
      if (!months.includes(start)) return { error: `No archived rates for ${start}. Valid months: ${months.join(", ")}.` };
      if (term !== 3 && term !== 5) return { error: "term must be 3 or 5." };
      if (!(principal >= 1000)) return { error: "principal must be at least 1000." };
      if (!(amortizationYears >= 1 && amortizationYears <= 40)) return { error: "amortizationYears must be between 1 and 40." };
      const vmode = variablePayment === "fixed" ? "vrm" : "arm";

      form.elements.start.value = start;
      form.elements.term.value = String(term);
      form.elements.vmode.value = vmode;
      form.elements.principal.value = String(Math.round(principal));
      form.elements.amort.value = String(Math.round(amortizationYears));
      render();
      root.scrollIntoView?.({ behavior: "smooth", block: "start" });
      return summarize(rates, readInputs());
    },
  });

  await mc.registerTool({
    name: "read_comparison",
    description: "Return the comparison currently shown on the page, for whatever signing month, term and amounts the reader has set.",
    inputSchema: { type: "object", properties: {} },
    annotations: { readOnlyHint: true },
    execute() {
      return summarize(rates, readInputs());
    },
  });

  return true;
}
