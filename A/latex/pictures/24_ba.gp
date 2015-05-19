reset
#set size ratio 0.5

folder = "pictures/data/"

#set xrange [0.5:9000]
#set key left bottom Left
#set xtics (1 "10^{0}", 10 "10^{1}", 100 "10^{2}", 1000 "10^{3}")
#set ytics -8,1,0
#set yrange [2e-9:2]

#set logscale xy
#set mxtics 10
set grid
#set format y '$10^{%T}$'
set xlabel '$p_\mathrm{lost}$'
set ylabel '$S$ ($\le 1$) and $\langle s \rangle^\mathrm{f}$ ($\ge 1$)'

set arrow 1 from 0.3125,graph 0 to 0.3125,2.55 nohead
set arrow 2 from 421/500.,graph 0 to 421/500.,1.31 nohead
set arrow 3 from 415/500.,graph 0 to 415/500.,1.66 nohead
set arrow 4 from 213/500.,graph 0 to 213/500.,graph 1 nohead
set arrow 5 from 138/500.,graph 0 to 138/500.,6.25 nohead
set arrow 6 from 0.458,graph 0 to 0.458,2.77 nohead

set yrange [0:6.5]
set key reverse Left
set key spacing 1.25
plot folder . "barabasi_failure.dat" u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#0000aa" t '\fs{BA failure}' ,\
     folder . "barabasi_failure.dat" u ($0/500):3 w lp pt 7 ps 0.6 lc rgb "#0000aa" t '' ,\
     folder . "barabasi_hub.dat"     u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#008888" t '\fs{BA hub}',\
     folder . "barabasi_hub.dat"     u ($0/500):3 w lp pt 7 ps 0.6 lc rgb "#008888" t '',\
     folder . "barabasi_evil.dat"    u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#00aa00" t '\fs{BA evil}',\
     folder . "barabasi_evil.dat"    u ($0/500):3 w lp pt 7 ps 0.6 lc rgb "#00aa00" t '',\
     1/0 lc rgb '#ffffff' t ' ',\
     folder . "erdos_failure.dat"    u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#bbcc00" t '\fs{ER failure}',\
     folder . "erdos_failure.dat"    u ($0/500):3 w lp pt 7 ps 0.5 lc rgb "#bbcc00" t '',\
     folder . "erdos_hub.dat"        u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#cc8800" t '\fs{ER hub}',\
     folder . "erdos_hub.dat"        u ($0/500):3 w lp pt 7 ps 0.5 lc rgb "#cc8800" t '',\
     folder . "erdos_evil.dat"       u ($0/500):1 w lp pt 7 ps 0.6 lc rgb "#e50000" t '\fs{ER evil}',\
     folder . "erdos_evil.dat"       u ($0/500):3 w lp pt 7 ps 0.5 lc rgb "#e50000" t ''


