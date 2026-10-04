import numpy as np, sys
from fractions import Fraction as F
MU = 13/84
def Z(rho, tau, mu=MU, use12=True):
    def f(u):
        m = min(rho, tau-4*u)
        if use12: m = min(m, 2*tau-12*u)
        return 2*u + m
    cands = [0, mu*tau, (tau-rho)/4, (2*tau-rho)/12, tau/8]
    return max(f(min(max(u,0),mu*tau)) for u in cands)

def rho_bound(delta, tau, v, ests):
    s = 1 - v
    out = [max(tau, 0.0)]
    if 'mvt' in ests: out.append(max(tau, delta) - delta + 2*v*delta)
    if 'hux' in ests: out.append(max(2*v*delta, tau - 2*delta + 6*v*delta))
    if 'gm' in ests: out.append(max(2*v*delta, (-2/5+4*v)*delta, tau + (-8/5+4*v)*delta))
    if 'gm12' in ests and 5*tau/6 <= delta <= tau and s >= 0.7:
        best = 1e9
        for k in range(1, 60):
            t1 = k*tau/(k+1) + (4-6*s)*k*delta/(k+1)
            t2 = (5-6*s)*4*k*delta/(4*k+3) + 2*tau/(4*k+3)
            best = min(best, max(t1, t2))
        out.append(max((2-2*s)*delta, tau/2 + (3-4*s)*delta, best))
    if 'jut3' in ests:
        out.append(max((2-2*s)*delta, tau + (10-16*s)*delta/3, tau + (18-24*s)*delta))
    return max(0.0, min(out))

def worst(h, ests, mu=MU, use12=True, nd=60, nv=1001, taus=None):
    d0 = 0.5 - h/4
    if taus is None: taus=[1-h]
    W=-1e9; arg=None
    for tau in taus:
        om = h - abs(tau-(1-h))
        for delta in np.linspace(d0, 0.5, nd):
            for v in np.linspace(0, 0.5, nv):
                rho = rho_bound(delta, tau, v, ests)
                E = om - tau - 2*v*delta + Z(rho, tau, mu, use12) - h/2
                if E > W: W=E; arg=(round(delta,5), round(tau,5), round(v,5), round(rho,5))
    return W, arg

def hmax(ests, mu=MU, use12=True, **kw):
    lo, hi = 0.5, 2/3
    for _ in range(22):
        m = (lo+hi)/2
        w,_ = worst(m, ests, mu, use12, **kw)
        if w < 1e-12: lo = m
        else: hi = m
    return lo, worst(hi, ests, mu, use12, **kw)
if __name__ == '__main__':
    for name, ests, mu, u12 in [
        ('GMRR: mvt+hux, Weyl, 4th', {'mvt','hux'}, 1/6, False),
        ('mvt+hux, Bourgain, 4th+12th', {'mvt','hux'}, MU, True),
        ('+GM1.1, Weyl, 4th only', {'mvt','hux','gm'}, 1/6, False),
        ('+GM1.1, Weyl, 4th+12th', {'mvt','hux','gm'}, 1/6, True),
        ('+GM1.1, Bourgain, 4th only', {'mvt','hux','gm'}, MU, False),
        ('+GM1.1, Bourgain, 4th+12th', {'mvt','hux','gm'}, MU, True),
        ('+GM1.1+12.1, Weyl, 4th+12th', {'mvt','hux','gm','gm12'}, 1/6, True),
        ('+GM1.1+12.1, Bourgain, 4th+12th', {'mvt','hux','gm','gm12'}, MU, True),
        ('+Jutila3 too, Bourgain, 4th+12th', {'mvt','hux','gm','gm12','jut3'}, MU, True),
    ]:
        lo,(w,arg) = hmax(ests, mu, u12, nd=25, nv=401)
        print(f'{name:45s} h_max~{lo:.5f}  worst-at-just-above: {arg}', flush=True)
