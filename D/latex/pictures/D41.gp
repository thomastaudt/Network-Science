

set xlabel '$p$'
set ylabel 'outcome fraction'
set key bottom
set xrange [0.2:0.8]
plot 'pictures/data/fracs.dat' u ((($0/133.)*0.8)+0.2):2 w lp pt 7 t '\enquote{Paradies}',\
     'pictures/data/fracs.dat' u ((($0/133.)*0.8)+0.2):1 w lp pt 7 t '\enquote{Love}'
