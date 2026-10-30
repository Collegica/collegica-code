# LeRobot on a machine with no GPU and no Hugging Face — the run

The question: with the weights out of reach, what can be verified about the
open VLAs from the code that runs them? LeRobot — the framework that ships
SmolVLA, π0, π0.5, GR00T, X-VLA, EO-1, EVO-1, MolmoAct2 and WALL-OSS as
policies — was installed and its policy configurations read from the
installed package, on 13 September 2026.

## The machine

A cloud Ubuntu 24.04.4 container: 4 vCPUs (Intel Xeon @ 2.10 GHz), 15 GB
RAM, no GPU, Python 3.10–3.13 available, `uv` installed. `huggingface.co`
is blocked by the session's network policy (403 at the proxy), so no model,
config or dataset could be downloaded from the Hub; PyPI and GitHub were
reachable.

## Two installs, two versions

**Python 3.11, `pip`:**

```bash
python3.11 -m venv .venv && . .venv/bin/activate
time pip install "lerobot[smolvla]"
```

4 min 13 s wall; an **8.3 GB** environment; and `lerobot 0.4.4` — the
February 2026 release — with torch 2.10.0, transformers 4.57.6. Not because
0.4.4 is current: because 0.5.0 onward is `requires_python >= 3.12`, and pip
silently picks the newest release the interpreter is allowed to have.
`pip index versions lerobot` under 3.11 says the same, "lerobot (0.4.4)",
with no hint that six newer releases exist.

**Python 3.12, `uv`:**

```bash
uv venv --python 3.12 .venv
time uv pip install --python .venv/bin/python "lerobot[smolvla]"
```

1 min 5 s wall; a **4.9 GB** environment; `lerobot 0.6.1` (3 August 2026),
torch 2.11.0+cu130, transformers 5.5.4. The CUDA-enabled torch wheel
installs on a machine with no GPU and falls back to CPU at run time.

## Reading the configurations

[`configs.py`](configs.py) imports LeRobot, lists its policy packages, and
instantiates each VLA's configuration dataclass with its defaults, printing
the fields that describe the model's shape. No network is needed for most
of them; none was available.

```
lerobot 0.6.1; import 10.11s
20 policy packages: act, diffusion, eo1, evo1, fastwam, gaussian_actor, groot,
lingbot_va, molmoact2, multi_task_dit, pi0, pi05, pi0_fast, rtc, smolvla, tdmpc,
vla_jepa, vqbet, wall_x, xvla
WARNING:root:No accelerated backend detected. Using default cpu, this will be slow.
```

| Policy | Backbone (default) | Chunk / executed | Images | Head |
|---|---|---|---|---|
| `smolvla` | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct`, `num_vlm_layers = 16`, expert width × 0.75 | 50 / 50 | padded to 512 × 512 | flow matching |
| `pi0` | `paligemma_variant = gemma_2b`, `action_expert_variant = gemma_300m` | 50 / 50 | 224 × 224 | flow matching |
| `pi0_fast` | same | 50 / 50 | 224 × 224 | FAST tokens |
| `pi05` | same | 50 / 50 | 224 × 224 | flow matching |
| `groot` | `base_model_path = nvidia/GR00T-N1.7-3B` | 40 / 40 | 256 × 256 | flow-matching DiT |
| `xvla` | Florence-2 config, `tokenizer_name = facebook/bart-large`, `len_soft_prompts = 32` | 32 / 32 | — | flow matching |
| `eo1` | `Qwen/Qwen2.5-VL-3B-Instruct` — **could not instantiate**: the config fetches the backbone's configuration from the Hub at construction (`OSError: Can't load the configuration of 'Qwen/Qwen2.5-VL-3B-Instruct'`) | 16 / 16 (from source) | 64–128 patches of 28 px (from source) | flow matching |
| `evo1` | `OpenGVLab/InternVL3-1B-hf` | 50 / 50 | 448 × 448 | `action_head = flowmatching` |
| `molmoact2` | (set at load time) | 30 / 30 | — | flow-matching expert |
| `wall_x` | `x-square-robot/wall-oss-flow` | 32 / 32 | — | `prediction_mode = diffusion` |
| `vla_jepa` | (world-model line) | 7 / 7 | — | — |

All defaults are float32; every policy warns that it will run on CPU
"and this will be slow." The `dtype` field on the π0 family and X-VLA
accepts `bfloat16`.

## What this shows, and what it does not

- The shape is the same everywhere: a named VLM backbone, an action head,
  and a chunk of 16–50 future actions predicted at once and executed before
  the model is asked again. The chunk sizes above are the framework's
  defaults, not the papers' — but they are what a `lerobot-train` run gets
  unless told otherwise.
- The Python-version trap from the Isaac Sim article repeats exactly: a
  3.11 interpreter sees a six-month-old LeRobot and nothing newer.
- One configuration (EO-1) needs the Hub to exist at all. The others hold
  their shape in code; their weights, of course, do not.
- Not run: any model. No weights could be fetched, so nothing was loaded,
  timed or evaluated — the 450M figure for SmolVLA, the VRAM tables, the
  success rates, are the projects' numbers, not this machine's. The
  hardware guide's own verdict on this class of machine, "Don't train. Use
  Colab or rent a GPU," stands.
