import time, warp as wp
t0 = time.perf_counter(); wp.init(); t1 = time.perf_counter()
print("warp", wp.__version__, "| devices:", [str(d) for d in wp.get_devices()], "| cuda available:", wp.is_cuda_available(), f"| init {t1-t0:.2f}s")

@wp.kernel
def saxpy(a: float, x: wp.array(dtype=float), y: wp.array(dtype=float)):
    i = wp.tid()
    y[i] = a * x[i] + y[i]

n = 10_000_000
x = wp.full(n, 1.0, dtype=float, device="cpu"); y = wp.zeros(n, dtype=float, device="cpu")
t0 = time.perf_counter(); wp.launch(saxpy, dim=n, inputs=[2.0, x, y], device="cpu"); wp.synchronize(); t1 = time.perf_counter()
print(f"first launch, including the JIT compile: {t1-t0:.2f}s")
t0 = time.perf_counter()
for _ in range(10): wp.launch(saxpy, dim=n, inputs=[2.0, x, y], device="cpu")
wp.synchronize(); t1 = time.perf_counter()
print(f"10 more launches of a {n:,}-element kernel: {(t1-t0)/10*1000:.1f} ms each | y[0] = {y.numpy()[0]}")
