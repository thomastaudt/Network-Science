folder = "pictures/data/"
set xlabel 'time $t$'
set ylabel 'workload $\sin \left(\Delta\theta \right)$'

#set multiplot

set title '\textbf{(a)}'

#set key invert
#set key reverse Left
set key top left
set rmargin scr 0.90
set lmargin scr 0.10

#set xrange [0:30]
set yrange [-1:0]

dt = 0.001
every = 100

plot folder."phases_ring.txt" u ($0*dt*every):1 w l t '\footnotesize original ring',\
     folder."phases_same.txt" u ($0*dt*every):1 w l t '\footnotesize source to source',\
     folder."phases_diag.txt" u ($0*dt*every*5):1  every 5  t'\footnotesize source to sink',\

	 
