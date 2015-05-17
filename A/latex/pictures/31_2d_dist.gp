
folder = 'pictures/data/'

set bmargin scr 0.1
set tmargin scr 0.90

set ylabel 'degree dist. $P_\mathrm{d}(k)$'
set ylabel offset 1 
set xlabel 'degree $k$'
set xtics 0,1,4

set yrange [0:0.8]
set multiplot 
#set yrange [0:1.05]
#set xrange [-0.1:2]
set lmargin scr 0.095
set rmargin scr 0.460
set title '\textbf{a)}'
plot folder . '31_2d_ddist.dat' u 0:($4/625)  w lp pt 7 ps 1.0 t '\fs{$p=0.25$}', \
     folder . '31_2d_ddist.dat' u 0:($7/625)  w lp pt 7 ps 1.0 t '\fs{$p=0.50$}', \
     folder . '31_2d_ddist.dat' u 0:($10/625) w lp pt 7 ps 1.0 t '\fs{$p=0.75$}', \

set title '\textbf{b)}'
set key right
set ylabel 'cluster size dist. $P_\mathrm{C}(s)$'
set xlabel 'cluster size $s$'
#set yrange [0:100]
set xtics auto
set autoscale y
#set yrange [0:250]
set xrange [-50:625]
set xrange [-2:67]
set yrange [0:0.37]
#set yrange [0:0.06]
#set logscale y
#set yrange auto
set lmargin scr 0.585
set rmargin scr 0.95
set key spacing 1.4


set xtics ("0" 0, "20" 20, "575" 45, "625" 65)

scaler(x) = x <= 30 ? x :(x > 30 && x < 595 ? 1/0 : x-560)

set ytics 0,0.1,0.3
set label '\textbf{$\git$}' at screen 0.57+(0.95-0.57)/2,0.1 front
set ylabel offset 1.3

plot folder . '31_2d_cdist.dat' u (scaler($0)):($4)  w lp pt 7 ps 0.6 t '\fs{$p=0.25$}', \
     folder . '31_2d_cdist.dat' u (scaler($0)):($10) w lp pt 7 ps 0.6 t '\fs{$p=0.75$}', \

