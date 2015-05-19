
folder = 'pictures/data/'

set xlabel 'occupation probability $p$'
set ylabel 'relative largest cluster size'

set xrange [0:0.01]

plot folder . '12_largest.dat' w lp pt 7 t ''
