// Cloudflare Worker entry: MCP over Streamable HTTP at /mcp, stateless (a fresh
// server per request; nothing to store, nothing to authenticate, everything it
// serves is already public on collegica.org).

import { WebStandardStreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/webStandardStreamableHttp.js";
import { buildServer, DEFAULT_BASE } from "./server.js";
import { concepts } from "./okf.js";

const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, POST, DELETE, OPTIONS",
  "access-control-allow-headers": "content-type, accept, mcp-session-id, mcp-protocol-version, last-event-id, authorization",
  "access-control-expose-headers": "mcp-session-id",
  "access-control-max-age": "86400",
};
const withCors = (res) => { const h = new Headers(res.headers); for (const [k, v] of Object.entries(CORS)) h.set(k, v); return new Response(res.body, { status: res.status, statusText: res.statusText, headers: h }); };

export async function handle(request, env = {}, deps = {}) {
  const url = new URL(request.url);
  if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });

  if (url.pathname === "/" || url.pathname === "") {
    return withCors(Response.json({
      name: "collegica-mcp",
      description: "Read-only MCP server for Collegica: its knowledge bundle and the fixed-vs-variable mortgage simulator.",
      endpoint: `${url.origin}/mcp`,
      transport: "streamable-http (stateless, JSON responses)",
      tools: ["search_concepts", "read_concept", "list_signing_months", "compare_mortgage"],
      concepts: concepts.length,
      docs: "https://github.com/Collegica/collegica-code/tree/main/apps/collegica-mcp",
    }));
  }
  if (url.pathname !== "/mcp") return withCors(new Response("Not found", { status: 404 }));

  const server = buildServer({ base: env.OKF_BASE || DEFAULT_BASE, ...deps });
  const transport = new WebStandardStreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
  await server.connect(transport);
  return withCors(await transport.handleRequest(request));
}

export default { fetch: (request, env) => handle(request, env) };
