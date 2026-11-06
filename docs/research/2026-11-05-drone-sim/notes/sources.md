# Sources checked

**Access and confidence.** Read 2026-11-05. Bitcraze, PX4 and ArduPilot
pages read in full through a text reader; Transport Canada's landing pages
read, the detailed rules page not found (404), so the 250 g threshold comes
from Transport Canada's own *Drone Zone* newsletter (October 2025) and fees
are left out. Prices: one Canadian retailer, on the day.

## Bitcraze (Crazyflie)

- [Crazyflie 2.1+](https://www.bitcraze.io/products/crazyflie-2-1-plus/):
  take-off weight 29 g; 92 × 92 × 29 mm; 7 min flight time with the stock
  battery; 40 min to charge; maximum recommended payload 15 g; decks mount
  on top and bottom.
- [Getting started](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/):
  250 mAh LiPo; "Place the battery between the pins and insert the battery
  holder board onto the pins" (on top of the board).
- [Flow deck v2](https://www.bitcraze.io/products/flow-deck-v2/): 1.6 g,
  VL53L1x ToF + PMW3901 optical flow, "designed for mounting under".
- [Lighthouse deck](https://www.bitcraze.io/products/lighthouse-positioning-deck/):
  2.7 g; four receivers; uses HTC Vive / SteamVR base stations.
- [Positioning overview](https://www.bitcraze.io/documentation/system/positioning/).
- Price: C$342.86 at [RobotShop Canada](https://ca.robotshop.com/products/bitcraze-crazyflie-21)
  (5 Nov 2026); Bitcraze's own store lists US$240.

## Simulators

- PX4 + Gazebo: [docs](https://docs.px4.io/main/en/sim_gazebo_gz/). Gazebo
  (Harmonic on Ubuntu 22.04) is the supported simulator; `make px4_sitl gz_x500`
  flies a quadcopter.
- ArduPilot SITL: [docs](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html).
  The autopilot code built for a PC, with built-in physics; runs on Linux
  and Windows; Mission Planner can start it.
- Crazyflie: [CrazySim](https://github.com/gtfactslab/CrazySim) (ICRA 2024,
  Georgia Tech): the Crazyflie firmware in software-in-the-loop with Gazebo;
  a community project, not official Bitcraze.
- CARLA-Air: see `../../reports/2026-11-05-drone-sim/README.md`.

## Rules in Canada

- Transport Canada, [Drone Zone, October 2025](https://tc.canada.ca/en/aviation/drone-safety/drone-zone/drone-zone-issue-3-october-2025):
  under 250 g is a microdrone; 250 g or more must be registered, and the
  pilot needs a Pilot Certificate. Microdrones still follow the safety rules.
- [Getting a drone pilot certificate](https://tc.canada.ca/en/aviation/drone-safety/drone-pilot-licensing/getting-drone-pilot-certificate):
  basic, advanced and Level 1 complex.

## The post and the clones

- The LinkedIn post: <https://lnkd.in/p/ge5Ph_2R> (late October 2026), 41
  comments. Commenters are private individuals: paraphrase, don't name.
- [kanishka-namdeo/build-a-drone](https://github.com/kanishka-namdeo/build-a-drone)
  (MIT, created 30 Oct 2026), [benjaminmuuo/drone-simulator](https://github.com/benjaminmuuo/drone-simulator).
