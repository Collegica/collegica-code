# NVIDIA NuRec for robotics: research record

17 November 2026. Supports `website/robotics/nurec/index.md`, issue #220.

## What this is

The owner supplied a research brief, "NVIDIA Omniverse NuRec: Architecture,
Performance, and Ecosystem Analysis" (`source/brief.md`, converted from the
.docx, citation markers removed). It was produced by an AI research tool
using partly third-party sources. A separate agent checked its claims against
NVIDIA's own pages, repositories and papers, and I re-read three of the
load-bearing sources myself (the Niantic Spatial post, NVIDIA's one-camera
recipe, the Isaac Sim 6.2 NuRec page). **Nothing was run:** NuRec needs a
Linux machine with more than 24 GB of NVIDIA GPU memory, and none was
available.

The article was narrowed to 3D and simulation at the owner's request, so
fleet-scale and driving-business material in the brief is not used.

## Used in the article (confirmed against a primary source)

- Apache-2.0 open-sourcing at 26.10 (October 2026; the page gives only the
  month), `nre` to `nurec` rename; 26.08 removed the older renderer, replaced
  Difix configs with Harmonizer, added arm64 for GB300 and DGX Spark.
- Requirements: Docker 23.0.1, Container Toolkit 1.13.5, driver R580, CUDA 12.8,
  more than 24 GB (48 GB recommended), x86_64 only; supported GPU list from the
  hardware page.
- 3DGUT: CVPR 2025 oral, fisheye and rolling shutter, 0.38M vs 1.07M
  particles against FisheyeGS; gsplat up to 4x less memory, 15% less time;
  3DGRT (SIGGRAPH Asia 2024) needs ray-tracing hardware; 3DGRUT combines
  rasterisation and ray tracing.
- Instant NuRec: about 1.5 s; arXiv v1 15 Jul 2026, v2 11 Nov 2026; PSNR
  34.38 (NuRec) vs 29.93 (Instant Dense); optional extras under a
  non-commercial NVIDIA licence.
- Harmonizer: single-step image diffusion, from Cosmos Predict2 0.6B, 212 ms
  temporal and 28 ms non-temporal per 576x1024 image on an H100; NVIDIA Open
  Model License.
- Robotics recipes (mono: COLMAP + 3DGUT, smartphone, 60% overlap, ground plane,
  "no inherent collision properties"; stereo: cuSFM, FoundationStereo, nvblox,
  3DGRUT, `export_usdz`).
- OpenUSD: USDZ is "a zero compression, unencrypted zip archive"; Alliance for
  OpenUSD; Isaac Sim 6.x ParticleField vs 5.x `OmniNuRecVolumeAPI`; do not open
  a `.usdz` as the root stage; DLSS Frame Generation artefacts.
- Niantic Spatial post of 20 July 2026: 360-degree camera, MVSAnywhere
  collision mesh, 1,024 rollouts, 97.8% vs 93.8% (Zurich), 75.0% vs 70.9%
  (London), zero-shot real-robot transfer, stated limits.
- Newton: built on Warp, Linux Foundation, started by Disney Research, Google
  DeepMind and NVIDIA.

## In the brief but left out (not confirmed, or different)

- **28.26 dB** (not on the arXiv or project page), **850,000 Gaussians
  sampled**, **Python 3.11 for 26.03**, "first public release 26.03" (the
  notes date 26.03 to April 2026 and do not say first public).
- **Throughput and scale:** 3.33 reconstructions/hour, 100 FPS at 1080p,
  4-5x on 8 GPUs, 4,000 daily reconstructions, the Li Auto study. Not on the
  pages read; the scaling best-practices page was not opened.
- **150 GB disk** and the **"Built on NVIDIA Cosmos" attribution** (not on the
  hardware, software or Harmonizer pages).
- "Brief says Instant NuRec exports only static .ply": the repository also
  writes `.sky.npz` and optionally `.dynamic.npz`.
- The "Marble" column of the OmniDreams table (unchecked). OmniDreams FPS
  figures were confirmed in the paper (68 FPS 1-camera, up to 105 FPS 4-camera
  on 16 GB300) but are not used.
- Brief's wording "3DGUT ... Gaussians"; the project page says "particles".

## Sources that could not be read

- 404: Isaac Sim "latest" neural-rendering page and the 5.0 NuRec assets page.
- 403: Omniverse neural-rendering documentation (supported cameras, LiDAR and
  physics inside Isaac Sim are therefore not claimed).
- Not fetched: NuRec scaling best-practices page, the SIGGRAPH press release,
  the NVIDIA blog on the Flexion work (only the Niantic post was read), the
  second half of the OmniDreams paper.

## For the owner

- The article says nothing was run. If you want a tested version, it needs a
  Linux machine with a 24 GB+ data-centre or workstation card (the TrueNAS box
  has an RTX 3070, which is below the stated minimum).
- Cosmos Transfer 2.5's repository says it is no longer under active
  development and points to Cosmos 3; the article says to check the version.

## Added 18 November: Omniverse, LiDAR and physics in Isaac Sim

Sources gathered by a second research agent and spot-checked by re-reading
four pages: RTX Lidar (6.x, updated 14 Oct 2026), Omniverse particle fields
(updated 17 Nov 2026), Newton in Isaac Sim, the Isaac Sim licence FAQ, plus
the NuRec release notes (26.04 and 26.09 LiDAR entries). Used in the article.

Not confirmed, so not claimed: that RTX Lidar returns hits from a
ParticleField (no NVIDIA page says it does or does not; a search snippet
mentions "experimental lidar rendering of NuRec-trained splats" in ovrtx
0.7.0, not opened); PhysX timestep or speed figures; a method to derive
collision from a splat; GPU convex-hull vertex limits (search snippet only);
Omniverse pricing (none published on the pages read). The Newton 1.0 post (16 March 2026) was re-read and confirms the GA, "production-ready" and 252x/475x figures; the Isaac Lab 3.0 backend list comes from the agent's reading of the Isaac Lab docs and was not re-read.

Unreadable: 404 on Isaac Lab physics-backend and Isaac Sim fundamentals
pages and a lidar scan-pattern page; 403 on the Omniverse collider-compounds
page; the PhysX Limitations page redirects to the home page. The Isaac Sim
6.0 and 6.1 release notes and 5.x physics pages were not read.
