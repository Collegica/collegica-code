import json, sys, copy
sys.path.insert(0, "src")
from plugins.aerodynamics.engine.aerosandbox_engine import AeroSandboxEngine
from plugins.aerodynamics.engine.base import FlightCondition, AnalysisMethod
p = json.load(open("../wing/project.json"))
def wing(c): return next(x for x in c if x["name"]=="Main Wing")
def run(comps, label):
    cond = FlightCondition(velocity=25, alpha=2, altitude=0, sweep_min=-4, sweep_max=12, sweep_steps=9)
    r = AeroSandboxEngine().analyze(comps, cond, method=AnalysisMethod.AERO_BUILDUP)
    ref=r.reference
    print(f"{label}: S={ref.s_ref:.3f} m2 b={ref.b_ref:.3f} m  AR={ref.b_ref**2/ref.s_ref:.2f}  CLmax={r.cl_max:.2f}  CDmin={r.cd_min:.4f}  L/Dmax={r.ld_max:.1f} @ {r.ld_max_alpha:.1f}deg  e={r.oswald_efficiency}")
w = wing(p["components"])
print("wing profiles:", [(q.get("chord"), q["position"]) for q in w["parameters"]["geometry"]["profiles"]])
run(p["components"], "baseline")
# longer span: scale y of every profile by 1.25
c2 = copy.deepcopy(p["components"]); 
for q in wing(c2)["parameters"]["geometry"]["profiles"]: q["position"]["y"] *= 1.25
run(c2, "span +25%")
c3 = copy.deepcopy(p["components"])
for q in wing(c3)["parameters"]["geometry"]["profiles"]: q["chord"] *= 0.8
run(c3, "chord -20%")
