folder = 'pictures/data/'


#plot folder.'p_dist_0.dat' u 1:(1./10000) smooth freq w i lw 2 t '$d = 1$'


n = 10000.


#set yrange [-0.3:0.3]
reset
set xrange [0:30]
#set yrange [0:0.5]
set ylabel 'frequency'

set ytics 0, 0.1, 0.5
set yrange [0:0.5]

set multiplot
set rmargin scr 0.48
set bmargin scr 0.57
set lmargin scr 0.10

plot folder.'p_dist_0_new.dat' u 1:(1./n) smooth freq w i lt 1 lw 4 t '\footnotesize{$d=1$}'

reset 
set lmargin scr 0.57
set bmargin scr 0.57
set xrange [0:30]
#set arrow 1 from 3,0.55 to 3,graph 0 lc rgb "#666666" nohead

plot folder.'p_dist_1_new.dat' u 1:(1./n) smooth freq w i lt 2 lw 4 t '\footnotesize{$d=2$}'
     #folder.'12_ps_simp_data.dat' u ($0+1):1 w p pt 7 ps 1.0 lc rgb "#cccccc" t ''

reset 
set ylabel 'frequency'
set xrange [0:30]
set rmargin scr 0.48
set tmargin scr 0.48
set lmargin scr 0.10
set yrange [0:0.25]
##set yrange [-0.4:0.8]
##set xrange [0:25]
##set xlabel 'number of communities'
#set xlabel 'number of communities'
#set ylabel 'modularity Q'
set xlabel 'length $\lambda$ of the message''s path'
plot folder.'p_dist_2_new.dat' u 1:(1./n) smooth freq w i lt 3 lw 4 t '\footnotesize{$d=3$}'

#set arrow 1 from 9,0.82 to 9,graph 0 lc rgb "#666666" nohead
#set arrow 2 from 25,0.62 to 25,graph 0 lc rgb "#666666" nohead

#plot folder.'12_ps_comp_data.dat' u ($0+1):1 w lp lt 3 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_2$}' ,\
     #folder.'12_ps_comp_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''


#set xlabel 'number of communities'

reset 

set xlabel 'length $\lambda$ of the message''s path'
set lmargin scr 0.57
set tmargin scr 0.48
set yrange [0:0.5]
set xrange [0:30]

plot folder.'p_dist_3_new.dat' u 1:(1./n) smooth freq w i lt 4 lw 4 t '\footnotesize{$d=4$}'
#set arrow 1 from 4,0.14 to 4,graph 0 lc rgb "#666666" nohead

#plot folder.'12_le_data.dat' u ($0+1):1 w lp lt 4 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_3$}' ,\
     #folder.'12_le_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''


#unset multiplot                                      

