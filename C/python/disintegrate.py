import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def disintegrate(gr):
    components = list(nx.connected_components(gr))
    num_comps = len(components)
    num_nodes = nx.number_of_nodes(gr)
    yield components
    while num_comps < num_nodes:
        bw = nx.edge_betweenness_centrality(gr)              # betweenness dict
        to_remove = max(bw.keys(), key=(lambda x: bw[x]))    # edge with highest betweenness
        gr.remove_edge(*to_remove)                           # throw it away
        components = list(nx.connected_components(gr))
        new_num_comps = len(components)
        if new_num_comps > num_comps:
            num_comps = new_num_comps
            yield components

def community_quality( net, comps ):
  edges = net.edges()
  #comps = nx.connected_components(net)
  for c in range(len(comps)):
    for n in comps[c]:
      net.node[n]['comp'] = c
  
  # construct e
  m = np.zeros((len(comps), len(comps)))
  for i,j in net.edges():
    m[net.node[i]['comp'], net.node[j]['comp']] += 1
    if net.node[j]['comp'] !=  net.node[i]['comp']:
      m[net.node[j]['comp'], net.node[i]['comp']] += 1
  
  
  m /= len(net.edges())
  a = np.sum(m, axis=0)
  Q = 0
  for i in range(len(comps)):
    Q += m[i,i] - a[i]**2
  
  return Q


def optpart(net):
  qualities = []
  best = 0
  bc = None
  bestnet = net.copy()
  victim = net.copy()
  for c in disintegrate(victim):
    Q = community_quality(net, c)
    qualities.append(Q)
    if Q > best:
      best = Q
      bc = c
      bestnet = net.copy()
  
  return bc, best, bestnet, qualities
  
m =  np.loadtxt("karate_network.txt")
g = nx.Graph(m)
best, val, net, qs = optpart(g)
#[net.node[i]['comp'] for i in net.node]