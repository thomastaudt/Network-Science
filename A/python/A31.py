import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import scipy.stats as ss
#import scipy.stats.linregress as linreg

# Define a function that carries out the necessary evolution analysis for task A.3.1
def backwards_percolation_analysis(gr, k=1, times=1, start=0., end=1.):
    # Some used sizes
    l = len(gr.edges())
    n = len(gr.nodes())
    start = round(l*start)
    end = round(l*end)
    # The array of probabilities
    p = np.array(range(end, start-1, -k), dtype=float) / l
    # Reverse this array
    p = p[::-1]
    # Create the arrays to fill with data
    comp1 = np.zeros(len(p)) # sizes of biggest compontent
    comp2 = np.zeros(len(p)) # sizes of second biggest component
    cnum = np.zeros(len(p)) # number of components
    # Probability for a node being in the 'infinite' component
    P = np.zeros(len(p))
    # Cluster Distribution, meaning: The probability development of a node
    # being in a cluster with size i is cdist[:,i]
    cdist = np.zeros((len(p), n+1))
    fcdist = np.zeros((len(p), n+1))
    avg_csizes = np.zeros(len(p)) # average size of components
    avg_fcsizes = np.zeros(len(p)) # average size of 'finite' components
    # Degree distribution
    ddist = np.zeros((len(p), np.max(list(nx.degree(gr).values()))+1))
        
    for t in range(0, times):
        print("t =", t)
        # Make a copy in order to not alter g
        g = gr.copy()
        # Remove enough edges so that we are at the 'end' value
        g.remove_edges_from(random.sample(gr.edges(), l - end))
        # Take away edges. This way the dimension should not really change 
        # but we get lower densities with every step. Use this to do the calculations
        for i in range(0, len(p)):
            # Get the sizes of the two largest connected components 
            comps = sorted(nx.connected_components(g), key = len)
            cnum[-i-1] += len(comps)
            comp1[-i-1] += len(comps[-1])
            comp2[-i-1] += 0 if len(comps) == 1 else len(comps[-2])
            # Probability for a node being in the largest cluster
            P[-i-1] += comp1[-i-1] / n
            # Temporary distribution for all clusters
            tmp_cdist = np.bincount([len(c) for c in comps], minlength=cdist.shape[1]) * \
                        np.array([j for j in range(0,n+1)]) / \
                        float(n)
            # Temporary distribution for the finite clusters
            tmp_fcdist = np.bincount([len(c) for c in comps[:-1]], minlength=fcdist.shape[1]) * \
                         np.array([j for j in range(0,n+1)]) / \
                         float(n)

            cdist[-i-1,:] += tmp_cdist 
            fcdist[-i-1,:] += tmp_fcdist 
            # Average cluster size
            #print(comps)
            #print('cdist', cdist[-i-1,:], 'expected', np.dot(cdist[-i-1,:], [j for j in range(0, n+1)]))
            avg_csizes[-i-1] += np.dot(tmp_cdist, [j for j in range(0, n+1)])
            avg_fcsizes[-i-1] += np.dot(tmp_fcdist, [j for j in range(0, n+1)])
            # Cluster degree distribution
            #print(i, len(g.edges()), k)
            # Degree distribution
            ddist[-i-1,:] += np.bincount(list(nx.degree(g).values()), minlength=ddist.shape[1])
            # Cluster distribution
            #cdistribution[i,:] = 
            # Debug
            #print("size", len(g.edges()), "maxsize", l, "prob", len(g.edges()) / l, "realprob", p[-i-1])
            # Remove edges for the next step
            if i < len(p)-1: g.remove_edges_from(random.sample(g.edges(), k))
    # Return all the information
    return {'p'          : p, 
            'cnum'       : cnum/times, 
            'comp1'      : comp1/times, 
            'comp2'      : comp2/times, 
            'avg_csizes' : avg_csizes/times, 
            'avg_fcsizes': avg_fcsizes/times,
            'cdist'      : cdist/times, 
            'fcdist'     : fcdist/times, 
            'ddist'      : ddist/times,
            'P'          : P/times
           }


