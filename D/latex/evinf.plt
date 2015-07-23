set key bottom right
set xlabel 'Infectiousness $\beta$'
set ylabel 'Percentage Infected $q$'
plot "data/everinfected0.05.txt" t '$\gamma = 0.05$', "data/everinfected0.25.txt" t '$\gamma = 0.25$', 'data/everinfected0.5.txt' t '$\gamma = 0.5$', 'data/everinfected0.75.txt' t '$\gamma=0.75$', 'data/everinfected0.95.txt' t '$\gamma = 0.95$'