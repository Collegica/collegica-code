# Planning to Age Well, with AI — video

A 90-second summary of the [aging-well article](https://www.collegica.org/aging-well/ai-planning/),
built with [HyperFrames](https://hyperframes.heygen.com) (`npx hyperframes`). Kinetic
type and the article's own Mind/Muscle/Money banner, in Collegica's own palette — no
generated imagery, renders locally for free.

## Rebuild

```bash
npx --yes hyperframes@0.8.33 check                                        # lint + runtime + layout + contrast
npx --yes hyperframes@0.8.33 render -o _output/aging-well-ai-planning.mp4 --crf 23
cp _output/aging-well-ai-planning.mp4 ../../website/static/video/aging-well/ai-planning.mp4
```

## Narration

`audio/frame-0N.wav` are generated with [Kokoro](https://github.com/hexgrad/Kokoro-82M)
(local, free, neural — `hyperframes tts`, voice `af_heart`), one file per frame, timed
against each frame's own composition. A first pass used macOS's built-in `say -v
Samantha`, which was noticeably robotic; Kokoro reads far more naturally at the same
zero cost.

Kokoro needs a one-time Python environment (not committed — see `.gitignore`):

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install kokoro-onnx soundfile      # first use downloads the model (324 MB) and voices (28 MB) into ~/.cache/hyperframes/tts/
npx --yes hyperframes@0.8.33 tts "Your line here." -v af_heart -o audio/frame-0N.wav
```

To change the script: edit the text, regenerate the WAV, re-measure its duration
(`ffprobe -show_entries format=duration`), and scale that frame's GSAP cue timings in
`compositions/frames/` and its `data-duration`/`data-start` (and the following frames'
starts) in `index.html` proportionally to the new duration.

**Pronunciation fix:** Kokoro reads "Collegica" wrong by default. Frame 7's TTS input
spells it "College-ika" (which reads correctly as "College" + "ika") while the on-screen
text and URL stay spelled correctly as "Collegica" — the respelling is audio-only, never
shown.

## Structure

- `index.html` — master timeline, stitches the 7 frames + narration with hard cuts and a
  short crossfade.
- `compositions/frames/0N-*.html` — one self-contained composition per frame.
- `assets/owl-mmm.jpg` — the article's own banner image, reused as-is (the OWL Planning
  logo baked into it is composited from [`../brand/`](../brand/), the shared logo
  library — not referenced directly by any composition here).
- `audio/` — narration WAVs (24 kHz mono, as Kokoro writes them).
