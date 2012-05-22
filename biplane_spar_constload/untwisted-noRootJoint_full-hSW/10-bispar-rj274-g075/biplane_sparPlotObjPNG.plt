

 ############
 # Title: [scheduleload]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\scheduleload.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "scheduleload";
 set xlabel "TIME [sec]";
 set autoscale x;
 set ylabel "TIME FUNCTION";
 set autoscale y;
 plot '.\FIGURES\scheduleload.mdt' using 1:2 title "History" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [constloaddistTable]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\constloaddistTable.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "constloaddistTable";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISTRIBUTED FORCE ALONG i3 [N/m]";
 set autoscale y;
 plot '.\FIGURES\constloaddistTable.mdt' using 1:2 title "Fi3" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [OriDist]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\OriDist.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "OriDist";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "TWIST ANGLE [deg]";
 set autoscale y;
 plot '.\FIGURES\OriDist.mdt' using 1:2 title "Phi" with lines linestyle 1 , \
 set nomultiplot;
 set output;

 ############
 # Title: [curveCD]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveCDQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveCD";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  1.98000e+001];
 set ylabel "X2 [m]";
 set yrange [-9.90000e+000 :  9.90000e+000];
 plot '.\FIGURES\curveCD.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveCD]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveCDQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveCD";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  1.98000e+001];
 set ylabel "X3 [m]";
 set yrange [-7.03900e+000 :  1.27610e+001];
 plot '.\FIGURES\curveCD.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveCD]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveCDQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveCD";
 set xlabel "X2 [m]";
 set xrange [-9.90000e+000 :  9.90000e+000];
 set ylabel "X3 [m]";
 set yrange [-7.03900e+000 :  1.27610e+001];
 plot '.\FIGURES\curveCD.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveGH]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveGHQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveGH";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  1.98000e+001];
 set ylabel "X2 [m]";
 set yrange [-9.90000e+000 :  9.90000e+000];
 plot '.\FIGURES\curveGH.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveGH]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveGHQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveGH";
 set xlabel "X1 [m]";
 set xrange [ 0.00000e+000 :  1.98000e+001];
 set ylabel "X3 [m]";
 set yrange [-1.27610e+001 :  7.03900e+000];
 plot '.\FIGURES\curveGH.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveGH]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveGHQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveGH";
 set xlabel "X2 [m]";
 set xrange [-9.90000e+000 :  9.90000e+000];
 set ylabel "X3 [m]";
 set yrange [-1.27610e+001 :  7.03900e+000];
 plot '.\FIGURES\curveGH.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveEF]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveEFQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveEF";
 set xlabel "X1 [m]";
 set xrange [ 2.52000e+001 :  9.19000e+001];
 set ylabel "X2 [m]";
 set yrange [-3.33500e+001 :  3.33500e+001];
 plot '.\FIGURES\curveEF.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveEF]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveEFQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveEF";
 set xlabel "X1 [m]";
 set xrange [ 2.52000e+001 :  9.19000e+001];
 set ylabel "X3 [m]";
 set yrange [-3.33500e+001 :  3.33500e+001];
 plot '.\FIGURES\curveEF.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveEF]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveEFQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveEF";
 set xlabel "X2 [m]";
 set xrange [-3.33500e+001 :  3.33500e+001];
 set ylabel "X3 [m]";
 set yrange [-3.33500e+001 :  3.33500e+001];
 plot '.\FIGURES\curveEF.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [CurveSquare]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\CurveSquareQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "CurveSquare";
 set xlabel "X1 [m]";
 set xrange [-5.00000e-001 :  5.00000e-001];
 set ylabel "X2 [m]";
 set yrange [-5.00000e-001 :  5.00000e-001];
 plot '.\FIGURES\CurveSquare.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [CurveSquare]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\CurveSquareQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "CurveSquare";
 set xlabel "X1 [m]";
 set xrange [-5.00000e-001 :  5.00000e-001];
 set ylabel "X3 [m]";
 set yrange [-5.00000e-001 :  5.00000e-001];
 plot '.\FIGURES\CurveSquare.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [CurveSquare]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\CurveSquareQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "CurveSquare";
 set xlabel "X2 [m]";
 set xrange [-5.00000e-001 :  5.00000e-001];
 set ylabel "X3 [m]";
 set yrange [-5.00000e-001 :  5.00000e-001];
 plot '.\FIGURES\CurveSquare.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm00Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propCDQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm02Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propCDQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm03Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propCDQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propCDQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propCDQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQm22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propCDQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk11Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk12Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk13Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propCDQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk14Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk24Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk34Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk44Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk15Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk25Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk35Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk45Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk55Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk16Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk26Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk36Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propCDQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk46Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk56Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQk66Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propCDQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propCDQmucQ.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propCDQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm00Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propGHQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm02Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propGHQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm03Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propGHQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propGHQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propGHQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQm22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propGHQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk11Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk12Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk13Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propGHQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk14Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk24Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk34Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk44Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk15Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk25Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk35Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk45Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk55Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk16Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk26Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk36Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propGHQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk46Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk56Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQk66Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propGHQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propGHQmucQ.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propGHQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveDE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveDEQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveDE";
 set xlabel "X1 [m]";
 set xrange [ 1.98000e+001 :  2.52000e+001];
 set ylabel "X2 [m]";
 set yrange [-2.70000e+000 :  2.70000e+000];
 plot '.\FIGURES\curveDE.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveDE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveDEQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveDE";
 set xlabel "X1 [m]";
 set xrange [ 1.98000e+001 :  2.52000e+001];
 set ylabel "X3 [m]";
 set yrange [-1.26950e+000 :  4.13050e+000];
 plot '.\FIGURES\curveDE.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveDE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveDEQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveDE";
 set xlabel "X2 [m]";
 set xrange [-2.70000e+000 :  2.70000e+000];
 set ylabel "X3 [m]";
 set yrange [-1.26950e+000 :  4.13050e+000];
 plot '.\FIGURES\curveDE.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm00Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propDEQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm02Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propDEQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm03Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propDEQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propDEQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propDEQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQm22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propDEQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk11Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk12Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk13Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propDEQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk14Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk24Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk34Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk44Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk15Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk25Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk35Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk45Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk55Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk16Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk26Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk36Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propDEQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk46Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk56Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQk66Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propDEQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propDEQmucQ.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propDEQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveHE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveHEQcv1Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveHE";
 set xlabel "X1 [m]";
 set xrange [ 1.98000e+001 :  2.52000e+001];
 set ylabel "X2 [m]";
 set yrange [-2.70000e+000 :  2.70000e+000];
 plot '.\FIGURES\curveHE.mdt' using 1:2 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveHE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveHEQcv2Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveHE";
 set xlabel "X1 [m]";
 set xrange [ 1.98000e+001 :  2.52000e+001];
 set ylabel "X3 [m]";
 set yrange [-4.13050e+000 :  1.26950e+000];
 plot '.\FIGURES\curveHE.mdt' using 1:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [curveHE]
 ############
 reset
 set terminal png small size 1000,1000;
 set output '.\FIGURES\curveHEQcv3Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "curveHE";
 set xlabel "X2 [m]";
 set xrange [-2.70000e+000 :  2.70000e+000];
 set ylabel "X3 [m]";
 set yrange [-4.13050e+000 :  1.26950e+000];
 plot '.\FIGURES\curveHE.mdt' using 2:3 title "Curve" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm00Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propHEQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm02Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propHEQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm03Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propHEQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propHEQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propHEQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQm22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propHEQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk11Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk12Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk13Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propHEQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk14Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk24Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk34Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk44Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk15Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk25Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk35Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk45Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk55Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk16Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk26Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk36Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propHEQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk46Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk56Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQk66Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propHEQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propHEQmucQ.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propHEQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm00Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN M00 [kg/m]";
 set autoscale y;
 plot '.\FIGURES\propEFQm00Q.mdt' using 1:2 title "m00" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm02Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM2 [kg]";
 set autoscale y;
 plot '.\FIGURES\propEFQm02Q.mdt' using 1:2 title "m02" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm03Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MASS/SPAN . XM3 [kg]";
 set autoscale y;
 plot '.\FIGURES\propEFQm03Q.mdt' using 1:2 title "m03" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M33 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propEFQm33Q.mdt' using 1:2 title "m33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M23 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propEFQm23Q.mdt' using 1:2 title "m23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQm22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "MOMENT OF INERTIA/SPAN M22 [kg.m^2/m]";
 set autoscale y;
 plot '.\FIGURES\propEFQm22Q.mdt' using 1:2 title "m22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk11Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K11 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk11Q.mdt' using 1:2 title "k11" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk12Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K12 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk12Q.mdt' using 1:2 title "k12" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk22Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K22 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk22Q.mdt' using 1:2 title "k22" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk13Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K13 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk13Q.mdt' using 1:2 title "k13" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk23Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K23 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk23Q.mdt' using 1:2 title "k23" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk33Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K33 [N]";
 set autoscale y;
 plot '.\FIGURES\propEFQk33Q.mdt' using 1:2 title "k33" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk14Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K14 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk14Q.mdt' using 1:2 title "k14" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk24Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K24 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk24Q.mdt' using 1:2 title "k24" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk34Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K34 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk34Q.mdt' using 1:2 title "k34" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk44Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K44 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk44Q.mdt' using 1:2 title "k44" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk15Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K15 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk15Q.mdt' using 1:2 title "k15" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk25Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K25 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk25Q.mdt' using 1:2 title "k25" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk35Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K35 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk35Q.mdt' using 1:2 title "k35" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk45Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K45 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk45Q.mdt' using 1:2 title "k45" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk55Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K55 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk55Q.mdt' using 1:2 title "k55" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk16Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K16 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk16Q.mdt' using 1:2 title "k16" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk26Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K26 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk26Q.mdt' using 1:2 title "k26" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk36Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K36 [N.m]";
 set autoscale y;
 plot '.\FIGURES\propEFQk36Q.mdt' using 1:2 title "k36" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk46Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K46 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk46Q.mdt' using 1:2 title "k46" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk56Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K56 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk56Q.mdt' using 1:2 title "k56" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQk66Q.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "STIFFNESS COEFFICIENT K66 [N.m^2]";
 set autoscale y;
 plot '.\FIGURES\propEFQk66Q.mdt' using 1:2 title "k66" with lines linestyle 1 ;
 set nomultiplot;
 set output;

 ############
 # Title: [propEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\propEFQmucQ.png';
 set key; set border; set grid; set nomultiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set title "propEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DAMPING COEFFICIENT [1/sec]";
 set autoscale y;
 plot '.\FIGURES\propEFQmucQ.mdt' using 1:2 title "muc" with lines linestyle 1 ;
 set nomultiplot;
 set output;