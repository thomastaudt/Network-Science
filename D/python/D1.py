# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:04:35 2015

@author: Erik
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rng

def timestep(graph, beta, gamma):
  new = graph.copy()
  for i in graph.nodes():
    if graph.node[i]['state'] == 'infected':
      for n in graph.edge[i]:
        if graph.node[n]['state'] == 'susceptible':
          if rng.random() < beta:
            new.node[n]['state'] = 'infected'
      if rng.random() < gamma:
        new.node[i]['state'] = 'recovered'
    
  return new

def victim_population(n, m):
  g = nx.barabasi_albert_graph(n, m)
  for i in g.nodes():
    g.node[i]['state'] = 'susceptible'
  return g

def col(state):
  if state == "susceptible":
    return "blue"
  elif state == "infected":
    return "red"
  elif state == "recovered":
    return "green"

def draw_states(graph):
  cls = [col(g[1]['state']) for g in graph.nodes_iter(data=True)]
  #plt.figure()
  nx.draw( graph, node_color = cls, with_labels=False)
  plt.show()

#n = victim_population(50, 3)
#n.node[rng.choice(n.nodes())]['state'] = 'infected'
#for i in range(6):
#  plt.figure(figsize=(4,4))
#  draw_states(n)
#  plt.savefig("infection"+str(i)+".svg")
#  n = timestep(n, 0.5, 0.5)



def ever_infected(n, m, beta, gamma):
  n = victim_population(n, m)
  n.node[rng.choice(n.nodes())]['state'] = 'infected'
  while( "infected" in nx.get_node_attributes(n, "state").values()):
    n = timestep(n, beta, gamma)
  return np.sum([ 1 if i == "recovered" else 0 for i in nx.get_node_attributes(n, "state").values()])

def ever_infected_graph(gamma):
  res = np.zeros(40)
  for i in range(40):
    beta = i / 40.0
    for j in range(100):
      res[i] += ever_infected(50, 3, beta, gamma)
  res /= 100 * 50
  np.savetxt("everinfected"+str(gamma)+".txt",  np.transpose((np.linspace(0.0, 39/40.0, num=40), res)) )
  return np.linspace(0.0, 39/40.0, num=40), res

plt.scatter(*ever_infected_graph(0.05))

## calculate flux
#def fluxify(net):
#  for n in net.nodes():
#    sums = np.sum([e['weight'] for e in net.edge[n].values()])
#    if net.has_edge(n, n):
#      net.remove_edge(n, n)
#    for e in net.edge[n]:
#        net.edge[n][e]['flux'] = net.edge[n][e]['weight'] / float(sums)
#        net.edge[n][e]['d'] = 1 - np.log(net.edge[n][e]['flux'])
#
#def init_SIR(net, tmax=1e99):
#  for i in net.nodes():
#    net.node[i]['j'] = 0.0
#    net.node[i]['s'] = 1.0
#    net.node[i]['T'] = tmax
#  net.node['South Africa']['j'] = 0.001
#  net.graph['time'] = 0
#
#
#def sigm(x):
#  if x < 1:
#    return 0
#  return 1
#
#def step_SIR(net):
#  beta = 0.285
#  alpha = 1.5*beta
#  eps = 1e-6
#  gamma = 2.8e-3
#  dt = 0.02
#  
#  for n in net.nodes():
#    j = net.node[n]['j']
#    s = net.node[n]['s']
#    dj = alpha * s * j * sigm(j / eps) - beta * j
#    ds = -alpha * s * j * sigm(j / eps)
#    fj = 0.0
#    fs = 0.0
#    for e in net.edges_iter(n, data=True):
#      fj += e[2]['flux'] * (net.node[e[1]]['j'] - net.node[e[0]]['j'])
#      fs += e[2]['flux'] * (net.node[e[1]]['s'] - net.node[e[0]]['s'])
#    dj += gamma * fj
#    ds += gamma * fs
#    net.node[n]['dj'] = dj
#    net.node[n]['ds'] = ds
#    # update phase
#  net.graph['time'] += dt
#  for n in net.nodes():
#    net.node[n]['j'] += net.node[n]['dj'] * dt
#    net.node[n]['s'] += net.node[n]['ds'] * dt
#    if net.node[n]['j'] > eps:
#      net.node[n]['T'] = min(net.node[n]['T'], net.graph['time'])
#
#def set_effective_distance(net, node, attrib = "D"):
#  spaths = nx.shortest_path_length(net, node, weight = "d")
#  for t in spaths:
#    net.node[t][attrib] = spaths[t]
#
#def print_SIR( net ):
#  cls = [g[1]['j'] for g in net.nodes_iter(data=True)]
#  print cls  
#  plt.figure()
#  nx.draw_networkx( net, with_labels = False, node_color = cls, node_size=100, width = 0.5, linewidths=0.5 )
#  plt.show()
#
#def print_arrival( net ):
#  cls = [g[1]['T'] for g in net.nodes_iter(data=True)]
#  plt.figure()
#  nx.draw_networkx( net, with_labels = False, node_color = cls, node_size=100, width = 0.5, linewidths = 0.5)
#  plt.show()
#
#def arrival_vs_distance( net, attrib="D" ):
#  distance = []
#  times = []
#  for i in net.nodes():
#    distance.append( net.node[i][attrib] )
#    times.append( net.node[i]['T'] )
#  plt.figure()
#  plt.scatter( distance, times )
#  plt.show()
#
## test programme
##if network is None:
#network = nx.read_gml('countriesNetwork.gml')
#net = network.copy()
#fluxify( net)
#init_SIR( net, 12000*0.025)
#print_SIR( net )
#for i in range(12000):
#  step_SIR(net)
#print_SIR(net)
#print_arrival( net )
#
#set_effective_distance( net, "South Africa")
#arrival_vs_distance( net )
#
#
#set_effective_distance( net, "Peru")
#arrival_vs_distance( net )
#
#set_effective_distance( net, "Indonesia")
#arrival_vs_distance( net )