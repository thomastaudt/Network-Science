folder = 'pictures/data/'


#set yrange [-0.3:0.3]
#set xrange [0:35]
set ylabel 'stability r'

set label '$G_0$' at graph 0.925, 0.85
#set arrow 1 from 2,0.21 to 2,graph 0 lc rgb "#666666" nohead
#set arrow 2 from 5,0.21 to 5,graph 0 lc rgb "#666666" nohead
set yrange [1e-4:1]
set logscale xy
set format y '$10^{%L}$'
set key bottom left reverse Left
set multiplot
set tmargin scr 0.975
set rmargin scr 0.975
set bmargin scr 0.775
set lmargin scr 0.10

set label '\footnotesize $h_\mathrm{max} = 2$' at 10,0.13 center rotate by -15.5

plot folder.'13_ka_data.dat' i 1 u ($0+1):1 w l lw 2 t '\footnotesize{$h=2$}' ,\
     folder.'13_ka_data.dat' i 3 u ($0+1):1 w l lw 2 t '\footnotesize{$h=4$}' ,\
     folder.'13_ka_data.dat' i 4 u ($0+1):1 w l lw 2 t '\footnotesize{$h=5$}' ,\
     folder.'13_ka_data.dat' i 5 u ($0+1):1 w l lw 2 t '\footnotesize{$h=6$}' ,\


reset 

set label '$G_1$' at graph 0.925, 0.85

set ylabel 'stability r'
set yrange [1e-2:1]
set logscale xy
set format y '$10^{%L}$'
set key bottom left reverse Left
set tmargin scr 0.725
set rmargin scr 0.975
set bmargin scr 0.525
set lmargin scr 0.10

set label '\footnotesize $h_\mathrm{max} = 3$' at 10,0.13 center rotate by -15.5

plot folder.'13_ps_simp_data.dat' i 2 u ($0+1):1 w l lw 2 t '\footnotesize{$h=3$}' ,\
     folder.'13_ps_simp_data.dat' i 4 u ($0+1):1 w l lw 2 t '\footnotesize{$h=5$}' ,\
     folder.'13_ps_simp_data.dat' i 5 u ($0+1):1 w l lw 2 t '\footnotesize{$h=6$}' ,\
     folder.'13_ps_simp_data.dat' i 6 u ($0+1):1 w l lw 2 t '\footnotesize{$h=7$}' ,\


reset 

set label '$G_2$' at graph 0.925, 0.85
set ylabel 'stability r'
set yrange [1e-2:1]
set logscale xy
set format y '$10^{%L}$'
set key bottom left reverse Left
set tmargin scr 0.475
set rmargin scr 0.975
set bmargin scr 0.275
set lmargin scr 0.10

set arrow from 60, graph 1 to 60, 0.085 lt -1 nohead
set arrow from 5, graph 1 to 5, 0.5 lt -1 nohead

set label '\footnotesize $h_\mathrm{max} = 9$' at 2.5,0.75 center rotate by -4.5
set label '\footnotesize $h_\mathrm{max} = 8$' at 22.5,0.350 center rotate by -12.5
set label '\footnotesize $h_\mathrm{max} = 2$' at 75,0.0920 center rotate by -18

plot folder.'13_ps_comp_data.dat' i 1 u ($0+1):1 w l lw 2 t '\footnotesize{$h=2$}' ,\
     folder.'13_ps_comp_data.dat' i 7 u ($0+1):1 w l lw 2 t '\footnotesize{$h=8$}' ,\
     folder.'13_ps_comp_data.dat' i 8 u ($0+1):1 w l lw 2 t '\footnotesize{$h=9$}' ,\
     folder.'13_ps_comp_data.dat' i 24 u ($0+1):1 w l lw 2 t '\footnotesize{$h=25$}' ,\




     
reset 

set label '$G_3$' at graph 0.925, 0.85
set ylabel 'stability r'
set yrange [1e-4:1]
set logscale xy
set format y '$10^{%L}$'
set key bottom left reverse Left
set tmargin scr 0.225
set rmargin scr 0.975
set bmargin scr 0.025
set lmargin scr 0.10

set xlabel 'time scale $t$'

set label '\footnotesize $h_\mathrm{max} = 4$' at 4.5,0.15 center rotate by -20.5
set label '\footnotesize $h_\mathrm{max} = 3$' at 12,0.002 center rotate by -43.5

set arrow from 9,0.5*1e-2 to 9, graph 1 lt -1 nohead

plot folder.'13_le_data.dat' i 2 u ($0+1):1 w l lw 2 t '\footnotesize{$h=3$}' ,\
     folder.'13_le_data.dat' i 3 u ($0+1):1 w l lw 2 t '\footnotesize{$h=4$}' ,\
     folder.'13_le_data.dat' i 19 u ($0+1):1 w l lw 2 t '\footnotesize{$h=20$}' ,\
     folder.'13_le_data.dat' i 49 u ($0+1):1 w l lw 2 t '\footnotesize{$h=50$}' ,\


unset multiplot                                      

