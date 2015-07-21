
N = 10
M = 300
Tend = 5

# create adjacency-matrices
K, K_ = trial(Tend=Tend, N=N, M=M)
print("Uncorrected:")
print(K)
print()
print(K_)
K_[K_ < 0.05] = 0
K_[K_ > 1] = 1.1515

print("Corrected:")
print(K)
print()
print(K_)

K_diff = np.abs(K - K_)

Q = Q_95(K, K_)

# create graphs
G  = nx.DiGraph(K)
G_ = nx.DiGraph(K_)
G_diff = nx.DiGraph(K_diff)

# get (fixed) positions and values for the edge-widths from the weights
pos = nx.circular_layout(G)
edgewidth  = [ 2*d['weight'] for (u,v,d) in G.edges(data=True) ]
edgewidth_ = [ 2*d['weight'] for (u,v,d) in G_.edges(data=True) ]
edgewidth_diff = [ 2*d['weight'] for (u,v,d) in G_diff.edges(data=True) ]

# plot the original graph
plt.figure(figsize=(4,4))
nx.draw(G, pos=pos, edge_color="gray", width = edgewidth, node_size=300, node_color="black")
plt.savefig("pictures/N%d_M%d_T%d_Q%f_orig.svg" % (N,M,Tend,Q))
plt.clf()

# plot the reconstructed graph
nx.draw(G_, pos=pos, edge_color="gray", width = edgewidth_, node_size=300, node_color="black")
plt.savefig("pictures/N%d_M%d_T%d_Q%f_rec.svg" % (N,M,Tend,Q))
plt.clf()

# plot the difference graph
nx.draw(nx.compose(G, G_), pos=pos, edge_color="gray", width = edgewidth_diff, node_size=300, node_color="black")
plt.savefig("pictures/N%d_M%d_T%d_Q%f_diff.svg" % (N,M,Tend,Q))
plt.show()
plt.clf()
