

 ############
 # Title: [svy_disp_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_CDQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_CD.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_CD.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_CD.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_CDQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_CD.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_CD.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_CD.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_CDQforQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_CD.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_CD.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_CD.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_CDQmomQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_CD.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_CD.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_CD.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_CDQstrQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_CD.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_CD.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_CD.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_CD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_CDQkapQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_CD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_CD.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_CD.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_CD.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_GHQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_GH.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_GH.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_GH.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_GHQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_GH.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_GH.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_GH.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_GHQforQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_GH.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_GH.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_GH.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_GHQmomQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_GH.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_GH.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_GH.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_GHQstrQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_GH.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_GH.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_GH.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_GH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_GHQkapQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_GH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_GH.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_GH.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_GH.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_DEQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_DE.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_DE.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_DE.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_DEQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_DE.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_DE.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_DE.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_DEQforQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_DE.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_DE.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_DE.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_DEQmomQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_DE.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_DE.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_DE.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_DEQstrQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_DE.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_DE.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_DE.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_DE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_DEQkapQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_DE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_DE.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_DE.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_DE.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_HEQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_HE.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_HE.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_HE.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_HEQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_HE.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_HE.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_HE.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_HEQforQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_HE.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_HE.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_HE.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_HEQmomQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_HE.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_HE.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_HE.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_HEQstrQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_HE.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_HE.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_HE.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_HE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_HEQkapQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_HE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_HE.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_HE.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_HE.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_EFQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\svy_disp_EF.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_EF.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_EF.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_disp_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_disp_EFQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_disp_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\svy_disp_EF.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\svy_disp_EF.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\svy_disp_EF.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_EFQforQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "FORCE [N]";
 set autoscale y;
 plot '.\FIGURES\svy_force_EF.mdt' using 1:2 title "F_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_EF.mdt' using 1:3 title "F_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_EF.mdt' using 1:4 title "F_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_force_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_force_EFQmomQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_force_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT [N.m]";
 set autoscale y;
 plot '.\FIGURES\svy_force_EF.mdt' using 1:5 title "M_1" with lines linestyle 1 , \
      '.\FIGURES\svy_force_EF.mdt' using 1:6 title "M_2" with lines linestyle 2 , \
      '.\FIGURES\svy_force_EF.mdt' using 1:7 title "M_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_EFQstrQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STRAINS";
 set autoscale y;
 plot '.\FIGURES\svy_strain_EF.mdt' using 1:2 title "E_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_EF.mdt' using 1:3 title "E_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_EF.mdt' using 1:4 title "E_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [svy_strain_EF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\svy_strain_EFQkapQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "svy_strain_EF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "CURVATURES [1/m]";
 set autoscale y;
 plot '.\FIGURES\svy_strain_EF.mdt' using 1:5 title "K_1" with lines linestyle 1 , \
      '.\FIGURES\svy_strain_EF.mdt' using 1:6 title "K_2" with lines linestyle 2 , \
      '.\FIGURES\svy_strain_EF.mdt' using 1:7 title "K_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;