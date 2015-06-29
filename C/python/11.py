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
  
#m =  np.loadtxt("karate_network.txt")
#g = nx.Graph(m)
#best, val, net, qs = optpart(g)
#[net.node[i]['comp'] for i in net.node]

## KARATE
#########
def karate():
    mat = np.loadtxt("karate_network.txt")
    color_comps = [[0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21], 
                   [32, 33, 2, 8, 9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
    gr = nx.Graph(mat)
    colors = { node : 0 if node in color_comps[0] else 1 for node in gr.nodes() }
    nx.set_node_attributes(gr, 'color', colors)
    return gr

## SIMPLE POLYSTAR
def simple_polystar():
    n = 3
    k = 6
    ang = 2*np.pi
    r1 = 1
    r2 = 0.3
    polystar_gr = nx.Graph()
    # Add centers and connect them circularly
    for i in range(0, n):
        polystar_gr.add_node(i, pos=(r1*np.cos(i/n*2*np.pi), r1*np.sin(i/n*2*np.pi)),
                                size=300,
                                color=i
                            )
        polystar_gr.add_edge(i, (i+1) % n)
    # Add children to the centers
    for i in range(0, n):
        for j in range(k*i+n, k*(i+1)+n):
            polystar_gr.add_node(j, pos=(r1*np.cos(i/n*2*np.pi) + r2*np.cos(j/k*2*np.pi),
                                         r1*np.sin(i/n*2*np.pi) + r2*np.sin(j/k*2*np.pi)),
                                    size=30,
                                    color=i
                                )
            polystar_gr.add_edge(i, j)
            polystar_gr.add_edge(j, ((j+1)-(k*i+n)) % k + k*i+n)
    return polystar_gr



## COMPLEX POLYSTAR
###################
def complex_polystar():
    n = 8
    k = 20
    ang = 2*np.pi
    r1 = 1.20
    r2 = 0.3
    polystar_gr = nx.Graph()

    polystar_gr.add_node(-k-1, pos=(0,0), size=300, color=-1)

    for j in range(-k, 0):
        polystar_gr.add_node(j, pos = (r2*np.cos((j+0.5)/k*2*np.pi), r2*np.sin((j+0.5)/k*2*np.pi)),
                                 size=30,
                                 color=-1
                            )
        polystar_gr.add_edge(-k-1, j)
        polystar_gr.add_edge(j, ((j+1)+k) % k - k)
        polystar_gr.add_edge(j, ((j+2)+k) % k - k)
        #polystar_gr.add_edge(j, ((j+3)+k) % k - k)



    # Add centers and connect them circularly
    for i in range(0, n):
        polystar_gr.add_node(i, pos=(r1*np.cos(i/n*2*np.pi), r1*np.sin(i/n*2*np.pi)),
                                size=300,
                                color=i
                            )
        polystar_gr.add_edge(i, (i+1) % n)
        polystar_gr.add_edge(i, (i+2) % n)
        polystar_gr.add_edge(i, (i+3) % n)
        if i % 4 == 0: polystar_gr.add_edge(-k-1, i)


    # Add children to the centers
    for i in range(0, n):
        for j in range(k*i+n, k*(i+1)+n):
            polystar_gr.add_node(j, pos=(r1*np.cos(i/n*2*np.pi) + r2*np.cos(j/k*2*np.pi),
                                         r1*np.sin(i/n*2*np.pi) + r2*np.sin(j/k*2*np.pi)),
                                    size=30,
                                    color=i
                                )
            if j % 2 == 0:
                polystar_gr.add_edge(i, j)
            polystar_gr.add_edge(j, ((j+1)-(k*i+n)) % k + k*i+n)
            polystar_gr.add_edge(j, ((j+2)-(k*i+n)) % k + k*i+n)
    return polystar_gr


def draw_number():
    i = 0
    while True:
        yield i
        i += 1


def layered_erdos():
    gr = nx.Graph()
    n_over = 4
    radius = 0.4
    n_under = [25, 25, 25, 25]
    positions = [(1,1), (1,-1), (-1,-1), (-1,1)]
    p_over = 0.15
    p_under = 0.75
    comps = []
    draw = draw_number()
    for j in range(n_over):
        comps.append([ draw.__next__() for i in range(n_under[j]) ])
    nodes = sum(comps, []) 
    for j in range(n_over):
        h = 0
        x = positions[j][0]
        y = positions[j][1]
        for node in comps[j]:
            h += 1
            angle = h/len(comps[j])*2*np.pi
            gr.add_node(node, color=j, pos=(x + radius*np.cos(angle), y + radius*np.sin(angle)) )
    for n1 in nodes:
        for j in range(n_over):
            for n2 in comps[j]:
                if n1 < n2:
                    if n1 in comps[j]:
                        if np.random.sample() < p_under:
                            gr.add_edge(n1, n2)
                    else:
                        if np.random.sample() < p_over:
                            gr.add_edge(n1, n2)
    #
    return gr

def community_matrix(components):
    c = len(components)
    nodes = sum(components, []) # + makes list concatenation!
    N = sum(map(lambda x: len(x), components))
    matrix = np.zeros((N, c))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i,j] = 1 if nodes[i] in components[j] else 0
    return matrix

def degree_vector(adj_matrix):
    return np.array(np.sum(adj_matrix, axis = 1)).flatten()

def transition_matrix(adj_matrix):
    d = degree_vector(adj_matrix)
    D_inverse = np.diag(1/d)
    return D_inverse * adj_matrix

def steady_state(adj_matrix):
    d = degree_vector(adj_matrix)
    return d / np.sum(d)

def stability(gr, components, times):
    adj_matrix = nx.adjacency_matrix(gr).todense()
    H  = community_matrix(components)
    M  = transition_matrix(adj_matrix)
    pi = steady_state(adj_matrix)
    Pi = np.diag(pi)
    pi.resize(len(pi), 1)
    r = np.zeros(len(times))
    for i in range(len(times)):
        R  = H.T * (Pi * M**times[i] - pi * pi.T) * H
        r[i] = np.trace(R)
    return r

def stability_mins(gr, components, until):
    times = np.array(list(range(0, until)))
    r = stability(gr, components, times)
    r_mins = np.array( [ np.min(r[:i]) for i in range(1, len(r)+1) ] )
    return r_mins
