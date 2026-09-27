# A Year of Spending, from Your Own Statements — video

A 90-second summary of the [budget-from-statements article](https://www.collegica.org/aging-well/budget-from-statements/),
built with [HyperFrames](https://hyperframes.heygen.com) (`npx hyperframes`). Kinetic
type and the article's own banner in Collegica's own palette — no generated
imagery, renders locally for free. Same approach as the
[`ai-planning`](../ai-planning/README.md) and [`next-job`](../next-job/README.md)
videos; read either project's README for the full rationale (Kokoro TTS
setup, the "Collegica" pronunciation fix, the render/check/deploy loop) —
this one only notes what differs.

## Rebuild

```bash
python3 -m venv .venv && source .venv/bin/activate   # first time only
pip install kokoro-onnx soundfile                     # first time only
npx --yes hyperframes@0.8.33 check
npx --yes hyperframes@0.8.33 render -o _output/budget-from-statements.mp4 --crf 23
cp _output/budget-from-statements.mp4 ../../website/static/video/aging-well/budget-from-statements.mp4
```

## Structure

- `index.html` — master timeline, 7 frames, hard cuts with a short crossfade.
- `compositions/frames/0N-*.html` — one composition per frame: hook (only
  one of six kinds of movement is spending), the six-kinds chip reveal, the
  article's own banner with the CSV/PDF-reconcile badges, the
  recurring/irregular output cards, three lessons from building it, the
  in-your-browser checklist, close with the URL.
- `assets/owl-budget.jpg` — the article's own banner image, reused as-is.
- `audio/` — narration WAVs, Kokoro `af_heart`, one per frame.

Same pronunciation note as the other two videos: frame 7's TTS input spells
"Collegica" as "College-ika" for correct pronunciation; the on-screen text
and URL stay spelled correctly.
