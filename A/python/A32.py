import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import scipy.stats as ss


def generic_product_rule(g, op):
    sel1 = random.sample(g.nodes(), 2)
    if nx.has_path(g, *sel1):
        g.add_edge(*sel1)
        return sel1
    sel2 = random.sample(g.nodes(), 2)
    if nx.has_path(g, *sel2):
        g.add_edge(*sel2)
        return sel2
    elif op( len(nx.node_connected_component(g, sel2[0])) * len(nx.node_connected_component(g, sel2[1])), \
             len(nx.node_connected_component(g, sel1[0])) * len(nx.node_connected_component(g, sel1[1])) ):
        g.add_edge(*sel2)
        return sel2
    else:
        g.add_edge(*sel1)
        return sel1
             
def product_rule(g, *args): return generic_product_rule(g, lambda x,y: x < y)

def anti_product_rule(g, *args): return generic_product_rule(g, lambda x,y: x > y)

def er_rule(g, *args):
    #sel = random.choice(list(nx.non_edges(g)))
    while True:
        sel = random.sample(g.nodes(), 2)
        if not g.has_edge(*sel):
            g.add_edge(*sel)
            return sel
    #return sel

def brute_rule(g, *args):
    subgraphs = sorted(nx.connected_component_subgraphs(g), key=len)
    if len(subgraphs) == 1: return er_rule(g)
    # connect different subgraphs of smallest size
    edge = (subgraphs[0].nodes()[0], subgraphs[1].nodes()[0])
    g.add_edge(*edge)
    return edge

def anti_brute_rule(g, *args):
    subgraphs = sorted(nx.connected_component_subgraphs(g), key=len)
    if len(subgraphs) == 1: return er_rule(g)
    edge = (subgraphs[-1].nodes()[0], subgraphs[-2].nodes()[0])
    g.add_edge(*edge)
    return edge

# N: number of nodes in graph
# k: number of edges per time step
# n: number of time steps to carry out
def percolation_transition(rule, N, n, trials=10):
    time_steps = np.array(list(range(0, n)))
    comp1 = np.zeros(n)
    for t in range(0, trials):
        print(t+1, "/", trials)
        g = nx.empty_graph(N)
        for i in range(0, n):
            comps = sorted(nx.connected_components(g), key = len)
            comp1[i] += len(comps[-1])
            rule(g)
    plt.scatter(time_steps, comp1/N/trials)
    return time_steps, comp1/trials

t, er_comp1 = percolation_transition(er_rule, 500, 2000, trials = 1)
t, pr_comp1 = percolation_transition(product_rule, 500, 2000, trials = 1 )
t, apr_comp1 = percolation_transition(anti_product_rule, 500, 2000, trials = 1 )
t, br_comp1 = percolation_transition(brute_rule, 500, 2000, trials = 1 )
t, abr_comp1 = percolation_transition(anti_brute_rule, 500, 2000, trials = 1 )

data = np.vstack((t, er_comp1, pr_comp1, apr_comp1, br_comp1, abr_comp1)).T
header = 't er pr apr br abr'

np.writetxt('34_35_pec_transitions.dat', data, header=header)
