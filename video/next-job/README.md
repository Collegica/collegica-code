# Finding Your Next Job, with AI — video

A 90-second summary of the [next-job article](https://www.collegica.org/aging-well/next-job/),
built with [HyperFrames](https://hyperframes.heygen.com) (`npx hyperframes`). Kinetic
type and the article's own banner in Collegica's own palette — no generated
imagery, renders locally for free. Same approach as the
[`ai-planning` video](../ai-planning/README.md); read that project's README for
the full rationale (Kokoro TTS setup, the "Collegica" pronunciation fix,
the render/check/deploy loop) — this one only notes what differs.

## Rebuild

```bash
python3 -m venv .venv && source .venv/bin/activate   # first time only
pip install kokoro-onnx soundfile                     # first time only
npx --yes hyperframes@0.8.33 check
npx --yes hyperframes@0.8.33 render -o _output/next-job.mp4 --crf 23
cp _output/next-job.mp4 ../../website/static/video/aging-well/next-job.mp4
```

## Structure

- `index.html` — master timeline, 7 frames, hard cuts with a short crossfade.
- `compositions/frames/0N-*.html` — one composition per frame: hook, the
  two Canadian numbers over the article's own banner, the two-readers
  argument, what AI is/isn't good at, the one-folder rule, the five plans as
  a checklist, close with the URL.
- `assets/owl-next-job.jpg` — the article's own banner image, reused as-is.
- `audio/` — narration WAVs, Kokoro `af_heart`, one per frame.

Same pronunciation note as `ai-planning`: frame 7's TTS input spells
"Collegica" as "College-ika" for correct pronunciation; the on-screen text
and URL stay spelled correctly.
