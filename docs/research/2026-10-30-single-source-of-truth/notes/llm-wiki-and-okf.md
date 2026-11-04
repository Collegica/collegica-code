# LLM Wiki, Open Knowledge Format, and how an AI reaches a business's knowledge

Research note, 2026-10-30. For the "single source of truth" article.

## Access and confidence

**Read in full (primary text, verbatim, via `curl` or `gh api`):**

- Karpathy's "LLM Wiki" gist, `llm-wiki.md` (raw file, about 12 KB). Created
  2026-04-04T16:25:13Z, per GitHub's gist listing for user `karpathy`.
- OKF `SPEC.md` v0.2, in full, from **both** the frozen copy in
  `GoogleCloudPlatform/knowledge-catalog/okf/` and the canonical copy in
  `GoogleCloudPlatform/open-knowledge-format`. A `diff` showed the two files
  are byte-identical on 2026-10-30.
- `knowledge-catalog` root `README.md`, `knowledge-catalog/okf/README.md`, and
  the first ~60 lines of the `open-knowledge-format` README.
- Collegica's `https://www.collegica.org/okf/index.md`,
  `https://www.collegica.org/llms.txt` and `https://www.collegica.org/okf/about.md`.
- The llms.txt proposal source, `https://llmstxt.org/index.md` (first ~80
  lines read; the rest was searched with `grep` only).
- Commit metadata for the OKF spec in both repositories, and the repository
  metadata for `open-knowledge-format`, through the GitHub API.

**Read through a summarising fetch tool (WebFetch), so any wording is the tool's paraphrase and is not checked verbatim against the page:**

- MCP introduction on modelcontextprotocol.io. The tool returned what looks like
  the page body, so I treat it as near-verbatim.
- Microsoft Learn, "Add SharePoint as a knowledge source" (Copilot Studio). The
  tool returned the full page, so I treat it as near-verbatim.
- Claude Help Center, "What are Projects?" (summarised).
- OpenAI API docs, File search guide (summarised).
- Anthropic, "Introducing Contextual Retrieval" (summarised).

**Read only as snippets:** the gist comment thread. I pulled the first 1,000
comments through the GitHub API, read them only as 220 to 600 character
excerpts, and searched them with `grep` for criticism. I stopped there, so the
thread may be longer.

**Could not verify:**

- **Karpathy's X posts.** The gist comments refer to an earlier "tweet" or "X
  post" that "went viral". Those are commenters' words, and I did not open the
  post. x.com serves a JavaScript wall, and I did not try to get around it. The
  date, wording and engagement of the X post are therefore **unverified**. It
  probably came out a day or two before 2026-04-04, but that is an unverified
  inference.
- **Blog responses and reviews of LLM Wiki outside the gist thread.** Web
  search was unavailable in this session (the per-session search budget was
  used up). I found no independent blog criticism, only commenters' criticism
  on the gist.
- **Evidence that small businesses use shared markdown or wiki knowledge
  bases with AI assistants.** I found **no** well-sourced survey or study. The
  gist's own "Business/team" example is a suggestion, not evidence of adoption.
- **The OKF publication date.** The spec text itself carries no date. The dates
  below come from git commits.
- **Whether llms.txt is "not an official standard".** A WebFetch summary said
  so, but I did not find the sentence in the part of the source I read. Treat
  that wording as **unverified**. What the source does show is that it is
  framed as a "proposal".

## 1. Karpathy's "LLM Wiki"

**Primary source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
(raw: `https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/llm-wiki.md`).
Title "llm-wiki". Created 2026-04-04 (UTC), per the GitHub API. The gist
describes itself as "an idea file", meant to be pasted into your own agent,
such as Codex, Claude Code or OpenCode.

### Core claim versus RAG

- Karpathy says that with RAG, upload-and-ask tools, NotebookLM and ChatGPT
  file uploads, the LLM is "rediscovering knowledge from scratch on every
  question". He adds: "There's no accumulation."
- In his approach the LLM "incrementally builds and maintains a persistent
  wiki". When a source arrives, the LLM integrates it into existing pages. It
  updates entity pages, revises summaries, and notes contradictions with older
  claims.
- His key phrase is that the wiki is "a persistent, compounding artifact".
  Knowledge is "compiled once and then *kept current*".
- The human curates sources, asks questions and directs the analysis. The LLM
  does "the grunt work": summarising, cross-referencing and filing.
- His analogy: "Obsidian is the IDE; the LLM is the programmer; the wiki is
  the codebase."

### Architecture: three layers

1. **Raw sources.** A curated collection of articles, papers, images and data
   files. They are "immutable": the LLM reads them and never edits them. He
   calls this layer "your source of truth".
