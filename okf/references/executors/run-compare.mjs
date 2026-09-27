#!/usr/bin/env node
// Executor for the mortgage computation (OKF §10.2).
//
// Runs the sanctioned computation with the parameters given on the command
// line and prints a receipt: enough for an attester to confirm that exactly
// this computation ran against exactly this data with exactly these inputs.
//
//   node run-compare.mjs --start 2021-09 --term 5 [--principal 500000] [--amort 25]
//
// The agent supplies parameter values only. It does not edit the computation.

import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const COMPUTATION = join(here, "..", "computations", "mortgage.js");
const DATA = join(here, "..", "data", "rates.json");

const sha256 = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");

function args(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) out[argv[i].slice(2)] = argv[i + 1], i++;
  }
  return out;
}

const a = args(process.argv.slice(2));
if (!a.start || !a.term) {
  console.error("usage: node run-compare.mjs --start YYYY-MM --term 3|5 [--principal N] [--amort N]");
  process.exit(2);
}
const parameters = {
  start: a.start,
  term: Number(a.term),
  ...(a.principal ? { principal: Number(a.principal) } : {}),
  ...(a.amort ? { amortYears: Number(a.amort) } : {}),
};

const { compare } = await import(COMPUTATION);
const rates = JSON.parse(readFileSync(DATA, "utf8"));
const c = compare(rates, parameters);

// Keep the receipt small: drop the month-by-month paths, keep every figure an
// article or an agent would actually quote.
const trim = (r) => ({
  firstPayment: r.firstPayment, peakPayment: r.peakPayment, interest: r.interest,
  paid: r.paid, endBalance: r.endBalance, triggerHit: r.triggerHit,
});
const receipt = {
  computation: "references/computations/mortgage.js",
  computation_sha256: sha256(COMPUTATION),
  rates_sha256: sha256(DATA),
  parameters,
  result: {
    start: c.start, term: c.term, months: c.months, complete: c.complete,
    offer_as_of: c.offer.asOf, fixedRate: c.fixedRate, variableStart: c.variableStart,
    variableLow: c.variableLow, variableHigh: c.variableHigh, variableMean: c.variableMean,
    fixed: trim(c.fixed), arm: trim(c.arm), vrm: trim(c.vrm),
  },
  ran_at: new Date().toISOString(),
};
process.stdout.write(JSON.stringify(receipt, null, 2) + "\n");
