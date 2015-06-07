folder = "pictures/data/"
set xlabel 'time $t$'
set ylabel 'phase $\theta\times10^{-3}/\mathrm{rad}$'
#set y2label 'power $p$'
#set yrange [-0.15:0.5]
#set y2range [-2:2]
#set y2tics
set key bottom

set multiplot

set title '\textbf{(a)}'

set key invert
set key reverse Left
set key top left
set rmargin scr 0.51
set lmargin scr 0.10
plot folder."21_3.txt" u ($0*0.01):($1/1000) w l lw 1 t '\footnotesize{$\theta_1$}',\
     folder."21_3.txt" u ($0*0.01):($2/1000) w l t '\footnotesize{$\theta_2$}',\
     folder."21_3.txt" u ($0*0.01):(($1-$2)/1000) w l lw 1.5 t '\footnotesize{$\theta_1 - \theta_2$}'

reset
set key top left
set key reverse Left
set title '\textbf{(b)}'
#set yrange [-0.15:0.5]
#set xrange [-0.3:0.3]
#set yrange [-0.2:0.3]
set xlabel '$\omega / \mathrm{rad} / \mathrm{s}$'
#set ylabel '$\theta / \mathrm{rad}$' offset +2
unset ylabel
set ytics format ''
set lmargin scr 0.58
set rmargin scr 0.99
plot folder."21_3.txt" u 3:($1/1000) w l lw 1 t '\footnotesize{$(\theta_1, \omega_1)$}',\
     folder."21_3.txt" u 4:($2/1000) w l lw 1 t '\footnotesize{$(\theta_2, \omega_2)$}',\
