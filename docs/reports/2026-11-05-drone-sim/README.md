# CARLA-Air on the TrueNAS: test report

Run 2026-11-05 for the drone-simulator article, as set out in the
proposal (`docs/proposals/2026-11-03-drone-sim/`, not public). Question: can a
real Unreal Engine drone simulator run headless on the homelab box, and what
does it cost in memory and GPU?

**Result: yes.** CARLA-Air v0.1.7 ran off-screen in a container on the RTX
3070, rendered Town10HD at about 60 frames per second idle and 36 while
flying the drone and saving camera frames, and used about 2.5 GB of RAM and
2.5 GB of GPU memory.

## Setup

| | |
|---|---|
| Box | TrueNAS SCALE 24.10, i7-12700KF, 31 GB RAM (about 8 GB free at the start), RTX 3070 8 GB, driver 550.127.05 |
| Simulator | CARLA-Air v0.1.7 Ubuntu build from [Hugging Face](https://huggingface.co/tianlezeng/CarlaAIr-v0.1.7): one 6.8 GB zip, SHA-256 matching the listing, 16 GB unpacked |
| Container | Ubuntu 22.04 with Vulkan and X11 runtime libraries, CARLA-Air's own `carla` Python module and the `airsim` client ([`setup/Dockerfile`](setup/Dockerfile)); non-root user; memory capped at 8 GB |
| Launch | `CarlaUE4-Linux-Shipping CarlaUE4 Town10HD -carla-rpc-port=2000 -RenderOffScreen -quality-level=Low -nosound` |
| Storage | ZFS dataset `Storage2T/collegica-drone-sim`, 40 GB quota |

**The one fix needed:** the NVIDIA container runtime put the driver
libraries in the container but no Vulkan driver file, so Vulkan fell back to
the software renderer (llvmpipe). Pointing a driver file at the GPU's
headless library, `libEGL_nvidia.so.0`
([`setup/nvidia_icd.json`](setup/nvidia_icd.json)), made the RTX 3070
visible; pointing it at `libGLX_nvidia.so.0` failed without a display.

## What the script did

[`setup/fly_test.py`](setup/fly_test.py), run inside the container:

1. Measured the server's frame rate for 20 seconds with nothing happening.
2. Spawned a car on CARLA's autopilot with a chase camera.
3. Through AirSim: took off, climbed to 30 m, and flew a 40 m square at
   6 m/s, saving the drone camera's view at each corner.
4. Measured the frame rate during the square, then landed and cleaned up.

## Results

| Measure | Value |
|---|---|
| Frame rate, idle | 59.7 frames per second |
| Frame rate, drone flying a square, car driving, images saved | 36.2 frames per second |
| Time for the 160 m square at 6 m/s | 33.1 s (26.7 s of pure travel at that speed; the rest is accelerating, braking at corners and saving images) |
| Container RAM | 2.4–2.5 GB |
| GPU memory | about 2.4 GB of 8 GB |
| GPU use (single readings) | 39% 90 s after launch; 7% right after the run |
| Download and unpack | about 3 minutes and 2 minutes |

Corner positions from AirSim's position estimate were within 0.25 m of the
targets ([`setup/fly_test.json`](setup/fly_test.json)).

Frames: [the drone at 30 m](frames/drone-30m.jpg),
[the second corner](frames/drone-wp2.jpg),
[the car's chase camera](frames/car-camera.jpg).

## Things the article should know

- **It looks right.** At the lowest quality setting the city, the car and
  the drone's view are convincing. That is the article's point: looks are
  not evidence of correct physics.
- **The drone flies AirSim's SimpleFlight controller**, not PX4 or
  ArduPilot. Connecting real flight software was not tried.
- **Two oddities in the telemetry, not investigated:** the drone's height
  started at +29 m in AirSim's frame (z points down, so 29 m below its
  origin) and climbed 58 m to reach "30 m"; and the land command returned
  after half a second with the drone still at 31 m.
- **Licence:** the Hugging Face listing says MIT for CARLA-Air's code and
  CC-BY for CARLA's assets, matching the GitHub README's licence section
  (its badge still says "Custom (Non-Commercial)"). The frames above are
  CARLA's Town10HD rendered by us; credit CARLA if they are published.
- **Headroom:** the box had about 8 GB free; the run used a third of that.
  Higher quality settings, more sensors or PX4 would need more.

## Left on the box

The container is stopped and removed. Still on the TrueNAS: the dataset
`Storage2T/collegica-drone-sim` (16 GB: the unpacked simulator, the zip, the
frames) and the 388 MB image `collegica/drone-sim:carlaair-0.1.7`.
