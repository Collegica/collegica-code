The notes behind the local-agent guide: the components, the three ways of serving a model, and the measured run on a 24 GB Mac.

# Research Reports

* [A local agent on your own machine — plan and research](local-agent.md) - What was verified and against what, the decisions behind the guide, what was and was not run on this machine, and the traps hit.

# Research Notes

* [Good enough for the job — from Greg Isenberg's video](isenberg.md) - What a thirty-nine-minute founder's map of local AI claims — the four pieces, the vocabulary, the Gemma family, three ways to run it, the local-then-hosted pipeline, ten runs then a comparison — what the guide took from it, where it disagrees, and that it is sponsored.
* [LM Studio Bionic — an agent with the runtime inside it](bionic.md) - What Bionic is from its own docs: projects and sessions, the local / remote / cloud choice per session and what costs credits, skills in the Agent Skills format, and LM Studio as a server for Hermes. Not run.
* [Prefill, the KV cache, and a Strix Halo — from Rob Braxman's video](braxman.md) - What a twenty-minute practitioner video claims — the 16K-token agent prompt, prefill versus generation, the KV cache, four tuning levers, 688/53 tokens a second on gpt-oss-120b — with every flag checked against llama.cpp's README and none of the numbers reproduced.
* [The measured run — Gemma 4 12B through Ollama and Hermes on a 24 GB Mac](run.md) - Cold load, warm generation speed, memory, the context check, and a tool-using task end to end, with the thinking cost an interviewer pays.
* [The three components — Gemma 4, Ollama, Hermes and Hermes Desktop](components.md) - Gemma 4's sizes, modalities and 4-bit memory table from Google; Ollama's tags and the 4,096-token default; Hermes's 64K rule and where Desktop really lives on disk.
* [Three ways to serve a local model — Ollama, Docker Model Runner, vLLM](serving-options.md) - The endpoint, the install, the context setting and the tool-call flags for each, with which of the three was run on this machine and why the other two were not.
