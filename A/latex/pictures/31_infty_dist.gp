
folder = 'pictures/data/'

set bmargin scr 0.1
set tmargin scr 0.95

set ylabel 'degree dist. $P_\mathrm{d}(k)$'
set ylabel offset 1 
set xlabel 'degree $k$'
#set xtics 0,1,4

#set xrange [0:0.01]
#set yrange [0:0.8]
set multiplot 
#set yrange [0:1.05]
#set xrange [-0.1:2]
set lmargin scr 0.095
set rmargin scr 0.460
set title '\textbf{a)}'
set xrange [-1:9]
set yrange [0:0.8]
set key spacing 1.25
plot folder . '31_infty_ddist.dat' u 0:($2/250)  w lp pt 7 ps 1.5 t '$p=1.6\times 10^{-3}$', \
     folder . '31_infty_ddist.dat' u 0:($4/250)  w lp pt 7 ps 1.5 t '$p=4.8\times 10^{-3}$', \
     folder . '31_infty_ddist.dat' u 0:($11/250) w lp pt 7 ps 1.5 t '$p=16\times 10^{-3}$', \

set title '\textbf{b)}'
set key right
set ylabel 'cluster size dist. $P_\mathrm{C}(s)$'
set xlabel 'cluster size $s$'
#set yrange [0:100]
set xtics auto
set autoscale xy
#set yrange [0:250]
#set xrange [-50:625]
set xrange [-2:32]
#set yrange [0:0.37]
#set yrange [0:0.06]
#set logscale y
#set yrange auto
set lmargin scr 0.585
set rmargin scr 0.95
set key spacing 1.4


set xtics ("0" 0, "5" 5, "240" 20, "245" 25, "250" 30)

scaler(x) = x <= 10 ? x :(x > 10 && x < 225 ? 1/0 : x-220)
#scaler(x) = x

#set ytics 0,0.1,0.3
set label '\textbf{$\git$}' at 12.5,0 front
set ylabel offset 1.3

plot folder . '31_infty_cdist.dat' u (scaler($0)):($2)  w lp pt 7 ps 0.6 t '$p=1.6\times 10^{-3}$', \
     folder . '31_infty_cdist.dat' u (scaler($0)):($11) w lp pt 7 ps 0.6 t '$p=16\times 10^{-3}$', \

