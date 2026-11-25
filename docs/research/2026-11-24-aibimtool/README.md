# AIBIMTool, tried on 2026-11-24

Notes behind the article `website/ai/aibimtool/`. Everything below was observed
in a browser on the **free plan**; nothing was bought, no new project was made
and nothing was sent to the vendor.

## The test

One synthetic brief (made up, no real client or site), 160 m2 in total:

> Design a detached two-storey house with a rectangular footprint of 10 m by
> 8 m (80 m2 per floor, 160 m2 total) and a flat roof. Ground floor: living
> room 30 m2, kitchen-dining 20 m2, study 10 m2, WC 4 m2, entrance hall with
> staircase 16 m2. First floor: bedroom 1 18 m2, bedroom 2 14 m2, bedroom 3
> 12 m2, bathroom 10 m2, landing with staircase 14 m2, storage 12 m2. Storey
> height 3.0 m. Include a front door, and windows to every habitable room.

The room areas add up to exactly 80 m2 per floor, so the brief leaves no room
for walls. That is deliberate: it shows what the tool does with a brief that
cannot be met.

## What happened, in order

1. Account: free plan, "one free generation, 100 credits".
2. 2026-11-23: three submissions of the brief (the brief, then two "please try
   again") each returned "The AI service is busy or at its limit right now.
   Nothing was charged; please try again in a few minutes." The balance stayed
   at 100.
3. 2026-11-24, after the vendor's outage was reported resolved: the same brief
   was sent once more in the same project. It ran for 2 min 43 s and finished.
   The tool reported "5 steps · 15 credits used", then "Your free generation is
   complete", and the balance shown was 0. (15 credits used and a balance of 0
   do not obviously agree; the screen does not explain it.)
4. A purchase dialog ("Insufficient Credits") appeared. It was cancelled.

## The result

Model areas, net inside the walls, as the tool reported them in chat, against
the brief:

| Room | Brief (m2) | Model (m2) | Difference |
|---|---|---|---|
| Living room | 30 | 27.7 | -7.7% |
| Kitchen-dining | 20 | 18.2 | -9.0% |
| Study | 10 | 8.6 | -14% |
| WC | 4 | 3.0 | -25% |
| Entrance hall | 16 | 14.7 | -8.1% |
| Bedroom 1 | 18 | 16.3 | -9.4% |
| Bedroom 2 | 14 | 12.8 | -8.6% |
| Bedroom 3 | 12 | 10.6 | -11.7% |
| Bathroom | 10 | 6.8 | -32% |
| Landing | 14 | 22.8 (includes the corridor) | +63% |
| Storage | 12 | 4.1 | -66% |

Ground-floor rooms sum to 72.2 m2 of 80; first-floor rooms to 73.4 m2 of 80.

The tool said, unprompted, that the first-floor rooms come out well under the
brief and that it did not fix that; that it had not re-run its linter after the
last stair step (the linter's "no stair between storeys" finding was therefore
unresolved); and that its isometric view showed stray spikes on the roof, which
it read as a rendering artefact. We did not see spikes in the 3D view
(`screenshots/design-view-3d.jpg`).

The Program tab loaded a spreadsheet with achieved and target areas per room.
Its figures differ slightly from the chat table (landing 20.80 against 22.8,
kitchen-dining 18.15 against 18.2). Every row shows a height of 2750 mm. The
model tree shows the ground floor at 3,000 mm and the first floor at
2,750 mm, against the 3.0 m asked for.

## IFC export: not tested, behind a paywall

- The file menu has Export with four entries: Model (IFC), Areas, Take-off and
  Bill of Quantities. Each carries a "Starter" badge. None was clicked.
- The BIM tab is locked behind the Studio plan. The dialog quoted CA$279 a
  month billed yearly (CA$3,348 a year), or CA$429 monthly.
- The Starter plan was quoted at CA$79 a month billed yearly (CA$139 monthly)
  and lists IFC4 export. The marketing page said $49 and $189 a month, so the
  prices on the site and in the app disagree.
- So the claim that the output opens in Revit, Archicad or Rhino was **not
  checked**. The free IFC viewer was not tried either.

## Not done

Open the exported IFC anywhere; compare the model with a hand drawing; check
the doors, windows and stair; the API, CLI and MCP; the program sheet's Xlsx
and PDF export (not clicked).
