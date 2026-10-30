# OpenAI: ChatGPT desktop app and Codex — research notes (2026-10-22)

## Access and confidence

All pages below were read on 2026-10-22.

**The big change since mid-2025:** on 2026-07-09 OpenAI merged the standalone Codex app into a **new ChatGPT desktop app** (macOS, Windows, and Linux in preview). The new app has three modes: **Chat**, **Work** (an agent for non-coding knowledge work) and **Codex** (for coding). The old ChatGPT desktop app is now called **ChatGPT Classic** and is still supported. "Work with Apps", the Option+Space companion bar and Record were Classic features. Article claims that rely on 2024–25 knowledge of "the ChatGPT desktop app" are now out of date.

**Read in full (primary sources):**
- learn.chatgpt.com docs. `developers.openai.com/codex` now 308-redirects here. Each page has a Markdown version at `/docs/<slug>.md`, fetched with curl: app, quickstart, use-chatgpt, projects, appshots, computer-use, artifacts-viewer, permission-modes, sandboxing, agent-approvals-security, auth, pricing, models, codex/cli, windows/windows-app, windows/wsl, agent-configuration/agents-md, extend/mcp (intro + CLI section), customization/computer-history, enterprise/chatgpt-work-overview, enterprise/chatgpt-work-local-security, environments/modes. Also the index https://learn.chatgpt.com/llms.txt and the single-file export https://learn.chatgpt.com/docs/llms-full.txt (searched for config-advanced OSS mode).
- help.openai.com and openai.com, read in a real browser because plain fetches return 403: "Moving to the new ChatGPT desktop app", "Work with Apps on macOS", "Data controls in ChatGPT", "ChatGPT macOS app release notes", "ChatGPT Record", "OpenAI open-weight models (gpt-oss)", the openai.com announcement "ChatGPT is now a partner for your most ambitious work" (2026-07-09), and https://openai.com/open-models/.
- github.com/openai/codex README (via WebFetch). GitHub API: latest release `rust-v0.163.0` published 2026-10-15; Apache-2.0 licence; about 130k stars. Issue #32576.

**Snippet-only (search results, not opened):** "Introducing gpt-oss" (openai.com/index/introducing-gpt-oss), launch date 5 Aug 2025 (search snippet). Also third-party coverage (Neowin, The New Stack, 9to5Mac) of the July merge, used only to confirm the date.

**Not verified:**
- The exact per-plan message limits (the pricing table did not render in Markdown).
- The full Temporary Chat article.
- Whether "Work with Apps" exists inside the *new* app. It is not documented there; Appshots plus Computer Use appear to replace it. Treat this as inference.
- Whether gpt-oss has been superseded. Search found no newer open-weight release, but this is not confirmed by an OpenAI page.
- Consumer retention for Codex local sessions beyond the general ChatGPT rules.

---

## 1. ChatGPT desktop app: local files and the local machine

**Two apps exist today.**
- New **ChatGPT** desktop app = Chat + Work + Codex. Platforms: macOS and Windows; Linux in preview. https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app ; https://learn.chatgpt.com/docs/linux/linux-app.md
- **ChatGPT Classic** = the previous app. It "continues to receive model updates, bug fixes, security patches". It is noted that "New agent features may be available only in the new app." (same help article)
- Announced 2026-07-09. The desktop app has "Chat, Work, and Codex available to users on every plan, including Free." The Atlas browser is being sunset. https://openai.com/index/chatgpt-for-your-most-ambitious-work/

**Reading a folder directly and editing files on disk (new app): yes.**
- Quickstart: "Start a chat, create a project, or open a folder. ChatGPT can read and modify files in the folder you choose." https://learn.chatgpt.com/docs/quickstart.md
- A *local project* "gives chats access to one or more folders on your computer". By contrast, a ChatGPT (cloud) project "doesn't provide direct access to a folder on your computer". https://learn.chatgpt.com/docs/projects.md
- Work can run **Cloud** (hosted, keeps going after you close the app) or **Work locally** ("Use files, apps, or the browser on your computer"), when enabled for the account. https://learn.chatgpt.com/docs/use-chatgpt.md
- Codex chats run **Local** (directly in the project dir), **Worktree** (Git worktree) or **Cloud**. A cloud task does not get local files: "Your computer's local files … aren't automatically transferred to it." https://learn.chatgpt.com/docs/environments/modes.md
- The app previews generated docs, decks, spreadsheets, PDFs and HTML, and compiles `.tex`. You can annotate a preview to ask for a targeted revision. https://learn.chatgpt.com/docs/artifacts-viewer.md