# Get the percolation coefficients if given the analysis dict and the percolation threshold
def percolation_coefficients(gvals, pc, min_dist=5e-2, max_dist=1e-1):
    # The coefficients searched for are 
    # * gamma (average finite cluster size), 
    # * beta (percolation probability)
    # * tao, sigma: can be calculated by gamma and beta
    #
    # Some preparations, since a suitable area for fitting has to be chosen
    mask_post = np.array([ max_dist >  p - pc > min_dist for p in gvals['p'] ])
    mask_pre  = np.array([ max_dist > -p + pc > min_dist for p in gvals['p'] ])
    # Get the gamma values
    gamma_post, ax_post, r_value, p_value, gamma_post_err = ss.linregress(np.log10(gvals['p'][mask_post]-pc), np.log10(gvals['avg_fcsizes'][mask_post]))
    gamma_pre, ax_pre, r_value, p_value, gamma_pre_err = ss.linregress(np.log10(-gvals['p'][mask_pre]+pc), np.log10(gvals['avg_fcsizes'][mask_pre]))
    # Get the beta values -- here only post makes any sense (theoretically...) since P == 0 for p < pc *cough*
    beta, ax, r_value, p_value, beta_err = ss.linregress(np.log10(gvals['p'][mask_post]-pc), np.log10(gvals['P'][mask_post]))
    # Give back the values
    return { 'gamma_post'    : gamma_post,
             'gamma_post_ax' : ax_post,
             'gamma_pre'     : gamma_pre,
             'gamma_pre_ax'  : ax_pre,
             'beta'          : beta
           }

# A function to save all necessary data in files
def save_percolation_data(fname, gvals):
    header = '#1(p) 2(cnum) 3(comp1) 4(comp2) 5(avg_csizes) 6(avg_fcsizes) 7(P)'
    data = np.vstack( (gvals['p'], 
                       gvals['cnum'], 
                       gvals['comp1'], 
                       gvals['comp2'], 
                       gvals['avg_csizes'], 
                       gvals['avg_fcsizes'], 
                       gvals['P']) ).T
    np.savetxt(fname, data, header=header)

    
# Something to do fast plotting
def plot_percolation_data(gvals, m, M):
    for var in gvals:
        plt.title(var)
        if len(gvals[var].shape) == 1 and var != 'p':
            plt.vlines([m,M], 0, np.max(gvals[var]))
            plt.scatter(gvals['p'], gvals[var])
            plt.show()


## DIMENSION 2 ##
# Generate an mxm grid, so that we have a graph of dimension 2
#m = 25
#g1 = nx.grid_2d_graph(m, m)
#g1vals = backwards_percolation_analysis(g1, 1, 500, start = 0.40, end = 0.60)
#print(percolation_coefficients(g1vals, 0.5))

## DIMENSION \infty ##

m = 0.25*1e-3
M = 0.1*1e-2
N = 500
pc = 1./N

g2 = nx.complete_graph(N)
g1vals = backwards_percolation_analysis(g2, 2, 400, start = 0., end = 0.005)
save_percolation_data('inf_20', g1vals)
print(percolation_coefficients(g1vals, pc, m, M))
plot_percolation_data(g1vals, pc+m, pc+M)

# logarithmic scatter
mask1 = np.array([  M > p - pc > m for p in g1vals['p']  ])
mask2 = g1vals['p'] < pc - m

plt.title('log of avg_fcsizes')
plt.scatter(np.log10(g1vals['p'][mask1]-pc), np.log10(g1vals['avg_fcsizes'][mask1]))
plt.scatter(np.log10(-g1vals['p'][mask2]+pc), np.log10(g1vals['avg_fcsizes'][mask2]), color='r')
plt.show()

plt.title('log of P')
plt.scatter(np.log10(g1vals['p'][mask1]-pc), np.log10(g1vals['P'][mask1]))
plt.show()

