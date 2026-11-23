import sys
sys.path.insert(0, "src"); sys.path.insert(0, ".")
from setuav_studio.project import open_project
from setuav_studio.solver import SolverConfig
from plugins.electrical_propulsion.solver import OperatingPointSolver, SOLVER_ID_OPERATING_POINT
proj = open_project("../wing")
p = OperatingPointSolver.default_parameters(); print(p)
for v,t in ((0,100),(0,50),(12,40),(25,100)):
    q=dict(p); 
    for k in q:
        if k.startswith("airspeed"): q[k]=v
        if k.startswith("throttle"): q[k]=t
    r = OperatingPointSolver(SolverConfig(solver_id=SOLVER_ID_OPERATING_POINT,name="op",parameters=q), proj).run()
    print(f"V={v} thr={t}%:", {k:(round(x.value,3) if isinstance(x.value,float) else x.value) for k,x in r.summary.items()})
