# Homelab projects: primary-source research note

Compiled 2026-10-31. Every source below was read on 2026-10-31. Quotes are kept under 15 words. Everything else is a paraphrase of the cited page. Nothing here comes from memory.

## Access and confidence

> **Correction (2026-10-31, main session):** GitHub's "latest release" for
> nextcloud/server is v33.0.10, a maintenance release of an older line. The
> newest stable Nextcloud is **v35.0.2** (2026-10-15; 35.0.0 on 2026-09-15),
> per the full release list; 34.0.5 is the previous maintained line and has
> Docker Hub tags. Use 35 as "current" in the article.


**Read in full, or in full for the relevant sections (GitHub API, raw markdown):**
- Nextcloud AIO `readme.md` (main branch): intro, "How to use this?", Network FAQ, Infrastructure, macOS, TrueNAS, updates and the whole Backup section. Also `local-instance.md` in full.
- Frigate docs at tag `v0.18.2` (`docs/docs/...`): `frigate/index.md`, `frigate/hardware.md` (detectors section), `frigate/installation.md` (dependencies, OS, storage, ports, shm, Docker, HA App), `guides/getting_started.md` (config steps 1–7), `troubleshooting/dummy-camera.md` (in full), `configuration/record.md` (intro, examples, storage-full section), `configuration/authentication.md` (relevant parts), `integrations/home-assistant.md` (installation, Tailscale, entities).
- Frigate GitHub release notes for v0.16.0, v0.17.0, v0.18.0 and v0.18.2 (via `gh api .../releases/tags/<tag>`): headline sections.
- Home Assistant docs source (`home-assistant/home-assistant.io`, branch `current`): `source/installation/index.html`, `source/_includes/installation/container.md`, `container/compose.md`, `source/_includes/installation/operating_system.md` (relevant parts), `source/_docs/configuration/remote.markdown`, `source/_docs/configuration/securing.markdown` (first ~40 lines), and the 2025-05-22 deprecation blog post (opening).
- Immich docs at tag `v3.3.5`: `install/requirements.md` (in full), `install/docker-compose.mdx`, `partials/_docker-compose-install-steps.mdx`, `administration/backup-and-restore.md` (relevant sections), `features/mobile-backup.md`, `features/ml-hardware-acceleration.md` (opening), `FAQ.mdx` (ML sections), `docker/docker-compose.yml`, README.
- restic `README.md` (main), opening and design principles. Tailscale `README.md` (main), opening.

**Snippets only:**
- Frigate `configuration/object_detectors.md`, `semantic_search.md`, `face_recognition.md`, `license_plate_recognition.md`, `genai/config.md`, `genai/objects.md` (grep plus the opening sections).
- **tailscale.com/pricing and tailscale.com/kb/1151/what-is-tailscale via WebFetch.** WebFetch passes the page through a summariser model, so the "quotes" from these two pages are second-hand. Check them on the live page before publishing.

