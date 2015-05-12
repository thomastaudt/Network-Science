#set terminal pdfcairo enhanced dashed 
#set termoption dash

set size ratio 0.5

folder = "data/"

set xrange [0.5:9000]
set key left bottom
#set xtics (1 "10^{0}", 10 "10^{1}", 100 "10^{2}", 1000 "10^{3}")
#set ytics -8,1,0
set yrange [2e-9:2]

set logscale xy
#set format x '10^{%T}'
set mxtics 10
set grid
set format y '$10^{%T}$'
set xlabel 'Degree $k$'
set ylabel '$P(k)$'
#set format y '10^{%.0M}'
#set ytics ("10^{0}" 1, "" 1e-1, "10^{-2}" 1e-2, "" 1e-3, "10^{-4}" 1e-4, "" 1e-5, "10^{-6}" 1e-6, "" 1e-7, "10^{-8}" 1e-8)

#set mytics 10
#set key reverse
#set key invert
#set key reverse Left
#set output 'scale1.pdf'
#plot folder . "ba_m1_n500k.dat" pt 7 ps 0.3 lc rgb "#aa0a00" t '{/Ubuntu-Italic m =}{/Ubuntu  1 }' ,\
         #0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''

#set output 'scale2.pdf'
#plot folder . "ba_m1_n500k.dat" pt 7 ps 0.3 lc rgb "#aa0a00" t '{/Ubuntu-Italic m =}{/Ubuntu  1 }' ,\
     #folder . "ba_m5_n500k.dat" pt 7 ps 0.3 lc rgb "#194bc1" t '{/Ubuntu-Italic m =}{/Ubuntu  5}' ,\
         #0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''

#set output 'scale3.pdf'
plot folder . "ba_m1_n500k.dat" pt 7 ps 0.3 lc rgb "#aa0a00" t '{/Ubuntu-Italic m =}{/Ubuntu  1 }' ,\
     folder . "ba_m5_n500k.dat" pt 7 ps 0.3 lc rgb "#194bc1" t '{/Ubuntu-Italic m =}{/Ubuntu  5}' ,\
     folder . "ba_m20_n500k.dat" pt 7 ps 0.3 lc rgb "#00a12b" t '{/Ubuntu-Italic m =}{/Ubuntu  20}' ,\
         0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''
#set output 'scale3_mono.pdf'
#plot folder . "ba_m1_n500k.dat" pt 1 ps 0.5 lc rgb "#aa0a00" t '{/Ubuntu-Italic m =}{/Ubuntu  1 }' ,\
     #folder . "ba_m5_n500k.dat" pt 4 ps 0.5 lc rgb "#194bc1" t '{/Ubuntu-Italic m =}{/Ubuntu  5}' ,\
     #folder . "ba_m20_n500k.dat" pt 6 ps 0.5 lc rgb "#00a12b" t '{/Ubuntu-Italic m =}{/Ubuntu  20}' ,\
         #0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''

#set output 'log_bin.pdf'
#plot folder . "ba_logbin_m1_n500k.dat" pt 7 ps 0.3 lc rgb "#aa0a00" t '{/Ubuntu-Italic m =}{/Ubuntu  1 }' ,\
     #folder . "ba_logbin_m5_n500k.dat" pt 7 ps 0.3 lc rgb "#194bc1" t '{/Ubuntu-Italic m =}{/Ubuntu  5}' ,\
     #folder . "ba_logbin_m20_n500k.dat" pt 7 ps 0.3 lc rgb "#00a12b" t '{/Ubuntu-Italic m =}{/Ubuntu  20}' ,\
         #0.5*x**(-3) lw 1 lt 2 lc rgb "#666666" t ''


