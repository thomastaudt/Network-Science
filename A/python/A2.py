# -*- coding: utf-8 -*-
"""
Created on Tue May 05 15:03:46 2015

@author: Erik
"""

import networkx as nx
import random as rnd
import matplotlib.pyplot as plt
import numpy as np

def weigh_edges(g):
	# add attribute to all edges
	for p,q,d in g.edges_iter(data=True):
		d['importance'] = 0
	
	# iterate over all paths in the network
	# TODO maybe random samples?
	for i in g.nodes_iter():
		# find shortest path from i to all other nodes
		paths = nx.single_source_shortest_path(g, i)
		for shortest in paths.values():
			for k in range(0, len(shortest)-1):
				# increase counter for all edges 
				g[shortest[k]][shortest[k+1]]['importance'] += 1
	
	for i in g.nodes_iter(data=True):
		i[1]['importance'] = 0
		edges = g.edges_iter(i[0], data=True)
		for v1,v2,d in edges:
			i[1]['importance'] += d['importance']
	
	return g

NUM_NODES = 100

g = nx.barabasi_albert_graph(NUM_NODES, 5)
#g = nx.erdos_renyi_graph(NUM_NODES, 0.1)
g = weigh_edges(g)
nx.draw_networkx(g, node_color=[n[1]['importance'] for n in g.nodes_iter(data="True")])


def test_network(graph, N, selector):
  network = graph.copy()
  Svals = np.zeros(N) # relative largest component size
  pl = np.zeros(N)    # avg shortest path length
  s_vals = np.zeros(N)  # avg cluster size excluding largest
  num_of_cmp = np.zeros(N)  # number of components
  for i in range(0, N):
    kill = selector(network)
    network.remove_node(kill)
    components = nx.connected_component_subgraphs(network)
    Svals[i] = float(len(components[0])) / len(network)
    if len(components[0]) > 1:
      pl[i] = nx.average_shortest_path_length(components[0])
    if len(components) > 1:
      for j in range(1, len(components)): #largest included now
        s_vals[i] += len(components[j]) * len(components[j])
      s_vals[i] /= float(len(components)-1) * float(len(network.nodes()))
    num_of_cmp[i] = len(components)
  return network, Svals, pl, s_vals, num_of_cmp

def random_selector(g):
  return rnd.choice(g.nodes())

def hub_selector(g):
  st = sorted(g.degree_iter(), cmp = lambda x,y: 1 if x[1] < y[1] else -1)
  return st[0][0]

def evil_selector(g):
  g = weigh_edges(g)
  st = sorted(g.nodes_iter(data=True), cmp = lambda x, y: 1 if x[1]['importance'] < y[1]['importance'] else -1)
  return st[0][0]

plt.figure()
#print(g.degree([5]), g.degree([0]))
g2, S2, pl2, s2,c2 = test_network(g, NUM_NODES-1, hub_selector)
#nx.draw_networkx(g2, node_color=[n[1]['importance'] for n in g2.nodes_iter(data="True")])

plt.figure()
g3, S3, pl3, s3,c3 = test_network(g, NUM_NODES-1, evil_selector)
#nx.draw_networkx(g3, node_color=[n[1]['importance'] for n in g2.nodes_iter(data="True")])

g4, S4, pl4, s4, c4 = test_network(g, NUM_NODES-1, random_selector)

print(S2, S3)

plt.figure()
plt.plot(S2)
plt.plot(S3)
plt.plot(S4)

plt.figure()

plt.plot(pl2)
plt.plot(pl3)
plt.plot(pl4)

plt.figure()
plt.plot(s2)
plt.plot(s3)
plt.plot(s4)


plt.figure()
plt.plot(c2)
plt.plot(c3)
plt.plot(c4)
#print(nx.average_shortest_path_length(g2), nx.average_shortest_path_length(g3))
