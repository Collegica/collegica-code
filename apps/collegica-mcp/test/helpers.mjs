import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { handle } from "../src/index.js";
import { resetRatesCache } from "../src/mortgage.js";

const okfDir = join(dirname(fileURLToPath(import.meta.url)), "../../../okf");
export const BASE = "https://fake.test/okf";

/** A fetch that serves the repo's okf/ folder as if it were the live site. */
export const localFetch = async (url) => {
  const rel = String(url).replace(BASE + "/", "");
  try { return new Response(await readFile(join(okfDir, rel)), { status: 200 }); }
  catch { return new Response("not found", { status: 404 }); }
};

/** The Worker's handler behind a real HTTP socket, so a real MCP client can talk to it. */
export async function serve(deps = {}, env = { OKF_BASE: BASE }) {
  resetRatesCache();
  const srv = createServer(async (req, res) => {
    const chunks = []; for await (const c of req) chunks.push(c);
    const body = chunks.length ? Buffer.concat(chunks) : undefined;
    const request = new Request(`http://localhost:${srv.address().port}${req.url}`, { method: req.method, headers: req.headers, body: ["GET", "HEAD"].includes(req.method) ? undefined : body });
    const response = await handle(request, env, { fetchFn: localFetch, ...deps });
    res.writeHead(response.status, Object.fromEntries(response.headers));
    res.end(Buffer.from(await response.arrayBuffer()));
  });
  await new Promise((r) => srv.listen(0, r));
  const url = `http://localhost:${srv.address().port}`;
  const client = new Client({ name: "test", version: "0" });
  await client.connect(new StreamableHTTPClientTransport(new URL(`${url}/mcp`)));
  return { url, client, close: async () => { await client.close(); srv.close(); } };
}

export const call = async (client, name, args = {}) => {
  const r = await client.callTool({ name, arguments: args });
  return { isError: Boolean(r.isError), data: JSON.parse(r.content[0].text) };
};
