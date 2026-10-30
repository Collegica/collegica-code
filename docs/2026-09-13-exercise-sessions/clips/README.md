# One dead bug, five video models — cost and form, 2026-09-13

The same prompt (`dead-bug-prompt.txt`, written to the `exercise-videos`
skill's template) sent to five text-to-video models through HiggsField in
one batch, 16:9, silent, ten seconds where the model allows it. Costs are
the preflight figures from `get_cost`, confirmed identical in the
transaction log. Form was judged from the contact sheets beside this file
(2 frames a second, whole clip), not from every frame, and by an editor,
not a trainer.

| Model | Credits | Output | Form verdict |
|---|---|---|---|
| **Wan 3.0** (720p, thinking on, audio off) | **17.5** | 1280 × 720, 30 fps, 10.0 s | **Correct.** True tabletop start, one leg extends while the opposite arm lowers overhead, the other leg stays in tabletop, sides alternate. The only clip that is a dead bug as taught. |
| Seedance 2.5 (720p, audio off) | 65 | 1280 × 720, 24 fps, 10.0 s | Close. Opposite arm and leg move together and alternate, but the resting foot is on the floor with the knee bent, not in tabletop: the easier "modified" version. Cleanest light and framing. |
| Kling v3.0 (pro, 1080p, sound off) | 17.5 | 1920 × 1080, 24 fps, 10.0 s | Partly wrong. Resting leg lies flat; at the extremes both arms go overhead together instead of one. Sharp image, true side view. |
| Google Veo 3.1 (fast, high, 8 s) | 22 | 1920 × 1080, 24 fps, 8.0 s | Wrong exercise. Feet on the floor, knees bent, one arm held up and one straight leg raised and lowered: a leg raise, not a dead bug. Veo also rewrote the prompt into its own structured brief (`enhance_prompt: true`), which is where the drift began. |
| MiniMax H3 (2K) | 20 | 2560 × 1440, 24 fps, 10.1 s | Wrong exercise, wrong scene. Heel slides along the floor with the opposite arm lowering; a bright room with a mirror instead of the neutral studio; the figure small in the frame. |

Total spent: 142 credits of 1,026. Preflighted but not run: FLUX 3 Video
55, Gemini Omni Flash 1.1 30.

## What this says

- **Price did not predict form.** The cheapest model produced the only
  correct clip; the most expensive produced the second best; two mid-priced
  ones produced a different exercise.
- **The failure mode is substitution, not sloppiness.** Every clip is
  anatomically clean and smooth. Three of five quietly performed an easier
  or different movement — feet on the floor, a leg slide, both arms
  together. A viewer who does not know the dead bug would not notice, which
  is exactly why a generated clip cannot ship without a person who knows
  the exercise checking it.
- **The cue that mattered was "shins parallel to the floor".** The
  tabletop position is the dead bug; models that dropped a foot to the
  floor had lost it. For floor exercises, name the position of the
  *non-moving* limbs as precisely as the moving ones.
- **Ten seconds holds two slow repetitions**, one per side, in every
  model that kept the exercise. Do not ask for more.

## Files

`inspect.sh NAME URL` downloads a clip, prints its dimensions, frame rate
and duration, and writes `NAME-contact.jpg`. The MP4s stay on disk and out
of git (`.gitignore`); the contact sheets are the record. Job ids:
Seedance f2954fa9, Kling 516daec6, Veo 033c4f84, Wan 591b8d9c, MiniMax
b44e76ab.
