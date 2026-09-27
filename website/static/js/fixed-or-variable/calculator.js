// The in-page calculator: pick a signing month and a term, see what fixed and
// variable would each have cost against the Bank of Canada's actual rate path.
// Same simulator as the article's tables (mortgage.js); same data (rates.json).

import { compare, chartSvg, labelOf, monthIndex, ymOf, offersOn, primeOn } from "./mortgage.js";

const money = (x) => "$" + Math.round(x).toLocaleString("en-CA");
const pct = (x) => x.toFixed(2) + "%";

export async function mount(root) {
  const base = new URL(".", import.meta.url);
  const rates = await (await fetch(new URL("rates.json", base))).json();

  // Only months we have actually pinned rates for. Interpolating between them
  // would invent contracts nobody was offered, so the reader picks a real date
  // or nothing. Needs at least a year of rate path after it to be worth running.
  const lastStart = ymOf(monthIndex(rates.dataThrough) - 11);
  const months = Object.keys(rates.offers).sort().filter((m) => m <= lastStart);
  const initial = months.includes("2021-09") ? "2021-09" : months[0];

  root.innerHTML = `
    <form class="fov-form" aria-label="Fixed or variable, in hindsight">
      <label>Signed in
        <select name="start">${months.map((m) => `<option value="${m}"${m === initial ? " selected" : ""}>${labelOf(m)}</option>`).join("")}</select>
      </label>
      <fieldset><legend>Term</legend>
        <label><input type="radio" name="term" value="5" checked> 5 years</label>
        <label><input type="radio" name="term" value="3"> 3 years</label>
      </fieldset>
      <fieldset><legend>Variable payment</legend>
        <label><input type="radio" name="vmode" value="arm" checked> adjusts with the rate</label>
        <label><input type="radio" name="vmode" value="vrm"> fixed at signing</label>
      </fieldset>
      <label>Mortgage
        <span class="fov-unit"><span class="fov-pre">$</span><input name="principal" type="number" inputmode="numeric" min="50000" step="10000" value="500000"></span>
      </label>
      <label>Amortization
        <span class="fov-unit"><input name="amort" type="number" inputmode="numeric" min="5" max="30" step="1" value="25"> years</span>
      </label>
    </form>
    <div class="fov-out" aria-live="polite"></div>
    <figure class="fov-chart fov-live"></figure>
    <p class="fov-note"></p>`;

  const form = root.querySelector("form");
  const out = root.querySelector(".fov-out");
  const fig = root.querySelector(".fov-live");
  const note = root.querySelector(".fov-note");

  // The form, read as compare() inputs plus the variable-payment mode.
  function readInputs() {
    const f = new FormData(form);
    return {
      start: f.get("start"),
      term: Number(f.get("term")),
      vmode: f.get("vmode"),
      principal: Math.max(1000, Number(f.get("principal")) || 500000),
      amortYears: Math.min(40, Math.max(1, Number(f.get("amort")) || 25)),
    };
  }

  function render() {
    const { start, term, vmode, principal, amortYears } = readInputs();
    const c = compare(rates, { start, term, principal, amortYears });
    const v = c[vmode];
    const d = v.interest - c.fixed.interest;
    const who = d > 0 ? "Fixed" : "Variable";
    const span = c.complete ? `over the ${term}-year term` : `over the ${c.months} months so far`;
    const trig = v.triggerHit ? ` The fixed payment stopped covering the interest in ${labelOf(v.triggerHit)} — the trigger rate — and the balance grew from there.` : "";
    const balNote = Math.abs(v.endBalance - c.fixed.endBalance) > 1000
      ? ` Balance at the end: ${money(c.fixed.endBalance)} fixed, ${money(v.endBalance)} variable.` : "";

    out.innerHTML = `
      <table class="fov-table">
        <thead><tr><th scope="col"></th><th scope="col">${term}-year fixed</th><th scope="col">Variable</th></tr></thead>
        <tbody>
          <tr><th scope="row">Rate at signing</th><td>${pct(c.fixedRate)}</td><td>${pct(c.variableStart)} <span class="fov-dim">(prime − ${c.offer.varDisc.toFixed(2)})</span></td></tr>
          <tr><th scope="row">Rate ${c.complete ? "over the term" : "so far"}</th><td>${pct(c.fixedRate)}</td><td>${pct(c.variableLow)} – ${pct(c.variableHigh)} <span class="fov-dim">(avg ${pct(c.variableMean)})</span></td></tr>
          <tr><th scope="row">First payment</th><td>${money(c.fixed.firstPayment)}</td><td>${money(v.firstPayment)}</td></tr>
          <tr><th scope="row">Highest payment</th><td>${money(c.fixed.peakPayment)}</td><td>${money(v.peakPayment)}</td></tr>
          <tr><th scope="row">Interest charged</th><td>${money(c.fixed.interest)}</td><td>${money(v.interest)}</td></tr>
          <tr><th scope="row">Owing at the end</th><td>${money(c.fixed.endBalance)}</td><td>${money(v.endBalance)}</td></tr>
        </tbody>
      </table>
      <p class="fov-verdict"><strong>${who} won</strong> for a mortgage signed in ${labelOf(start)}: ${money(Math.abs(d))} less interest ${span}.${trig}${balNote}</p>`;

    const from = ymOf(Math.max(monthIndex("2021-01"), monthIndex(start) - 6));
    fig.innerHTML = chartSvg(rates, [c], {
      from,
      alt: `Prime rate from ${labelOf(from)} to ${labelOf(rates.dataThrough)}, with the ${term}-year fixed rate and the variable rate available in ${labelOf(start)}`,
    });
    note.textContent = `Rates on offer are the best broadly available insured rates archived for ${labelOf(c.offer.asOf)}; prime is the Bank of Canada rate plus ${rates.primeSpread.toFixed(2)}. An illustrative simulation, not a quote: each month is charged the rate in force on its first day, semi-annual compounding is applied to every product (some lenders compound variable mortgages monthly), and no fees, penalties or prepayments are modelled. On the fixed-payment variable, unpaid interest is left to accumulate — real lenders often step in instead. Change the mortgage and amortization to your own; the winner does not change, only the size of the gap.`;
  }

  form.addEventListener("input", render);
  form.addEventListener("submit", (e) => e.preventDefault());
  render();

  // Where the browser exposes a model context (WebMCP), let the reader's own
  // agent drive this form and read the result. Loaded only there, so no other
  // browser pays for the module; a failure here leaves the calculator as is.
  if (document.modelContext) {
    import("./tools.js")
      .then((m) => m.registerTools({ rates, months, form, readInputs, render, root }))
      .catch((err) => console.warn("WebMCP tools not registered:", err));
  }
}

// Auto-mount on the article's placeholder.
const el = document.getElementById("fov-calc");
if (el) mount(el).catch((err) => { el.textContent = "The calculator could not load: " + err.message; });