**File uploads.** You can attach documents, presentations, spreadsheets, PDFs, images and data exports, to summarize, compare, extract or clean them. https://learn.chatgpt.com/docs/use-chatgpt.md

**Appshots (new app; the successor to window-reading).**
- An appshot sends the frontmost window, as an image plus its available text, to a chat. Trigger it by pressing both Command keys (macOS) or both Alt keys (Windows).
- It is stored "locally in the session file". For Google Docs/Gmail it may get only the visible screenshot.
- macOS permissions: Screen & System Audio Recording (image) and Accessibility (text).
- https://learn.chatgpt.com/docs/appshots.md

**Computer Use (agent mode on the desktop).**
- Availability: in the new app on macOS and Windows, with Work and Codex, in supported regions. You install the Computer Use plugin first.
- What it does: ChatGPT can "see and operate graphical user interfaces".
- Approvals: it asks per app, and offers an "Always allow" list.
- Limits: it can't automate terminal apps or ChatGPT itself, and can't approve OS security prompts.
- Windows: it takes over the foreground.
- macOS: an optional "locked use" mode installs an authorization plug-in so a task can run after the Mac locks.
- Permissions on macOS: Screen Recording + Accessibility for "Codex Computer Use".
- https://learn.chatgpt.com/docs/computer-use.md

**Built-in browser, Chrome extension and plugins.**
- The desktop app has a built-in browser. The Chrome extension gives a ChatGPT sidebar in Chrome. https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- Plugins (formerly connectors/apps) link Google Drive, SharePoint, Slack and others. https://learn.chatgpt.com/docs/use-chatgpt.md

**MCP.** "Model Context Protocol (MCP) lets ChatGPT and Codex use tools and information from other systems". Plugins package MCP connections. https://learn.chatgpt.com/docs/extend/mcp.md

**Computer History (macOS, opt-in).** It turns clicks, typing and accessibility text into local Markdown "memories" under `~/.codex/memories/extensions/skysight/`.
- Event files stay on the Mac for up to 48 hours.
- They are sent to OpenAI servers for summarizing. OpenAI "does not retain those event files after processing … and does not use them for training".
- https://learn.chatgpt.com/docs/customization/computer-history.md

**Work with Apps (ChatGPT Classic, macOS).**
- Needs version 1.2025.057+. Open it with Option+Space (Chat Bar) or the "Work with Apps" button.
- It reads Apple Notes, Notion, TextEdit, Quip, Xcode, Script Editor, VS Code and forks, JetBrains IDEs, Terminal, iTerm, Warp and Prompt.
- It includes "the last 200 lines of open panes". Editing works in IDEs only (as a reviewable diff).
- Permissions: it uses the macOS Accessibility API; VS Code needs the "ChatGPT – Work with Code on macOS" extension.
- The content becomes part of chat history.
- https://help.openai.com/en/articles/10119604-work-with-apps-on-macos

**Screen sharing (Classic, macOS).** Shortcuts let you share the main desktop (Cmd+Shift+1) or the active window (Cmd+Shift+2). These come from the 2024-08-06 release notes. https://help.openai.com/en/articles/9703738-chatgpt-macos-app-release-notes

**Record mode.**
- Classic: for Plus, Pro, Business, Enterprise and Edu, macOS only. It captures mic + system audio, with sessions capped at 240 minutes.
- Audio is "deleted afterward"; transcripts and canvases can be used for training if "Improve the model" is on.
- In the new app it is being replaced by a "Meetings plugin" (beta, Mac, Pro/Business). https://help.openai.com/en/articles/11487532-chatgpt-record
- A user reported the Record button missing after migrating: https://github.com/openai/codex/issues/32576 (open, 2026-07-12).

