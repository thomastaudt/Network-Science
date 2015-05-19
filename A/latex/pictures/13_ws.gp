
folder = 'pictures/data/'

set xlabel 'Rewire probability $p$'
set ylabel 'Ratio $L(p)/L(0)$ and $C(p)/C(0)$'
#set xrange [-0.02:0.35]
#set yrange [0:100]
#set key spacing 1.25
set multiplot 

set bmargin scr 0.1
set tmargin scr 0.90

set lmargin scr 0.1
set rmargin scr 0.50
set title '\textbf{a)}'
set xrange [1e-4:1]
set logscale x
set yrange [0:1.2]
set format x "$10^{%T}$"
logs(x) = 10**((x - 1)/24 * 4 - 4)
plot folder . 'small_world_strogatz_k=5_N=500.dat' u (logs($0)):($1/0.5) w lp pt 7 t '\fs{$C(p)$}', \
    folder . 'small_world_strogatz_k=5_N=500.dat' u (logs($0)):($2/62.875) w lp pt 7 t '\fs{$L(p)$}', \
          

#unset ylabel
#set ytics format ''

#set lmargin scr 0.55
#set rmargin scr 0.95
#set xrange [0:2]

#set xlabel '$k/ (p(N-1))$'
#set title '\textbf{b)}'
#plot folder . 'er_hist_N=50_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=50$}', \
     #folder . 'er_hist_N=100_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=100$}', \
     #folder . 'er_hist_N=500_p=0.1.dat' u 3:4 w lp pt 7 t '\fs{$n=500$}', \
