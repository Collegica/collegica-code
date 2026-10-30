# Why a desktop or terminal agent on your own files beats pasting into a chat — evidence, 2026-10-22

## Access and confidence

- **Read via a fetch-and-summarise tool (wording close, not guaranteed
  verbatim):** Simon Willison's "lethal trifecta", "Designing agentic loops"
  and Cowork first-impressions posts; agents.md; agentskills.io;
  modelcontextprotocol.io home and versioning pages; the Linux Foundation's
  AAIF press release; Anthropic's context-engineering post and its software-
  development Economic Index report; Meta's "Agents Rule of Two"; METR's
  2025 developer study; Claude's "Using Cowork safely" help article; Claude
  Code's memory docs (saved locally and grepped, so those quotes are exact);
  Ollama's FAQ.
- **Snippet-only:** the Cowork launch coverage (VentureBeat, MarkTechPost,
  Jan 2026) from search results; MCP's December 2025 move to the AAIF also
  appears on the MCP blog (not opened).
- **Not found:** a controlled study of *non-programmers* comparing a
  file-working agent with copy-paste chat. The usage evidence below is from
  coding; say so in the article.
- **Caution:** the URL `claude.com/blog/cowork-research-preview` now returns
  current product copy (Cowork "is now just Claude", on Pro, Max and Team),
  not the January launch post.

## 1. Context from a folder, not a pasted snippet

- Anthropic, "Effective context engineering for AI agents" (2025-09-29):
  agents keep references and "dynamically load data into context at runtime
  using tools"; "Folder hierarchies, naming conventions, and timestamps"
  are signals; Claude Code uses `head` and `tail` to analyse large data
  "without ever loading the full data objects into context".
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  → The point for readers: you don't choose what to paste; the agent looks.
- Same post: an agent "maintaining a NOTES.md file" to track progress — the
  memory is a file you can open. Same URL.
- Willison: Claude Code is "a 'general agent' disguised as a developer
  tool", useful for "any computer task" done by running commands.
  https://simonwillison.net/2026/Jan/12/claude-cowork/

## 2. Outputs written back as real files

- Cowork (Anthropic's agent for non-coders in the Claude desktop app, launched
  Jan 2026 as a research preview): pick a folder, the agent reads, edits and
  creates files there; press examples are receipts → an expense spreadsheet,
  tidying Downloads, a report from scattered notes (snippet).
  https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no
- Current Cowork page: "Deleting anything needs your approval"; you
  "come back to polished work for your review".
  https://claude.com/blog/cowork-research-preview
- Usage data (coding only): Anthropic's Economic Index found Claude Code
  conversations 79% "automation" vs 49% on Claude.ai, and "feedback loop"
  patterns 35.8% vs 21.3% (data April 6–13, 2025, 500,000 interactions).
  https://www.anthropic.com/research/impact-software-development
  → Evidence that the agent does the task rather than handing back text to
  copy; not evidence of better quality.
- Counterweight: METR's RCT (July 2025) found experienced open-source
  developers 19% *slower* with early-2025 AI tools (Cursor), while believing
  they were ~20% faster; METR says later tools showed different results.
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  → Use to keep claims honest: the case for files is fewer copy steps and a
  checkable result, not guaranteed speed.

## 3. Repeatability: instruction files and skills

- **AGENTS.md:** "A simple, open format for guiding coding agents"; "now
  stewarded by the Agentic AI Foundation under the Linux Foundation"; used by
  60,000+ open-source projects; read by Codex, Jules, Cursor, Copilot, VS
  Code, Aider, Zed and others. https://agents.md/
- **CLAUDE.md:** "Claude reads them at the start of every session"; Claude
  Code "can read AGENTS.md as your project instructions" with no extra
  setup; target "under 200 lines"; and they are "context, not enforced
  configuration" — use a hook to block an action for certain.
  https://code.claude.com/docs/en/memory
- **Agent Skills:** "a folder containing a `SKILL.md` file" plus optional
  scripts and references; loaded by "progressive disclosure" (name and
  description first, full instructions on match); "originally developed by
  Anthropic, released as an open standard". https://agentskills.io/
  Hermes and LM Studio Bionic both read this format (see `hermes.md` and the
  Sept `bionic.md` note).
- Point for the article: a pasted prompt dies with the chat; an instruction
  file or skill sits in the folder and runs the same way next time, in more
  than one app.

## 4. MCP as the shared plug

- "An open-source standard for connecting AI applications to external
  systems"; "Think of MCP like a USB-C port for AI applications"; supported
  by Claude, ChatGPT, VS Code, Cursor and others.
  https://modelcontextprotocol.io/
- Current protocol revision: **2026-07-28** (date-stamped; earlier
  handshake-based revisions are `2025-11-25` and before).
  https://modelcontextprotocol.io/specification/versioning
- Governance: Anthropic donated MCP to the **Agentic AI Foundation**, a
  Linux Foundation directed fund, announced 2025-12-09, alongside Block's
  goose and OpenAI's AGENTS.md; platinum members AWS, Anthropic, Block,
  Bloomberg, Cloudflare, Google, Microsoft, OpenAI.
  https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
  (No later change of home found.)

## 5. The risk: prompt injection and the lethal trifecta

- Willison's trifecta (2025-06-16): "Access to your private data", "Exposure
  to untrusted content", and the ability to "externally communicate". "We
  still don't know how to 100% reliably prevent this"; advice: avoid the
  combination "entirely". MCP "encourages users to mix and match tools".
  Guardrail claims of 95%: "in web application security 95% is very much a
  failing grade". https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Meta's "Agents Rule of Two" (2025-10-31): an agent should have no more than
  two of [A] untrustworthy inputs, [B] sensitive data, [C] changing state or
  communicating out; all three needs a human in the loop.
  https://ai.meta.com/blog/practical-ai-agent-security/
- Willison, "Designing agentic loops" (2025-09-30): YOLO risks are bad shell
  commands, exfiltration, and your machine used as a proxy; options are a
  sandbox, "someone else's computer", or accept the risk.
  https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
- Willison on Cowork: files mounted into a VM (Apple Virtualization
  Framework); and "I do not think it is fair" to ask non-programmers to spot
  prompt injection. https://simonwillison.net/2026/Jan/12/claude-cowork/
- Anthropic's own Cowork safety page frames injection as needing two
  conditions — reading untrusted content *and* being able to act; remove
  either and attacks get harder. "You remain responsible for all actions".
  https://support.claude.com/en/articles/13364135-using-cowork-safely
- Practical mitigations available in Hermes: manual approvals, deny rules,
  `HERMES_WRITE_SAFE_ROOT`, a Docker backend (see `hermes.md`).

## 6. Privacy: a local folder is not the same as a local model

- Hosted model, local files: the files the agent reads are sent to the
  provider. Cowork's help page says local files opened through the app are
  "processed on Anthropic's servers rather than staying on your computer"
  (cloud sessions). https://support.claude.com/en/articles/13364135-using-cowork-safely
- Local model: Ollama — "We don't see your prompts or data when you run
  locally"; its cloud models are processed but "do not store or log" content.
  https://docs.ollama.com/faq
- Hermes v0.22.0's built-in runtime: "nothing leaving it: no account, no
  API key". https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0
- The agent app itself may phone home separately from the model (Hermes:
  opt-in metrics, connectors via a Nous gateway — see `hermes.md`).
- Article framing: three settings, three answers — chat in a browser (you
  choose what to send, by hand); agent + hosted model (the agent chooses
  what to send, from the folder you open); agent + local model (nothing
  leaves, at the cost of speed and quality — see Sept `run.md`).
