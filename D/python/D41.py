import networkx as nx
import numpy as np
import scipy as sp
import random as rd
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt

def random_triade(G):
    nodes = G.nodes().copy()
    triade_nodes = np.random.choice(nodes, size=3, replace=False)
    triade = nx.subgraph(G, triade_nodes)
    return triade

def is_balanced(triade): 
    return True if (-1)**(3 - triade.number_of_edges()) == 1 else False

def imbalanced_triade(G, limit=1000):
    for i in range(limit):
        triade = random_triade(G)
        if not is_balanced(triade): return triade
    return None

def num_imbalanced_triades(G):
    num = 0
    nodes = G.nodes()
    for n1 in nodes[:-2]:
        for n2 in nodes[n1+1:-1]:
            for n3 in nodes[n2+1:]:
                if not is_balanced(nx.subgraph(G, [n1, n2, n3])): num += 1
    return num

def balance_triade_in_graph(G, triade, p):
    edges = triade.edges().copy()
    nodes = triade.nodes().copy()
    if len(edges) == 0: 
        G.add_edge(*np.random.choice(nodes, size=2, replace=False))
    else:
        if np.random.random() < p:
            comp = nx.complement(triade)
            G.add_edge(*comp.edges()[0])
        else:
            G.remove_edge(*rd.choice(edges))


def original_graph():
    romeos_family = nx.complete_graph(5)
    julias_family = nx.complete_graph(5)
    # The families clash <- aw, not good!
    family_fight = nx.disjoint_union(romeos_family, julias_family)
    # ... but Romeo and Julia make love nevertheless
    family_fight.add_edge(0, 9)
    return family_fight


def destiny(p=1./3.):
    family_fight = original_graph()
    
    i = 0
    while True:
        triade = imbalanced_triade(family_fight, limit = 1000)
        if triade == None:
            n = num_imbalanced_triades(family_fight)
            if n == 0: break
        else: balance_triade_in_graph(family_fight, triade, p)
    return family_fight


def family_positions():
    positions = []
    for i in range(0, 5):
        positions.append( (-1 + 0.75*np.cos((i-0)/5*2*np.pi), 
                                0.75*np.sin((i-0)/5*2*np.pi)) )
    for i in range(5, 10):
        positions.append( ( 1 - 0.75*np.cos((i-9)/5*2*np.pi),
                                0.75*np.sin((i-9)/5*2*np.pi)) )
    return positions


def destinies(times=1000, p=1./3.):
    num_love = 0
    fracs = np.zeros(times)
    for j in range(times):
        family_fight = original_graph()
        
        i = 0
        while True:
            triade = imbalanced_triade(family_fight, limit = 1000)
            if triade == None:
                n = num_imbalanced_triades(family_fight)
                if n == 0: break
            else: balance_triade_in_graph(family_fight, triade, p)
        if family_fight.has_edge(0, 9): 
            print("Destiny %d:" % (j+1,), "Love")
            num_love += 1
        else: print("Destiny %d:" % (j+1,), "Hate")
        fracs[j] = num_love/(j+1)
        print("Fraction: %f" % (fracs[j],))
    return num_love/times, fracs, family_fight
    
#P = np.linspace(0.1, 0.6, 20)
#fracs = np.array( [ destinies(p=p)[0] for p in P ] )



