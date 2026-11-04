# Your Own Cloud, Set Up by AI

Article of 2026-10-31 (`website/ai/homelab/`): a beginner's homelab
(Nextcloud, Immich, Frigate, Home Assistant) set up by Claude Code, tested
twice. Owner's choices: test on the Mac first, then on the owner's TrueNAS
with Coolify; core four apps; beginners, AI section.

- `notes/projects.md`: the apps' documentation, read from their GitHub
  repositories (sites not fetched); licences; with a correction on the
  current Nextcloud version (35.0.2, not the 33.0.10 GitHub marks "latest").
- `tests/mac-request.txt`, `tests/server-request.txt`: the requests given to
  Claude Code (headless, `claude -p`, an allow list of commands). The server
  request is lightly edited to drop local paths.

## Results

**Mac (Docker Desktop, Apple M4).** Run 1, 12.1 min, US$3.89: wrote the
Compose setup, pulled ~12 GB of images, saw 1.1 GB left on the disk and
stopped before starting anything, removing only its own images. Run 2
(after an unused 12 GB image was deleted with the owner's OK), 11.1 min,
US$8.26: all four apps running and tested (Nextcloud login and
WebDAV/CalDAV/CardDAV; Immich admin; Frigate test camera at 5 fps, CPU
detector ~18 ms; Home Assistant with five live Frigate sensors over MQTT).
Found and fixed: Frigate recording the moving test pattern nonstop at
~1.7 GB/hour; Immich starting before its database; Nextcloud cron.
Removed afterwards with `docker compose down --volumes --rmi all`.

**Home server (TrueNAS SCALE 24.10, Coolify 4.x).** One run, 23.0 min,
US$4.81, 133 turns, 10 commands refused by the allow list. Nextcloud
(with Postgres and Redis) and Home Assistant from Coolify's catalogue,
Frigate 0.18.2 with Mosquitto as a custom Compose service, in a new
project. Before starting: removed the public domain names the templates
assign, removed Home Assistant's privileged mode and host D-Bus access,
pinned the Nextcloud image (template used `latest`), put all data in a new
ZFS dataset with a 20 GB quota, capped logs and Frigate retention. Removal
steps written with Coolify's whole-server Docker cleanup turned off.
Detection on the CPU (the GPU detector needs a separately downloaded
model). Checked afterwards from the laptop: every pre-existing service had
the same status as before; the three new ones answered on the LAN only.
The test project is still on the server pending the owner's decision.

The server's addresses, identifiers and domain are deliberately not
recorded here.

## Hero

`hero-original.png`; GPT Image 2 via HiggsField (`gpt_image_2`, 16:9, 2k,
high; job `93be6f4a-98b4-4b57-961d-66d3a9133cbb`), house prompt with eyebrow
`AI`, title 'Your Own Cloud,' / 'Set Up' / 'by AI', subtitle 'Files, photos,
cameras and home, on a server you own.' Mark fix: 36 × 36 paper patch from
(190, 197) pasted at (151, 197). Banner: rows 60–1404 → 1774 × 887, plus
900 wide.
