
import numpy as np
from pydelay import dde23

# 
histfuncs = [lambda x,v=val: v for val in np.linspace(-2, 2, 30)]

eqns = {
        'theta' : 'w',
        'w' : 'dP - alpha*w - 2*K*sin(theta) - gamma*w(t-tau)'
       }

pars = {
        'tau'    : 1.0,
        'gamma'  : 0.0,
        'dP'     : 2.0,
        'alpha'  : 0.1,
        'K'      : 1.5,
       }

dde = dde23(eqns=eqns, params=pars)

dde.set_sim_params(tfinal=100, dtmax=0.005)

histfunc = {
            'w': lambda t: 0,
            'theta': lambda t: 0,
           }

dde.hist_from_funcs(histfunc, 101)

dde.run()
t = dde.sol['t']
theta = dde.sol['theta']
w = dde.sol['w']
np.savetxt("11_with_pydelay.dat", np.array([t, theta, w]).T)
