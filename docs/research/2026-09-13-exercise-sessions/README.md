# A session you can keep — plan and research

Plan and notes for the aging-well article on exercise routines and the
OWL Sessions app: the three families of movement the muscle plan needs,
how a session is built, and an app that runs it in the browser with
nothing uploaded. Started 2026-09-13, published 2026-09-14.

Audience: the reader of *Planning to Age Well, with AI* who agreed with
plan two and has not started it.

## What was verified, and how

| Claim | Checked against |
|---|---|
| WHO activity figures (150–300 min, 2+ strength days, 3+ balance days for 65+) | Already cited in the framework article; the guideline publication (25 November 2020) is the source — [`notes/routines.md`](notes/routines.md) |
| The anti-movement families and the McGill Big Three | Standard strength-coaching taxonomy; McGill's *Back Mechanic* for the Big Three — judgement, not a study |
| The session structure (five blocks, one-minute rests, 30/45/60) | Design decisions, explained in the note; the plans add up exactly to their lengths (`website/static/js/sessions/plans.js`) |
| The clips show the exercises they claim | Every clip compared from a 2 fps contact sheet by an editor, not a trainer — [`clips/README.md`](clips/README.md) for the five-model comparison, [`apps/owl-sessions/README.md`](../../../apps/owl-sessions/README.md) for the library |
| The app runs entirely in the page | Its source: no network calls; module scripts, one `<video>`, `AudioContext` beeps |

Not verified: any health claim beyond the WHO figures; the correctness of
the demonstrations to a trainer's standard. Both are said in the article.

## Decisions

1. **Routines, not exercises.** The framework article already lists the
   movements; this one is about the decisions a routine removes.
2. **Group by what the trunk does**, not by the barbell — anti-movement
   core, loaded, on the feet — because the anti-movement family is the one
   people skip and the one that protects a back.
3. **Thirty minutes is the default**; forty-five and sixty are the same
   blocks with more rounds.
4. **One-minute rests between blocks**, not between exercises; alternating
   muscles within a block is the rest.
5. **Say plainly that the clips are generated and how they were checked**,
   including the ones that failed. The failure mode (a clean performance of
   a different exercise) is the article's most useful paragraph.
6. **The curl-up stays out.** Two attempts produced a crunch; shipping it
   wrong would be worse than the gap.

## Traps hit

- Wan 3.0 crops heads on standing moves; 4:3 fixed some, Kling fixed the
  rest. Recorded in the library README and the skill.
- Seven concurrent Wan jobs hit a rate limit; presets can intercept a
  submission (`declined_preset_id`).
- A stick-figure prototype of the animations was built first and was not
  useful; it was discarded in favour of clips.
- The site's `static/img/events/*.png` rule caught a hero PNG once; heroes
  here go under `static/img/aging-well/`.

## Files

- [`notes/routines.md`](notes/routines.md) — the families, the session structure, the sources.
- [`clips/`](clips/) — the five-model dead-bug comparison.
- [`../../../apps/owl-sessions/`](../../../apps/owl-sessions/) — prompts, job log, contact sheets and the library README; the runtime is under `website/sessions/` and `website/static/js/sessions/`.
- [`hero.md`](hero.md) — the hero image and how it was made.
