

folder = 'pictures/data/'


set multiplot

set tmargin scr 0.90
set bmargin scr 0.15
set lmargin scr 0.10
set rmargin scr 0.50

set title '\textbf{(a)} Erdös-Renyi'
set xlabel 'coupling strength $\sigma$'
set ylabel '$r$'
set key bottom
set key spacing 1.2
set xrange [-0.01:0.21]
set yrange [0:1.5]

#g_erd1: <k> = 9.887733333333335, <k²> = 106.62093333333333, σ_c = 0.14798725768678045
#g_erd3: <k> = 29.70253333333333, <k²> = 903.196, σ_c = 0.05247851576711839
#g_erd3: <k> = 49.47193333333332, <k²> = 2472.1653333333334, σ_c = 0.0319338607879532

set key top right Left 
set key spacing 0.75

set arrow 1 from 0.147987,graph 0 to 0.147987,graph 1 lt -1 lw 2.5 lc rgb "#38aa38" nohead
set arrow 2 from 0.052478,graph 0 to 0.052478,graph 1 lt -1 lw 2.5 lc rgb "#2929bb" nohead
set arrow 3 from 0.031933,graph 0 to 0.031933,graph 1 lt -1 lw 2.5 lc rgb "#bb3333" nohead

set label 3 '\textcolor{OliveGreen}{\footnotesize $p=0.1$}' at 0.175,1.4 center
set label 2 '\textcolor{Blue}{\footnotesize $p=0.3$}' at 0.175,1.3 center
set label 1 '\textcolor{Red}{\footnotesize $p=0.5$}' at 0.175,1.2 center
a = 1.05
plot folder.'11_erd1.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#006600" t '',\
     folder.'11_erd1.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#77ee77" t '',\
     folder.'11_erd3.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#000066" t '',\
     folder.'11_erd3.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#6666ff" t '',\
     folder.'11_erd5.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#660000" t '',\
     folder.'11_erd5.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#ff5555" t ''


set title '\textbf{(b)} Scale-Free'
set lmargin scr 0.55
set ytics format ''
set ylabel ''
set rmargin scr 0.95

set arrow 1 from 0.109991,graph 0 to 0.109991,graph 1 lt -1 lw 2.5 lc rgb "#38aa38" nohead
set arrow 2 from 0.064900,graph 0 to 0.064900,graph 1 lt -1 lw 2.5 lc rgb "#2929bb" nohead
set arrow 3 from 0.047713,graph 0 to 0.047713,graph 1 lt -1 lw 2.5 lc rgb "#bb3333" nohead

set label 3 '\textcolor{OliveGreen}{\footnotesize $m=5~\,$}' at 0.16,1.4 center
set label 2 '\textcolor{Blue}{\footnotesize $m=10$}' at 0.16,1.3 center
set label 1 '\textcolor{Red}{\footnotesize $m=15$}' at 0.16,1.2 center

plot folder.'11_ba5.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#006600" t '',\
     folder.'11_ba5.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#77ee77" t '',\
     folder.'11_ba10.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#000066" t '',\
     folder.'11_ba10.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#6666ff" t '',\
     folder.'11_ba15.txt' u 1:2 w p pt 7 ps a*1.55 lc rgb "#660000" t '',\
     folder.'11_ba15.txt' u 1:2 w p pt 7 ps a*1.00 lc rgb "#ff5555" t ''
