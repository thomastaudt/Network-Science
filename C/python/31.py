import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

def random_pick(some_list, probabilities):
    x = random.uniform(0, sum(probabilities))
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item

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


def int_to_bits(i, l):
    chars = np.zeros(l)
    for j in range(l):
        r = i // 2**(l-j-1)
        chars[j] = r
        if r > 0: i = i - 2**(l-j-1)
    return chars

def all_coordinates(l):
    return np.array( [ int_to_bits(i, l) for i in range(2**l) ], dtype=int )


# g: group size of nodes with same social coordinates for one 
#    characteristic
# l: number of bits for one social coordinate of fixed characteristics
# N: number of nodes in total
# S: number of different characteristics
# k: desired mean degree of the resulting graph
# a: (alpha) Temperature -- how likely are connections between nodes 
#    of different social coordinates
def random_social_graph(g, l, S, k, a):
    N = g*2**l
    G = nx.empty_graph(N)
    # create the social coordinates vs
    vs = np.zeros((S,N,l), dtype=int)
    # for every characteristic
    for s in range(S):
        # want to choose g elements at random for every coordinate
        random_nodes = list(range(N))
        random.shuffle(random_nodes)
        for ch in all_coordinates(l):
            for node in random_nodes[0:g]:
                vs[s, node, :] = ch
            del random_nodes[0:g]

    # collect all distances in a matrix
    social_matrix = social_distance_matrix(vs)
    # now add edges until the average degree is greater or equal to k
    while nx.number_of_edges(G) < N*k:
        # choose random node
        node1 = np.random.randint(N)
        # and random characteristic
        s = np.random.randint(S)
        # create probabilities
        probs = [ np.exp( -a * social_matrix[s, node1, node2] ) for node2 in range(N) ]
        # finally pick a node to connect to
        node2 = node1
        while node2 == node1 or G.has_edge(node1, node2): node2 = random_pick( list(range(N)), probs )
        #while node2 == node1: node2 = random_pick( list(range(N)), probs )
        G.add_edge(node1, node2)
    # done constructing the graph
    return G, social_matrix, vs

# produce the graphs
plt.figure(figsize=(6,6))
plt.axis("off")
#
g = 5 
l = 3
k = 4
## graphs with only one characteristicum
S = 1
a = 1

G, mat, vs = random_social_graph(g,l,S,k,a)
nodes = G.nodes()

groups = []
i = 0
while nodes:
    node = nodes[1]
    group = [ n for n in nodes if mat[0, node, n] == 0 ]
    for n in group: nx.set_node_attributes(G, 'color', { n : i })
    nodes = [ node for node in nodes if node not in group ]
    # color is great!
    groups.append(group)
    i += 1

#colorful graphs!
#colors = list(nx.get_node_attributes(G, 'color').values())
#nx.draw(G, node_color=colors)
#plt.show()
for comps in disintegrate(G):
    colors = list(nx.get_node_attributes(G, 'color').values())
    nx.draw(G, node_color=colors)
    #plt.savefig("pictures/31_S%ia%i_%02i.svg" % (S,a,i))
    plt.savefig("pictures/31_S%ia%i_%02i_or.svg" % (S,a,len(comps)))
    plt.clf()



# graphs with two characteristicas
#S = 2
#a = 5

#G, mat, vs = random_social_graph(g,l,S,k,a)

#groups = []
#labels = {}
#i = 0
#r = 0

#for s in range(S):
    #nodes = G.nodes()
    #while nodes:
        #node = nodes[1]
        #group = [ n for n in nodes if mat[s, node, n] == 0 ]
        #if s == 0: 
            #for n in group: nx.set_node_attributes(G, 'color', { n : i })
        #if s == 1: 
            #for n in group: labels[n] = "%d" % r
            #r += 1
        #nodes = [ node for node in nodes if node not in group ]
        ## color is great!
        #groups.append(group)
        #i += 1

## colorful graphs!
##colors = list(nx.get_node_attributes(G, 'color').values())
##nx.draw_networkx(G, node_color=colors, labels=labels)
##lay = nx.spring_layout(G)

#for comps in disintegrate(G):
    #colors = list(nx.get_node_attributes(G, 'color').values())
    #nx.draw(G, node_color=colors, labels=labels)
    ##plt.savefig("pictures/31_S%ia%i_%02i.svg" % (S,a,i))
    #plt.savefig("pictures/31_S%ia%i_%02i_or.svg" % (S,a,len(comps)))
    #plt.clf()

