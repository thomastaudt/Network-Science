set key top left
set xlabel 'Effective Path Length'
set ylabel 'Arrival Time $T_A/\si{d}$'
plot "data/arrival_distance_Indonesia.txt" t 'Indonesia', "data/arrival_distance_Peru.txt" t 'Peru', "data/arrival_distance_SouthAfrica.txt" t 'South Africa'