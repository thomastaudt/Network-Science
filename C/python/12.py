
# Karate graph
ka_gr = karate()
ka_best, ka_val, ka_net, ka_qs = optpart(ka_gr)

plt.figure(figsize=(6,6))
i = 0
lay = nx.spring_layout(ka_gr)
for comps in disintegrate(ka_gr):
    i += 1
    colors = list(nx.get_node_attributes(ka_gr, 'color').values())
    nx.draw(ka_gr, node_color=colors, pos=lay)
    plt.savefig("pictures/12_ka_graph%03i.svg" % (i,))
    plt.clf()

np.savetxt("12_ka_data.dat", ka_qs)

## SIMPLE POLYSTAR
##################
ps_simp_gr = simple_polystar()
ps_simp_best, ps_simp_val, ps_simp_net, ps_simp_qs = optpart(ps_simp_gr)
plt.figure(figsize=(6,6))
i = 0
for comps in disintegrate(ps_simp_gr):
    i += 1
    pos = nx.get_node_attributes(ps_simp_gr, 'pos')
    sizes = list(nx.get_node_attributes(ps_simp_gr, 'size').values())
    colors = list(nx.get_node_attributes(ps_simp_gr, 'color').values())
    nx.draw(ps_simp_gr, pos=pos, node_size=sizes, node_color=colors)
    plt.savefig("pictures/12_ps_simp_graph%03i.svg" % (i,))
    plt.clf()
np.savetxt("12_ps_simp_data.dat", ps_simp_qs)


## COMPLEX POLYSTAR
##################
ps_comp_gr = complex_polystar()
ps_comp_best, ps_comp_val, ps_comp_net, ps_comp_qs = optpart(ps_comp_gr)
plt.figure(figsize=(6,6))
i = 0
for comps in disintegrate(ps_comp_gr):
    i += 1
    pos = nx.get_node_attributes(ps_comp_gr, 'pos')
    sizes = list(nx.get_node_attributes(ps_comp_gr, 'size').values())
    colors = list(nx.get_node_attributes(ps_comp_gr, 'color').values())
    nx.draw(ps_comp_gr, pos=pos, node_size=sizes, node_color=colors)
    plt.savefig("pictures/12_ps_comp_graph%03i.svg" % (i,))
    plt.clf()
np.savetxt("12_ps_comp_data.dat", ps_comp_qs)


## LAYERED ERDOS
################
le_gr = layered_erdos()
le_best, le_val, le_net, le_qs = optpart(le_gr)
plt.figure(figsize=(6,6))
i = 0
for comps in disintegrate(le_gr):
    i += 1
    colors = list(nx.get_node_attributes(le_gr, 'color').values())
    pos = nx.get_node_attributes(le_gr, 'pos')
    nx.draw(le_gr, node_color=colors, node_size=75, pos=pos, width=0.25)
    #plt.show()
    plt.savefig("pictures/12_le_graph%03i.svg" % (i,))
    plt.clf()
    if len(comps) >= 100: break
np.savetxt("12_le_data.dat", le_qs)
