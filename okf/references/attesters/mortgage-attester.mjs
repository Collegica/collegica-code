#!/usr/bin/env node
// Attester for the mortgage computation (OKF §10.2, §10.5).
//
// Deterministic, no LLM. Takes a receipt produced by the executor and answers
// one question: was this result produced by running the sanctioned
// computation, against the sanctioned data, with the claimed parameters?
//
//   node mortgage-attester.mjs receipt.json
//   node run-compare.mjs --start 2021-09 --term 5 | node mortgage-attester.mjs
//
// Exit 0 on a passing verdict, 1 on a failing one, 2 on a malformed receipt.

import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const COMPUTATION = join(here, "..", "computations", "mortgage.js");
const DATA = join(here, "..", "data", "rates.json");
const REL_TOL = 1e-9;

const sha256 = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const close = (a, b) => (a === b) || (typeof a === "number" && typeof b === "number" &&
  Math.abs(a - b) <= REL_TOL * Math.max(1, Math.abs(a), Math.abs(b)));

let receipt;
try {
  const src = process.argv[2] ? readFileSync(process.argv[2], "utf8") : readFileSync(0, "utf8");
  receipt = JSON.parse(src);
} catch (e) {
  console.error("attester: could not read receipt:", e.message);
  process.exit(2);
}
for (const k of ["computation_sha256", "rates_sha256", "parameters", "result"]) {
  if (!(k in receipt)) { console.error(`attester: receipt missing ${k}`); process.exit(2); }
}

const checks = [];
const check = (name, ok, detail) => checks.push({ name, ok, ...(detail ? { detail } : {}) });

// 1. Provenance: the computation and data that ran are the bundled ones.
const compHash = sha256(COMPUTATION), dataHash = sha256(DATA);
check("computation is the sanctioned file", receipt.computation_sha256 === compHash,
  receipt.computation_sha256 === compHash ? undefined : `receipt ${receipt.computation_sha256.slice(0, 12)}… bundle ${compHash.slice(0, 12)}…`);
check("data is the sanctioned file", receipt.rates_sha256 === dataHash,
  receipt.rates_sha256 === dataHash ? undefined : `receipt ${receipt.rates_sha256.slice(0, 12)}… bundle ${dataHash.slice(0, 12)}…`);

// 2. Parameters: only declared ones, of the declared types.
const allowed = { start: "string", term: "number", principal: "number", amortYears: "number" };
const p = receipt.parameters;
const extra = Object.keys(p).filter((k) => !(k in allowed));
check("only declared parameters were bound", extra.length === 0, extra.length ? `undeclared: ${extra.join(", ")}` : undefined);
const badType = Object.entries(p).filter(([k, v]) => k in allowed && typeof v !== allowed[k]).map(([k]) => k);
check("parameters have declared types", badType.length === 0, badType.length ? `wrong type: ${badType.join(", ")}` : undefined);
check("required parameters present", typeof p.start === "string" && typeof p.term === "number");

// 3. Fidelity: re-run the computation with the receipt's own parameters and
//    compare every figure the receipt reports.
let fidelityOk = true;
if (checks.every((c) => c.ok)) {
  const { compare } = await import(COMPUTATION);
  const rates = JSON.parse(readFileSync(DATA, "utf8"));
  const c = compare(rates, p);
  const expect = {
    start: c.start, term: c.term, months: c.months, complete: c.complete, offer_as_of: c.offer.asOf,
    fixedRate: c.fixedRate, variableStart: c.variableStart,
    variableLow: c.variableLow, variableHigh: c.variableHigh, variableMean: c.variableMean,
  };
  const mism = [];
  for (const [k, v] of Object.entries(expect)) {
    if (!close(receipt.result[k], v)) mism.push(`${k}: receipt ${receipt.result[k]} vs re-run ${v}`);
  }
  for (const kind of ["fixed", "arm", "vrm"]) {
    for (const f of ["firstPayment", "peakPayment", "interest", "paid", "endBalance", "triggerHit"]) {
      const got = receipt.result[kind]?.[f], exp = c[kind][f];
      if (!close(got, exp)) mism.push(`${kind}.${f}: receipt ${got} vs re-run ${exp}`);
    }
  }
  fidelityOk = mism.length === 0;
  check("result matches an independent re-run", fidelityOk, fidelityOk ? undefined : mism.slice(0, 5).join("; "));
} else {
  check("result matches an independent re-run", false, "skipped: provenance or parameter check failed");
  fidelityOk = false;
}

const ok = checks.every((c) => c.ok);
process.stdout.write(JSON.stringify({ ok, verdict: ok ? "ATTESTED" : "REJECTED", checks }, null, 2) + "\n");
process.exit(ok ? 0 : 1);
