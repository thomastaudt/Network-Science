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
