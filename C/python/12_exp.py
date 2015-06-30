# Karate network
karate_mat =  np.loadtxt("karate_network.txt")
karate_graph = nx.Graph(karate_mat)
best, val, net, qs = optpart(karate_graph)


## SIMPLE POLYSTAR
##################
## n-polygon of connected star-polygons as community structure
n = 3
k = 5
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

#pos = nx.get_node_attributes(polystar_gr, 'pos')
#sizes = list(nx.get_node_attributes(polystar_gr, 'size').values())
#colors = list(nx.get_node_attributes(polystar_gr, 'color').values())
plt.figure(figsize=(6,6))
#for comps in disintegrate(polystar_gr):
    pos = nx.get_node_attributes(polystar_gr, 'pos')
    sizes = list(nx.get_node_attributes(polystar_gr, 'size').values())
    colors = list(nx.get_node_attributes(polystar_gr, 'color').values())
    nx.draw(polystar_gr, pos=pos, node_size=sizes, node_color=colors)
    plt.show()

## COMPLEX POLYSTAR
###################
## n-polygon of connected star-polygons as community structure
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



# Add centers and connect them circularly
for i in range(0, n):
    polystar_gr.add_node(i, pos=(r1*np.cos(i/n*2*np.pi), r1*np.sin(i/n*2*np.pi)),
                            size=300,
                            color=i
                        )
    polystar_gr.add_edge(i, (i+1) % n)
    #polystar_gr.add_edge(i, (i+2) % n)
    if i % 4 == 0: polystar_gr.add_edge(-k-1, i)


# Add children to the centers
for i in range(0, n):
    for j in range(k*i+n, k*(i+1)+n):
        polystar_gr.add_node(j, pos=(r1*np.cos(i/n*2*np.pi) + r2*np.cos(((j+2)/k + i/n)*2*np.pi),
                                     r1*np.sin(i/n*2*np.pi) + r2*np.sin(((j+2)/k + i/n)*2*np.pi)),
                                size=30,
                                color=i
                            )
        if j == k*i+n+k//4 or j == k*i+n+3*k//4:
            polystar_gr.add_edge(i, j)
        if j != k*i+n and j != k*i+n+k//2: 
            polystar_gr.add_edge(j, ((j+1)-(k*i+n)) % k + k*i+n)


#pos = nx.get_node_attributes(polystar_gr, 'pos')
#sizes = list(nx.get_node_attributes(polystar_gr, 'size').values())
#colors = list(nx.get_node_attributes(polystar_gr, 'color').values())

best, val, net, qs = optpart(polystar_gr)


plt.figure(figsize=(6,6))
for comps in disintegrate(polystar_gr):
    pos = nx.get_node_attributes(polystar_gr, 'pos')
    sizes = list(nx.get_node_attributes(polystar_gr, 'size').values())
    colors = list(nx.get_node_attributes(polystar_gr, 'color').values())
    nx.draw(polystar_gr, pos=pos, node_size=sizes, node_color=colors)
    plt.show()
    break
    #if len(comps) > 2: break
#plt.axis('off')
#plt.gca().set_position([0, 0, 1, 1])
#plt.savefig("test.svg")

#plt.figure(figsize=[6,6])
#x = np.arange(0,100,0.00001)
#y = x*np.sin(2*pi*x)
#plt.plot(y)

# Binary trees as community structures
# Random networks with preference for interconnections
# [net.node[i]['comp'] for i in net.node]
