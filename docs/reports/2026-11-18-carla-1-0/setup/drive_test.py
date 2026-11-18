"""Collegica CARLA 1.0 test: car on autopilot in the server's default map, camera saving frames, log timing."""
import json
import time

import carla
import numpy as np
from PIL import Image

OUT = "/out"
log = {}

c = carla.Client("localhost", 2000)
c.set_timeout(300)
log["client_version"] = c.get_client_version()
log["server_version"] = c.get_server_version()
# The first attempt loaded Town10HD_Opt explicitly and the server crashed (signal 11);
# this version uses the map the server starts with.
world = c.get_world()
log["map"] = world.get_map().name
time.sleep(5)


def server_fps(seconds):
    s0, t0 = world.get_snapshot(), time.time()
    time.sleep(seconds)
    s1, t1 = world.get_snapshot(), time.time()
    return round((s1.frame - s0.frame) / (t1 - t0), 1)


log["idle_fps"] = server_fps(20)

bp = world.get_blueprint_library()
spawn = world.get_map().get_spawn_points()[0]
car = world.try_spawn_actor(bp.filter("vehicle.tesla.model3")[0], spawn)
log["car_spawned"] = car is not None
saved = []
if car:
    car.set_autopilot(True)
    cam_bp = bp.find("sensor.camera.rgb")
    cam_bp.set_attribute("image_size_x", "1280")
    cam_bp.set_attribute("image_size_y", "720")
    cam = world.spawn_actor(
        cam_bp, carla.Transform(carla.Location(x=-6, z=3), carla.Rotation(pitch=-12)), attach_to=car
    )
    count = [0]

    def on_image(im):
        count[0] += 1
        if count[0] % 20 == 0:
            arr = np.frombuffer(im.raw_data, dtype=np.uint8).reshape((im.height, im.width, 4))[:, :, :3][:, :, ::-1]
            Image.fromarray(arr).save(f"{OUT}/frame_{len(saved):03d}.jpg", quality=85)
            saved.append(im.frame)

    cam.listen(on_image)
    p0 = car.get_location()
    log["driving_fps"] = server_fps(40)
    p1 = car.get_location()
    log["distance_driven_m"] = round(p0.distance(p1), 1)
    log["camera_frames_received"] = count[0]
    log["frames_saved"] = len(saved)
    cam.stop()
    cam.destroy()
    car.destroy()

json.dump(log, open(f"{OUT}/drive_test.json", "w"), indent=2)
print(json.dumps(log, indent=2))
