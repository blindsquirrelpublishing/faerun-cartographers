#!/usr/bin/env python3
"""Basic geometry/grid checker for a shared engineering master (Python 3, standard library)."""
import json, math, sys, hashlib
from pathlib import Path

ALLOWED = {"official", "derived", "modelled", "invented"}

def points_nested(v):
    if isinstance(v,(list,tuple)) and len(v)>=2 and all(isinstance(x,(int,float)) and math.isfinite(x) for x in v[:2]):
        yield (float(v[0]),float(v[1]))
    elif isinstance(v,list):
        for x in v:
            yield from points_nested(x)

def main(p):
    raw=Path(p).read_bytes()
    d=json.loads(raw)
    errs=[]
    grid=d.get("grid",{})
    w=grid.get("columns",0); h=grid.get("rows",0); cell=grid.get("cell_feet",0)
    origin=grid.get("origin_xy",[0,0])
    if d.get("units")!="feet": errs.append("units must be feet")
    if not all(isinstance(a,(int,float)) and a>0 for a in [w,h,cell]): errs.append("grid dimensions/pitch invalid")
    if len(origin)!=2: errs.append("grid origin_xy must contain x and y")
    seen=set()
    if not isinstance(d.get("features"),list): errs.append("features must be a list")
    for i,f in enumerate(d.get("features",[])):
        key=f.get("id")
        if not key or key in seen: errs.append(f"feature {i}: duplicate/missing id")
        seen.add(key)
        if f.get("status") not in ALLOWED: errs.append(f"feature {key}: bad status")
        shape=f.get("geometry",{})
        pts=list(points_nested(shape.get("coordinates",[])))
        if not pts: errs.append(f"feature {key}: missing valid XY feet points")
        if shape.get("type")=="Polygon":
            rings=shape.get("coordinates",[])
            for r in rings:
                if len(r)<4 or r[0]!=r[-1]: errs.append(f"feature {key}: unclosed polygon ring")
    print(json.dumps({"city":d.get("city"),"revision":d.get("revision"),"grid_extent_ft":[w*cell,h*cell],
                      "features":len(d.get("features",[])),"sha256":hashlib.sha256(raw).hexdigest(),
                      "errors":errs},indent=2))
    return 1 if errs else 0

if __name__=="__main__":
    if len(sys.argv)!=2: sys.exit("Usage: validate_master.py geometry-master.json")
    sys.exit(main(sys.argv[1]))
