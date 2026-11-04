# Words in, joints out — plan and research

Plan and notes for the second Robotics article: vision-language-action
models — what the category is, the one shape nearly all of them share,
which ones can be downloaded, what they ask of the person who wants to
train one, and what could be checked from a machine with no GPU and no
access to the model hub. Started 2026-09-13, the same day as the NVIDIA
stack article, which it follows: GR00T N1.7 there is one row here.

Audience: someone who has seen a robot follow a spoken instruction in a
demo video and wants to know what is inside, what "open" means for each
one, and whether the $100 arm in the LeRobot community is a real way in.

## What was verified, and how

| Claim | Checked against |
|---|---|
| LeRobot's versions, dates, Python requirement, extras | PyPI's JSON API, queried from this machine — [`notes/models.md`](notes/models.md) |
| What each open model is, its backbone, head, licence, hardware line | The projects' GitHub READMEs, docs and licence files, read in full (raw `main`) |
| Each model's default backbone, chunk size, image size in the framework that runs it | LeRobot 0.6.1 installed here on Python 3.12 and its configuration dataclasses instantiated — [`notes/lerobot-run.md`](notes/lerobot-run.md) |
| The papers' figures (RT-2's tokens, Open X-Embodiment's counts, OpenVLA vs RT-2-X, π0's architecture, SmolVLA's corpus), and everything about Helix, Gemini Robotics, π0.6/π0.7 | Search-result snippets of the papers' and vendors' pages plus trade press — `arxiv.org`, `huggingface.co`, `pi.website`, `figure.ai`, `deepmind.google` and the `github.io` project pages were blocked by this session's egress policy. Marked *(search)* in the notes; lower confidence |

Not verified: any model's behaviour. Hugging Face was unreachable, so no
weights were downloaded; nothing was loaded, timed or evaluated. The
article says so, and quotes success rates and speeds as the projects'
claims, never as measurements.

## Decisions

1. **One shape, then the list.** The category is easier to hold as
   *backbone + action head + chunk* than as a dozen names; the names come
   after the shape, and the table of chunk sizes read from the installed
   code is the evidence that the shape is real.
2. **Open means three different things**, and the article keeps them apart:
   code licence, weights licence, and whether the weights exist at all.
   OpenVLA's weights carry Llama's licence; GR00T's carry NVIDIA's; π0.5 is
   Apache-2.0 end to end; π0.7 and Helix and Gemini Robotics 1.5 have none.
3. **LeRobot is the through-line.** Nine of the eleven VLAs the article
   names ship as LeRobot policies, its hardware guide is the only
   cross-model VRAM table anyone publishes, and its dataset format is what
   "your data" means in practice. It gets its own section.
4. **Write from the reader's machine.** No GPU, maybe a Mac: the closing
   section is what a VLA asks for — a robot, fifty-odd demonstrations, a
   rented GPU for an afternoon — in that order.
5. **Date everything.** Eleven models, three of them with releases in the
   last twelve weeks. The article names the day.
6. **No hero yet.** Generated (`hero.md`); the CDN was blocked; the article
   ships without a banner until the file is added — same as the NVIDIA one.

## Traps hit

- `pip install lerobot` under Python 3.11 quietly installs 0.4.4 (February
  2026) because 0.5+ requires 3.12; `pip index versions` says nothing. The
  same trap as `isaacsim`, one article earlier. The 3.11 install also took
  four times as long and twice the disk (8.3 GB) — different torch wheels.
- EO-1's configuration dataclass calls the Hugging Face Hub in its
  constructor, so it cannot even be instantiated offline; every other VLA
  config could.
- GitHub release pages read through a summarising fetch report relative
  dates as the wrong year; dates come from PyPI or from dated posts.
- Guessed repository addresses fail quietly: the EO-1 upstream README was
  not found at the address tried and was not read; its facts are from
  LeRobot's config (first-hand) and LeRobot's release blog *(search)*.
- LeRobot's own README lists "Pi0, Pi0Fast, Pi0.5, GR00T N1.7, SmolVLA,
  XVLA, EO-1, MolmoAct2, WALL-OSS, EVO1" as VLAs and VLA-JEPA, LingBot-VA
  and FastWAM as world models; the installed package has 20 policy folders.
  The article names the VLAs and mentions the rest exist.
