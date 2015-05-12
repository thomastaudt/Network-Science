# -*- coding: utf-8 -*-
"""
Created on Tue May 05 15:03:46 2015

@author: Erik
"""

import networkx as nx
import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def watt_strogatz(N, k, p):
  # iterate over all edges
  G = nx.Graph()
  G.add_nodes_from(range(0,N))
  
  # regular network
  for i in range(1, k+1):
    for n in range(0, N):
      # connect (n, n+i)
      G.add_edge(n, (n+i)%N)
  
  # rewire
  for i in range(1, k+1):
    for n in range(0, N):
      if rnd.random() < p:
        G.remove_edge(n, (n+i)%N)
        # find a new edge randomly, making sure (n,n) is not chosen        
        new = rnd.randint(0, N-2)
        if new == n:
          new = N-1
          
        G.add_edge(n, new)
        
  return G


def small_word_effect(generator, size):
  prob = np.logspace(-4, 0.0, num=25)
  prob[0] = 0
  clusters = np.zeros(len(prob))
  TRIALS = 10
  avgl = np.zeros( len(prob) )
  counts = np.zeros( len(prob) )
  for j in range(0, len(prob)):
    p = prob[j]
    print(p)
    while counts[j] < TRIALS:
      graph = generator(size, p)
      if nx.is_connected(graph):
        clusters[j] += nx.average_clustering(graph)
        avgl[j] += nx.average_shortest_path_length(graph)
        counts[j] += 1
    
  
  clusters /= counts
  avgl /= counts
  print(clusters)
  print( avgl, counts)
  plt.figure()
  
  plt.semilogx()

  plt.scatter(prob[1:], clusters[1:]/clusters[0], color="b")
  plt.scatter(prob[1:], avgl[1:]/avgl[0], color="g")
  
def strogatz2d(size, k, p):
  # generate regualr grid
  graph = nx.grid_2d_graph(int(np.sqrt(size)), int(np.sqrt(size)), True)
  graph.remove_edges_from( graph.edges() )

  def distance(v1, v2):
    return np.sum(np.abs(np.array(v1) - v2))
  
  for i in graph.nodes_iter():
    for j in graph.nodes_iter():
      if i[0] < j[0]:
        continue
      if i[0] == j[0] and i[1] <= j[1]:
        continue
      if distance(i,j) <= k:
        if rnd.random() < p:
          rnode = rnd.choice(graph.nodes())
          graph.add_edge(i, rnode)
        else:
          graph.add_edge(i, j)
        
  draw = {n : np.array(n) + (rnd.uniform(-0.1, 0.1), rnd.uniform(-0.1, 0.1)) for n in graph.nodes()}
  return graph#, draw