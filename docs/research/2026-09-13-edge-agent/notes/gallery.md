# The AI Edge Gallery, FunctionGemma, and Hermes on Termux, read 2026-09-13

## Access and confidence

- **Read in full:** the Gallery repository README (google-ai-edge/gallery,
  release 1.0.19 on 2026-09-02), its `Function_Calling_Guide.md`,
  `mcp/README.md` and `skills/README.md`, the FunctionGemma docs page and
  Hugging Face card, the Mobile Actions docs page, and Hermes's
  Android/Termux installation page.
- **Not run:** the Gallery app itself (no phone in the room yet; the macOS
  build exists and was not tried), FunctionGemma, Hermes on Termux.

## The Gallery app

"A gallery that showcases on-device ML/GenAI use cases and allows people
to try and use models locally." Android 12 and up, iOS 17 and up, and a
macOS download. Play Store id `com.google.ai.edge.gallery`; App Store id
6749645337; APKs on GitHub releases. Features as the README names them:
AI Chat with Thinking Mode; Ask Image; Audio Scribe ("transcribe and
translate voice recordings"); Prompt Lab; **Agent Skills** ("augment model
capabilities with tools like Wikipedia for fact-grounding, interactive
maps, and rich visual summary cards… load modular skills from a URL");
**Mobile Actions** ("offline device controls and automated tasks powered
entirely by a finetune of FunctionGemma 270m"); Tiny Garden; **Model
Management & Benchmark** ("run benchmark tests to understand exactly how
each model performs on your specific hardware"). "All model inferences
happen directly on your device hardware."

### Skills (`skills/README.md`)

Each skill is a `SKILL.md` with metadata and instructions; the LLM sees
the names and descriptions appended to its system prompt and "invokes it
automatically" when a request matches. Because "on-device LLMs operate
within a sandboxed mobile environment" and "cannot easily execute
arbitrary system commands," a skill executes either as **JavaScript in a
hidden webview** or as a **native app intent** (email, messages). Skills
load from the community list, a URL, or a local file.

### MCP (`mcp/README.md`, "currently experimental")

The app is an MCP client: "connects to configured MCP servers, dynamically
loading and parsing JSON schemas for available tools," injects them into
the on-device model's prompt, routes calls to the server, with
"per-invocation prompts and toggleable 'always allow' rules." Servers must
speak **StreamableHTTP**, not stdio — the README wraps `mcp-server-fetch`
with `supergateway --stdio 'mcp-server-fetch' --outputTransport
streamableHttp` — and "requires the local server to have a publicly
routable URL," suggesting a Cloudflare quick tunnel. Recommended model:
"Gemma-4-E4B for better model quality." Cloud servers get custom headers
for auth; OAuth is "in progress."

### Function calling in the app (`Function_Calling_Guide.md`)

Mobile Actions is built on the Kotlin tool API: a `MobileActionsTools`
class implementing `ToolSet`, one `@Tool(description = …)` method per
action (flashlight on/off, create contact, send email, show map, open
Wi-Fi settings, create calendar event), each `@ToolParam` described; the
method hands an `Action` to the app, which performs it with an `Intent` or
a system service, and returns `mapOf("result" to "success")` to the model.
The conversation is created with `listOf(tool(MobileActionsTools(…)))`.
Adding an action is three edits and `./gradlew installDebug`.

## FunctionGemma

"A specialized version of our Gemma 3 270M model tuned for function
calling," 32K context, Gemma license, open weights "licensed for
responsible commercial use." Intended "to be fine-tuned for your specific
function-calling task, including multi-turn use cases." Chat template
uses a `developer` role ("You are a model that can do function calling
with the following functions") and emits calls like
`<start_function_call>call:get_current_temperature{location:<escape>London<escape>}<end_function_call>`.
Mobile Actions accuracy on the card: 58% base, 85% after fine-tuning. The
fine-tuned `.litertlm` builds are `litert-community/functiongemma-270m-ft-mobile-actions`:
275 MB generic (`mobile_actions_q8_ekv1024.litertlm`), 543–547 MB for
Tensor G5/G6 NPUs. GGUF and MLX conversions exist from unsloth,
lmstudio-community and mlx-community, so the same model runs through
Ollama or LM Studio on a laptop.

## Hermes on Android (Termux)

Hermes lists "Linux / macOS / WSL2 / Android (Termux)" and has a Termux
page: the one-line installer, or `pkg install -y git python clang rust
make pkg-config libffi openssl nodejs ripgrep ffmpeg`, clone, venv,
`export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"`, `pip install
-e '.[termux]' -c constraints-termux.txt`, symlink `hermes` into
`$PREFIX/bin`. Works: CLI, cron, PTY terminal, Telegram gateway, MCP,
memory, ACP. Does not: voice transcription (no ctranslate2 wheel), Docker
isolation, browser automation, and Android "may still suspend Termux
background jobs." Python must be ≥ 3.11 and < 3.14 while "current Termux
ships 3.14.x" — a version pin is needed. "Tier 2 platform with best-effort
maintenance." Model configuration is the usual `hermes model` or
`~/.hermes/.env`; nothing on the page about a model on the phone itself.

The bridge the article proposes, documented and not run: `litert-lm-api`
publishes `android_23_arm64_v8a` wheels, so `litert-lm serve` can run in
Termux and Hermes can point at `http://127.0.0.1:9379/v1`. Hermes's own
rule that tool use needs a 64K context (providers page, from the local
agent article) meets a model whose card says 32K; what Hermes does with
that is the first thing to test when a phone is on the desk.
