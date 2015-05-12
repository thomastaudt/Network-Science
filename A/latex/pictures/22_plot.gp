set size ratio 0.5

folder = "pictures/data/"

set xrange [0.5:9000]
set key left bottom Left
#set xtics (1 "10^{0}", 10 "10^{1}", 100 "10^{2}", 1000 "10^{3}")
#set ytics -8,1,0
set yrange [2e-9:2]

set logscale xy
set mxtics 10
set grid
set format y '$10^{%T}$'
set xlabel 'Degree $k$'
set ylabel '$P(k)$'


plot folder . "ba_m1_n500k.dat" pt 7 ps 0.6 lc rgb "#aa0a00" t '$~m=1$'   ,\
     folder . "ba_m5_n500k.dat" pt 7 ps 0.6 lc rgb "#194bc1" t '$~m=1$'   ,\
     folder . "ba_m20_n500k.dat" pt 7 ps 0.6 lc rgb "#00a12b" t '$~m=20$' ,\
     0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''
