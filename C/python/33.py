import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

def maximum_shortest_path(G):
    max_path = 0
    for i in nx.nodes_iter(G):
        for j in nx.nodes_iter(G):
            if nx.has_path(G, i,j):
                path = nx.shortest_path_length(G, i, j)
                if path > max_path:
                    max_path = path
    return max_path




def ij_pair(G, distance):
    N = nx.number_of_nodes(G)
    i = np.random.randint(N)
    j_list = []
    for j in G.nodes_iter():
        if nx.shortest_path_length(G, i, j) == distance:
            j_list += [j]
    if j_list != []:
        return i, random.choice(j_list)
    else:
        return ij_pair(G, distance)


def message_passing(distance, G, l, x, relay):
    (i, j) = ij_pair(G, distance)
    print(i, "-->", j)
    for t in range(25):
        x_max = l+1 #l is maximal possible distance
        k_max = [] #node,s k with minimal distance
        for e in G.edges([i]):
            k = e[1]
            x_val = min(x[:,k,j])
            if x_val < x_max:
                k_max = [k]
                x_max = x_val
            elif x_val == x_max:
                k_max += [k]
        i = random.choice(k_max)
        if i == j:
            print("found:", i)
            break
        relay[i] += 1
    return t+1, relay


def message_passing_hist(graphs, max_distance, repitition):
    g = 5
    l = 3
    k = 4
    s = 2
    a = 1
    p_ld = np.zeros((max_distance, repitition*len(graphs)))
    relay = np.zeros(g*2**l)
    i = -1
    for (G, x, vs) in graphs:
        i += 1
        for k in range(repitition):
            for distance in range(1,max_distance+1):
                p_ld[distance-1, i*repitition + k], relay = message_passing(distance, G, l, x, relay)
    return p_ld, relay

# set all parameters
g = 5
l = 3
k = 4
s = 2
a = 1
mat = []

# create the graphs
graphs = []
j = 0
while j < 50:
    G = random_social_graph(g,l,s,k,a)
    if maximum_shortest_path(G[0]) > 3:
        graphs.append(G)
        j += 1
# calculate the histogram_data

p, relay = message_passing_hist(graphs, 4, 200)

#Plot Histogram
for d in range(4):
    distr = p[d,:]
    np.savetxt("p_dist_%i_new.dat" % d, distr)
    #plt.hist([i-0.5 for i in distr], max(distr) - min(distr), normed=0.5, facecolor='green', alpha=1)
    #plt.xlabel('message time')
    #plt.ylabel('frequency')
    #plt.show()
