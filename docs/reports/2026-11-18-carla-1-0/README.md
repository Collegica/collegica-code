# CARLA 1.0 on the home server: it did not start

18 November 2026. Follow-up to [`2026-11-05-drone-sim`](../2026-11-05-drone-sim/README.md),
run the day after CARLA 1.0 was released (17 November 2026, Unreal Engine 5.8).

## Result

**CARLA 1.0 did not start** on the home server's RTX 3070 (8 GB), driver
550.127.05, headless in Docker. Every launch ended with the same message from
the engine:

> Vulkan device could not be created at the project's supported feature levels

No frame was rendered, so none of the measurements in the November 5 report
(frame rate, memory, driving) could be repeated for 1.0. `setup/drive_test.py`
was written for the test and never ran.

## What was tried

- Image `carlasim/carla:1.0` (15.7 GB), pulled from Docker Hub. Python wheels
  for 3.10 to 3.15 ship inside it.
- Same headless graphics fix as the earlier test: `--gpus all`,
  `NVIDIA_DRIVER_CAPABILITIES=all`, and the EGL `nvidia_icd.json` mounted at
  `/etc/vulkan/icd.d/` (see the November 5 report).
- Command: `CarlaUnreal.sh -RenderOffScreen -nosound -quality-level=Low`,
  memory capped at 10 GB, ports on 127.0.0.1.
- Variants, all failing: added `-vulkan`; `-sm5`; `-ForceFeatureLevelES31`;
  `-vulkan -dx11`. The Vulkan loader reported only that a Mesa virtio driver was
  skipped; it printed no NVIDIA error. The engine wrote no log file to a mounted
  folder (`-ABSLOG`).
- The container did not run out of memory (`OOMKilled` false, exit code 1).

## What this does not show

The cause was not found. It could be the driver (550.127.05 is the version
TrueNAS ships here; CARLA's announcement names driver 570 or later only for
RTX 50-series cards and gives no minimum for others), the headless EGL route
this box needs, or the card. Epic's documentation was not read for Unreal
Engine 5.8's graphics minimums. No driver change was tried: on TrueNAS the
driver comes with the system update.

## Side effect worth knowing

Before this test the box's Docker service was down (status FAILED, "Unable to
determine default interface") and every container, Coolify included, was
stopped. With the owner's go-ahead it was restarted with
`midclt call service.restart docker`; about 50 containers came back within a
minute, one (a Supabase studio container) still starting. The 15.7 GB CARLA 1.0
image remains on the box's Docker storage.

## For the owner

- Remove the image when you no longer need it: `docker rmi carlasim/carla:1.0`.
- The static-gateway fix in TrueNAS network settings would stop the Docker
  service failing at boot; it was not changed.