---

## 2. Codex CLI (and Codex in the app / IDE)

**Install** (https://learn.chatgpt.com/docs/codex/cli.md ; https://github.com/openai/codex):
- macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- Windows (PowerShell): `irm https://chatgpt.com/codex/install.ps1 | iex`
- Or `npm install -g @openai/codex`, or `brew install --cask codex`
- Then run `codex` in a project directory and choose Sign in with ChatGPT.
- The repo describes itself as "a lightweight coding agent that runs in your terminal". It is open source under Apache-2.0. Latest release: rust-v0.163.0 (2026-10-15).

**Platforms.**
- macOS (Apple Silicon + x86_64), Linux (x86_64, arm64), and Windows native (PowerShell + native Windows sandbox) or WSL2.
- WSL1 was dropped from 0.115: "WSL1 is no longer supported."
- https://learn.chatgpt.com/docs/windows/wsl.md ; https://learn.chatgpt.com/docs/windows/windows-app.md

**How it works on files.**
- "Codex CLI treats the directory where you start it as the project". `--cd`/`-C` sets the directory explicitly. https://learn.chatgpt.com/docs/projects.md
- It inspects files, makes edits and runs local tools. The docs advise Git checkpoints before and after a task. https://learn.chatgpt.com/docs/codex/cli.md
- `codex exec` runs non-interactively; `codex resume` reopens a session; `--image` attaches screenshots; `--search` turns on live web search.

**Sandbox and approvals.**
- Modes: `read-only`, `workspace-write` (the default low-friction mode) and `danger-full-access`.
- Approval policies: `on-request` and `never`. `untrusted` is retired.
- An `approvals_reviewer = auto_review` setting sends approval requests to a reviewer agent instead of the user.
- UI labels: "Ask for approval", "Approve for me" and "Full access". In the CLI, use `/permissions`.
- https://learn.chatgpt.com/docs/sandboxing.md ; https://learn.chatgpt.com/docs/permission-modes.md

**OS enforcement:**
- macOS: Seatbelt (`sandbox-exec`).
- Linux: `bwrap` + seccomp by default. Landlock is now a legacy option (`codex sandbox landlock` alias still exists).
- Windows: the native MXC sandbox.
- https://learn.chatgpt.com/docs/agent-approvals-security.md

**Network.** "By default, the agent runs with network access turned off". Writes are limited to the workspace. Web search defaults to an OpenAI-maintained *cache*, which reduces prompt-injection risk. https://learn.chatgpt.com/docs/agent-approvals-security.md

**AGENTS.md.**
- "Codex reads `AGENTS.md` files before doing any work." The global file is `~/.codex/AGENTS.md`; project files are found by walking from the Git root down to the current directory.
- The combined cap is 32 KiB by default.
- https://learn.chatgpt.com/docs/agent-configuration/agents-md.md

**MCP.** Add a server with `codex mcp add <name> -- <command>`, or with `[mcp_servers.<name>]` in `~/.codex/config.toml`. Both stdio and remote/OAuth servers are supported. https://learn.chatgpt.com/docs/extend/mcp.md

**Models (as of today).**
- GPT-6.1 Sol (recommended for complex work) and GPT-6 Luna (focused tasks; Free/Go).
- GPT-6 Astra is "Our most capable model" and is suggested for Computer Use.
- GPT-5.6 Sol/Terra/Luna are still available during the rollout.
- GPT-5.5 retired from ChatGPT-sign-in Codex on 2026-10-14.
- Switch with `/model` or `codex --model gpt-6.1-sol`.
- https://learn.chatgpt.com/docs/models.md

**The Codex desktop app** no longer exists as a separate product. It became the new ChatGPT desktop app (Codex mode) on 2026-07-09. The IDE extension (VS Code and forks) remains. https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app ; https://learn.chatgpt.com/docs/codex/ide.md

**Sign-in: ChatGPT plan vs API key.**
- The desktop app, CLI and IDE all support both. Codex Cloud needs ChatGPT sign-in.
- "With an API key, usage follows your API organization's retention and data-sharing settings".
- To use a key in the CLI: `printenv OPENAI_API_KEY | codex login --with-api-key`.
- https://learn.chatgpt.com/docs/auth.md

---

## 3. Pricing and plan requirements

Source: https://learn.chatgpt.com/docs/pricing.md

- "ChatGPT Work and Codex are included in your ChatGPT Free, Go, Plus, Pro, Business, Edu, or Enterprise plan". Work and Codex share one usage pool.
- **Free ($0) and Go ($8/mo):** GPT-6 Luna in the desktop app, "subject to rollout". No image generation on Free.
- **Plus ($20/mo):** Codex on web, CLI, IDE and iOS; GPT-6.1 Sol and GPT-6 Luna; you can buy extra credits.
- **Pro: $100, $200 or $500/mo.** No five-hour limit currently; Ultrafast mode on Pro $500.
- **Business:** $20/user/mo billed annually ($25 monthly), 2+ users. Includes "No training on your business data by default".
- **Enterprise/Edu:** contact sales; adds data retention and residency controls.
- **API key:** pay-as-you-go at API rates; CLI/SDK/IDE only, with no cloud features.
- Limits are counted per 5-hour window and vary by task. Check them with `/status` in the CLI or at chatgpt.com/codex/settings/usage.
- Desktop Voice costs about $0.05/min of usage budget.
- The 2026-07-09 announcement confirms the desktop app with Chat/Work/Codex is on "every plan, including Free". https://openai.com/index/chatgpt-for-your-most-ambitious-work/

---

## 4. Privacy and data

**What leaves the machine.**
- "Local files can remain on the device, but relevant file excerpts, prompts, screenshots, browser content, or tool results may be sent to OpenAI services". Also: "Local execution does not mean offline or device-only model inference." https://learn.chatgpt.com/docs/enterprise/chatgpt-work-local-security.md
- Appshots share the captured image and text with ChatGPT. Computer Use screenshots fall under your ChatGPT data controls. https://learn.chatgpt.com/docs/appshots.md ; https://learn.chatgpt.com/docs/computer-use.md
- Codex CLI keeps session transcripts locally under `CODEX_HOME`, configurable with `history.persistence`. https://learn.chatgpt.com/docs/agent-approvals-security.md

**Training opt-out.**
- With "Improve the model for everyone" off, "your new conversations won't be used to train OpenAI models."
- On personal plans the setting "also applies to your Codex tasks".
- Codex has a *separate* "Include environments" setting for environment context, which the ChatGPT toggle does not change.
- Thumbs-up or thumbs-down feedback can still send the whole conversation for training.
- https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt

**Temporary Chat.**
- These chats do not appear in history, do not update memories, and are not used for training. They "may be retained for up to 30 days for safety purposes". (Same data-controls article.)
- The new desktop app has a "New temporary chat (ChatGPT only)" shortcut, Cmd+Shift+N. It is not available in Codex mode, per the commands reference in llms-full.txt.

**Deletion and retention.**
- Deleted chats are removed "within 30 days" unless de-identified or held for legal or security reasons. https://help.openai.com/en/articles/10119604-work-with-apps-on-macos
- Workspace retention varies by data type: compliance logs 30 days; Enterprise transient uploads can expire after 48 hours. https://learn.chatgpt.com/docs/enterprise/chatgpt-work-overview.md

**Business plans.**
- "By default, OpenAI does not use content from ChatGPT Business, Enterprise, Edu … to train its models." https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt
- Local computer access with Work Cloud "does not provide strict zero data retention". https://learn.chatgpt.com/docs/enterprise/chatgpt-work-local-security.md

**API-key use** follows the API organization's retention settings, not ChatGPT's. https://learn.chatgpt.com/docs/auth.md

---

## 5. Local or open models

**Codex CLI with local models: yes.**
- `--oss` uses "a local open source provider such as Ollama or LM Studio". Choose one with `--local-provider`, or set `oss_provider = "ollama"` / `"lmstudio"` in config. If neither is set, interactive mode prompts you to choose and `codex exec` exits with an error.
- https://learn.chatgpt.com/docs/config-file/config-advanced.md (found via llms-full.txt)
- Custom providers (any OpenAI-compatible base URL, e.g. `http://localhost:11434/v1`, Mistral, Azure) and a built-in Amazon Bedrock provider are supported.
- A provider can be configured with no auth, which "is useful for local models". https://learn.chatgpt.com/docs/auth.md
- The ChatGPT desktop app itself is not documented as running local models. Its local mode still calls OpenAI servers (see §4).

**gpt-oss.**
- gpt-oss-120b (fits one 80 GB GPU) and gpt-oss-20b. Apache 2.0, text-only reasoning models.
- "not served through the OpenAI API and are not available in ChatGPT."
- They run on vLLM, Ollama, llama.cpp or LM Studio. OpenAI "does not receive or process the data you send to these self-hosted models". OpenAI does not provide support for self-hosted setups.
- https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss ; https://openai.com/open-models/ ("designed to run locally on desktops, laptops").
- Launch date 2025-08-05 (snippet). No newer open-weight release was found.

---

## 6. Concrete local-file tasks for non-programmers

Examples OpenAI itself gives, all doable in the desktop app's Work mode on a chosen folder:
- "Combine the spreadsheets in this folder, clean inconsistent records … create a concise report with charts". https://learn.chatgpt.com/docs/quickstart.md
- "Review the reports and notes in this project … create a one-page decision memo". (quickstart)
- Clean a messy CSV "into a clean copy without changing the original". https://learn.chatgpt.com/docs/app.md
- Analyze a data export into interactive visuals; turn scattered sources into a PRD; synthesize feedback. (app.md)
- Create or refine documents, decks, spreadsheets and PDFs with an in-app preview and annotations. https://learn.chatgpt.com/docs/artifacts-viewer.md
- Schedule recurring work, such as a daily brief or refreshing a deck when feedback arrives. https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- Show it a window via Appshot (an email, a settings panel, an error) and ask for the next step. https://learn.chatgpt.com/docs/appshots.md
- Turn meetings into notes and action items (Record / Meetings plugin, Mac). https://help.openai.com/en/articles/11487532-chatgpt-record

---

## 7. Limits and risks

- **Not offline.** Local execution still sends excerpts, screenshots and tool output to OpenAI (§4).
- **Full access is dangerous.** On Windows, full access "might perform unintentional destructive actions that can lead to data loss". https://learn.chatgpt.com/docs/windows/windows-app.md
- **Prompt injection.** Web pages or READMEs can make the agent "fetch and follow untrusted instructions"; Computer History raises this risk. https://learn.chatgpt.com/docs/agent-approvals-security.md ; https://learn.chatgpt.com/docs/customization/computer-history.md
- **Computer Use** acts in signed-in browsers "as coming from your account". It takes over the Windows desktop, and the docs say to stay present for payments and credentials. https://learn.chatgpt.com/docs/computer-use.md
- **Accuracy.** "A polished response can still be incomplete or wrong". High-stakes decisions need expert review. https://learn.chatgpt.com/docs/use-chatgpt.md
- **Usage limits.** They are opaque and task-dependent; image generation burns them 3–5x faster. https://learn.chatgpt.com/docs/pricing.md
- **Fragmentation.** Features differ between ChatGPT Classic and the new app (Work with Apps and Record live in Classic), across plans, regions and rollouts, and Linux is still in preview. Features "depend on your plan, platform, region, rollout". https://learn.chatgpt.com/docs/use-chatgpt.md
- **Linux sandbox setup.** It needs `bubblewrap`, and Ubuntu 24.04 needs an extra AppArmor profile. https://learn.chatgpt.com/docs/sandboxing.md
- **Local models (`--oss`)** are far weaker than the hosted models and need serious hardware: gpt-oss-20b needs about 16 GB of memory per the snippet sources. This is not verified on an OpenAI page beyond "run locally on desktops, laptops".
