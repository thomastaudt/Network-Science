
folder = 'pictures/data/'

set bmargin scr 0.1
set tmargin scr 0.90

set ylabel 'cluster size'
set xlabel '$(p-p_c)\times 10^3$'

set key left spacing 1.25

set multiplot 
#set yrange [0:1.05]
#set xrange [-0.1:2]
set lmargin scr 0.1
set rmargin scr 0.49
set title '\textbf{a)}'
#set arrow from graph 0.5,0 to graph 0.5,1 nohead lt -1 lc rgb "#777777"
set logscale xy

pc = 0.0040

#set style arrow 8 heads size screen 0.008,90 ls 3 lc rgb "black"
g1 = 0.7*1e-3
g2 = 3.2*1e-3
set style rect fc lt -1 fs solid 0.10  lw 0.5 lc rgb "#444444"
set obj 1 rect from g1*1e3,graph 0 to g2*1e3,graph 1 behind
#Fitting procedure
f(x) = a*x + b

clipper(x) = x > g1 && x < g2 ? x : 1/0
fit f(x) folder.'31_infty.dat' u (log10(clipper($1-pc))):(log10($3)) via a,b

#set xrange [2e-4:1]
set yrange [30:400]
set ytics (50, 100, 200, 300, 400)

#set label sprintf("%.3f", a) at 0.01,400
set label 1 sprintf('\fs{$\beta \approx %.3f$}', a) at graph 0.1,graph 0.5

set key at graph 0.01, 0.925
set key reverse Left
set xrange [0.007:20]
plot folder.'31_infty.dat' u (($1-pc)*1e3):3 w lp pt 7 ps 0.5 t '\fs{$\mathrm{max}_C$}', \
     10**b * (x/1e3)**a t '\fs{$\sim(p-p_c)^\beta$}' lt -1 lc rgb "#666666"

reset

set bmargin scr 0.1
set tmargin scr 0.90
set logscale xy
set key reverse Left
set title '\textbf{b)}'
pc = 0.0040
#set key right
#unset ylabel
##set yrange [0:100]


g1 = 1e-3
g2 = 8.5e-3
set style rect fc lt -1 fs solid 0.10  lw 0.5 lc rgb "#444444"
set obj 1 rect from g1*1e3,graph 0 to g2*1e3,graph 1 behind


#f(x) = a*x + b

clipper(x) = x > g1 && x < g2 ? x : 1/0
fit f(x) folder.'31_infty.dat' u (log10(clipper($1-pc))):(log10($6)) via a,b

set lmargin scr 0.56
set rmargin scr 0.95
set yrange [1e-5:100]
set format y '\fs{$10^{%T}$}'
set ytics offset 0.65
#set xrange [2e-3:1]
##set yrange [100:450]
#set yrange [0.01:150]
#set ytics (0.1, 1, 10, 100)
#set key at 0.0018, 0.016
#set key reverse Left

set key reverse Left
set key at graph 0.55, 0.25

set label 1 sprintf('\fs{$\gamma \approx %.3f$}', a) at graph 0.1,graph 0.5
plot folder.'31_infty.dat' u (($1-pc)*1e3):($6) w lp pt 7 ps 0.5 t '\fs{$\langle s\rangle^\mathrm{f}$}', \
     10**b * (x/1e3)**a t '\fs{$\sim(p-p_c)^\gamma$}' lt -1 lc rgb "#666666"


###set autoscale xy
###set logscale xy
##plot 10**b * x**a
##plot folder . '31_2d.dat' u 1:4 w lp pt 7 ps 0.5 t '$\mathrm{max}_C^\mathrm{f}$', \
     ##folder . '31_2d.dat' u 1:6 w lp pt 7 ps 0.5 t '$\langle s\rangle^\mathrm{f}$', \
     ###folder . '31_2d.dat' u 1:($7) w lp pt 7 ps 0.3 t '$\langle s\rangle^\mathrm{f}$', \
