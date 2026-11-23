# SetUAV Studio, tried on 2026-11-23

Notes behind the article `website/robotics/uav-design-studio/`.

## What was tested

- Studio from <https://github.com/Setuav/Studio> (MIT, version 0.1.0, 719
  commits on `main` at the time), installed with `uv sync --locked` on macOS.
  The app opened the bundled example, `tests/fixtures/fixed-wing/`.
- The three analyses were run **without the GUI**, by calling the plugin code
  the same way the project's own tests do. The scripts are in `scripts/` and
  expect to run from a Studio checkout (`uv run --locked python <script>`) with
  a copy of the fixture in `../wing`.
- Not tested: building an aircraft from scratch in the GUI, the airspeed and
  throttle sweeps, the other two aerodynamic methods, or any real aircraft.

## Results (example aircraft, 1548 g, 3S 6000 mAh, SunnySky X2814 KV900, APC 12x6)

AeroBuildup, 25 m/s, sea level (`aero_compare.py`):

| Design | S (m2) | b (m) | AR | CLmax | CDmin | L/D max |
|---|---|---|---|---|---|---|
| Baseline | 0.284 | 1.503 | 7.95 | 1.41 | 0.0199 | 16.8 |
| Span +25% | 0.355 | 1.841 | 9.54 | 1.43 | 0.0181 | 19.5 |
| Chord -20% | 0.227 | 1.503 | 9.94 | 1.45 | 0.0226 | 17.0 |

Flight performance, defaults (polar at 15 m/s) (`flight_performance.py`):

| | Baseline | Span +25% |
|---|---|---|
| Stall speed (m/s) | 7.72 | 6.93 |
| L/D max | 14.2 | 16.0 |
| Best range speed (m/s) | 11.9 | 10.5 |
| Cruise power (W) | 27.8 | 22.1 |
| Endurance (min) | 137 | 174 |
| Range (km) | 85.9 | 95.7 |
| Max level speed (m/s) | 32.0 | 31.4 |

The mass stayed 1548 g in both: the wing has no mass of its own in the
example, so a longer wing weighs nothing more. This flatters the long wing.

Operating point (`operating_point.py`):

| Airspeed (m/s) | Throttle | Thrust (N) | Electrical power (W) | Current (A) |
|---|---|---|---|---|
| 0 | 100% | 23.7 | 462 | 38.9 |
| 0 | 50% | 7.3 | 82 | 6.6 |
| 12 | 40% | 1.16 | 30 | 2.4 |
| 25 | 100% | 8.3 | 348 | 28.8 |

## Checks

- Stall speed by hand, sqrt(2W / (rho S CLmax)) with W = 15.18 N, S = 0.28405 m2,
  CLmax = 1.4656: 7.72 m/s. Matches the tool.
- L/D max by hand, 0.5 / sqrt(CD0 k) with the tool's own CD0 = 0.01894 and
  k = 0.06555: 14.2. Matches the tool. (Ideal induced drag alone, k = 1/(pi e AR)
  = 0.049, would give 16.3: the fitted k is larger.)
- Static thrust by momentum theory, T = FM^(2/3) (2 rho A)^(1/3) P^(2/3), with
  A = 0.0730 m2, shaft power about 370 W (80% of 462 W) and a figure of merit
  of 0.7: about 23 N. The tool says 23.7 N. This is a consistency check, not a
  validation.
- No datasheet or bench test for this exact motor and propeller on 3S turned
  up in a web search on 2026-11-23, so the propulsion numbers are not checked
  against a maker.

## Oddities

- The example's stored results (`results/cruise/`) are placeholders with fake
  checksums.
- Its `wing_area` constant reads 32 mm2, while the geometry has 0.284 m2. A
  relation (`wing-sizing`) is meant to drive the wing span from area and
  aspect ratio. Not investigated further.
- Max climb angle comes out as 90 degrees and rate of climb 14 m/s: the motor
  can lift more than the aircraft weighs.