2. **The wiki.** A directory of markdown files that the LLM writes: summaries,
   entity and concept pages, comparisons, an overview, a synthesis. "The LLM
   owns this layer entirely." You read it.
3. **The schema.** A file such as CLAUDE.md (Claude Code) or AGENTS.md (Codex)
   that sets out structure, conventions and workflows. He calls it "the key
   configuration file". It turns the LLM into "a disciplined wiki maintainer".
   The person and the LLM co-evolve it.

### Operations

- **Ingest.** Drop a source into the raw folder. The LLM reads it, discusses
  takeaways, writes a summary page, updates the index and related pages, and
  appends to the log. A single source "might touch 10-15 wiki pages".
  Karpathy prefers one source at a time, with himself involved, but notes
  that batch ingest is possible.
- **Query.** The LLM searches the pages and answers with citations. The answer
  can be a page, a table, a Marp deck, a matplotlib chart or a canvas. His key
  point is that "good answers can be filed back into the wiki", so
  explorations compound.
- **Lint.** A periodic health check. It looks for contradictions, stale claims,
  orphan pages, missing concept pages, missing cross-links, and data gaps that
  a web search could fill.

### Index and log

- `index.md` is a content catalogue: one line per page, organised by
  category. The LLM reads it first when it answers a question. He reports this
  works "surprisingly well at moderate scale". By moderate he means about 100
  sources and hundreds of pages, and at that size the index "avoids the need
  for embedding-based RAG".
- `log.md` is append-only and chronological. He suggests a fixed heading
  prefix such as `## [2026-04-02] ingest | Title`, so that `grep` can parse it.

### Tools he mentions

