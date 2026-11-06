# Drone Lab, read from its source

**Access and confidence.** The app at <https://drone-engineer.vercel.app> is a
single 548 KB HTML file with its JavaScript inline and readable (fetched
2026-11-05; `last-modified: Thu, 05 Nov 2026 11:34:31 GMT`, so it is still
being changed). No author, licence or repository is named in it. Its comments
refer to a `SKILL.md` drawing contract and to `crafts/NN-key.js` files built
into the page by `scripts/build.py`: the format AI coding assistants use for
instructions, which suggests (not proves) it was built with one. Line numbers
below are in that file. High confidence in what the code does; nothing here
says how closely it was meant to match reality.

## The flight model (`multirotor`, lines ~797–850)

- **Attitude is set, not simulated.** In angle mode, roll and pitch move
  toward stick × 38° with a first-order lag (`k = dt × 9`); in acro mode, they
  integrate stick × 540°/s. There is no rotational inertia, no motor
  spin-up, no torque balance and no PID controller in the physics: the
  "PID" in the parts text is description only.
- **Thrust** = effective throttle × number of motors × the static maximum
  thrust per motor; effective throttle follows throttle² with a lag. Thrust
  does not change with airspeed or climb rate (a real propeller loses thrust
  as it moves through the air).
- **Drag** is one coefficient (0.045 by default) times velocity × (speed + 1).
- **Wind** is a gentle sinusoid of about 1.2 m/s when switched on.
- **Faults are scripted:** a reversed flight controller or swapped props
  adds a fixed spin on take-off; an over-revved motor builds "heat" and
  desyncs after a threshold.
- **The battery** (`batteryStep`) draws current from a power law of throttle,
  with an empirical voltage curve, `cells × (3.3 + 0.9 × charge^0.7)`, minus
  a sag of 0.012 V per amp per 6 cells. Low-voltage warning at 3.5 V per cell,
  cut-out at 3.2 V.
- **Sensors are perfect:** the model knows its exact position and attitude.
  An uncalibrated accelerometer is modelled as a fixed sideways drift.

## The calculator (`calc`, line 691; craft overrides elsewhere)

- Voltage = cells × 3.7 V (nominal); rpm = KV × voltage (the motor's
  **unloaded** speed).
- Thrust per motor (g) = 1.06 × prop factor × (rpm / 1000)².
- Hover power = all-up weight ÷ (5.4 g/W × prop efficiency); hover current =
  power ÷ voltage.
- Hover time = 80% of capacity ÷ hover current; flying time = 42% of hover
  time (85% for the cinematic drone, 92% for the Crazyflie).
- Hover throttle = √(weight ÷ total thrust).

These are rules of thumb tuned per craft (the constants differ for each
drone), not a model of the motor and propeller.

### The default 5-inch freestyle quad

6S 1100 mAh, 2306 1750KV, 5×4.3×3 props: all-up weight 514 g, 1,600 g thrust
per motor, 12.5:1 thrust-to-weight, 28% hover throttle, 4.3 A hover, 12.3
min hover, 5.2 min flying. Computed with the formulas above (node).

| Battery | Motor | Thrust / motor | Weight | T:W | Flying time |
|---|---|---|---|---|---|
| 6S 1100 | 1750KV | 1,600 g | 514 g | 12.5 | 5.2 min |
| 6S 1800 | 1750KV | 1,600 g | 618 g | 10.4 | 7.0 min |
| 4S 1500 | 1750KV | 711 g | 518 g | 5.5 | 4.7 min |
| 6S 1100 | 2450KV | 3,136 g | 510 g | 24.6 | 5.2 min (flagged: over-revved) |

Not checked against a motor test: T-Motor and other makers publish the full
thrust tables only as images, which we could not read reliably.

### The Crazyflie (line ~4920)

Default: 1S 250 mAh, stock 7×16 coreless motors, 45 mm props, Flow deck and
Lighthouse deck fitted. Thrust 13.4 g per motor (53.6 g total), all-up weight
28.4 g, thrust-to-weight 1.89, hover 1.74 A, 6.9 min hover, 6.3 min flying.

Against Bitcraze's own figures (see `bitcraze.md`):

| | Drone Lab | Bitcraze |
|---|---|---|
| Take-off weight | 28.4 g **with** Flow (1.6 g) and Lighthouse (1.8 g) decks | 29 g **without** decks; Flow 1.6 g, Lighthouse 2.7 g, so 33.3 g with both |
| Flight time | 6.3 min with both decks | 7 min with the stock battery, no decks |
| Lighthouse deck | 1.8 g | 2.7 g |
| Battery position | under the board, velcro strap (`z:-1`) | on top, between the pins, held by the battery-holder board |
| Base stations | two on the cage's corner posts (in the 5 Nov version) | required for Lighthouse positioning |

So the weight is about 5 g (15%) light against a recommended maximum payload
of 15 g, and the flight time is for a lighter drone than the one drawn. The
battery placement is the one the LinkedIn commenter criticised; the missing
base stations they mentioned are now in the scene.
