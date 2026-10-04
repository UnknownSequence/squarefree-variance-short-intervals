from opt2 import *
import numpy as np
ALL={'mvt','hux','gm','gm12','jut3'}
def need_delta(h, ests, mu, nv=3001):
    tau=1-h
    def bad(d):
        for v in np.linspace(0,0.5,nv):
            rho=rho_bound(d,tau,v,ests)
            if h-tau-2*v*d+Z(rho,tau,mu,True)-h/2>1e-12: return True
        return False
    lo,hi=h/2,0.5
    for _ in range(30):
        m=(lo+hi)/2
        if any(bad(d) for d in np.linspace(m,0.5,16)): lo=m
        else: hi=m
    return hi
print("h, Prop1 max delta (1/2-h/4), Prop2 min delta [GM1.1+Weyl+4th], [all inputs, Bourgain, 4th+12th], (3h-1)/2")
for h in [0.5715,0.573,0.575,0.5775,0.58,0.585,0.59,0.6,0.62,0.64,0.66]:
    a=need_delta(h,{'mvt','hux','gm'},1/6); b=need_delta(h,ALL,MU)
    print(f"{h:.4f}  {0.5-h/4:.5f}  {a:.5f}  {b:.5f}  {(3*h-1)/2:.5f}", flush=True)
