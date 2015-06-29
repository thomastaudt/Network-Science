folder = 'pictures/data/'


set yrange [-0.3:0.3]
set xrange [0:35]
set ylabel 'modularity Q'

set arrow 1 from 2,0.21 to 2,graph 0 lc rgb "#666666" nohead
set arrow 2 from 5,0.21 to 5,graph 0 lc rgb "#666666" nohead

set multiplot
set rmargin scr 0.48
set bmargin scr 0.57
set lmargin scr 0.10
plot folder.'12_ka_data.dat' u ($0+1):1 w lp lw 2 pt 6 ps 1.2 t '\footnotesize{$G_0$}' ,\
     folder.'12_ka_data.dat' u ($0+1):1 w p pt 7 ps 1.0 lc rgb "#cccccc" t ''

reset 
set lmargin scr 0.57
set bmargin scr 0.57
set yrange [-0.4:0.8]
set xrange [0:25]

set arrow 1 from 3,0.55 to 3,graph 0 lc rgb "#666666" nohead

plot folder.'12_ps_simp_data.dat' u ($0+1):1 w lp lt 2 lw 2 pt 6 ps 1.2  t '\footnotesize{$G_1$}' ,\
     folder.'12_ps_simp_data.dat' u ($0+1):1 w p pt 7 ps 1.0 lc rgb "#cccccc" t ''

reset 
set xrange [0:30]
set rmargin scr 0.48
set tmargin scr 0.48
set lmargin scr 0.10
#set yrange [-0.4:0.8]
#set xrange [0:25]
#set xlabel 'number of communities'
set xlabel 'number of communities'
set ylabel 'modularity Q'

set arrow 1 from 9,0.82 to 9,graph 0 lc rgb "#666666" nohead
set arrow 2 from 25,0.62 to 25,graph 0 lc rgb "#666666" nohead

plot folder.'12_ps_comp_data.dat' u ($0+1):1 w lp lt 3 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_2$}' ,\
     folder.'12_ps_comp_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''


set xlabel 'number of communities'

reset 

set xlabel 'number of communities'
set lmargin scr 0.57
set tmargin scr 0.48
set yrange [-0.05:0.20]
set xrange [0:30]

set arrow 1 from 4,0.14 to 4,graph 0 lc rgb "#666666" nohead

plot folder.'12_le_data.dat' u ($0+1):1 w lp lt 4 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_3$}' ,\
     folder.'12_le_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''


unset multiplot                                      

