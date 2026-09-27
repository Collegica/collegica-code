// Reading the OKF bundle the way llms.txt says to: state the trust tier, flag
// draft/deprecated, and refuse to present a stale fact as current.

import index from "./generated/concepts.json" with { type: "json" };

export const concepts = index.concepts;
export const indexBuiltAt = index.builtAt;

/** absent/empty → unverified; only agent/process actors → machine-confirmed; any human: → human-reviewed. */
export function trustTier(verified) {
  const list = verified == null ? [] : [].concat(verified);
  if (list.length === 0) return "unverified";
  return list.some((v) => String(v.by).startsWith("human:")) ? "human-reviewed" : "machine-confirmed";
}

/** The provenance summary that goes with every concept an agent reads. */
export function provenance(c, now = new Date()) {
  const verified = c.verified == null ? [] : [].concat(c.verified);
  const last = verified.length ? verified[verified.length - 1] : null;
  const stale = c.stale_after ? now >= new Date(c.stale_after) : false;
  const warnings = [];
  if (c.status === "draft" || c.status === "deprecated") warnings.push(`status is ${c.status}`);
  if (stale) warnings.push(`stale since ${c.stale_after}: report dated facts as stale, not current`);
  return {
    path: c.path,
    type: c.type,
    title: c.title,
    trust: trustTier(verified),
    verified_by: last ? last.by : null,
    verified_at: last ? last.at : null,
    status: c.status,
    stale_after: c.stale_after,
    stale,
    warnings,
    url: c.resource && c.resource.startsWith("http") ? c.resource : null,
  };
}

const words = (s) => String(s ?? "").toLowerCase().split(/[^\p{L}\p{N}]+/u).filter(Boolean);

/** Rank concepts by a query over title, tags, description and path. Empty query lists everything. */
export function search({ query = "", type, tag, limit = 10 } = {}, now = new Date()) {
  const q = words(query);
  let hits = concepts
    .filter((c) => (!type || c.type.toLowerCase() === type.toLowerCase()) && (!tag || c.tags.map((t) => t.toLowerCase()).includes(tag.toLowerCase())))
    .map((c) => {
      const title = words(c.title), tags = c.tags.flatMap(words), desc = words(c.description), path = words(c.path);
      let score = 0;
      for (const w of q) {
        if (title.includes(w)) score += 3;
        if (tags.includes(w)) score += 2;
        if (desc.includes(w)) score += 1;
        if (path.includes(w)) score += 1;
      }
      return { c, score };
    })
    .filter((h) => q.length === 0 || h.score > 0)
    .sort((a, b) => b.score - a.score || a.c.title.localeCompare(b.c.title));
  const total = hits.length;
  hits = hits.slice(0, Math.min(Math.max(limit, 1), 50));
  return {
    total,
    returned: hits.length,
    results: hits.map(({ c }) => ({ ...provenance(c, now), description: c.description, tags: c.tags })),
  };
}

const PATH_OK = /^[A-Za-z0-9][A-Za-z0-9/_.-]*\.md$/;

/** Fetch one concept's text live from the site. Only indexed paths are served. */
export async function readConcept({ path, offset = 0, max_chars = 30000 }, { base, fetchFn = fetch, now = new Date() }) {
  const clean = String(path ?? "").replace(/^\/+/, "");
  const c = PATH_OK.test(clean) && !clean.includes("..") ? concepts.find((x) => x.path === clean) : undefined;
  if (!c) return { error: `Unknown concept path "${path}". Use search_concepts to find valid paths.` };
  const res = await fetchFn(`${base}/${c.path}`, { cf: { cacheTtl: 600 } });
  if (!res.ok) return { error: `Could not fetch ${c.path} (HTTP ${res.status}).` };
  const text = await res.text();
  const start = Math.max(0, offset), end = Math.min(text.length, start + Math.min(Math.max(max_chars, 1000), 100000));
  return {
    provenance: provenance(c, now),
    total_chars: text.length,
    offset: start,
    truncated: end < text.length,
    next_offset: end < text.length ? end : null,
    text: text.slice(start, end),
  };
}
