# collegica-mcp

A read-only [MCP](https://modelcontextprotocol.io) server for Collegica, as a
Cloudflare Worker. It gives any MCP client (Claude, ChatGPT, Claude Code, an
editor) two things the site already has:

- **The knowledge bundle.** `search_concepts` and `read_concept` walk the 86
  concepts in [`okf/`](../../okf/). Every result carries its trust tier
  (unverified / machine-confirmed / human-reviewed), who verified it and when,
  its status, and whether it is stale — the reading rules in
  [`llms.txt`](https://www.collegica.org/llms.txt), applied by the server rather than left
  to the client.
- **The mortgage simulator.** `list_signing_months` and `compare_mortgage` run
  the same `compare()` as the article's tables and calculator
  ([`mortgage.js`](../../website/static/js/fixed-or-variable/mortgage.js)),
  shaped by the same `summarize()` as the WebMCP tools on the page. Same inputs,
  same numbers.

This is the door for agents that cannot use the page's
[WebMCP tools](../../website/static/js/fixed-or-variable/tools.js): those need a
browser that implements `document.modelContext`, and most assistants are not one.

## Design

- **Stateless, no auth.** MCP over Streamable HTTP at `/mcp`, JSON responses, a
  fresh server per request. Everything it serves is already public on
  collegica.org; there is nothing to store and nothing to log in to.
- **Data is live, code is bundled.** Concept text and `rates.json` are fetched
  from the site (`OKF_BASE`), so content and rate updates need no redeploy. If the
  rates fetch fails, the copy bundled at deploy time is used, and the result says
  which (`ratesSource`). Only the *list* of concepts is fixed at deploy time
  (`scripts/build-index.mjs`), so a redeploy is needed to make a **new** concept
  searchable.
- **`read_concept` serves only indexed paths.** Not a proxy: a path that is not in
  the index (`../x.md`, a URL) is refused.
- **Errors are results.** Validation failures come back as `isError` tool results
  that say how to recover (the valid months, the tool to call), because a thrown
  error reaches the agent as an opaque "invocation failed".
- **All four tools are `readOnlyHint`.** The simulation is illustrative, not a
  quote or advice; the tool descriptions and results say so.

## Run and test

```bash
cd apps/collegica-mcp
npm install
npm test            # 11 tests: a real MCP client over HTTP, reading the repo's own okf/
npm run dev         # wrangler dev on http://127.0.0.1:8787  (MCP at /mcp)
```

`npm test` needs no network. `npm run dev` runs the real Workers runtime and reads
from the live site.

## Deploy

Live at **https://mcp.collegica.org** (MCP at `/mcp`; `GET /` describes it).

```bash
npx wrangler login          # once
npm run deploy              # builds the index, then wrangler deploy
```

Redeploy when a new concept should become searchable (the list of concepts is
fixed at deploy time; their text and the rates are read live). The stable name
is the custom domain `mcp.collegica.org`, set on the `collegica-mcp` Worker in
the Cloudflare dashboard; the `workers.dev` address keeps working alongside it.

Connect a client:

- **Claude Code:** `claude mcp add --transport http collegica https://mcp.collegica.org/mcp`
- **Claude / ChatGPT apps:** add the URL as a custom connector (no auth).
- **Any client:** it is listed in [`llms.txt`](https://www.collegica.org/llms.txt) for agents to find.
