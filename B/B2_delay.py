
import numpy as np
from pydelay import dde23

histfuncs = [lambda x: 1.0,
             lambda x: 0.5,
             lambda x: 0.0,
             lambda x: -0.5,
             lambda x: -1.0]

eqns = {
        'x' : 'x(t - tau)'
       }

pars = {
        'tau' : 1.0
       }

dde = dde23(eqns=eqns, params=pars)

dde.set_sim_params(tfinal=5, dtmax=0.01)

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
    np.savetxt("B22_plus_const_%d.dat" % (i,), np.array([t, x]).T)
