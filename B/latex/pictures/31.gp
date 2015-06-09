folder = "pictures/data/"
set xlabel 'time $t$'
set ylabel 'workload $\sin \left(\Delta\theta \right)$'

#set multiplot

#set title '\textbf{(a)}'

#set key invert
#set key reverse Left
#set key top left
set rmargin scr 0.90
set lmargin scr 0.10

#set xrange [0:30]
set yrange [-1:0.0]
set key above reverse Left

dt = 0.001
every = 100

plot folder."phases_ring.txt" u ($0*dt*every):1 w l lw 2 t '\footnotesize \textbf{(a)} original ring',\
     folder."phases_same.txt" u ($0*dt*every):1 w l lw 2 t '\footnotesize \textbf{(b)} sink to sink $1 \rightarrow 3$',\
     folder."phases_diag.txt" u ($0*dt*every):1 w p ps 0.4 pt 6  t '\footnotesize \textbf{(c)} source to sink $1 \rightarrow 4$',\

	 
