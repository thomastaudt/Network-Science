set key top left Left reverse
set ylabel 'Arrival Time $T_A/\si{d}$'
set xrange [-5:25]
set yrange [-10:130]

set xtics 0, 5, 20

set multiplot

set title '\textbf{(a)}'
set xlabel ' '
set lmargin screen 0.12; set rmargin screen 0.40;
plot "data/arrival_distance_Indonesia.txt"  lc 1  pt 7 ps 1.00 t '\footnotesize Indonesia'

unset ylabel
set ytics ''

set title '\textbf{(b)}'
set xlabel 'Effective Path Length'
set lmargin screen 0.40; set rmargin screen 0.68;
plot "data/arrival_distance_Peru.txt"    lc 2    pt 7 ps 1.00 t '\footnotesize Peru'

set title '\textbf{(c)}'
set xlabel ' '
set lmargin screen 0.68; set rmargin screen 0.96;
plot "data/arrival_distance_SouthAfrica.txt" lc 3 pt 7 ps 1.00 t '\footnotesize South Africa'

unset multiplot
