

folder = 'pictures/data/'

set bmargin scr 0.1
set tmargin scr 0.90

set ylabel 'cluster size'
set xlabel 'occupation probability $p\times 10^3$'
set xrange [0:0.015*1e3]
set key right bottom spacing 1.5

set multiplot 
#set yrange [0:1.05]
#set xrange [-0.1:2]
set lmargin scr 0.1

set rmargin scr 0.49
set title '\textbf{a)}'
set arrow from first 4.,graph 0 to first 4.,graph 1 nohead lt -1 lc rgb "#777777"
set arrow from first 4.5622,graph 0 to first 4.5622,graph 1 nohead lt -1 lc rgb "#aa0000"
plot folder . '31_infty.dat' u ($1*1e3):3 w lp pt 7 ps 0.5 t '\fs{$\mathrm{max}_C$}', \
     folder . '31_infty.dat' u ($1*1e3):5 w lp pt 7 ps 0.5 t '\fs{$\langle s\rangle$}', \

set title '\textbf{b)}'
set key right top
unset ylabel
#set yrange [0:100]
set lmargin scr 0.56
set rmargin scr 0.95
plot folder . '31_infty.dat' u ($1*1e3):4 w lp pt 7 ps 0.5 t '\fs{$\mathrm{max}_C^\mathrm{f}$}', \
     folder . '31_infty.dat' u ($1*1e3):6 w lp pt 7 ps 0.5 t '\fs{$\langle s\rangle^\mathrm{f}$}', \
     #folder . '31_2d.dat' u 1:($7) w lp pt 7 ps 0.3 t '$\langle s\rangle^\mathrm{f}$', \
