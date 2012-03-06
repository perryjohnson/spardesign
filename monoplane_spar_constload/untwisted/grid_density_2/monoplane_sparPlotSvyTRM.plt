

 ############
 # Title: [svy_disp_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_spar.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_spar.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_spar.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [svy_disp_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_spar.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_spar.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_spar.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [svy_force_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_spar.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_spar.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_spar.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [svy_force_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_spar.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_spar.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_spar.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [svy_strain_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_spar.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_spar.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_spar.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [svy_strain_spar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_spar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_spar.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_spar.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_spar.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 pause -1 "Hit return to continue";