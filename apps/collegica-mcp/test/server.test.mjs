import test from "node:test";
import assert from "node:assert/strict";
import { serve, call, BASE } from "./helpers.mjs";
import { trustTier } from "../src/okf.js";

test("trust tiers follow llms.txt", () => {
  assert.equal(trustTier(undefined), "unverified");
  assert.equal(trustTier([]), "unverified");
  assert.equal(trustTier([{ by: "claude/opus-5" }]), "machine-confirmed");
  assert.equal(trustTier([{ by: "process:bankofcanada" }]), "machine-confirmed");
  assert.equal(trustTier([{ by: "claude/opus-5" }, { by: "human:behzad" }]), "human-reviewed");
  assert.equal(trustTier({ by: "human:behzad", at: "2026-09-12T23:41:00Z" }), "human-reviewed"); // OKF allows a single entry
});

test("lists exactly the four read-only tools", async () => {
  const s = await serve();
  try {
    const { tools } = await s.client.listTools();
    assert.deepEqual(tools.map((t) => t.name).sort(), ["compare_mortgage", "list_signing_months", "read_concept", "search_concepts"]);
    for (const t of tools) assert.equal(t.annotations.readOnlyHint, true, t.name);
  } finally { await s.close(); }
});

test("search finds the mortgage article with its trust tier, and flags staleness by the clock", async () => {
  const fresh = await serve({ now: () => new Date("2026-09-24T00:00:00Z") });
  try {
    const { data } = await call(fresh.client, "search_concepts", { query: "mortgage fixed variable" });
    const top = data.results[0];
    assert.equal(top.path, "finance/fixed-or-variable.md");
    assert.equal(top.trust, "human-reviewed");
    assert.equal(top.stale, false);
  } finally { await fresh.close(); }
  const late = await serve({ now: () => new Date("2026-11-01T00:00:00Z") });
  try {
    const { data } = await call(late.client, "search_concepts", { query: "fixed or variable", type: "Article" });
    assert.equal(data.results[0].stale, true);
    assert.match(data.results[0].warnings.join(" "), /stale/);
  } finally { await late.close(); }
});

test("search filters by type and tag, and an empty query lists", async () => {
  const s = await serve();
  try {
    const all = (await call(s.client, "search_concepts", { limit: 50 })).data;
    assert.ok(all.total >= 80);
    const notes = (await call(s.client, "search_concepts", { type: "Research Note", limit: 50 })).data;
    assert.ok(notes.results.every((r) => r.type === "Research Note"));
    const none = (await call(s.client, "search_concepts", { query: "zzzznothing" })).data;
    assert.equal(none.returned, 0);
  } finally { await s.close(); }
});

test("read_concept returns text with provenance, and pages long concepts", async () => {
  const s = await serve();
  try {
    const { data } = await call(s.client, "read_concept", { path: "finance/fixed-or-variable.md", max_chars: 1000 });
    assert.equal(data.provenance.trust, "human-reviewed");
    assert.equal(data.truncated, true);
    assert.equal(data.text.length, 1000);
    const next = (await call(s.client, "read_concept", { path: "finance/fixed-or-variable.md", offset: data.next_offset, max_chars: 1000 })).data;
    assert.equal(next.offset, 1000);
    assert.notEqual(next.text, data.text);
  } finally { await s.close(); }
});

test("read_concept refuses anything not in the index", async () => {
  const s = await serve();
  try {
    for (const path of ["../secret.md", "/etc/passwd", "finance/../../x.md", "nope.md", "https://evil.test/x.md", ""]) {
      const r = await call(s.client, "read_concept", { path });
      assert.equal(r.isError, true, path);
      assert.match(r.data.error, /search_concepts/);
    }
  } finally { await s.close(); }
});

test("compare_mortgage reproduces the calculator's number", async () => {
  const s = await serve();
  try {
    const months = (await call(s.client, "list_signing_months")).data;
    assert.equal(months.months.length, 12);
    assert.equal(months.ratesSource, "live");
    const { data } = await call(s.client, "compare_mortgage", { start: "2022-06", term: 3, variablePayment: "fixed", principal: 400000, amortizationYears: 30 });
    assert.equal(data.verdict.winner, "fixed");
    assert.equal(data.verdict.interestSaved, 11443); // the same figure the page and the WebMCP tool showed
    assert.equal(data.variable.triggerRateHit, "Nov 2022");
  } finally { await s.close(); }
});

test("compare_mortgage errors carry the recovery hint and are flagged isError", async () => {
  const s = await serve();
  try {
    const bad = await call(s.client, "compare_mortgage", { start: "1999-01", term: 5 });
    assert.equal(bad.isError, true);
    assert.match(bad.data.error, /Valid months: 2021-06/);
    const badTerm = await s.client.callTool({ name: "compare_mortgage", arguments: { start: "2022-06", term: 4 } });
    assert.equal(badTerm.isError, true); // rejected by the input schema
  } finally { await s.close(); }
});

test("falls back to the bundled rates when the live fetch fails", async () => {
  const s = await serve({ fetchFn: async () => new Response("down", { status: 503 }) });
  try {
    const { data } = await call(s.client, "compare_mortgage", { start: "2021-09", term: 5 });
    assert.equal(data.ratesSource, "bundled");
    assert.equal(data.verdict.winner, "fixed");
  } finally { await s.close(); }
});

test("root describes the endpoint, unknown paths 404, preflight is allowed", async () => {
  const s = await serve();
  try {
    const info = await (await fetch(s.url + "/")).json();
    assert.equal(info.name, "collegica-mcp");
    assert.ok(info.endpoint.endsWith("/mcp"));
    assert.equal((await fetch(s.url + "/nope")).status, 404);
    const pre = await fetch(s.url + "/mcp", { method: "OPTIONS" });
    assert.equal(pre.status, 204);
    assert.equal(pre.headers.get("access-control-allow-origin"), "*");
  } finally { await s.close(); }
});

test("a tool with no inputs works whether the client sends arguments, {} or nothing", async () => {
  const s = await serve();
  try {
    for (const args of [undefined, {}]) {
      const r = await s.client.callTool({ name: "list_signing_months", arguments: args });
      assert.equal(r.isError, undefined, JSON.stringify(args));
      assert.equal(JSON.parse(r.content[0].text).months.length, 12);
    }
  } finally { await s.close(); }
});
