// Fixed or variable, in hindsight — the one simulator behind the article.
//
// Plain ES module, no dependencies. Runs the same in Node (docs/…/build.mjs
// generates the article's tables and chart from it) and in the browser (the
// calculator on the page imports it). Rate inputs come from rates.json, which
// is sourced line by line in docs/research/2026-09-10-fixed-or-variable/notes/.
//
// Canadian convention throughout: rates are annual, compounded semi-annually.

export function monthlyRate(annualPct) {
  return Math.pow(1 + annualPct / 200, 1 / 6) - 1;
}

export function payment(balance, annualPct, monthsLeft) {
  const i = monthlyRate(annualPct);
  if (i === 0) return balance / monthsLeft;
  return (balance * i) / (1 - Math.pow(1 + i, -monthsLeft));
}

// "2021-09" → 2021*12+8 ; a month index that survives arithmetic.
export function monthIndex(ym) {
  const [y, m] = ym.split("-").map(Number);
  return y * 12 + (m - 1);
}
export function ymOf(idx) {
  const y = Math.floor(idx / 12), m = (idx % 12) + 1;
  return `${y}-${String(m).padStart(2, "0")}`;
}
export function labelOf(ym) {
  const [y, m] = ym.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, 1)).toLocaleDateString("en-CA", { month: "short", year: "numeric", timeZone: "UTC" });
}

// The overnight rate in force on the first of a month: the last change dated
// on or before that day.
export function overnightOn(rates, ym) {
  const first = `${ym}-01`;
  let r = rates.overnight[0][1];
  for (const [d, v] of rates.overnight) if (d <= first) r = v;
  return r;
}
export function primeOn(rates, ym) {
  return overnightOn(rates, ym) + rates.primeSpread;
}

// Contract terms on offer at a signing month: nearest listed month on or
// before it. Returns {fixed5, fixed3, varDisc, ...} plus the month used.
export function offersOn(rates, ym) {
  const keys = Object.keys(rates.offers).sort();
  let use = keys[0];
  for (const k of keys) if (k <= ym) use = k;
  return { ...rates.offers[use], asOf: use };
}

/**
 * Replay one contract.
 * @param {object} o
 * @param {number} o.principal
 * @param {number} o.amortYears
 * @param {string} o.start          "YYYY-MM"
 * @param {number} o.months         payments to replay (term, or months elapsed so far)
 * @param {(ym:string)=>number} o.rateFor   annual rate in force in a given month
 * @param {"fixed"|"arm"|"vrm"} o.mode  fixed payment & rate | variable, payment re-set on each change | variable, payment fixed at signing
 */
export function replay(o) {
  const total = o.amortYears * 12;
  const s = monthIndex(o.start);
  let bal = o.principal;
  const r0 = o.rateFor(o.start);
  let pmt = payment(bal, r0, total);
  const res = {
    mode: o.mode, firstPayment: pmt, peakPayment: pmt, minPayment: pmt,
    interest: 0, paid: 0, endBalance: 0, triggerHit: null, path: [],
  };
  let last = r0;
  for (let k = 0; k < o.months; k++) {
    const ym = ymOf(s + k);
    const r = o.rateFor(ym);
    res.path.push([ym, r]);
    if (o.mode === "arm" && r !== last) pmt = payment(bal, r, total - k);
    last = r;
    const interest = bal * monthlyRate(r);
    if (o.mode === "vrm" && interest > pmt) {
      // Past the trigger rate: the payment no longer covers interest and the
      // shortfall is added to the balance (negative amortization).
      if (!res.triggerHit) res.triggerHit = ym;
      bal += interest - pmt;
      res.interest += interest;
      res.paid += pmt;
      continue;
    }
    let principal = pmt - interest;
    if (principal > bal) { principal = bal; pmt = bal + interest; }
    bal -= principal;
    res.interest += interest;
    res.paid += pmt;
    res.peakPayment = Math.max(res.peakPayment, pmt);
    res.minPayment = Math.min(res.minPayment, pmt);
  }
  res.endBalance = bal;
  return res;
}

/**
 * The comparison the article and the calculator both show.
 * @param {object} rates      parsed rates.json
 * @param {object} o
 * @param {string} o.start    "YYYY-MM"
 * @param {3|5} o.term
 * @param {number} [o.principal=500000]
 * @param {number} [o.amortYears=25]
 * @param {string} [o.until]  last month with data, "YYYY-MM"; term is truncated to it
 * @param {{month:string, rate:number}} [o.lockIn]  optional: variable holder locks into 5y fixed
 */
export function compare(rates, o) {
  const principal = o.principal ?? 500000;
  const amortYears = o.amortYears ?? 25;
  const until = o.until ?? rates.dataThrough;
  const termMonths = o.term * 12;
  const available = monthIndex(until) - monthIndex(o.start) + 1;
  const months = Math.max(1, Math.min(termMonths, available));
  const offer = offersOn(rates, o.start);
  const fixedRate = o.term === 3 ? offer.fixed3 : offer.fixed5;
  const varFor = (ym) => primeOn(rates, ym) - offer.varDisc;
  const base = { principal, amortYears, start: o.start, months };

  const out = {
    start: o.start, term: o.term, months, complete: months === termMonths, offer,
    fixedRate, variableStart: varFor(o.start),
    fixed: replay({ ...base, mode: "fixed", rateFor: () => fixedRate }),
    arm: replay({ ...base, mode: "arm", rateFor: varFor }),
    vrm: replay({ ...base, mode: "vrm", rateFor: varFor }),
  };
  if (o.lockIn) {
    const lockFor = (ym) => (ym < o.lockIn.month ? varFor(ym) : o.lockIn.rate);
    out.locked = replay({ ...base, mode: "arm", rateFor: lockFor });
  }
  const path = out.arm.path.map((p) => p[1]);
  out.variableLow = Math.min(...path);
  out.variableHigh = Math.max(...path);
  out.variableMean = path.reduce((a, b) => a + b, 0) / path.length;
  return out;
}

