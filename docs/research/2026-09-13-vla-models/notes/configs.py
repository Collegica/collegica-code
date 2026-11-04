import dataclasses, importlib, pkgutil, time
t0 = time.perf_counter()
import lerobot, lerobot.policies as P
print(f"lerobot {lerobot.__version__}; import {time.perf_counter()-t0:.2f}s")
names = sorted(m.name for m in pkgutil.iter_modules(P.__path__) if m.ispkg and m.name not in ("common",))
print(len(names), "policy packages:", ", ".join(names))
KEYS = ["vlm_model_name", "vlm_base", "base_model_path", "paligemma_variant", "action_expert_variant",
        "pretrained_name_or_path", "tokenizer_name", "num_vlm_layers", "expert_width_multiplier",
        "chunk_size", "n_action_steps", "image_resolution", "resize_imgs_with_padding", "image_size",
        "image_min_pixels", "image_max_pixels", "action_head", "prediction_mode", "len_soft_prompts", "dtype"]
for name in ["smolvla", "pi0", "pi0_fast", "pi05", "groot", "xvla", "eo1", "evo1", "molmoact2", "wall_x", "vla_jepa"]:
    try:
        mod = importlib.import_module(f"lerobot.policies.{name}.configuration_{name}")
    except Exception as e:
        print(f"\n[{name}] import failed: {type(e).__name__}: {str(e)[:90]}"); continue
    cfgs = [c for c in vars(mod).values() if dataclasses.is_dataclass(c) and isinstance(c, type) and c.__name__.endswith("Config") and c.__module__ == mod.__name__]
    for C in cfgs:
        try:
            c = C()
        except Exception as e:
            print(f"\n[{name}] {C.__name__}: cannot instantiate defaults ({type(e).__name__}: {str(e)[:80]})"); continue
        vals = {k: getattr(c, k) for k in KEYS if hasattr(c, k)}
        print(f"\n[{name}] {C.__name__}")
        for k, v in vals.items(): print(f"   {k} = {v!r}")
