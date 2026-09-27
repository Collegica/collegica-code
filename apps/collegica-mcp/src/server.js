// The MCP surface: four read-only tools. Errors come back as tool results
// (isError) carrying the message, so the agent can see how to recover.

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { search, readConcept, indexBuiltAt, concepts } from "./okf.js";
import { loadRates, listMonths, compareMortgage } from "./mortgage.js";

export const DEFAULT_BASE = "https://www.collegica.org/okf";

const text = (obj, isError = false) => ({ content: [{ type: "text", text: JSON.stringify(obj, null, 2) }], ...(isError ? { isError: true } : {}) });
const result = (obj) => text(obj, Boolean(obj && obj.error));
const READ_ONLY = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false };

export function buildServer({ base = DEFAULT_BASE, fetchFn = fetch, now = () => new Date() } = {}) {
  const server = new McpServer(
    { name: "collegica", version: "0.1.0" },
    {
      instructions:
        "Collegica (collegica.org) as tools. Use search_concepts and read_concept for what the site says: every result carries a trust tier " +
        "(unverified / machine-confirmed / human-reviewed) and a stale flag, so state them and do not quote a stale figure as current. " +
        "For mortgage numbers, run compare_mortgage rather than reading figures off an article. It is an illustrative simulation, not a quote or advice.",
    },
  );

  server.registerTool("search_concepts", {
    title: "Search Collegica",
    description:
      `Search the ${concepts.length} concepts (articles, research notes, guides, computations, datasets) in Collegica's Open Knowledge Format bundle by keyword, type or tag. ` +
      "Each hit carries its trust tier, verifier, status and stale flag. Leave query empty to list. Use read_concept to open one.",
    inputSchema: {
      query: z.string().optional().describe("Keywords, e.g. 'mortgage fixed variable'."),
      type: z.string().optional().describe("Concept type, e.g. Article, 'Research Note', Guide, 'Attested Computation'."),
      tag: z.string().optional().describe("Exact tag, e.g. finance."),
      limit: z.number().int().min(1).max(50).optional().describe("Max results, default 10."),
    },
    annotations: { title: "Search Collegica", ...READ_ONLY },
  }, async (args) => result({ ...search(args, now()), index_built_at: indexBuiltAt }));

  server.registerTool("read_concept", {
    title: "Read a Collegica concept",
    description:
      "Read one concept's full markdown, live from collegica.org, with its provenance: trust tier, who verified it and when, status, and whether it is stale. " +
      "Long concepts are paged: pass next_offset back as offset. Take paths from search_concepts.",
    inputSchema: {
      path: z.string().describe("Concept path from search_concepts, e.g. finance/fixed-or-variable.md."),
      offset: z.number().int().min(0).optional().describe("Character offset to start from, default 0."),
      max_chars: z.number().int().min(1000).max(100000).optional().describe("Page size, default 30000."),
    },
    annotations: { title: "Read a Collegica concept", ...READ_ONLY, openWorldHint: true },
  }, async (args) => result(await readConcept(args, { base, fetchFn, now: now() })));

  server.registerTool("list_signing_months", {
    title: "Mortgage signing months",
    description: "List the signing months the Fixed-or-Variable simulator can replay, with the fixed and variable rates on offer in each. Only these months are valid for compare_mortgage.",
    // No inputSchema: MCP lets a client omit `arguments` for a tool that takes none,
    // and an empty schema would reject that.
    annotations: { title: "Mortgage signing months", ...READ_ONLY, openWorldHint: true },
  }, async () => { const { rates, source } = await loadRates({ base, fetchFn }); return result({ ...listMonths(rates), ratesSource: source }); });

  server.registerTool("compare_mortgage", {
    title: "Fixed vs variable, in hindsight",
    description:
      "Replay a Canadian mortgage signed in a given month as both a fixed-rate and a variable-rate contract against the Bank of Canada's actual rate path. " +
      "Returns rates, payments, interest charged, balance owing and which product won. Illustrative simulation, not a quote or advice. Call list_signing_months for valid months.",
    inputSchema: {
      start: z.string().describe("Signing month, YYYY-MM, one of list_signing_months."),
      term: z.union([z.literal(3), z.literal(5)]).describe("Term in years: 3 or 5."),
      variablePayment: z.enum(["adjusts", "fixed"]).optional().describe("'adjusts' re-sets the payment when the rate changes; 'fixed' keeps the payment set at signing. Default adjusts."),
      principal: z.number().min(1000).optional().describe("Mortgage amount in CAD. Default 500000."),
      amortizationYears: z.number().int().min(1).max(40).optional().describe("Amortization in years. Default 25."),
    },
    annotations: { title: "Fixed vs variable, in hindsight", ...READ_ONLY, openWorldHint: true },
  }, async (args) => { const { rates, source } = await loadRates({ base, fetchFn }); const r = compareMortgage(rates, args); return result(r.error ? r : { ...r, ratesSource: source }); });

  return server;
}