**Not verified / not found:**
- The Nextcloud AIO README gives **no minimum RAM or CPU**. It covers architectures, storage advice and VPS notes only.
- The restic README has **no 3-2-1 advice**. A GitHub code search of restic/restic for "3-2-1" returned nothing. The 3-2-1 advice in this note comes from Immich's docs.
- The Home Assistant docs repo has no Frigate integration page. The Frigate integration is a HACS custom integration, documented by Frigate.
- The Tailscale KB guides for Nextcloud and Home Assistant were not read. Tailscale use here is sourced from the Nextcloud, HA and Frigate docs.
- The Nextcloud AIO Tailscale guide is a GitHub discussion (#6817) and was **not read**.
- Docs sites (docs.frigate.video, docs.immich.app, home-assistant.io, restic.readthedocs.io) were not fetched. I read their source in the GitHub repos instead.

Versions confirmed via GitHub API on 2026-10-31: AIO v14.4.3 (2026-10-29), Nextcloud server v33.0.10 (2026-10-15), Frigate v0.18.2 (2026-10-15), v0.18.1 (2026-10-13), v0.18.0 (2026-09-12), v0.17.0 (2026-02-27), v0.16.0 (2025-08-16), HA core 2026.10.4 (2026-10-24), Immich v3.3.5 (2026-10-21), Tailscale v1.104.4 (2026-10-28), restic v0.19.1 (2026-07-05).

## Licences (GitHub API `repos/<r> .license.spdx_id`, 2026-10-31)

| Project | Repo | SPDX |
|---|---|---|
| Nextcloud AIO | nextcloud/all-in-one | AGPL-3.0 |
| Nextcloud server | nextcloud/server | AGPL-3.0 |
| Frigate | blakeblackshear/frigate | MIT |
| Frigate HA integration | blakeblackshear/frigate-hass-integration | MIT |
| Home Assistant core | home-assistant/core | Apache-2.0 |
| Home Assistant OS | home-assistant/operating-system | Apache-2.0 |
| Immich | immich-app/immich | AGPL-3.0 |
| Tailscale client | tailscale/tailscale | BSD-3-Clause |
| restic | restic/restic | BSD-2-Clause |

The Tailscale README says the macOS, iOS and Windows GUI wrappers are "not open source", while the repo code is open source.

---

## 1. Nextcloud All-in-One (AIO)

Source: https://github.com/nextcloud/all-in-one/blob/main/readme.md (read 2026-10-31); https://github.com/nextcloud/all-in-one/blob/main/local-instance.md (read 2026-10-31)

**What it is.** It opens with: "The official Nextcloud installation method." It bundles Nextcloud, Client Push, Redis/APCu, PostgreSQL and optional extras: Nextcloud Office, Talk plus TURN, Talk recording, a BorgBackup-based backup, Imaginary, ClamAV, full-text search, Whiteboard and community containers. A `mastercontainer` orchestrates the other containers and has a web interface for installation, updates and backups. Up to 100 users are free; more users need Nextcloud Enterprise.

**Install command (Linux, no existing reverse proxy):**
```sh
sudo docker run \
  --init \
  --sig-proxy=false \
  --name nextcloud-aio-mastercontainer \
  --restart always \
  --publish 80:80 \
  --publish 8080:8080 \
  --publish 8443:8443 \
  --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
  --volume /var/run/docker.sock:/var/run/docker.sock:ro \
  ghcr.io/nextcloud-releases/all-in-one:latest
```
- The README says not to rename the container or the volume, because updates and backups depend on those names.
- For production it suggests "using the example Compose file rather than `docker run`" (`compose.yaml` in the repo).
- Snap-based Docker is not supported. Install Docker from docs.docker.com.
- After start, open `https://<server-ip>:8080`. Use the IP address, not a domain, because HSTS can break domain access later. Port 8080 uses a self-signed certificate.

**Hardware and OS.**
- Architectures: x86_64/amd64 and aarch64/arm64.
- Storage: SD cards are discouraged. SSD is recommended; HDD works but is slower.
- KVM or non-virtualised VPS are recommended. Some VPS providers are listed as problematic (old Strato/Virtuozzo, Hostinger).
- **No minimum RAM or CPU is stated in the README.** The defaults include max 512 MB RAM per PHP process (adjustable). Resource limiting points to discussion #7273.
- "Runs on all platforms Docker supports (e.g. also on Windows and Macos)".
- TrueNAS SCALE 24.10+ has a full Docker environment. A community guide is in discussion #5506.

**Ports** (from "Explanation of used ports"):
- 8080/TCP: AIO interface, self-signed certificate.
- 80/TCP: ACME http-challenge and redirect.
- 8443/TCP: AIO interface with a valid certificate. Needs ports 80 and 8443 forwarded plus a domain.
- 443/TCP: the Apache container (Nextcloud itself). Must be open or forwarded for public access.
- 443/UDP: optional, for HTTP/3.
- 3478/TCP+UDP: Talk TURN server.
- Mandatory open ports, if the interface is reached internally on 8080: 443/TCP, 443/UDP (optional), and 3478 for Talk.

**HTTPS and domains.**
- "Automatic TLS included (by using Let's Encrypt)".
- An IP address instead of a domain is not supported: "No and it will not be added."
- Self-signed certificates for Nextcloud are not supported.
- Ports other than 443 are not supported. Subdirectories and multiple domains are not supported.
- New: AIO can register a free deSEC subdomain under `dedyn.io` from its interface. It then enables the Caddy community container as a reverse proxy, plus dnsmasq for LAN resolution, and keeps the DNS record updated.
- `local-instance.md` lists ways to run "only locally" while keeping a valid certificate:
  1. deSEC, the recommended option
  2. Tailscale
  3. a domain plus a reverse proxy, opening only port 80 for ACME, plus local DNS such as Pi-hole
  4. the ACME DNS-challenge
  5. Cloudflare Tunnel, which makes the instance public
  6. a bought certificate
- Beginner point: AIO needs working HTTPS even for LAN-only use: "you're still required to have https working properly."

**macOS / Docker Desktop for testing.**
- Supported. The README says "it is recommended to use OrbStack instead of Docker Desktop" for better Linux compatibility.
- With Docker Desktop, use `--volume /var/run/docker.sock.raw:/var/run/docker.sock:ro` instead of the Linux socket mount. Otherwise "it should work and behave the same like on Linux."
- Caveat for a test run: a valid domain and certificate are still needed to finish setup. The AIO interface on 8080 works by IP.

**Tailscale / no public domain.**
- In the feature list: "Can be used via Tailscale", linking discussion #6817 (a community guide by @Perseus333, not read).
- For people who want neither an IP-only setup nor a public instance, the README points to the deSEC domain, then Tailscale as the alternative.
- The README's Cloudflare notes list many limitations: TLS terminated at Cloudflare (a privacy concern), the 100 MB upload limit on the free plan, the 100 s timeout, Talk TURN problems and so on. It says it is "rather recommended" to use deSEC or Tailscale instead.

**Built-in backup (BorgBackup).**
- Backups are "incremental, differential, compressed and encrypted."
- Created and restored from the AIO interface ("Create Backup", "Restore selected backup"), with an integrity check.
- The encryption key is shown once in the interface. Without it you cannot restore.
- Daily backups can be enabled after the first backup. They can also auto-update containers, Nextcloud and its apps.
- Covered: database, files and mastercontainer config. Not covered: external-storage mounts. You can add extra Docker volumes or host paths.
- Default retention is `--keep-within=7d --keep-weekly=4 --keep-monthly=6`, adjustable via `BORG_RETENTION_POLICY`.
- Recommended target: an external drive mounted at e.g. `/mnt/backup`, which protects against failure of the Docker-volume drive.
- Remote borg repositories are supported directly and allow append-only keys "to counter ransomware". Alternatives: rsync/rclone of the local archive using the `aio-lockfile`, BorgBase guides, or your own script.
- The README gives an example script for syncing local backups to another drive.
- "It is recommended to create a backup before any container update."

**Updates.**
- The interface shows when container updates exist: Stop containers, then Start and update containers.
- The mastercontainer has its own update button.
- A daily cron job notifies Nextcloud admins about updates.

**Security-relevant notes from the README.**
- Containers run in their own Docker network, and "only really necessary ports are exposed".
- Many containers run as non-root with a read-only root filesystem.
- The mastercontainer mounts the Docker socket read-only. A manual install without socket access exists.
- Fail2ban can be added.
- "A+ security in Nextcloud security scan".
- Note: AIO cannot run offline or air-gapped. It needs update checks and app store access.

---

## 2. Frigate

Sources (all read 2026-10-31, docs at tag v0.18.2; repo default branch is `dev`):
- https://github.com/blakeblackshear/frigate/tree/v0.18.2/docs/docs: files listed in Access above
- Release notes: https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0, /v0.17.0, /v0.16.0, /v0.18.2

**What it does.** `index.md` calls it "A complete and local NVR designed for Home Assistant with AI object detection."
- It uses cheap motion detection to decide where to run object detection.
- It records with retention based on detected objects and restreams RTSP.
- It talks to other systems over MQTT.
- It integrates with HA through a custom component.
- "CPU detection should only be used for testing purposes."

**Hardware recommendations** (`frigate/hardware.md`):
- **Cameras:** H.264 video plus AAC audio gives the best compatibility. Multiple substreams help. The author recommends Dahua, Hikvision and Amcrest, in that order, with affiliate links. "WiFi cameras are not recommended". Keep Reolink at 5MP or lower.
- **Server:** the author's favourite is the Beelink EQ13 (Intel N100, dual NICs, "a dedicated private network for your cameras where they can be blocked from accessing the internet"). Avoid the Beelink EQ14 for now. Any Intel CPU with AVX + AVX2 that runs Debian "should work fine". Look for M.2 or PCIe slots for accelerators. A table rates an Intel 125H with "Includes NPU for more efficient detection in 0.17+".
- **Detectors:**
  - **Google Coral:** "no longer recommended for new Frigate installations". It is still supported and power-efficient. USB needs no driver; M.2/PCIe needs the gasket driver.
  - **OpenVINO (Intel):** iGPU on 6th-gen and newer, Arc GPUs, Intel NPUs, and most AMD CPUs (unofficially). Example: Intel N100 about 15 ms (MobileNetV2).
  - **Hailo-8/8L:** M.2 or Raspberry Pi 5 HAT. Default model YOLOv6n.
  - **NVIDIA:** via the `onnx` detector. Needs CUDA 12.x, driver 545 or newer, compute capability 5.0 or higher, and nvidia-container-runtime. RTX 3070 YOLOv9 t-320: 6 ms.
  - **Apple Silicon (M1+):** works, but "can not run within a container". A ZMQ proxy talks to a host-side detector (github.com/frigate-nvr/apple-silicon-detector). Added in 0.17.
  - Also: AMD ROCm, AMD XDNA2 (community), MemryX MX3, Rockchip RKNN, Synaptics, AXERA, Jetson (community).
- **CPU detector caveat** (`object_detectors.md`): "not recommended for actual use". OpenVINO in CPU mode is "often more efficient". **Conflict in the docs:** `object_detectors.md` says the default is "a single CPU detector", while `getting_started.md` (Step 4) says the default is "a single OpenVINO detector running on the CPU". I did not resolve which is current.

**Install basics** (`installation.md`):
- Docker Compose is recommended.
- It "runs best with Docker installed on bare metal Debian-based distributions". VMs are not recommended (some succeed on Proxmox).
- Windows is "not officially supported" (WSL might work).
- An MQTT broker is optional but required for the HA integration.
- Image: `ghcr.io/blakeblackshear/frigate:stable`.
- Ports:
  - 8971: authenticated UI. Reverse proxies should use it.
  - 5000: internal unauthenticated UI. "Access to this port should be limited."
  - 8554: RTSP restream, unauthenticated by default.
  - 8555: WebRTC.
- In the example compose file, 5000 is commented out with the note "Expose carefully."
- shm: the Docker default is 64 MB. "about 210MB for 2 cameras detecting at 720p". The example uses `shm_size: "512mb"`.
- Volumes: `/config` (config.yml plus sqlite), `/media/frigate` (recordings, clips, exports), and a tmpfs for `/tmp/cache`.
- It can also run as a **Home Assistant App** (formerly add-on) via the repository `https://github.com/blakeblackshear/frigate-hass-addons`. Limits on HA OS: no AMD GPU, no Intel NPU, no NVIDIA, and no separate local media storage.

**Minimal config.yml structure** (getting_started.md, Steps 4 and 6):
```yaml
mqtt: ...
detectors:
  ov:
    type: openvino
    device: GPU
model: ...            # OpenVINO ssdlite_mobilenet_v2 paths given in docs
cameras:
  name_of_your_camera:
    ffmpeg:
      inputs:
        - path: rtsp://10.0.10.10:554/rtsp
          roles: [detect]
        - path: rtsp://10.0.10.10:554/high_res_stream
          roles: [record]
    detect: ...
    record:
      enabled: True
```
- From 0.17 there is an "Add Camera" wizard in the UI. From 0.18, "Full UI Configuration" lets you edit every section in Settings, and YAML is "still fully supported".
- 0.16 breaking change: "Object detection is now disabled by default" (a migrator sets `detect: enabled: true`).

**Recording and retention** (`record.md`, getting_started.md):
- Recordings are written "without re-encoding" to `/media/frigate/recordings`, in UTC folders.
- Since 0.17, retention is tiered: `continuous`, `motion`, `alerts`, `detections`, each with `days`.
- Example "most conservative" setup: continuous 3 days, motion 7 days, alerts and detections 30 days.
- Getting started: "By default, Frigate will retain video of all tracked objects for 10 days."
- Exports are never removed by retention.
- When the disk has less than about one hour of recording space left, Frigate deletes the oldest recordings "regardless of retention settings". Non-Frigate files on the same disk can trigger this.

**What's new, 0.16 to 0.18** (release notes):
- **0.16** (2025-08-16):
  - Face Recognition, with sub-labels on known faces
  - License Plate Recognition (e.g. `AB12345` --> `Bob's Car`)
  - a Viewer role
  - Jina V2 semantic search (multilingual), with semantic search now optional for GenAI
  - bird classification
  - TensorRT detector removed in favour of ONNX
  - Neither face recognition nor LPR requires Frigate+.
- **0.17** (2026-02-27):
  - GenAI review summaries: title, description, and a dangerous/suspicious/normal classification
  - semantic search triggers
  - custom classification model training (state and object)
  - Apple Silicon detector, YOLOv9 on Coral, MemryX
  - tiered retention
  - Add Camera wizard
  - go2rtc `exec`/`expr`/`echo` sources removed by default "to reduce the security risk"
- **0.18** (2026-09-12):
  - Full UI configuration, with most settings applied without restart
  - Profiles (named overrides, switchable via UI or MQTT)
  - GenAI with multiple providers and per-provider `roles`, plus a llama.cpp provider
  - **Chat**, a tool-calling LLM agent that answers questions about cameras and events
  - remote embeddings
  - Motion Search and Motion Review
  - **Debug Replay**
  - case management for exports
  - FFmpeg 8
  - snapshots now WebP, no annotated JPEGs
  - DeGirum detector removed; DeepStack deprecated
- **0.18.2** (2026-10-15): "a maintenance release ... that includes some security fixes". It fixes three advisories, including two RCE-as-root issues (GHSA-qjjw-3v66-279f, GHSA-93xj-hg88-ffg7). This is a good concrete argument for keeping it updated.

**Enrichment requirements:**
- Semantic search: "A minimum of 8GB of RAM", a CPU with AVX + AVX2, and 16 GB plus a GPU recommended. "Small or underpowered systems like a Raspberry Pi will not run" it reliably. Runs locally; models download once from HuggingFace.
- Face recognition: AVX + AVX2. The `small` model runs on CPU; `large` needs a GPU or NPU. Runs locally after a one-time download.
- LPR: "At least 4GB of RAM" plus AVX + AVX2.
- GenAI: there are local providers (llama.cpp, Ollama, OpenAI-compatible) that "keep all data processing private". "Running Generative AI models on CPU is not recommended". Cloud providers include Gemini, OpenAI, Azure OpenAI and Ollama Cloud. Object descriptions send detect-stream images of the tracked object to the provider. That is a privacy point if the provider is a cloud service.

**Testing without a real camera** (`troubleshooting/dummy-camera.md`, documented). The "Manual Dummy Camera" loops a video file:
```yaml
cameras:
  test:
    ffmpeg:
      inputs:
        - path: /media/frigate/car-stopping.mp4
          input_args: -re -stream_loop -1 -fflags +genpts
          roles:
            - detect
    detect:
      enabled: true
    record:
      enabled: false
    snapshots:
      enabled: false
```
- `-re -stream_loop -1` plays the file in real time and loops it indefinitely. The docs suggest `hwaccel_args: ""` if FFmpeg fails.
- 0.18's **Debug Replay** replays already-recorded footage through detection in the UI.
- Caveat: this page is framed for debugging, not as a getting-started path. Using it as a "try Frigate with no camera" step is our framing.

**Home Assistant integration** (`integrations/home-assistant.md`):
- "The best way to integrate with Home Assistant is to use the official integration" (blakeblackshear/frigate-hass-integration), installed via HACS.
- It requires HA's MQTT integration, and Frigate connected to the same broker.
- Entities: camera, image, sensor, switch and binary_sensor (motion and occupancy per camera, zone and object).
- Over Tailscale, the docs say to use `http://<frigate_device_tailscale_ip>:5000` and bind port 5000 only to the Tailscale IP (`"<tailscale_ip>:5000:5000"`).
- The App and the integration are different things. The integration is needed either way.

**Auth / security** (`authentication.md`):
- "On startup, an admin user and password are generated and printed in the logs." The docs recommend changing it after first login.
- Minimum password length is 12 characters. Passwords are stored as PBKDF2-SHA256 hashes.
- Port 8971 is authenticated; 5000 is not.

---

## 3. Home Assistant

Sources (home-assistant/home-assistant.io, branch `current`, read 2026-10-31):
- https://github.com/home-assistant/home-assistant.io/blob/current/source/installation/index.html
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_includes/installation/container.md
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_includes/installation/container/compose.md
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_includes/installation/operating_system.md
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_docs/configuration/remote.markdown
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_docs/configuration/securing.markdown
- https://github.com/home-assistant/home-assistant.io/blob/current/source/_posts/2025-05-22-deprecating-core-and-supervised-installation-methods-and-32-bit-systems.markdown

**Installation types.**
- Only two are supported now: Home Assistant OS and Home Assistant Container. The 2025-05-22 post deprecated the Core and Supervised methods and 32-bit systems, with support ending at 2025.12.
- **HA OS:** "the recommended installation type for most users". It supports **apps** (the docs now say "apps"; the Frigate docs mention the former name "add-on"). Options: Green (preinstalled), Yellow, Raspberry Pi 4/5 ("minimum 2 GB RAM"), Odroid, generic x86-64, or a VM.
- **Container:** "Home Assistant Container installations don't have access to apps." You manage updates yourself. "Some integrations, such as Thread and Z-Wave, are controlled by apps", and Container has no out-of-the-box support for them. The comparison table shows both types have backups; only OS has apps.
- Container prerequisite: Docker Engine 23.0.0 or later. "Docker _Desktop_ will not work; you must use Docker _Engine_." **So testing HA Container on a Mac with Docker Desktop is not supported by the docs.** The macOS install page includes only the HA OS page (a VM route).
- Example compose: image `stable`, `network_mode: host`, `privileged: true`, `/config` volume, `stop_grace_period: 60s`. The UI is at `http://<host>:8123`.

**Minimum hardware.**
- VM minimum: "Memory: 2 GB of RAM" and "Processors: 2 vCPUs".
- Raspberry Pi 4 or 5 with a minimum of 2 GB RAM.
- The x86-64 install needs a USB stick of at least 8 GB for the installer.
- Internet is needed on first boot of HA OS to download Core.

**Ports (remote.markdown).** "New installations of Home Assistant Operating System use port 80." HA OS installs set up before 2026.8 keep their old port, usually 8123. Other install types use 8123.

**Remote access and security.**
- "By default, you can only reach your Home Assistant from your local network".
- Recommended option: Home Assistant Cloud (Nabu Casa, paid). It needs no open ports.
- VPN: "A secure way" is a VPN "such as Tailscale or ZeroTier One".
- Port forwarding carries the caution "Just putting a port up is not secure." The docs also mention CG-NAT.
- Securing checklist: a strong unique password and MFA, `secrets.yaml` (not encrypted), and "Keep your system up to date with each monthly release." For SSH, `PermitRootLogin no` and key authentication.

**Frigate integration.** It is not part of HA core docs. It is the HACS custom integration documented by Frigate (section 2).

---

## 4. Immich

Sources (immich-app/immich at tag v3.3.5, read 2026-10-31):
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/install/requirements.md
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/install/docker-compose.mdx and `docs/docs/partials/_docker-compose-install-steps.mdx`
- https://github.com/immich-app/immich/blob/v3.3.5/docker/docker-compose.yml
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/administration/backup-and-restore.md
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/features/mobile-backup.md
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/features/ml-hardware-acceleration.md
- https://github.com/immich-app/immich/blob/v3.3.5/docs/docs/FAQ.mdx
- https://github.com/immich-app/immich/blob/v3.3.5/README.md

**Requirements:**
- **OS:** Linux 64-bit is recommended. "Non-Linux OSes tend to provide a poor Docker experience and are strongly discouraged." Docker Desktop on Mac is possible but gets less support. Full VMs are fine; Docker in LXC is "not recommended".
- **RAM:** "Minimum 6GB, recommended 8GB." With 4 GB, run it with machine learning disabled.
- **CPU:** minimum 2 cores, recommended 4. amd64 or arm64. Since v3, the ML container on amd64 needs x86-64-v2 ("Most CPUs released since ~2012").
- **Storage:** a Unix-compatible filesystem (EXT4, ZFS, APFS…). Thumbnails and transcodes add 10–20%. Postgres (1–3 GB) should be on local SSD, "never a network share of any kind". NTFS/exFAT will not work for the database.
- **Software:** Docker plus the Compose plugin. The command is `docker compose`; the old `docker-compose` is not supported.

**Official Docker Compose install** ("Docker Compose is the recommended method"):
```bash
mkdir ./immich-app && cd ./immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
# edit .env: UPLOAD_LOCATION, DB_PASSWORD (A-Za-z0-9 only), TZ
docker compose up -d
```
- The web UI is at `http://<machine-ip-address>:2283`. The first user to register becomes admin.
- Services: `immich_server`, `immich_machine_learning`, `immich_redis` (Valkey), and `immich_postgres` (a custom Postgres with VectorChord).

**Machine learning container:**
- It runs CLIP for smart search, plus face detection and recognition.
- It can be disabled per feature or entirely in Admin Settings. It can also be removed by commenting out `immich-machine-learning` in compose.
- It can run on a separate, more powerful machine (a "remote machine learning" guide).
- Hardware-accelerated ML (described as "still experimental"): CUDA (compute capability 5.2+), ROCm, OpenVINO, ARM NN and RKNN. Linux or WSL2 only.
- On a Raspberry Pi, transcoding and ML "can be too heavy".

**Backup warnings:**
- README banner: "Always follow 3-2-1 backup plan for your precious photos and videos!"
- The backup doc's "danger" box says it only shows what to back up: "You still need to take care of using an actual backup tool".
- Automatic database dumps go to `UPLOAD_LOCATION/backups` (default: daily at 2:00, keep 14), but "Database backups do **not** contain photos or videos".
- Immich "does not scan the library folder, so database backups are essential."
- Back up the whole `UPLOAD_LOCATION`. Do not edit the files there by hand.
- Ordering: stop `immich-server` during the backup. If you can't, back up the database first and the files second.
- Post-install partial: "at least two local copies and one copy offsite in cold storage."

**Mobile app backup:**
- iOS App Store, Google Play, GitHub APK, F-Droid and Obtainium.
- It uploads selected albums when the app opens or resumes, and periodically in the background.
- It deduplicates by checksum.
- "By default, Immich will only upload photos and videos when connected to Wi-Fi."

---

## 5. Tailscale

Sources:
- https://github.com/tailscale/tailscale/blob/main/README.md (read 2026-10-31)
- https://tailscale.com/kb/1151/what-is-tailscale (WebFetch, summarised, read 2026-10-31)
- https://tailscale.com/pricing (WebFetch, summarised, read 2026-10-31)

**What it does:**
- README tagline: "Private WireGuard® networks made easy".
- KB, via the summariser: "encrypted point-to-point connections using the open source WireGuard protocol". It is a peer-to-peer mesh that works across NAT "without requiring port forwarding".
- In plain words: each device joins your private network (a "tailnet"), and devices reach each other by a private address without opening ports on the router. This is our paraphrase.
- The client daemon runs on Linux, Windows, macOS and partly on BSDs. There are iOS, Android, Synology and QNAP packages. The GUI wrappers on closed platforms are not open source.

**Free Personal plan** (via WebFetch summariser; **re-check on the live page before publishing**):
- "Up to 6 users"
- "Unlimited user devices"
- "50 tagged resources to start"
- 1,000 minutes per month of ephemeral resources
- Paid tiers named: Standard and Premium (per-user prices shown in USD); Enterprise is custom.

**Use with the other apps (from those apps' docs):**
- Nextcloud AIO: "Can be used via Tailscale". This is the alternative to deSEC for no-domain or no-port-443 setups (community guide, discussion #6817, not read).
- Home Assistant: a VPN "such as Tailscale" is listed as a secure remote-access method. The companion app's sensors do not update without the VPN connection when away.
- Frigate HA integration: use the Tailscale IP with port 5000, bound only to that IP.

---

## 6. restic, and backups generally

Source: https://github.com/restic/restic/blob/main/README.md (read 2026-10-31)

**What restic is:**
- "restic is a backup program that is fast, efficient and secure."
- Runs on Linux, macOS, Windows, FreeBSD and OpenBSD.
- Workflow: `restic init --repo ...`, then `restic backup`, then `restic restore` or `restic mount`.
- The README warns: "Losing your password means that your data is irrecoverably lost."
- Backends: local, SFTP, REST server, S3-compatible, B2, Azure, GCS, Swift, and others via rclone.
- "Saving a backup on the same machine is nice but not a real backup strategy."
- Design: encrypted and integrity-checked, assuming the storage location is untrusted. Deduplicated and incremental.

**3-2-1:**
- **Not found in the restic README or repo** (code search of restic/restic for "3-2-1" returned nothing).
- The 3-2-1 advice comes from Immich: the README banner, the backup doc linking Backblaze's 3-2-1 article, and the post-install line "at least two local copies and one copy offsite".

**Nextcloud AIO's own backup:** see section 1. It is BorgBackup, encrypted, with a key you must save. It is managed from the interface, local or remote, with append-only keys against ransomware. Retention 7d/4w/6m.

---

## 7. Security essentials (documented only)

- **Do not expose admin and unauthenticated ports.**
  - Frigate port 5000 is unauthenticated: "Access to this port should be limited". The compose example says "Expose carefully". RTSP on 8554 is unauthenticated by default.
  - HA: reach it from outside via HA Cloud or a VPN rather than "exposing it directly to the internet". "Just putting a port up is not secure."
  - AIO: only 443 (and 3478 for Talk) need forwarding. The 8080 interface is for LAN access by IP.
  - Immich: Postgres "is not publicly exposed".
- **Isolate cameras:** Frigate's hardware page values dual NICs for a camera network "blocked from accessing the internet". WiFi cameras are not recommended (that one is a reliability point).
- **Default and generated passwords:**
  - Frigate generates an admin password in the logs at first start; change it (minimum 12 characters).
  - Immich: change `DB_PASSWORD` in `.env`. The first registered user becomes admin, so register right away.
  - HA: strong unique passwords plus MFA. Only give administrator access to accounts that need it.
  - AIO: save the borg encryption key.
- **Updates:**
  - HA: "Keep your system up to date with each monthly release."
  - AIO: daily update-check notifications; back up before updating.
  - Frigate: 0.18.2 fixed RCE-as-root advisories, a concrete reason to update.
  - The Frigate 0.17 notes removed go2rtc exec sources to "reduce the security risk".
- **Least privilege:** AIO lists non-root containers, a read-only root filesystem and a read-only socket mount, and supports rootless Docker. HA advises `PermitRootLogin no` and SSH keys.
- **Backups:** Immich says 3-2-1 and use a real backup tool. restic says a backup on the same machine is "not a real backup strategy". AIO says back up before every update and keep the key.
- **Cloud AI privacy:** Frigate GenAI sends images to the provider you configure. The local providers (llama.cpp, Ollama) keep processing private but need a GPU.
