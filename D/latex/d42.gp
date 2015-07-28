

set multiplot

lborder = 0.1
rborder = 0.95

tborder = 0.98
bborder = 0.05

# oszis
# ################  

unset key

set xtics 0, 64, 256
set xrange [-24:280]
set ytics ('0'  0, '$\pi$' pi, '$2\pi$' 2*pi)
set yrange [-1:8]
set lmargin scr lborder + 0. * (rborder - lborder) / 3.
set rmargin scr lborder + 1. * (rborder - lborder) / 3.

set tmargin scr bborder + 3. * (tborder - bborder) / 3.
set bmargin scr bborder + 2. * (tborder - bborder) / 3.


set xtics format ''
set ylabel '\textbf{(a)} $\quad\theta(x)$'
set title '$t = 0$'
plot "data/oszis0.txt" lc 1


set lmargin scr lborder + 1. * (rborder - lborder) / 3.
set rmargin scr lborder + 2. * (rborder - lborder) / 3.

set ytics ('' 0, '' pi, '' 2*pi)

set title '$t = 40$'
set ylabel ''
plot "data/oszis2.txt" lc 2

set lmargin scr lborder + 2. * (rborder - lborder) / 3.
set rmargin scr lborder + 3. * (rborder - lborder) / 3.

set title '$t = 80$'
set ylabel ''
plot "data/oszis4.txt" lc 3

# lpc
# ############
reset

unset key
set xtics format ''
set tmargin scr bborder + 2. * (tborder - bborder) / 3.
set bmargin scr bborder + 1. * (tborder - bborder) / 3.

set xtics 0, 64, 256
set xrange [-24:280]
#set ytics 0,1,7
set yrange [0:1]
set lmargin scr lborder + 0. * (rborder - lborder) / 3.
set rmargin scr lborder + 1. * (rborder - lborder) / 3.


set ylabel '\textbf{(b)} $\quad R(x)$'
plot "data/lpc0.txt" lc 1

set ytics format ''

set lmargin scr lborder + 1. * (rborder - lborder) / 3.
set rmargin scr lborder + 2. * (rborder - lborder) / 3.

set ylabel ''
plot "data/lpc2.txt" lc 2

set lmargin scr lborder + 2. * (rborder - lborder) / 3.
set rmargin scr lborder + 3. * (rborder - lborder) / 3.

set ylabel ''
plot "data/lpc4.txt" lc 3

# lap
# ############
reset

unset key
set ytics ('0'  0, '$\pi$' pi, '$2\pi$' 2*pi)
set yrange [-1:8]

set tmargin scr bborder + 1. * (tborder - bborder) / 3.
set bmargin scr bborder + 0. * (tborder - bborder) / 3.

set xtics 0, 64, 256
set xrange [-24:280]
#set ytics 0,1,7
#set yrange [0:1]
set lmargin scr lborder + 0. * (rborder - lborder) / 3.
set rmargin scr lborder + 1. * (rborder - lborder) / 3.


set ylabel '\textbf{(c)} $\quad\Theta(x)$'
plot "data/lap0.txt" lc 1

set ytics ('' 0, '' pi, '' 2*pi)

set lmargin scr lborder + 1. * (rborder - lborder) / 3.
set rmargin scr lborder + 2. * (rborder - lborder) / 3.

set xlabel 'Oscillators $x$'
set ylabel ''
plot "data/lap2.txt" lc 2

set lmargin scr lborder + 2. * (rborder - lborder) / 3.
set rmargin scr lborder + 3. * (rborder - lborder) / 3.

set xlabel ''
set ylabel ''
plot "data/lap4.txt" lc 3



