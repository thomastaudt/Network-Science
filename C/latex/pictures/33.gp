folder = 'pictures/data/'


#plot folder.'p_dist_0.dat' u 1:(1./10000) smooth freq w i lw 2 t '$d = 1$'

n = 50000.

#set yrange [-0.3:0.3]
reset
set key center top
set xrange [0:30]
#set yrange [0:0.5]
set ylabel 'frequency'

set ytics 0, 0.2, 0.8
set yrange [0:0.8]

set multiplot
set tmargin scr 0.96
set rmargin scr 0.48
set bmargin scr 0.70
set lmargin scr 0.10
set xrange [-2:32]
set xtics ("0" 0, "5" 5, "10" 10, "15" 15, "20" 20, "25" 25, "fail" 30)

plot folder.'p_0_newest.dat' u 1:(1./n) smooth freq w i lt 1 lw 5 t '\footnotesize{$d=1$}'

reset 
set key center top
set lmargin scr 0.57
set tmargin scr 0.96
set bmargin scr 0.70
#set arrow 1 from 3,0.55 to 3,graph 0 lc rgb "#666666" nohead
set xrange [-2:32]
set xtics ("0" 0, "5" 5, "10" 10, "15" 15, "20" 20, "25" 25, "fail" 30)

set ytics 0, 0.1, 0.8
set yrange [0:0.4]
plot folder.'p_1_newest.dat' u 1:(1./n) smooth freq w i lt 2 lw 5 t '\footnotesize{$d=2$}'
     #folder.'12_ps_simp_data.dat' u ($0+1):1 w p pt 7 ps 1.0 lc rgb "#cccccc" t ''

reset 
set key center top
set ylabel 'frequency'
set xrange [0:30]
set rmargin scr 0.48
set tmargin scr 0.63
set bmargin scr 0.37
set lmargin scr 0.10
set yrange [0:0.2]
set xrange [-2:32]
set xtics ("0" 0, "5" 5, "10" 10, "15" 15, "20" 20, "25" 25, "fail" 30)
##set yrange [-0.4:0.8]
##set xrange [0:25]
##set xlabel 'number of communities'
#set xlabel 'number of communities'
#set ylabel 'modularity Q'

set label '\footnotesize $\to 0.43$' at 28.5, graph 0.5 rotate by 90 center

plot folder.'p_2_newest.dat' u 1:(1./n) smooth freq w i lt 3 lw 5 t '\footnotesize{$d=3$}'

#set arrow 1 from 9,0.82 to 9,graph 0 lc rgb "#666666" nohead
#set arrow 2 from 25,0.62 to 25,graph 0 lc rgb "#666666" nohead

#plot folder.'12_ps_comp_data.dat' u ($0+1):1 w lp lt 3 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_2$}' ,\
     #folder.'12_ps_comp_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''


#set xlabel 'number of communities'

reset 
set key center top 

set lmargin scr 0.57
set tmargin scr 0.63
set bmargin scr 0.37
set yrange [0:0.2]

set xrange [-2:32]
set xtics ("0" 0, "5" 5, "10" 10, "15" 15, "20" 20, "25" 25, "fail" 30)
set label '\footnotesize $\to 0.67$' at 28.5, graph 0.5 rotate by 90 center
plot folder.'p_3_newest.dat' u 1:(1./n) smooth freq w i lt 4 lw 5 t '\footnotesize{$d=4$}'
#set arrow 1 from 4,0.14 to 4,graph 0 lc rgb "#666666" nohead

#plot folder.'12_le_data.dat' u ($0+1):1 w lp lt 4 lw 2.5 pt 6 ps 1.2  t '\footnotesize{$G_3$}' ,\
     #folder.'12_le_data.dat' u ($0+1):1 w p pt 7 ps 0.9 lc rgb "#cccccc" t ''

reset 
set key center top
set tmargin scr 0.30
set bmargin scr 0.04
set lmargin scr 0.34
set rmargin scr 0.73

set ylabel 'frequency'
set xlabel 'length $\lambda$ of the message''s path'
set yrange [0:0.1]

set xrange [-2:32]
set xtics ("0" 0, "5" 5, "10" 10, "15" 15, "20" 20, "25" 25, "fail" 30)
set label '\footnotesize $\to 0.82$' at 28.5, graph 0.5 rotate by 90 center
plot folder.'p_4_newest.dat' u 1:(1./n) smooth freq w i lt 6 lw 5 t '\footnotesize{$d=5$}'
#unset multiplot                                      

