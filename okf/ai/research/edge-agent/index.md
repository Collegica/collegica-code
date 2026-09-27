The notes behind the pocket-agent guide: LiteRT-LM and its APIs with Google's phone numbers, the AI Edge Gallery and FunctionGemma, and the runs on a 24 GB Mac — CLI, tools, server, Hermes through the server.

# Research Reports

* [An agent in your pocket — plan and research](edge-agent.md) - What was verified and against what, the decisions behind the guide, what was run on this Mac, what was run on a Galaxy S26 Ultra, and the traps hit on both.

# Research Notes

* [LiteRT-LM — the runtime, its APIs, and Google's numbers](litert-lm.md) - The runtime and its five language bindings, the .litertlm files and their quantisation, the CLI's commands, the Kotlin tool API, and Google's benchmark tables for Gemma 4 E2B and E4B on phones, laptops and a Raspberry Pi.
* [The AI Edge Gallery, FunctionGemma, and Hermes on Termux](gallery.md) - What the Gallery app does with skills, MCP and Mobile Actions; how FunctionGemma's 270M parameters call tools on a phone; and what Hermes's Termux page says works on Android.
* [The laptop run — Gemma 4 E2B and E4B through LiteRT-LM on a 24 GB Mac](laptop-run.md) - Every command run for the guide and what it returned: benchmarks on CPU and GPU, a two-tool task from a preset, the OpenAI-compatible server, Hermes through that server, and the Android example built.
* [The phone run — Gemma 4 E2B on a Galaxy S26 Ultra](phone-run.md) - A storage-permission trap that blocks the GPU backend on /data/local/tmp and its fix; the Kotlin example on both backends, including the CPU summary omission reproduced from the laptop; and the AI Edge Gallery's own Benchmark screen measured against Google's claimed table on the exact phone that table names.
