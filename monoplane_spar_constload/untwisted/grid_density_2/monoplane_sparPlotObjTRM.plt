

 ############
 # Title: [scheduleload]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "scheduleload";
 set xlabel "TIME [sec]";
 set autoscale x;
 set ylabel "TIME FUNCTION";
 set autoscale y;
 plot '.\FIGURES\scheduleload.mdt' using 1:2 title "History" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [curveSpar]
 ############
 reset
 set size ratio  1;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveSpar";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  9.19000e+001];
 set ylabel "X2 [m]";
 set yrange [-4.59500e+001 :  4.59500e+001];
 plot '.\FIGURES\curveSpar.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [curveSpar]
 ############
 reset
 set size ratio  1;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveSpar";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  9.19000e+001];
 set ylabel "X3 [m]";
 set yrange [-4.59500e+001 :  4.59500e+001];
 plot '.\FIGURES\curveSpar.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [curveSpar]
 ############
 reset
 set size ratio  1;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveSpar";
 set xlabel "X2 [m]";
 set xrange [-4.59500e+001 :  4.59500e+001];
 set ylabel "X3 [m]";
 set yrange [-4.59500e+001 :  4.59500e+001];
 plot '.\FIGURES\curveSpar.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [orientationSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "orientationSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "TWIST ANGLE [deg]";
 set autoscale y;
 plot '.\FIGURES\orientationSpar.mdt' using 1:2 title "Phi" with lines linestyle 1 , \
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propSparQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propSparQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propSparQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propSparQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propSparQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propSparQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propSparQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propSparQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propSparQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [propSpar]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propSpar";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propSparQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";

 ############
 # Title: [constloaddistTable]
 ############
 reset
 set size ratio 0.75;
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "constloaddistTable";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISTRIBUTED FORCE ALONG i3 [N/m]";
 set autoscale y;
 plot '.\FIGURES\constloaddistTable.mdt' using 1:2 title "Fi3" with lines linestyle 1 ;
 set nomultiplot;
 pause -1 "Hit return to continue";