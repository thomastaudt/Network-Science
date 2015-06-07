folder = "pictures/data/"
set xlabel 'time $t$'
set ylabel 'phase difference $\Delta\theta/\mathrm{rad}$'

set multiplot

set title '\textbf{(a)}'

set key invert
#set key reverse Left
#set key top right
set rmargin scr 0.50
set lmargin scr 0.10

set xrange [-5:30]

plot folder."23_0.dat" u 1:2 w l t '\footnotesize $\tau=0.0$',\
     folder."23_4.dat" u 1:2 w l t '\footnotesize $\tau=0.4$',\
     folder."23_8.dat" u 1:2 w l t '\footnotesize $\tau=0.8$',\



reset
set title '\textbf{(b)}'

#set arrow from 0,graph 0 to 0, graph 1 nohead lt -1 lw 1.5 lc rgb "#444444" front
set key invert

#set xrange
set yrange [-0.5:3.5]

set xlabel 'time $t$'
set lmargin scr 0.59
set rmargin scr 0.99
plot folder."23_12.dat" u 1:2 w l t '\footnotesize $\tau=1.2$',\
     folder."23_16.dat" u 1:2 w l t '\footnotesize $\tau=1.6$',\

#set xrange [-1:10]
#set cbrange [1:30]
##set palette model HSV rgbformulae 3,2,2
#unset colorbox
#set yrange [-1.5:1.5]
##set ytics -2, 1, 2
#set xlabel 'time $t$'
#set palette defined ( 0 "green", 1 "blue", 2 "red", 3 "orange" )
#plot for [i=1:30] folder."B22_minus_sin_".(30-i+1).".dat" u 1:2:(30-i+1) w l palette t ''
#set key top left
#set key reverse Left
#set title '\textbf{(b)}'
##set yrange [-0.15:0.5]
##set xrange [-0.3:0.3]
##set yrange [-0.2:0.3]
#set xlabel '$\omega / \mathrm{rad} / \mathrm{s}$'
##set ylabel '$\theta / \mathrm{rad}$' offset +2
#unset ylabel
#set ytics format ''
#plot folder."21_3.txt" u 3:($1/1000) w l lw 1 t '\footnotesize{$(\theta_1, \omega_1)$}',\
     #folder."21_3.txt" u 4:($2/1000) w l lw 1 t '\footnotesize{$(\theta_2, \omega_2)$}',\
