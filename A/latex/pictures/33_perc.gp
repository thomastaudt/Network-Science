folder = 'pictures/data/'

set ylabel 'largest component size / n'
set xlabel 'added edges / $10^3$'
#set xrange [-]
#set yrange [0:100]
set key spacing 1.25
set key bottom
set multiplot 

set bmargin scr 0.1
set tmargin scr 0.95

set yrange [0:1.05]
set xrange [-0.1:2]
set lmargin scr 0.1
set rmargin scr 0.50
set title '\textbf{a)}'
plot folder . '34_35_pec_transitions.dat' u ($1/1000):($2/250000) w lp pt 7 ps 0.3 t 'Erdös-Renyi', \
     folder . '34_35_pec_transitions.dat' u ($1/1000):($4/250000) w lp pt 7 ps 0.3 t 'product', \
     #folder . 'er_hist_N=350_p=0.25.dat' u 3:4 w lp pt 7 t '$p=0.25$', \

unset ylabel
set ytics format ''

set lmargin scr 0.55
set rmargin scr 0.95
set xrange [-0.1:2]

set title '\textbf{b)}'
plot folder . '34_35_pec_transitions.dat' u ($1/1000):($3/250000) w lp pt 7 ps 0.3 t 'anti-product', \
     folder . '34_35_pec_transitions.dat' u ($1/1000):($5/250000*500) w lp pt 7 ps 0.3 t 'extreme', \
     folder . '34_35_pec_transitions.dat' u ($1/1000):($6/250000*500) w lp pt 7 ps 0.3 t 'anti-Extreme', \
