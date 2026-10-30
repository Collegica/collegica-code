# Move Your Thesis from Word to Plain Text — video

A 75-second summary of the [markdown-thesis article](https://www.collegica.org/software/markdown-thesis/),
built with [HyperFrames](https://hyperframes.heygen.com) (`npx hyperframes`). Kinetic
type and real pages from the [quarto-thesis-starter](https://github.com/eLearningHub/quarto-thesis-starter)
example, in Collegica's own palette — no generated imagery, renders locally for
free. Same approach as the [`budget-from-statements`](../budget-from-statements/README.md)
and [`ai-planning`](../ai-planning/README.md) videos; read those READMEs for the
full rationale (Kokoro TTS setup, the "Collegica" pronunciation fix, the
render/check/deploy loop) — this one only notes what differs.

## Rebuild

```bash
python3 -m venv .venv && source .venv/bin/activate   # first time only
pip install kokoro-onnx soundfile                     # first time only
npx --yes hyperframes@0.8.33 check
npx --yes hyperframes@0.8.33 render -o _output/markdown-thesis.mp4 --crf 23
cp _output/markdown-thesis.mp4 ../../website/static/video/software/markdown-thesis.mp4
```

## Structure

- `index.html` — master timeline, the hero then 7 frames, hard cuts with a short crossfade.
- `compositions/frames/00-hero.html` — 2.4 s on the article's hero, so the
  poster and the first frame match.
- `compositions/frames/0N-*.html` — one composition per frame: hook (the
  chapter3_final_v2.docx pile and the template you must follow), what plain
  text looks like with its four marks, `pixi run import` keeping the Zotero
  citations, `pixi run word` producing one Word file, the Concordia and
  Stanford front pages, the three commands (or an AI assistant that never
  changes your words), close with the URL.
- `assets/hero-16x9.jpg` — the article's hero at its generated 16:9, before
  the 2:1 crop.
- `assets/*.png` — pages of the starter's Concordia and Stanford PDFs,
  rendered at 150 dpi.
- `audio/` — narration WAVs, Kokoro `af_heart`, one per frame.

Frame 7's TTS input spells "Collegica" as "College-ika" for correct
pronunciation; the on-screen text and URL stay spelled correctly.

## The hero

`website/static/img/software/markdown-thesis-hero.*` was generated with GPT
Image 2 (HiggsField `gpt_image_2`, 16:9, 2K, high quality; job
`b83bd911-008f-4419-a78b-e122802eefd4`, 2026-10-03), with the layout and
typefaces named in the prompt as in `docs/2026-09-13-edge-agent/hero.md`. The
model drew eight dots in the mark; a patch of blank paper from below it covers
the centre one, leaving the real seven. The PNG is that corrected 2688 × 1520;
the JPG is rows 60–1404 resized to 1774 × 887, plus a 900-wide variant.
