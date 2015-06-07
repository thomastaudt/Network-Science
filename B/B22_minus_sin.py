
import numpy as np
from pydelay import dde23

# 
histfuncs = [lambda x,v=val: 1*np.sin(v*np.pi*x) for val in np.linspace(1.,2.5,30)]

eqns = {
        'x' : '-x(t - tau)'
       }

pars = {
        'tau' : 1.0
       }

dde = dde23(eqns=eqns, params=pars)

dde.set_sim_params(tfinal=30, dtmax=0.01)

i = 0

for histfunc in histfuncs:
    i = i+1
    hf = {
          'x': histfunc
         }

    dde.hist_from_funcs(hf, 101)

    dde.run()
    t = dde.sol['t']
    x = dde.sol['x']
    np.savetxt("latex/pictures/data/B22_minus_sin_%d.dat" % (i,), np.array([t, x]).T)
