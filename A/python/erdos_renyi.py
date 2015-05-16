import networkx as nx
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def generate_erdos_renyi(N, n, base = None):
    """ N number of nodes
        n number of connections
    """
    # empty graph
    if base is None:
        G = nx.Graph()
        #set up nodes
        G.add_nodes_from(range( N ))
    else:
        G = base # extend base graph
    startedges = len(G.edges())
    #add edges
    for i in range(0, n):
        while True:
            v1 = rand.randint(0, N)
            v2 = rand.randint(0, N)
            if v1 != v2 and not G.has_edge(v1, v2):
                G.add_edge(v1, v2, t=i+startedges)
                #print("add", v1, v2)
                break
    
    return G

def A11():
    graph = generate_erdos_renyi(20, 10)
    nx.draw_circular(graph, edge_color = [e[2]['t'] for e in graph.edges(data=True)], 
                                 edge_cmap=plt.get_cmap("cool"), edge_vmax = 20, node_size=100)
    plt.figure()
    graph= generate_erdos_renyi(20, 10, graph)
    nx.draw_circular(graph, edge_color = [e[2]['t'] for e in graph.edges(data=True)], 
                                 edge_cmap=plt.get_cmap("cool"), edge_vmax = 20, node_size=100)
                             

def node_hist(N, p):
    TRIALS = 200
    summed = None
    for i in range(0, TRIALS):
        graph = nx.erdos_renyi_graph(N, p)
        hist = nx.degree_histogram(graph)
        if summed is None:
            summed = np.array(hist)
        elif len(summed) > len(hist):
            hist = np.array(hist)
            summed[0:len(hist)] += hist
        else:
            hist = np.array(hist)
            hist[0:len(summed)] += summed
            summed = hist
    
    summed = summed.astype(float)
    summed /= float(TRIALS)
    
    return summed

def A12_a():
    # varying N for constant p
    plt.figure()
    p = 0.1
    for N in [50, 100, 500]:
        h = node_hist(N, p) 
        x = np.arange(0.0, len(h)) / (N*p)
        txtdata = np.empty(( 4, len(x)))
        txtdata[0,:] = N
        txtdata[1,:] = p
        txtdata[2] = x
        txtdata[3] = h
        np.savetxt("er_hist_N=%g_p=%g.dat"%(N,p), txtdata.T, header="N\tp\tk\tp(k)")        
        plt.plot(x, h, label="N = %g"%(N))
    plt.legend()
    plt.xlabel("k/(Np)")
    plt.ylabel("p(k)")
    
    # varying p for constant N
    plt.figure()
    N = 350 # we need a high number to get a smoth graph for low p
    #TOOD how do we plot this data, to make it look nice?
    for p in [0.01, 0.05, 0.25]:
        h = node_hist(N, p) 
        x = np.arange(0.0, len(h)) / (N)
        txtdata = np.empty(( 4, len(x)))
        txtdata[0,:] = N
        txtdata[1,:] = p
        txtdata[2] = x
        txtdata[3] = h
        np.savetxt("er_hist_N=%g_p=%g.dat"%(N,p), txtdata.T, header="N\tp\tk\tp(k)")    
        plt.plot(x, h, label="p = %g"%(p))
    plt.legend()
    plt.xlabel("k/(Np)")
    plt.ylabel("p(k)")
