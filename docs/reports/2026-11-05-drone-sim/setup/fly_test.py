"""Collegica drone-sim test: fly CARLA-Air's drone over Town10HD, save frames, log timing."""
import json
import time

import airsim
import carla
import numpy as np
from PIL import Image

OUT = "/out"
log = {}

c = carla.Client("localhost", 2000)
c.set_timeout(30)
world = c.get_world()
log["map"] = world.get_map().name
log["server_version"] = c.get_server_version()


def server_fps(seconds):
    s0, t0 = world.get_snapshot(), time.time()
    time.sleep(seconds)
    s1, t1 = world.get_snapshot(), time.time()
    return round((s1.frame - s0.frame) / (t1 - t0), 1)


# Server frame rate with nothing happening (asynchronous mode).
log["idle_fps"] = server_fps(20)

# A car on autopilot, with a chase camera.
bp = world.get_blueprint_library()
car = world.try_spawn_actor(bp.filter("vehicle.tesla.model3")[0], world.get_map().get_spawn_points()[0])
frames = []
if car:
    car.set_autopilot(True)
    cam_bp = bp.find("sensor.camera.rgb")
    cam_bp.set_attribute("image_size_x", "1280")
    cam_bp.set_attribute("image_size_y", "720")
    cam = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=-6, z=3), carla.Rotation(pitch=-12)), attach_to=car)
    cam.listen(lambda im: frames.append(im) if len(frames) < 1 else None)

a = airsim.MultirotorClient()
a.confirmConnection()
a.enableApiControl(True)
a.armDisarm(True)
track = []
T0 = time.time()


def sample(tag):
    p = a.getMultirotorState().kinematics_estimated.position
    track.append({"t": round(time.time() - T0, 2), "tag": tag,
                  "x": round(p.x_val, 2), "y": round(p.y_val, 2), "z": round(p.z_val, 2)})


def shot(name):
    r = a.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])[0]
    img = np.frombuffer(r.image_data_uint8, dtype=np.uint8).reshape(r.height, r.width, 3)
    Image.fromarray(img[:, :, ::-1]).save(f"{OUT}/{name}.png")


sample("start")
a.takeoffAsync().join()
sample("takeoff")
a.moveToZAsync(-30, 5).join()
sample("climb to 30 m")
shot("drone-30m")

s0, t0 = world.get_snapshot(), time.time()
for i, (x, y) in enumerate([(40, 0), (40, 40), (0, 40), (0, 0)]):
    a.moveToPositionAsync(x, y, -30, 6).join()
    sample(f"waypoint {i + 1}")
    shot(f"drone-wp{i + 1}")
s1, t1 = world.get_snapshot(), time.time()
log["flying_fps"] = round((s1.frame - s0.frame) / (t1 - t0), 1)
log["square_seconds"] = round(t1 - t0, 1)

a.landAsync().join()
sample("land")
a.armDisarm(False)
a.enableApiControl(False)

if car:
    time.sleep(1)
    if frames:
        frames[0].save_to_disk(f"{OUT}/car-camera.png")
    cam.destroy()
    car.destroy()

log["track"] = track
json.dump(log, open(f"{OUT}/fly_test.json", "w"), indent=1)
print(json.dumps({k: v for k, v in log.items() if k != "track"}))
