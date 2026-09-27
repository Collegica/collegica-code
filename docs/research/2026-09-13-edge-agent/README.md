# An agent in your pocket — plan and research

Plan and notes for the third AI guide: what an agent can honestly do on a
phone, with Gemma 4 through LiteRT-LM — the Google AI Edge Gallery app,
FunctionGemma as a tool-calling model, and the Kotlin API — and where the
same runtime's server puts the phone in front of Hermes. Started
2026-09-13, after *An Agent on Your Own Machine*.

Audience: the reader of the local-agent guide who now wants the same
thing on the device that is actually with them — and wants the numbers
before buying anything.

## What was verified, and how

| Claim | Checked against |
|---|---|
| LiteRT-LM: platforms, five language bindings, tool calling, MTP drafters, v0.17.0 | Repository README and releases, read in full |
| Gemma 4 E2B/E4B files, sizes, quantisation, 32K context, NPU builds | `litert-community` model cards and file lists on Hugging Face |
| Google's phone, laptop and Raspberry Pi benchmarks for E2B and E4B | The Gemma 4 page on developers.google.com, tables copied whole — [`notes/litert-lm.md`](notes/litert-lm.md) |
| The Kotlin, Python, Swift and JavaScript APIs; the CLI's commands | The developer pages and `litert-lm --help`, 0.17.0 |
| The Gallery's features, requirements, skills, MCP, Mobile Actions | Gallery repository README, `skills/`, `mcp/`, `Function_Calling_Guide.md` — [`notes/gallery.md`](notes/gallery.md) |
| FunctionGemma: 270M, Gemma 3 base, 58 → 85 % after fine-tuning | Its docs page and Hugging Face card |
| Hermes on Android: install, what works, what does not | Hermes's Termux page |
| E2B and E4B benchmarks, a two-tool task, the server, Hermes through it | Run on this Mac — [`notes/laptop-run.md`](notes/laptop-run.md) |
| The Kotlin example, both backends, on real hardware | Run on a Galaxy S26 Ultra — [`notes/phone-run.md`](notes/phone-run.md) |
| The Gallery's own Benchmark screen against Google's claimed table | Run on the same S26 Ultra, app 1.0.19 — [`notes/phone-run.md`](notes/phone-run.md) |

Not run: the E4B, FunctionGemma, the Gallery's MCP and skills features,
and Hermes on Termux — all still documented from their sources, not
measured. Everything else in the "not run" column above the phone rows
was closed on 2026-09-14 when a Galaxy S26 Ultra was connected.

## Decisions

1. **Three tiers, in the order a reader meets them:** the app (install the
   Gallery, run the benchmark screen), the action model (FunctionGemma and
   Mobile Actions — the thing that is different on a phone), the API (the
   Kotlin example, and the CLI on a laptop first because the same file
   runs there).
2. **Google's numbers, labelled, beside numbers measured here.** The Mac
   in Google's table is the Mac on this desk, so the reader can see the
   gap between a benchmark bench and a working machine before reading the
   phone rows.
3. **Prefill is the phone number that matters — and the measured one, not
   the claimed one.** The local-agent guide established the two-number
   reading; this one applies it, then checks it: Google's claimed 3,808
   tokens a second on an S26 Ultra GPU became a measured 1,632 with
   Google's own benchmark app, on the phone Google's own table names.
4. **Hermes is the bridge, not the point.** `litert-lm serve` speaks
   OpenAI; Hermes runs on Termux; the two have not been tried together on
   a phone, and the guide says so. The 64K rule is documented as hit.
5. **No claims about "the phone".** Which chip, which backend, which
   file; each row names them.

## Traps hit

- `litertlm-android:0.17.0` needs the Kotlin 2.4 plugin; on 2.2 the
  compiler cannot read the library's metadata.
- The GPU backend writes a weight-cache file beside the model on first
  load; a model pushed to `/data/local/tmp` fails with "Permission
  denied" because the app cannot create a new file in shell's directory.
  Push the model to the app's own external-files directory instead —
  see [`notes/phone-run.md`](notes/phone-run.md).
- HiggsField's image defaults are 1k and low quality; resolution and
  quality must be passed explicitly for a hero.
- The first benchmark and the E4B download ran while other things ran;
  the numbers in the note were re-taken alone where it mattered.
- A plain-JSON proxy cannot sit between Hermes and the server: Hermes
  streams. The proxy that worked probes each request once, non-streaming,
  for the token count.
- The Hermes profile `pocket` on this machine declares a 64,000-token
  context the model does not have. It is there for the next test, not
  for use.

## Files

- [`notes/litert-lm.md`](notes/litert-lm.md) — the runtime, the APIs, Google's tables.
- [`notes/gallery.md`](notes/gallery.md) — the app, skills, MCP, FunctionGemma, Hermes on Termux.
- [`notes/laptop-run.md`](notes/laptop-run.md) — every command run on the Mac and what came back.
- [`notes/phone-run.md`](notes/phone-run.md) — the Galaxy S26 Ultra run: the storage-permission trap, both backends, and the Gallery's own benchmark against Google's claimed table.
- [`example/owl_tools.py`](example/owl_tools.py) — the two-tool preset for the CLI.
- [`example/android/`](example/android/) — the Kotlin app, built and run on real hardware.
- [`hero.md`](hero.md) — the hero image and how it was made.
