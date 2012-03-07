# check the spar cap height
set term wxt 0 title 'spar cap height'
set xlabel 'spar station # (-)'
set ylabel 'spar cap height (m)'
plot "biplane_spar_layup_20120306.txt" using 1:6 title 'biplane' with linespoints, "monoplane_spar_layup.txt" using 1:6 title 'monoplane' with linespoints

# check the root buildup height
set term wxt 1 title 'root buildup height'
set xlabel 'spar station # (-)'
set ylabel 'root buildup height (m)'
plot "biplane_spar_layup_20120306.txt" using 1:8 title 'biplane' with linespoints, "monoplane_spar_layup.txt" using 1:8 title 'monoplane' with linespoints

# check the shear web height
set term wxt 2 title 'shear web height'
set xlabel 'spar station # (-)'
set ylabel 'shear web height (m)'
plot "biplane_spar_layup_20120306.txt" using 1:10 title 'biplane' with linespoints, "monoplane_spar_layup.txt" using 1:10 title 'monoplane' with linespoints

# check edgewise spar profile
set term wxt 3 title 'edgewise spar profile'
set xlabel 'x1 (m)'
set ylabel 'x3 (m)'
set yrange [-15:15]
set size ratio -1
plot "biplane_spar_layup_20120306.txt" using 2:20 with linespoints notitle, "biplane_spar_layup_20120306.txt" using 2:(-1*$20) with linespoints notitle