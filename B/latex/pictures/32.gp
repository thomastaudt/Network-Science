reset

folder = "pictures/data/"
set xlabel '$p \left<k_0\right>$'
set ylabel 'relative size largest cluster $S$'

set multiplot
set key bottom right
set title '\textbf{(a) $k_0=10$}'

#set key invert
#set key reverse Left
#set key reverse top left
set rmargin scr 0.50
set lmargin scr 0.10

set yrange [0:1.1]
set xrange [0:10]

plot folder."N500k10" u ((1-$0/500.0)*10):($1) w l t '\footnotesize $N=500$',\
     folder."N1000k10" u ((1-$0/1000.0)*10):($1) w l t '\footnotesize $N=1000$',\
     folder."N1500k10" u ((1-$0/1500.0)*10):($1) w l t '\footnotesize $n=1500$',\


reset
set title '\textbf{(b) $N=1000$}'

#set arrow from 0,graph 0 to 0, graph 1 nohead lt -1 lw 1.5 lc rgb "#444444" front
#set key invert
set key bottom right

set xrange  [0:10]
set yrange [0:1.1]

set xlabel '$p\left<k_0\right>$'
set lmargin scr 0.59
set rmargin scr 0.99
plot folder."N1000k40" u ((1-$0/1000.0)*40):($1) w l t '\footnotesize $k=40$',\
	 folder."N1000k20" u ((1-$0/1000.0)*20):($1) w l t '\footnotesize $k=20$',\
     folder."N1000k10" u ((1-$0/1000.0)*10):($1) w l t '\footnotesize $k=10$',\