// ---------------------------------------------------------------------------
// The rate-path chart, as an SVG string. Site palette; text colours flip with
// the viewer's theme via the embedded <style>.
// ---------------------------------------------------------------------------

export function chartSvg(rates, contracts, opts = {}) {
  const from = opts.from ?? "2021-01";
  const to = opts.to ?? rates.dataThrough;
  const n = monthIndex(to) - monthIndex(from) + 1;
  const months = Array.from({ length: n }, (_, k) => ymOf(monthIndex(from) + k));
  const prime = months.map((ym) => primeOn(rates, ym));
  const W = 960, H = 420, L = 64, R = 24, T = 28, B = 56;
  const top = Math.max(8, Math.ceil(Math.max(...prime, ...contracts.map((c) => c.fixedRate)) + 0.5));
  const y = (r) => T + (H - T - B) * (1 - r / top);
  const x = (k) => L + (W - L - R) * (k / (n - 1));
  const idx = (ym) => monthIndex(ym) - monthIndex(from);

  const step = (vals, k0, stroke, extra = "") => {
    const pts = [];
    vals.forEach((v, j) => {
      const k = k0 + j;
      if (j) pts.push(`${x(k).toFixed(1)},${y(vals[j - 1]).toFixed(1)}`);
      pts.push(`${x(k).toFixed(1)},${y(v).toFixed(1)}`);
    });
    return `<polyline points="${pts.join(" ")}" fill="none" stroke="${stroke}" stroke-width="3" stroke-linejoin="round"${extra}/>`;
  };

  const p = [];
  p.push(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="${opts.alt ?? "Prime rate against the fixed and variable rates available at each signing date"}" font-family="IBM Plex Sans, system-ui, sans-serif" font-size="13">`);
  p.push(`<style>.ax{stroke:var(--cg-line,#B7AE98)}.grid{stroke:var(--cg-line,#B7AE98);stroke-opacity:.6}.lbl{fill:var(--cg-text-muted,#6B6657)}.leg{fill:var(--cg-text,#1E2333)}</style>`);
  for (let r = 0; r <= top; r++) {
    p.push(`<line class="grid" x1="${L}" y1="${y(r).toFixed(1)}" x2="${W - R}" y2="${y(r).toFixed(1)}"/>`);
    p.push(`<text class="lbl" x="${L - 10}" y="${y(r).toFixed(1)}" text-anchor="end" dominant-baseline="middle">${r}%</text>`);
  }
  const yearFrom = Number(from.slice(0, 4)), yearTo = Number(to.slice(0, 4));
  for (let yr = yearFrom; yr <= yearTo; yr++) {
    const k = idx(`${yr}-01`);
    if (k < 0 || k >= n) continue;
    p.push(`<text class="lbl" x="${x(k).toFixed(1)}" y="${H - B + 22}" text-anchor="middle">${yr}</text>`);
    p.push(`<line class="ax" x1="${x(k).toFixed(1)}" y1="${H - B}" x2="${x(k).toFixed(1)}" y2="${H - B + 6}"/>`);
  }
  p.push(`<line class="ax" x1="${L}" y1="${H - B}" x2="${W - R}" y2="${H - B}"/>`);
  p.push(step(prime, 0, "var(--fov-prime, #3A4366)"));
  const kp = Math.floor(n * 0.62);
  p.push(`<text class="leg" x="${x(kp).toFixed(1)}" y="${(y(prime[kp]) - 12).toFixed(1)}" font-weight="600">Prime</text>`);

  const palette = opts.palette ?? ["var(--fov-a, #C97B1E)", "var(--fov-b, #2F7268)"];
  contracts.forEach((c, i) => {
    const k0 = idx(c.start);
    const vals = c.arm.path.map((q) => q[1]);
    const col = palette[i % palette.length];
    p.push(step(vals, k0, col));
    const kEnd = k0 + vals.length - 1;
    p.push(`<line x1="${x(k0).toFixed(1)}" y1="${y(c.fixedRate).toFixed(1)}" x2="${x(kEnd).toFixed(1)}" y2="${y(c.fixedRate).toFixed(1)}" stroke="${col}" stroke-width="3" stroke-dasharray="8 6"/>`);
    const anchorEnd = kEnd > n * 0.7;
    const lx = anchorEnd ? x(kEnd) : x(k0) + 6;
    const anchor = anchorEnd ? ` text-anchor="end"` : "";
    const fixedAbove = c.fixedRate >= vals[0];
    p.push(`<text class="leg" x="${lx.toFixed(1)}" y="${(y(c.fixedRate) + (fixedAbove ? -8 : 18)).toFixed(1)}"${anchor}>${c.fixedTermLabel ?? `${c.term}-yr`} fixed, ${labelOf(c.start)}: ${c.fixedRate.toFixed(2)}%</text>`);
    const vy = anchorEnd ? y(vals[vals.length - 1]) : y(vals[0]);
    p.push(`<text class="leg" x="${lx.toFixed(1)}" y="${(vy + (fixedAbove ? 18 : -8)).toFixed(1)}"${anchor}>Variable, ${labelOf(c.start)}</text>`);
  });
  p.push(`</svg>`);
  return p.join("\n");
}
