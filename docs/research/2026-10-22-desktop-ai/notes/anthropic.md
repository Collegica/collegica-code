# Claude Desktop and Claude Code: research notes

Researched 2026-10-22 from Anthropic primary sources. All pages were fetched on 2026-10-22. Most of them are living docs with no fixed date; where a page showed a date, it is given.

## Access and confidence

**Read in full** (complete page text fetched):
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/data-usage
- https://code.claude.com/docs/en/security
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/llm-gateway
- https://code.claude.com/docs/en/third-party-integrations
- https://code.claude.com/docs/en/zero-data-retention
- https://code.claude.com/docs/en/costs
- https://claude.com/docs/third-party/claude-desktop/overview
- https://claude.com/docs/third-party/claude-desktop/local-access
- https://code.claude.com/docs/en/sandboxing and https://code.claude.com/docs/en/memory: the full text was saved, and I searched it for the relevant passages.

**Summarized by the fetch tool** (a small model paraphrased these pages; the short quotes come from it, so treat exact wording as likely but unconfirmed):
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/desktop (the Desktop app's Code tab)
- https://code.claude.com/docs/en/skills, https://code.claude.com/docs/en/model-config
- support.claude.com articles: Cowork on web/desktop/mobile (15520349), Use Cowork safely (13364135), Cowork architecture overview (14479288), Get started with Cowork (13345190), Local MCP servers on Desktop (10949351), Install Claude Desktop (10065433), Computer use in Cowork (14128542), Get started with Claude in Chrome (12012173; shows "Last updated August 26, 2026")
- https://claude.com/pricing, https://claude.com/product/cowork, https://claude.com/blog/cowork-is-now-claude
- https://www.anthropic.com/news/updates-to-our-consumer-terms (dated Aug 28, 2025)
- https://github.com/modelcontextprotocol/mcpb

**Search snippets only** (not opened): "What are skills?" (support 12512176), the Claude in Chrome GA article and its "<0.08%" attack-success figure, and the Windows computer-use announcement on X.

**Not verified / caveats:**
- **Pricing.** The pricing page gives Max as "From $100" with "5x or 20x more usage than Pro". The fetch did not show a separate Max 20x price. Search snippets and the Cowork product page say $100 to $200.
- **The pricing-page summary was unreliable.** The first fetch put a cross against "Desktop app" for Free and Pro. That contradicts the install article ("All subscription tiers can access Claude Desktop"). I re-fetched with a quote-only prompt, and the re-fetch does not list desktop as a gated feature. Trust the install article.
- **Cowork's naming and architecture are changing.** From Sept 16, 2026, "Claude Cowork is now just Claude": chat and Cowork merged, rolling out to Pro and Max first. Support pages still use "Cowork".
  - The architecture article describes a local VM on the desktop.
  - The availability article says new Pro and Max tasks run in the cloud "as of October 6".
  - The article should describe both, and date them.
- I did not read the Consumer Terms or Privacy Policy text directly. The training and retention statements below come from the Claude Code data-usage doc and the Aug 2025 announcement.

---

## 1. Claude Desktop and local files

**What it is.** A desktop app for macOS 13+, Windows 10+, and Linux (Ubuntu 22.04+ / Debian 12, beta). Download from claude.ai/download. "All subscription tiers can access Claude Desktop." Free gets Chat. Paid plans add Claude Code and Cowork. Source: https://support.claude.com/en/articles/10065433-install-claude-desktop

**The Cowork / agentic mode on a folder** (now merged into "one Claude", see the caveat above):
- **Folder access.** You connect local folders explicitly in the desktop app. Claude reaches your computer "only for the folders you've connected". A cloud session can use those folders "only while the desktop app is open". https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- **Plans.** A paid plan is required (Pro, Max, Team, Enterprise). https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- **Where it runs.** The architecture overview describes two modes. In the cloud, work runs in "an isolated, temporary sandbox on Anthropic-managed infrastructure". On the desktop, the agent loop runs on the device and code runs in an "isolated virtual machine (VM)". https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
  - The third-party Desktop docs confirm that the code-execution sandbox is a "Local VM" in standard Claude Desktop too. Within an attached folder, the agent can "read, create, and modify files anywhere inside those folders". https://claude.com/docs/third-party/claude-desktop/overview , https://claude.com/docs/third-party/claude-desktop/local-access
- **Permissions.**
  - There are three modes: Manual (asks for each action), Auto (a safety review runs automatically), and Skip (no checks). (13345190)
  - Deleting files always needs approval: "Claude requires your explicit permission before permanently deleting any files." (13345190, 13364135)
  - Admins (Enterprise / third-party) can restrict which folders may be attached with `allowedWorkspaceFolders`, including read-only (`ro`) mode. Paths are checked after symlinks are resolved. (local-access page)
- **Supported files.** .docx, .pdf, .txt, .md, .xlsx, .pptx, images, and code. https://claude.com/product/cowork

**Local MCP servers and desktop extensions:**
- Desktop extensions are "single-click installable packages" for local MCP servers. Install from Settings > Extensions > Browse extensions (an Anthropic-reviewed directory), or open a `.mcpb` file through Advanced settings > Install Extension. https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
- `.mcpb` (MCP Bundle) is a zip with a local MCP server plus `manifest.json`. It was renamed from DXT: "`.dxt` files becoming `.mcpb`". The format is open source, under github.com/modelcontextprotocol/mcpb. https://github.com/modelcontextprotocol/mcpb

**Computer use:**
- Beta, Pro and Max only: "Team and Enterprise plans don't have access" at this time. It works on macOS and Windows, in Cowork and Claude Code inside Desktop.
- It is off by default. On macOS it needs the Accessibility and Screen Recording permissions.
- It works from screenshots, so Claude can see anything visible on your screen.
- "Claude asks for your permission before accessing each application." Investment and crypto apps are blocked by default.
- https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork ; https://code.claude.com/docs/en/desktop (macOS 14+ for computer use; app tiers: view only for browsers, click only for terminals and IDEs, full control for everything else)

**Claude in Chrome:**
- An extension that can "read, click, and navigate websites". Available on all paid plans; off by default on Enterprise.
- It works with Desktop, Cowork and Claude Code.
- Anthropic's own warning: "enhanced with our safety classifiers but is still risky".
- https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

**Projects and skills:**
- Projects can be "tied to a local folder" (desktop only). (15520349)
- Skills are "folders of instructions, scripts, and resources". They are available on Free, Pro, Max, Team and Enterprise, and need code execution to be on. (snippet: https://support.claude.com/en/articles/12512176-what-are-skills)

---

## 2. Claude Code

**What it is.** "An agentic coding tool that reads your codebase, edits files, runs commands". It is available in the terminal, IDE, desktop app, and browser. https://code.claude.com/docs/en/overview

**Install** (https://code.claude.com/docs/en/setup):
- Native installer (recommended): `curl -fsSL https://claude.ai/install.sh | bash` on macOS, Linux and WSL; `irm https://claude.ai/install.ps1 | iex` in Windows PowerShell. It auto-updates.
- Other methods: Homebrew `brew install --cask claude-code`, WinGet `winget install Anthropic.ClaudeCode`, apt/dnf/apk, or npm `npm install -g @anthropic-ai/claude-code` (needs Node 22+). The npm package installs the same native binary. Homebrew and WinGet do not auto-update by default.
- Requirements: macOS 13+, Windows 10 1809+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+, 4 GB+ RAM, and an internet connection.
- On Windows, Git for Windows is optional; without it Claude Code uses PowerShell.
- Sandboxing is not supported on native Windows. Use WSL 2.

**Surfaces.**
- Terminal, VS Code / Cursor extension, JetBrains plugin, and web (claude.ai/code).
- The Desktop app's **Code tab** includes Claude Code ("you don't need to install the CLI separately") and needs a paid subscription. https://code.claude.com/docs/en/overview
- The Code tab offers local, cloud and SSH sessions, a project folder picker, visual diff review, scheduled tasks, and the same permission modes as the CLI. https://code.claude.com/docs/en/desktop

**How it reads and edits files.**
- It reads files in the working directory without asking.
- Reading outside that directory prompts once.
- Edits and shell commands depend on the permission mode. https://code.claude.com/docs/en/permission-modes
- Security doc: in Manual mode the working-directory boundary "is a permission prompt, so a Bash command you approve can still write anywhere your user account can". https://code.claude.com/docs/en/security

**Permission modes** (https://code.claude.com/docs/en/permission-modes):

| Mode | What it does |
|---|---|
| `default` / Manual | Only reads run without asking |
| `acceptEdits` | File edits and common filesystem commands run without asking |
| `plan` | Researches and proposes; edits are blocked until you approve the plan |
| `auto` | A classifier model reviews actions; blocks `curl \| bash`, force-push, production deploys and similar |
| `dontAsk` | For CI; anything that would prompt is denied |
| `bypassPermissions` | "Isolated containers and VMs only" |

- Shift+Tab cycles through the modes.
- Auto mode is now the built-in default for interactive terminal and VS Code sessions (v2.1.283+ per the permission-modes page; also stated on the security page).

**CLAUDE.md memory** (https://code.claude.com/docs/en/memory):
- Four locations: managed policy, `~/.claude/CLAUDE.md` (user), `./CLAUDE.md` or `./.claude/CLAUDE.md` (project), and `./CLAUDE.local.md` (personal, gitignored).
- It reads `AGENTS.md` when no CLAUDE.md exists.
- "Auto memory" holds notes Claude writes itself; the first 200 lines or 25KB load each session.
- Memory is "context, not enforced configuration". Use hooks to enforce a rule.

**Skills, hooks and MCP:**
- **Skills** are `SKILL.md` folders in `~/.claude/skills/` or `.claude/skills/`. They are invoked automatically or as `/skill-name`, and follow the Agent Skills open standard (agentskills.io). https://code.claude.com/docs/en/skills
- **Hooks** are "user-defined shell commands" that run at lifecycle points such as PreToolUse and PostToolUse, for "deterministic control". https://code.claude.com/docs/en/hooks-guide
- **MCP** servers are configured per user or project (`.mcp.json`). Anthropic "does not security-audit or manage any MCP server". https://code.claude.com/docs/en/security

**Sandboxing.**
- The sandbox is an OS-enforced boundary on the files and network domains that shell commands can reach. It uses Seatbelt on macOS and bubblewrap on Linux/WSL2. It is "off by default"; turn it on with `/sandbox`.
- It covers shell commands only. File tools, MCP servers and hooks run outside it.
- It is built on the open-source `@anthropic-ai/sandbox-runtime`.
- https://code.claude.com/docs/en/sandboxing

**Checkpoints and rewind.**
- `/rewind`, or Esc twice, restores code, the conversation, or both. The last 100 checkpoints are kept.
- **Limits:** "Checkpointing does not track files modified by Bash commands" (`rm`, `mv`, `cp`), and it is "Not a replacement for version control".
- https://code.claude.com/docs/en/checkpointing

**Plan mode.** "Claude researches and proposes changes without making them". After the plan, you choose to approve it in auto mode, approve with manual edits, or keep planning. https://code.claude.com/docs/en/permission-modes

---

## 3. Pricing and plan requirements

Source for prices: https://claude.com/pricing (fetched 2026-10-22).

| Plan | Price | Claude Code | Cowork / agentic tasks | Desktop | Computer use |
|---|---|---|---|---|---|
| Free | $0 | No ("The free claude.ai plan does not include Claude Code access", setup doc) | No (needs a paid plan) | Yes (chat) | No |
| Pro | $20/mo, or $17/mo billed annually ($200/yr) | Yes | Yes | Yes | Yes (beta) |
| Max | "From $100"/mo; 5x or 20x Pro usage; $200 tier per secondary sources | Yes | Yes | Yes | Yes (beta) |
| Team | Standard $25/seat monthly or $20 annually; Premium $125 monthly or $100 annually | Yes | Yes (beta per 15520349) | Yes | **No** |
| Enterprise | "US$20/seat/month, billed annually, 20 seat minimum" plus usage | Yes | Yes (admin-enabled) | Yes | **No** |

- **API key / Console.** Claude Code also works with an Anthropic Console account (pay per token), or with Bedrock, Google Cloud's Agent Platform (Vertex) or Microsoft Foundry. https://code.claude.com/docs/en/setup
- **Typical spend.** For enterprise API users: "around $13 per developer per active day and $150-250 per developer per month". https://code.claude.com/docs/en/costs
- **The Desktop Code tab** requires "a paid subscription". https://code.claude.com/docs/en/overview

---

## 4. Privacy and data

**What leaves the machine:**
- Claude Code "runs locally", but to reach the model it "sends data over the network". That "includes all user prompts and model outputs", and file contents Claude reads become part of those prompts. https://code.claude.com/docs/en/data-usage
- Cowork: local files reached through the desktop app are "processed on Anthropic's servers rather than staying on the device". https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
- Computer use sends screenshots, so "Claude can see anything visible on your screen" (paraphrase, 14128542).

**Training on consumer plans (Free, Pro, Max):**
- From the data-usage doc: "We give you the choice to allow your data to be used to improve future Claude models." Training happens "when this setting is on (including when you use Claude Code from these accounts)". https://code.claude.com/docs/en/data-usage
- The policy was introduced Aug 28, 2025. You can change it in Privacy Settings "at any time", and deleted conversations are not used for future training. https://www.anthropic.com/news/updates-to-our-consumer-terms
- The doc does not say whether the toggle is on or off by default. Third-party coverage called it a flipped default (opt-out); this is **not verified from a primary source**.

**Retention:**
- Consumer plans: 5 years if you allow training, 30 days if you don't. The setting lives at claude.ai/settings/data-privacy-controls.
- Commercial plans (Team, Enterprise, API): 30 days as standard.
- Feedback sent with `/feedback` is kept 5 years.
- On your own machine, transcripts are stored "locally in plaintext under `~/.claude/projects/`" for 30 days by default.
- https://code.claude.com/docs/en/data-usage

**Commercial training:** Anthropic "does not train generative models using code or prompts sent to Claude Code under commercial terms". (data-usage)

**Zero data retention (ZDR):**
- Only for qualified Claude for Enterprise accounts, enabled by Anthropic and "not included in the standard Claude for Enterprise plan".
- ZDR does **not** cover Cowork or claude.ai chat.
- It disables cloud sessions, Remote Control and feedback.
- Data flagged for policy violations may still be kept up to 2 years.
- https://code.claude.com/docs/en/zero-data-retention

**Telemetry.** Usage metrics "never include your code, prompts, or file paths". Opt out with `DISABLE_TELEMETRY=1` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. (data-usage)

---

## 5. Local or third-party models

**Claude Code:**
- Runs against the Anthropic API or a subscription, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform (formerly Vertex AI), or Microsoft Foundry. Corporate LLM gateways connect through `ANTHROPIC_BASE_URL`. https://code.claude.com/docs/en/third-party-integrations
- Anthropic explicitly "doesn't support routing Claude Code to non-Claude models through any gateway". https://code.claude.com/docs/en/llm-gateway
- Third-party gateways that point Claude Code at other models exist (LiteLLM-style proxies), but they are unsupported and outside Anthropic's docs.
- **No local-model support is documented.**

**Claude Desktop:**
- Standard Desktop uses Anthropic models via claude.ai.
- "Claude Desktop on 3P" is an organizational deployment mode that routes inference to Bedrock, Google Cloud's Agent Platform, Foundry, "any compatible gateway you operate", or the Anthropic API. Conversations are stored on the local device.
- It is aimed at regulated enterprises and is configured through MDM.
- The models are still Claude. Nothing on the page describes non-Claude or local models.
- https://claude.com/docs/third-party/claude-desktop/overview
- Desktop can, however, reach local tools through MCP extensions.

---

## 6. Local-file tasks for non-programmers (Anthropic's own examples)

- "Organizing files by type/date"; "Creating spreadsheets with formulas and presentations"; "Batch processing documents (receipts, transcripts)"; research synthesis from several sources; data analysis. https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Product-page scenarios (https://claude.com/product/cowork):
  - reconcile spreadsheets from "regional export folders and budget files" and flag the variances
  - a first-pass contract review against a playbook, with cited departures
  - organize quarterly call notes into recurring themes, with sources
  - a weekly marketing readout built from Drive files and Amplitude
- Output formats include .docx, .xlsx, .pptx and PDF. Claude Docs and Slides (Sept 16, 2026) export to PowerPoint or PDF. https://claude.com/blog/cowork-is-now-claude
- Scheduled tasks on Desktop "run on your machine, with direct access to your local files". https://code.claude.com/docs/en/overview
- The Claude Code CLI is pitched at code, but the same tools (read, edit, bash) work on any folder. `claude -p` pipes and bulk operations are documented. (overview)

---

## 7. Limits and risks

**Prompt injection:**
- Cowork safety page: "Claude can read information outside your trusted boundary" and "web content is a primary vector for prompt injection attacks". It recommends avoiding sensitive files such as financial documents, extending internet access "only to sites you trust", and using "Manually approve" for high-stakes work. https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- Claude Code security page: "no system is completely immune to all attacks". Advice: avoid piping untrusted content to Claude, and use VMs. https://code.claude.com/docs/en/security
- Claude in Chrome: "still risky". A search snippet reports Anthropic's internal attack-success rate below 0.08% and the line "Prompt injection is a moving target" (**snippet only**).

**Destructive actions:**
- Cowork: Claude "can read, write, and permanently delete these files", though deletion needs an "Allow". (13364135)
- Claude Code: `rm -rf ~` and `rm -rf /` are always blocked in Manual, acceptEdits, plan and dontAsk modes. Auto mode shows a 2-minute countdown prompt instead. https://code.claude.com/docs/en/permission-modes
- Rewind does not undo bash-made changes. (checkpointing)
- `bypassPermissions` is for isolated VMs only.

**Sandbox scope.** The sandbox covers shell commands only, and native Windows has no sandbox. Cowork's cloud isolation "doesn't limit what Claude reads or does" through the permissions you grant. (sandboxing, 13364135)

**Context limits.**
- 1M-token windows are native on newer models (Opus 4.7+, Sonnet 5+, Fable). Others have 200K. https://code.claude.com/docs/en/model-config
- Auto-compaction summarizes the history near the limit. Long sessions and many file reads use up plan limits fast: "one debugging session can consume more than a day of chat". https://code.claude.com/docs/en/costs

**Computer use.** "No safeguards are perfect". Don't use it for financial, legal or medical apps, or apps holding other people's personal data. (14128542)

**MCP and extensions.** Be cautious with unfamiliar MCPs and plugins. Anthropic reviews directory listings but does not security-audit servers. (13364135; security doc)
