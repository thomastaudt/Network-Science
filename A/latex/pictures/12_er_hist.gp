
folder = 'pictures/data/'

set ylabel 'Degree distribution $P(k)$'
set xlabel 'Degree $k$'
set xrange [-0.02:0.35]
set yrange [0:100]
set key spacing 1.25
set multiplot 

set bmargin scr 0.1
set tmargin scr 0.90

set lmargin scr 0.1
set rmargin scr 0.50
set title '\textbf{a)}'
plot folder . 'er_hist_N=350_p=0.01.dat' u 3:4 w lp pt 7 t '\fs{$p=0.01$}', \
     folder . 'er_hist_N=350_p=0.05.dat' u 3:4 w lp pt 7 t '\fs{$p=0.05$}', \
     folder . 'er_hist_N=350_p=0.25.dat' u 3:4 w lp pt 7 t '\fs{$p=0.25$}', \

unset ylabel
set ytics format ''

set lmargin scr 0.55
set rmargin scr 0.95
set xrange [0:2]

set title '\textbf{b)}'
plot folder . 'er_hist_N=50_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=50$}', \
     folder . 'er_hist_N=100_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=100$}', \
     folder . 'er_hist_N=500_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=500$}', \
