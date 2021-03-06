# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:36:38 2015

@author: Erik
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

def intersect(N1, N2, count_only=True):
  i, j = 0, 0
  if count_only:
    count = 0
  else:
    combined = []
  while(i < len(N1) and j < len(N2)):
    if(N1[i] < N2[j]):
      i += 1
    elif N1[i] > N2[j]:
      j += 1
    else:
      if count_only:
        count += 1
      else:
        combined.append(N1[i])
      i += 1
      j += 1
   
  if count_only:
    return count
  else:
    return combined
  
def lmcc(G1, G2):
  cm1 = max(nx.connected_components(G1), key=len)
  cm2 = max(nx.connected_components(G2), key=len)
  
  return intersect(sorted(cm1), sorted(cm2))

def interdep(N, k0):
  G1 = nx.erdos_renyi_graph(N, k0/(N-1.0))
  G2 = nx.erdos_renyi_graph(N, k0/(N-1.0))
  
  data = np.zeros((N, 2))  
  
  for i in range(N-1):
    kill = random.choice(G1.nodes())
    G1.remove_node(kill)
    G2.remove_node(kill)
    p = (i+1.0) / N
    # average degree
    data[i, 0] = p * k0#float(len(G1.edges()) + len(G2.edges())) / len(G1.nodes()) / 4
    data[i, 1] = lmcc(G1, G2) / float(N - i)
    
  return data

dat = None
hst = None
N = 1500
k0 = 10
for i in range(0, 50):
  print(i)
  if dat is None:
    dat = interdep(N, k0)
    hst = dat[:, 1]
  else:
    #dat = np.concatenate((dat, interdep(50, 6)), axis=0)
    hst += interdep(N, k0)[:, 1]

#hst, e = np.histogram(dat[:,0], weights=dat[:,1])
#factor = (e[2]-e[1]) / (1.0/N * k0)
plt.plot(hst / 50)
np.savetxt("N1000k10", hst)