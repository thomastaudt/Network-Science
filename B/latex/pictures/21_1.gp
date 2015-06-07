folder = "pictures/data/"
set xlabel 'time $t$'
set ylabel 'phase $\theta/\mathrm{rad}$'
#set y2label 'power $p$'
set yrange [-0.2:0.3]
#set y2range [-2:2]
#set y2tics

set multiplot

set title '\textbf{(a)}'

set key invert
set rmargin scr 0.51
set lmargin scr 0.10
plot folder."21_1.txt" u ($0*0.01):1 w l lw 1 t '\footnotesize{$\theta_1$}',\
     folder."21_1.txt" u ($0*0.01):2 w l t '\footnotesize{$\theta_2$}',\
     folder."21_1.txt" u ($0*0.01):($1-$2) w l lw 1.5 t '\footnotesize{$\theta_1 - \theta_2$}'

reset
set title '\textbf{(b)}'
set xrange [-0.3:0.3]
set yrange [-0.2:0.3]
set xlabel '$\omega / \mathrm{rad} / \mathrm{s}$'
#set ylabel '$\theta / \mathrm{rad}$' offset +2
unset ylabel
set ytics format ''
set lmargin scr 0.58
set rmargin scr 0.99
plot folder."21_1.txt" u 3:1 w l lw 1 t '\footnotesize{$(\theta_1, \omega_1)$}',\
     folder."21_1.txt" u 4:2 w l lw 1 t '\footnotesize{$(\theta_2, \omega_2)$}',\
