# Prefill, the KV cache, and a Strix Halo — from Rob Braxman's video, added 2026-09-13

## Access and confidence

- **Read in full:** the video's description (which carries the exact
  `llama-server` command, the build, and the two speed figures) and its
  auto-generated English captions, 2,943 words, downloaded with yt-dlp and
  read end to end. *Finally! A Local AI Breakthrough! So Much Faster!*, Rob
  Braxman Tech Deep Dive, 20 min 12 s, published 2026-09-11.
- **Checked against the source:** every flag in his command, against
  llama.cpp's `tools/server/README.md` on `master` the same day; the Vulkan
  build line against `docs/build.md`.
- **Not verified:** any of his numbers. Different hardware (AMD, 128 GB) from
  this guide's (Apple M4, 24 GB); nothing was re-run. Auto-captions
  mis-hear product names ("Open Cloth" for OpenClaw, "a llama" for Ollama);
  the description settles the ones that matter.

## What he claims

- **Hardware:** AMD Strix Halo, 128 GB unified memory, up to 96 GB for the
  GPU, "around $4,000 nowadays"; "the current sweet spot."
- **Models:** gpt-oss-120b MXFP4 (~63 GB file, "about 69 GB of VRAM") for
  reasoning and the private work — financial, tax, retirement, medical —
  he will not send to a hosted model; Qwen 3.6 35B (MoE, 12 GB) for coding,
  loaded alongside; Muse Glimmer (Meta, dense) also tried. Harness: OpenClaw;
  he names Hermes and Codex as alternatives.
- **The two metrics:** prefill (input, "encode") and output ("decode")
  tokens per second. A typical agent prompt "around 16K tokens." At his
  original ~100 prefill TPS that was "around 3 minutes just to read the
  prompt"; a hosted model, 3–10 s. Output mattered less: "most prompts to
  the AI result in short responses."
- **After tuning:** 688 prefill / 53 output TPS on gpt-oss-120b (from
  ~100 / 20); prefill of 16K now ~24 s, and after the first turn "often
  down to 1 or 2 seconds" because of the KV cache — the directives "never
  change," so only new tokens are read. Qwen 3.6 35B prefills at 1,071 TPS.
- **The four levers:** (1) llama.cpp compiled directly instead of Ollama —
  "a doubling"; (2) Vulkan over ROCm on AMD — "at any point in time one of
  these will be better; as of this moment, Vulkan is faster"; (3) a GPU
  boost-clock override; (4) MoE models — "often five times faster than the
  dense model counterparts."
- **Build and command:** `cmake -B build -DGGML_VULKAN=ON`; env
  `HIP_VISIBLE_DEVICES=-1`, `AMD_VULKAN_ICD=RADV`; `llama-server -m
  gpt-oss-120b-MXFP4.gguf -ngl 999 -c 131072 --jinja -fa on -ub 512 -b 2048
  --reasoning off --reasoning-format deepseek --cache-prompt --host 0.0.0.0
  --port 8081`.
- **Cautions:** context corruption on a local model when the context grows
  and compaction runs — "watch the context level… trim the context or
  start a new session"; hosted models have "a million tokens" and hide
  this.
- **Economics:** 1.2 billion tokens in one week-long job on a hosted open
  model (GLM 5.2), "around $70 for the week"; the same on a frontier API
  "over 10 grand a week." Local: "slower but free, and there are no limits."
- **Hardware advice:** a $4,000 Strix Halo "can now be justified"; a $5,500
  DGX Spark "even better" but "10% faster"; he argues against multi-3090
  rigs, a single RTX Pro 6000, or a $14K Mac Studio on cost.

## What the guide takes, and what it leaves

Taken: the prefill/generation distinction and the 16K-token agent prompt;
the KV cache as the mechanism that makes loops feasible; MoE as the size
to prefer; the flag set, re-described from the README (where `--jinja` and
`--cache-prompt` are now defaults); the context-corruption caution; his
numbers, attributed as his. Left: the OpenClaw harness, the clock-boost
procedure, the hardware buying advice beyond one sentence, and every
claim about model "smarts."

What it corrects in the guide's own account: the "about 60 tokens a
second" prompt figure came from a 30-token prompt and is not a prefill
rate; the twenty-minute run was thinking *and* re-reading, and only the
first was measured.
