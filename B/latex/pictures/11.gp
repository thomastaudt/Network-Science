
folder = 'pictures/data/'

set label 1 '\footnotesize{$\sigma_c\approx 0.016$}' at 0.0145, graph 0.70 center rotate by 90

set xlabel 'coupling strength $\sigma$'
set ylabel '$r$'
set key bottom
set key spacing 1.2
set xrange [-0.25/100:5.25/100]
set yrange [0:1.2]
set arrow from 1.596/100,graph 1 to 1.596/100,graph 0 lt -1 lw 2 lc rgb "#006600" nohead
a = 1.05
plot folder.'11_full.txt' u ($1/100):2 w p pt 7 ps a*1.55 lc rgb "#006600" t '',\
     folder.'11_full.txt' u ($1/100):2 w p pt 7 ps a*1.00 lc rgb "#77ee77" t ''