Obsidian, including its graph view, the Web Clipper, an attachment-download
hotkey, and the Marp and Dataview plugins. He also mentions
**qmd** (https://github.com/tobi/qmd), a local markdown search engine with a
CLI and an MCP server, and says the wiki is "just a git repo of markdown
files".

### Why it works, per him

The cost of a wiki is "the bookkeeping", and "Humans abandon wikis because the
maintenance burden grows faster than the value." LLMs "don't get bored". He
links the idea to Vannevar Bush's Memex (1945): Bush could not solve who does
the maintenance, and the LLM now can.

### Business use, per him (suggestion, not evidence)

He lists an internal team wiki maintained by LLMs and fed by Slack, meeting
transcripts, documents and customer calls, "possibly with humans in the loop".

### Follow-ups and criticism

All of the following are from the gist comment thread, which I read as
snippets on 2026-10-30. **These are commenters' opinions, not vetted sources.**

- **Implementations.** Within hours, many commenters posted their own builds.
  Examples include `browzy` (a CLI with ingest, compile, query and lint),
  `quicky-wiki` (with confidence-scored claims), `llm-context-base`, and
  `agentic-wiki-builder`. One commenter wrote that "implementation of this
  idea is a crowded place".
- **Error accumulation.** One commenter (frosk1, 2026-04-06) wrote that once a
  wrong fact is merged, "errors compound over time". Another (asong56,
  2026-04-07) wrote that hallucinations "can become permanently embedded as
  facts".
- **Provenance and drift.** Several commenters said that when sources change,
  compiled pages "might be wrong — and doesn't know it" (Jwcjwc12). Their fixes
  were content hashing, per-proposition source links, and confidence tags. One
  thread called "epistemic integrity" the most important unsolved problem.
- **Citations.** One commenter noted that "no hallucinated citations" is an
  aspiration, "not a technical guarantee" (Marekai).
- **Scale.** Commenters reported that the index stops being enough past "a few
  hundred pages", and that a schema creeps in anyway (mpazik).
- **"Nothing new".** Some commenters said it restates persistent context, the
  AGENTS.md idea, or Karpathy's own earlier "append-and-review note" blog post.
  I did not open that post: https://karpathy.bearblog.dev/the-append-and-review-note/
  returned "Not found" to a plain fetch.

**Relevance for the article:** the commenters' main objections are provenance,
trust and staleness. Those are exactly the fields OKF v0.2 standardises (see
§2). That is my own observation, not a claim either source makes.

## 2. Open Knowledge Format (OKF)

### Where it lives and its status

- The link in the brief,
  https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md,
  is now a **frozen snapshot**. The `okf/README.md` in that repo says, in bold,
  that OKF "now lives in its own repository". It also says: "Stop using the copy
  under `okf/`". That README notice was committed 2026-08-21 (#324).
- The canonical home is https://github.com/GoogleCloudPlatform/open-knowledge-format.
  The repo was created 2026-08-11, its last push was 2026-08-21, and it is
  licensed Apache-2.0. It had about 1,176 stars on 2026-10-30. It has no GitHub
  releases. Besides the spec, it contains a reference agent, sample bundles, and
  a `connectors/` folder with one file, `gcp-knowledge-catalog.md`.
- **Version:** the spec says "**Version 0.2**". It does not use the word
  "draft" about itself. A 0.x version and a "Considered and deferred" section
  suggest it is early-stage, but that is my reading.
- **Dates, from git:** OKF first landed in knowledge-catalog on 2026-06-12
  (v0.1, "Import Open Knowledge Format reference enrichment agent", #28). It
  migrated to v0.2 on 2026-07-24 (#227). The last spec change was 2026-08-21:
  "make every timestamp an ISO 8601 datetime with an explicit offset".
- **Publisher:** the spec lives in GitHub orgs owned by Google Cloud
  (GoogleCloudPlatform). But the knowledge-catalog root README ends with
  "This repository and its contents are not an official Google product." I did
  not find the same disclaimer in the part of the open-knowledge-format README
  that I read. The article should say "published in Google Cloud's GitHub
  organisation", not "a Google standard".
- **Intent, from the README:** OKF is "a **universal, vendor-neutral format**",
  "not tied to any particular agent, framework, model provider, or serving
  system". The Gemini/BigQuery reference agent is "a **proof of concept**", and
  "The format itself is the contribution". The parent product, Knowledge Catalog
  (formerly Dataplex), is described as an AI-powered data catalog that gives
  "semantics and business context to AI agents".

### What the spec says (v0.2)

- **Form:** "a directory of markdown files with YAML frontmatter". The spec
  adds that there is "no schema registry, no central authority, and no
  required tooling".
- **Motivation:** when a corpus is "continuously written and maintained by
  agents", a reader needs five answers. These are provenance, trust, freshness,
  lifecycle and attestation (§1).
- **Required:** only `type` (§4.1). Types are not centrally registered, and
  consumers must tolerate unknown types. "A concept carrying just `type` is
  fully conformant."
- **Recommended:** `title`, `description`, `resource` (a URI for the
  underlying asset) and `tags`. Any extra keys are allowed, and consumers must
  not reject unknown keys.
- **Provenance: `sources`** (§5.1). This is a list of entries. Within an entry,
  `resource` is required and `id` is optional. The `id` is used as a markdown
  footnote label for per-claim attribution, "keyed rather than positional"
  because agents rewrite the lists. Optional credibility signals are `author`,
  `usage_count` and `last_modified`, plus a sibling `usage_window`. The spec
  stores signals, "not a verdict"; it deliberately stores no credibility score.
- **Trust: `generated` and `verified`** (§5.2). `generated: { by, at }`
  records who wrote the current content and when. `verified` is a list of
  `{ by, at }` events. They are kept separate because "who *wrote* a concept
  need not be who *confirmed* it".
- **Trust tiers** (§5.3). These are derived, not stored. With no `verified`
  the concept is **unverified**. If only non-human actors verified it, it is
  **machine-confirmed**. Any `human:` actor makes it **human-reviewed**. The
  tiers are "advisory signals, not access control".
- **Actors** (§7): `<producer>/<version>` for agents, `human:<id>` for people,
  `process:<id>` for automated processes. Producers MUST use `human:` for
  human-confirmed content.
- **Lifecycle: `status`** (§5.4): `draft | stable | deprecated`. If it is
  absent, the concept is `stable`.
- **Lifecycle: `stale_after`** (§5.5). This is an absolute ISO 8601 instant,
  and a concept is stale when `now >= stale_after`. It is chosen over a
  relative TTL so that staleness is a plain comparison.
- **Index and log** (§8, §9). `index.md` and `log.md` are reserved at any
  level. `index.md` is a listing for "progressive disclosure" and carries no
  frontmatter. The one exception is that the bundle-root index may declare
  `okf_version`. `log.md` holds date-grouped entries, newest first, with
  `YYYY-MM-DD` headings.
- **Links** (§6). These are plain markdown links. A leading `/` means
  bundle-relative, and that is the recommended form. Consumers must tolerate
  broken links, since they "may simply represent not-yet-written knowledge".
  A `references/` folder is a naming convention, not a requirement.
- **Attested Computation** (§10). This is a concept with
  `type: Attested Computation`. It carries `runtime` (required), typed
  `parameters`, the computation (inline under `# Computation` or as a
  `computation` path), an `executor` that returns a receipt, and an `attester`.
  The attester is deterministic code with no LLM, and it checks the receipt.
  The agent "MAY only supply *values*" for the parameters and "MUST NOT author
  or edit the computation". The idea is that a consumer can check that a number
  "was produced the way we said it must be".
  `verified` and attestation are kept distinct. `verified` checks the
  definition and is stored in the bundle. Attestation checks each run and is
  not stored.
- **Conformance** (§11). Every non-reserved `.md` has parseable frontmatter
  with a non-empty `type`, and the reserved files follow §8 and §9. Consumers
  must not reject a bundle for missing optional fields, unknown types or keys,
  broken links, or missing indexes.
- **Deferred** (§12): the runtime protocol and receipt formats, the attester
  ABI and sandboxing, attestation caching, and semantic-layer templates.
- **v0.1 to v0.2** (§13). `timestamp` became `generated.at`. The body
  `# Citations` list became `sources`. Trust, lifecycle and attestation were
  added.

### Link between OKF and LLM Wiki (my observation; neither source cites the other)

OKF's `index.md` and `log.md` have the same roles as Karpathy's `index.md`
(a catalogue read first) and `log.md` (a chronological history). OKF
adds what the gist leaves to "your schema": machine-readable provenance, trust
tiers and expiry. I found **no** reference to Karpathy in the OKF spec or
README text that I read, so the article must not claim a lineage.

### How Collegica uses OKF (and what Collegica added beyond the spec)

These come from `okf/index.md`, `llms.txt` and `okf/about.md` on
collegica.org, read 2026-10-30.

- **Projection, not double authoring.** The human site is written in Quarto. A
  generator (`scripts/okf.py`) projects the source tree into an OKF bundle on
  every build, and the bundle is both committed and served at `/okf/`.
  The root `index.md` declares `okf_version: "0.2"` and calls the bundle "a
  proof of concept". *(Collegica's design; the spec does not prescribe this.)*
- **Sidecar manifest.** The judgement fields (`type`, who verified what,
  `stale_after`) live in `okf/manifest.yml`, not in the article frontmatter.
  Timestamps are derived from content or from git. *(Collegica's addition.)*
- **Honest trust tiers.** Articles are `generated` by a Claude actor and
  `verified` by `human:behzad`. Research notes are not verified, so they sit in
  the unverified tier. One Python computation is `verified` by `process:pytest`,
  which makes it machine-confirmed. *(This uses the spec's fields as intended.)*
- **Real attested computations.** The mortgage simulator (Node) and `bocrates`
  (Python) ship with an executor that emits a receipt of hashes, parameters and
  result, and an attester that re-runs and compares. *(The spec defines the
  interface. The receipt contents and hashing are Collegica's choices.)*
- **Extras the spec does not define:**
  - an `llms.txt` with "Reading rules for every assistant", which restates the
    tier, staleness and attestation rules as instructions;
  - a public Claude Code skill shipped *inside* the bundle as a `type: Skill`
    concept;
  - a read-only **MCP server** at `https://mcp.collegica.org/mcp` with
    `search_concepts`, `read_concept`, `list_signing_months` and
    `compare_mortgage`;
  - WebMCP tools registered on the calculator page;
  - a CI check that the committed bundle matches a fresh projection.
- **Custom `type` values** such as `Article`, `Video`, `Research Report`,
  `Research Note`, `Dataset`, `Application`, `Skill` and `Guide`. These are
  allowed, because the spec has no fixed taxonomy.

**Two inconsistencies on Collegica's side, worth fixing before the article:**

1. `llms.txt` and `okf/about.md` both link the spec at the **frozen**
   knowledge-catalog path. The canonical spec is now
   `GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md`. The content is
   identical today, but the old copy is marked unmaintained.
2. `okf/about.md`, under "Using the bundle with Claude", item 3, still says the
   MCP server is "Not built". `llms.txt` says it exists at
   `mcp.collegica.org`. One of the two is out of date; going by `llms.txt`, it
   is probably `about.md`.

## 3. llms.txt and MCP, for a small-business owner

### llms.txt

Source: https://llmstxt.org/ (source markdown at `https://llmstxt.org/index.md`).

- It was proposed by **Jeremy Howard**. The page header is dated **2024-09-03**
  and titled "The /llms.txt file, v2".
- **Problem:** "web pages are built for people". Navigation, ads and scripts
  get in an agent's way, and agents want "concise, expert-level information
  gathered in a single, accessible location".
- **What it is:** a markdown file at `/llms.txt`, or at any path, covering the
  pages under that path. It gives background, guidance and links to detailed
  markdown files. The proposal also asks for clean `.md` versions of pages, and
  `rel="alternate" type="text/markdown"` links that point to them.
- **Adoption, as the proposal itself claims it:** "thousands of sites publish
  an llms.txt file". Documentation platforms generate one, and Chrome
  Lighthouse audits for it as part of its agentic browsing checks. OpenAI,
  Anthropic and Gemini publish one for their developer docs. These are the
  author's claims, and I have not checked them independently.
- **Plain-language framing:** a signpost file at your website's front door that
  tells an AI assistant where the clean, current facts are. It does not make an
  AI read it. It only makes the right pages easy to find.

### Model Context Protocol (MCP)

Source: https://modelcontextprotocol.io/docs/getting-started/intro (via WebFetch).

- MCP is "an open-source standard for connecting AI applications to external
  systems". It lets assistants such as Claude or ChatGPT reach data sources,
  tools and workflows.
- The site's own analogy: "Think of MCP like a USB-C port for AI applications."
- Supported by Claude, ChatGPT, VS Code, Cursor and others, per the page.
- That page does not say who created MCP. From memory, MCP was introduced by
  Anthropic in November 2024. This is **unverified** in this session.
- **Plain-language framing:** llms.txt is a reading list an AI can follow. MCP
  is a plug that lets the AI *ask* your system questions or run a defined
  action, such as "look up this order" or "compare these two mortgages", and
  get a structured answer back. Collegica's MCP server is a working example.

## 4. Grounding: AI answers depend on what you feed them

**Small-business evidence:** none found that is well sourced (see Access and
confidence). Below are vendor documents only. They describe *mechanisms*, and
they are not independent evidence of quality.

- **Claude Projects** (Claude Help Center, "What are Projects?", via WebFetch).
  A project has its own knowledge base of uploaded files and its own
  instructions. On paid plans, when knowledge nears the context limit, Claude
  switches to retrieval (RAG), "expand capacity by up to 10x". The help page
  claims this works "while maintaining response quality", which is a vendor
  claim.
  https://support.claude.com/en/articles/9517075-what-are-projects
- **OpenAI File search** (Responses API guide, via WebFetch). Files go into
  "vector stores" with semantic and keyword search. The tool lets the model
  "augment the models' inherent knowledge". Responses carry file citations.
  https://developers.openai.com/api/docs/guides/tools-file-search
  (redirected from platform.openai.com/docs/guides/tools-file-search)
- **Microsoft Copilot Studio with SharePoint** (Microsoft Learn; ms.date
  2026-08-04, updated 2026-10-05). The agent "grounds only on the content of the
  files and pages you register". It does not follow hyperlinks inside them.
  It respects user permissions and sensitivity labels, and cannot ground on
  encrypted files.
  If you turn off web search and general knowledge, the agent answers
  "no response" rather than guessing. It also advises a maximum of 10 lists,
  and says lists over 35,000 rows affect "quality and latency".
  https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-sharepoint
- **Anthropic, Contextual Retrieval** (2024-09-19, via WebFetch). Standard
  chunking loses context, and the technique it introduces cuts top-20 retrieval
  failures by 49%, or 67% with reranking. These are Anthropic's own benchmark
  figures. The post also advises that a knowledge base under about 200,000
  tokens (about 500 pages) can simply go into the prompt whole. That is relevant
  to a small business, whose curated knowledge may fit.
  https://www.anthropic.com/news/contextual-retrieval

**The common thread for the article:** all three vendors' mechanisms answer
from whatever is in the registered source. None of them fixes a wrong or stale
source. That is the argument for one curated, dated, reviewed source of truth.
This is my synthesis, not a vendor claim.

## URLs used (all read 2026-10-30)

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (via GitHub API `gists/442a6bf555914893e9891c11519de94f/comments` and the raw file below)
- https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/llm-wiki.md
- https://api.github.com/users/karpathy/gists (gist creation dates)
- https://karpathy.bearblog.dev/the-append-and-review-note/ (fetch returned "Not found")
- https://x.com/karpathy (JavaScript wall; not read)
- https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md (raw)
- https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/README.md (raw)
- https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md (API)
- https://github.com/GoogleCloudPlatform/open-knowledge-format (API metadata, README, SPEC.md raw, commits)
- https://www.collegica.org/okf/index.md
- https://www.collegica.org/okf/about.md
- https://www.collegica.org/llms.txt
- https://llmstxt.org/ and https://llmstxt.org/index.md
- https://modelcontextprotocol.io/docs/getting-started/intro
- https://support.claude.com/en/articles/9517075-what-are-projects
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-sharepoint
- https://www.anthropic.com/news/contextual-retrieval
- https://github.com/tobi/qmd (named in the gist; not opened)
