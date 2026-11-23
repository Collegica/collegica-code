import sys, copy, json
sys.path.insert(0, "src"); sys.path.insert(0, ".")
from setuav_studio.project import open_project
from setuav_studio.solver import SolverConfig
from plugins.flight_performance.solver import FlightPerformanceSolver, SOLVER_ID_FLIGHT_PERFORMANCE
from plugins.electrical_propulsion.solver import *  # noqa
def cfg(**o):
    p = FlightPerformanceSolver.default_parameters(); p.update({"v_step":0.5,"alpha_step":1.0,**o})
    return SolverConfig(solver_id=SOLVER_ID_FLIGHT_PERFORMANCE, name="FP", parameters=p)
def run(label, mutate=None, **o):
    proj = open_project("../wing")
    if mutate: mutate(proj.data["components"])
    r = FlightPerformanceSolver(cfg(**o), proj).run()
    print("==", label, "mass_kg=%.3f" % proj.mass_properties.mass_kg)
    for k,v in r.summary.items(): print("  ", k, v.value, getattr(v,"unit",""))
run("baseline")
def span(c):
    w = next(x for x in c if x["name"]=="Main Wing")
    for q in w["parameters"]["geometry"]["profiles"]: q["position"]["y"] *= 1.25
run("span +25%", span)
