// Builds src/generated/concepts.json: one metadata record per OKF concept, read
// from the frontmatter of ../../okf/**/*.md. The Worker searches this list and
// only serves paths that appear in it; the full text of a concept is fetched
// live from the site, so a redeploy is needed only when concepts are added.

import { readdirSync, readFileSync, writeFileSync, mkdirSync, statSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { parse } from "yaml";

const here = dirname(fileURLToPath(import.meta.url));
const okf = join(here, "../../../okf");
const out = join(here, "../src/generated/concepts.json");

function* walk(dir) {
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) yield* walk(p);
    else if (name.endsWith(".md")) yield p;
  }
}

const concepts = [];
for (const file of walk(okf)) {
  const text = readFileSync(file, "utf8");
  const m = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!m) continue;
  const fm = parse(m[1]);
  if (!fm || !fm.type) continue; // index.md and log.md carry no concept type
  concepts.push({
    path: relative(okf, file),
    type: fm.type,
    title: fm.title ?? relative(okf, file),
    description: (fm.description ?? "").trim(),
    tags: fm.tags ?? [],
    status: fm.status ?? null,
    stale_after: fm.stale_after ?? null,
    // OKF allows one entry or a list; the server always sees a list.
    verified: fm.verified == null ? [] : [].concat(fm.verified),
    generated: fm.generated ?? null,
    resource: fm.resource ?? null,
  });
}

mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, JSON.stringify({ builtAt: new Date().toISOString(), concepts }, null, 1) + "\n");
console.log(`indexed ${concepts.length} concepts → src/generated/concepts.json`);
