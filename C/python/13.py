## KARATE
#########
ka_gr = karate()
gr = ka_gr.copy()
f = open("13_ka_data.dat", "w")
for comps in disintegrate(gr):
    r = stability_mins(ka_gr, comps, 100)
    print(len(comps))
    f.write("# comps %d\n" % (len(comps),))
    for val in r:
        f.write("%f\n" % (val,))
    f.write("\n\n")
    if len(comps) == 50: break

f.close()

## SIMPLE POLYSTAR
##################
ps_simp_gr = simple_polystar()
gr = ps_simp_gr.copy()
f = open("13_ps_simp_data.dat", "w")
for comps in disintegrate(gr):
    r = stability_mins(ps_simp_gr, comps, 100)
    print(len(comps))
    f.write("# comps %d\n" % (len(comps),))
    for val in r:
        f.write("%f\n" % (val,))
    f.write("\n\n")
    if len(comps) == 50: break

f.close()

## COMPLEX POLYSTAR
###################
ps_comp_gr = complex_polystar()
gr = ps_comp_gr.copy()
f = open("13_ps_comp_data.dat", "w")
for comps in disintegrate(gr):
    r = stability_mins(ps_comp_gr, comps, 100)
    print(len(comps))
    f.write("# comps %d\n" % (len(comps),))
    for val in r:
        f.write("%f\n" % (val,))
    f.write("\n\n")
    if len(comps) == 50: break

f.close()

## LAYERED ERDOS
################
le_gr = layered_erdos()
gr = le_gr.copy()
f = open("13_le_data.dat", "w")
for comps in disintegrate(gr):
    r = stability_mins(le_gr, comps, 100)
    print(len(comps))
    f.write("# comps %d\n" % (len(comps),))
    for val in r:
        f.write("%f\n" % (val,))
    f.write("\n\n")
    if len(comps) == 50: break

f.close()
