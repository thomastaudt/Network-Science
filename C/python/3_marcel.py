import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


# seems to be okay

# vs: 4d object object containing the social information
# vs[s,i,k], vs[s,j,k]:
# s:  characteristic that shall be looked at
# i:  node 1
# j:  node 2
# k:  binary coordinates for characteristic s
def social_distance(vs, s, i, j):
    if (vs[s, i, :] == vs[s, j, :]).all():
        return 0
    else:
        l = np.shape(vs)[2]
        for ll in range(l):
            ll2 = l-ll-1
            if vs[s, i, ll2] != vs[s, j, ll2]:
                return ll2+1


# okay
def social_distance_matrix(vs):
    x = np.zeros((np.shape(vs)[0], np.shape(vs)[1], np.shape(vs)[1]))
    # for all characteristics
    for s in range(np.shape(vs)[0]):
        # for all pair of nodes
        for i in range(np.shape(vs)[1]):
            for j in range(np.shape(vs)[1]):
                # get the social distance for pair of nodes for certain
                # characteristics
                x[s, i, j] = social_distance(vs, s, i, j)
    return x


def Q(k):
    N = np.shape(k)[0]
    Q = 0
    Edges = float(0.5*sum(sum(k)) + 0.5*np.matrix.trace(k))
    for i in range(N):
            a_i = 0
            for j in range(N):
			a_i += k[i,j] / Edges
		Q += k[i,i] / Edges - a_i*a_i
	return Q

def modularity(G0):
	G = G0.copy()
	P = np.zeros(nx.number_of_nodes(G))
	t = 0
	Parts_0 = 0
	LComp = True
	while LComp:
		t += 1
		max_b = 0
		max_e = []
		for e in G.edges_iter():
			b = nx.edge_betweenness_centrality(G, normalized=True, weight=None)[e]
			if b > max_b:
				max_b = b
				max_e = [e]
			elif b == max_b:
				max_e += [e]
		rm_e = max_e[np.random.randint(len(max_e))]
	
		G_Sub = list(nx.connected_component_subgraphs(G))
		Parts = len(G_Sub)
		if Parts > Parts_0:
			Parts_0 = Parts
			for p in range(Parts):
				for i in G_Sub[p].nodes():
					P[i] = p
		
			k = np.zeros((Parts,Parts))
			for e in G0.edges_iter():
				i = P[e[0]] - 1
				j = P[e[1]] - 1
				k[i][j] += 1
				if i!=j:
					k[j][i] += 1
			print t, Parts, Q(k)

		G.remove_edge(rm_e[0], rm_e[1])
		if nx.number_of_edges(G) == 0:
			LComp = False
	return G0
# okay
def random_pick(some_list, probabilities):
    x = random.uniform(0, sum(probabilities))
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item

def maximum_shortest_path(G):
	max_path = 0
	for i in nx.nodes_iter(G):
		for j in nx.nodes_iter(G):
			if nx.has_path(G, i,j):
				path = nx.shortest_path_length(G, i, j)
				if path > max_path:
					max_path = path
	return max_path

def create_c11_graph(N, g, l, S, k, alpha):
	G = nx.empty_graph(N)
	vs = np.zeros((S,N,l)) -1
	for s in range(S):
		distinct = int(N/g + 0.5)
		vs_distinct = np.zeros((distinct, l))
		
		for i in range(distinct):
			for j in range(l):
				vs_distinct[i,j] = i/(2**(l-j-1))%2
		
		for i in range(distinct):
			for gg in range(int(g)):
				node = -1
				while node == -1:
					node = np.random.randint(N)
					if vs[s, node,0] != -1:
						node = -1
				vs[s, node,:] = vs_distinct[i,:]
	
	x = social_distance_matrix(vs)
	while nx.number_of_edges(G) < N*k:
		i = np.random.randint(N)
		s = np.random.randint(S)
		j = i
		probabilities = np.zeros(N)
		for q in range(N):
			probabilities[q] = np.exp(-alpha*x[s, i, q])
		while j == i:
			j = random_pick(range(N), probabilities)
		G.add_edge(i,j)
	return G, x, vs

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
			break
		relay[i] += 1
	return t+1, relay

def message_passing_hist(G, max_distance, repitition, l, x):
	p_ld = np.zeros((max_distance, repitition))
	relay = np.zeros(nx.number_of_nodes(G))
	for distance in range(1,max_distance+1):
		for k in range(repitition):
			p_ld[distance-1, k], relay = message_passing(distance, G, l, x, relay)
	return p_ld, relay

#The

N = 40
g = 5.
l = 3
S = 2
k = 4
alpha = 1

#c31
G, x, vs = create_c11_graph(N, g, l, S, k, alpha)
betweenness = np.zeros(N)
for i in range(N):
	betweenness[i] = nx.betweenness_centrality(G, normalized=True, weight=None)[i]

#C.3.3
max_distance = maximum_shortest_path(G)
repitition = 2000

p_ld, relay = message_passing_hist(G, max_distance, repitition, l, x)

#print relay, betweenness


#Draw Graph
nx.draw(G)
plt.show()

plt.plot(betweenness, relay, 'r*')
plt.xlabel('betweenness')
plt.ylabel('relay frequency')
plt.show()
#Plot Histogram
for d in range(max_distance):
	distr = p_ld[d,:]
        np.savetxt("p_dist_%i" % d, distr)
	#plt.hist([i-0.5 for i in distr], max(distr) - min(distr), normed=0.5, facecolor='green', alpha=1)
	#plt.xlabel('message time')
	#plt.ylabel('frequency')
	#plt.show()
