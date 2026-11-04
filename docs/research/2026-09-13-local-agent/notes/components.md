# The three components — what each is, checked at the source on 2026-09-13

## Access and confidence

- **Read in full:** Google's Gemma 4 model overview and its inference-memory
  table; Ollama's Gemma 4 library page and tag list, quickstart, macOS page,
  FAQ, and its Hermes and Hermes Desktop integration pages; Hermes's
  installation, Desktop, model-providers and configuration pages; the local
  Hermes checkout (`hermes_cli/main_desktop.py`, `toolsets.py`).
- **Measured on this machine:** see [`run.md`](run.md).
- **Not read:** the Gemma 4 licence text in full (its page was fetched; the
  terms are summarised from Google's overview, which says "open weights and
  permit responsible commercial use"). Read the licence before shipping a
  product on it.

## Gemma 4 (Google)

Google's overview: text, image, video and audio input (audio natively on
E2B, E4B and 12B); 128K context on the small models, 256K on the medium;
built-in function calling; native system prompts. Five sizes:

| Size | Kind | BF16 | 8-bit | 4-bit (Q4_0) |
|---|---|---|---|---|
| E2B | edge | 11.4 GB | 5.7 GB | 2.9 GB |
| E4B | edge | 17.9 GB | 8.9 GB | 4.5 GB |
| 12B | dense, "unified" multimodal (encoder-free) | 26.7 GB | 13.4 GB | 6.7 GB |
| 26B A4B | mixture of experts, 4B active | 57.7 GB | 28.8 GB | 14.4 GB |
| 31B | dense | 69.9 GB | 34.9 GB | 17.5 GB |

Those are weights only; the context window's key/value cache comes on top.
Weights are on Kaggle and Hugging Face; Google publishes QAT (quantisation-
aware-trained) 4-bit variants for llama.cpp, LM Studio and Ollama.

## Ollama

Runs models locally behind an OpenAI-compatible API on port 11434. Library
tags for `gemma4`, with on-disk size and the context each advertises:

| Tag | Size | Notes |
|---|---|---|
| `gemma4:e2b` | 7.2 GB | |
| `gemma4:e4b` = `gemma4:latest` | 9.6 GB | what `ollama run gemma4` gets you |
| `gemma4:12b` | 7.6 GB | smaller on disk than e4b; the QAT 4-bit |
| `gemma4:26b` | 19 GB | MoE, 4B active |
| `gemma4:31b` | 20 GB | |

All tags: 128K context window, text and image input. Ollama's own Hermes page
recommends `gemma4` at "~16 GB VRAM"; its Gemma 4 page lists `ollama launch
hermes --model gemma4` as a first-class integration.

Install: the app from ollama.com/download (macOS Sonoma or newer; M-series
for GPU, x86 CPU-only). The app puts the `ollama` CLI on the path with your
permission. Models live in `~/.ollama`. `brew install ollama` gives the server
and CLI without the app. Uninstall is documented file by file on the macOS page.

**Context length.** Ollama's default context is 4,096 tokens (FAQ). Set
`OLLAMA_CONTEXT_LENGTH` on the server: `OLLAMA_CONTEXT_LENGTH=65536 ollama
serve`, or for the macOS app `launchctl setenv OLLAMA_CONTEXT_LENGTH 65536`
then restart the app (FAQ). It cannot be set through the OpenAI-compatible API.

## Hermes Agent and Hermes Desktop

Hermes (Nous Research, MIT) is the agent; Desktop is "a native app built
around the same agent you get from the CLI — same config, same keys, same
sessions, same skills, same memory" (Hermes's Desktop page). Recommended
install on macOS and Windows: the Hermes Desktop installer, which installs
the CLI and the app together. Or the CLI installer (`curl … install.sh |
bash`) then `hermes desktop`, which builds the packaged app on first launch.

On this machine: the CLI is v0.21.2 at `~/.hermes/hermes-agent`; the Desktop
app that `hermes desktop` built is `apps/desktop/release/mac-arm64/Hermes.app`
inside that checkout — Electron, 311 MB, bundle version 0.17.2, id
`com.nousresearch.hermes`. (`/Applications/Hermes.app` is the *setup* app,
`com.nousresearch.hermes.setup`, not Desktop.)

**Hermes and a local model.** Hermes's providers page: local Ollama is the
"Custom endpoint" flow — base URL `http://localhost:11434/v1`, no key — or in
`config.yaml`: `model: {default: <tag>, provider: custom, base_url:
http://localhost:11434/v1, context_length: 64000}`. And the sentence the whole
install turns on: **"Hermes Agent requires at least 64,000 tokens of context
for agent use with tools. Smaller windows are rejected at startup."** With
Ollama's 4,096 default, the first `hermes chat` fails. The providers page
calls this "the #1 source of confusion when integrating Ollama with tools
like Hermes."

Profiles: `hermes profile create <name>` makes an isolated instance with its
own config, keys and skills, and a wrapper command of the same name
(`exec hermes -p <name> "$@"`). Desktop honours profiles.
