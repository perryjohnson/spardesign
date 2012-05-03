

 ############
 # Title: [surveyAB]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyABQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyAB";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyAB.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyAB.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyAB.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyAB]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyABQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyAB";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyAB.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyAB.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyAB.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyBC]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyBCQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyBC";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyBC.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyBC.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyBC.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyBC]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyBCQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyBC";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyBC.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyBC.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyBC.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyBG]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyBGQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyBG";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyBG.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyBG.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyBG.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyBG]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyBGQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyBG";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyBG.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyBG.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyBG.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyCDQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyCD.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyCD.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyCD.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyCD]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyCDQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyCD";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyCD.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyCD.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyCD.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyGHQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyGH.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyGH.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyGH.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyGH]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyGHQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyGH";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyGH.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyGH.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyGH.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyDEQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyDE.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyDE.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyDE.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyDE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyDEQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyDE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyDE.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyDE.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyDE.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyHEQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyHE.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyHE.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyHE.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyHE]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyHEQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyHE";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyHE.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyHE.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyHE.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyEFQdisQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "DISPLACEMENTS [m]";
 set autoscale y;
 plot '.\FIGURES\surveyEF.mdt' using 1:2 title "u_1" with lines linestyle 1 , \
      '.\FIGURES\surveyEF.mdt' using 1:3 title "u_2" with lines linestyle 2 , \
      '.\FIGURES\surveyEF.mdt' using 1:4 title "u_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;

 ############
 # Title: [surveyEF]
 ############
 reset
 set terminal png small size 1000, 750;
 set output '.\FIGURES\surveyEFQrotQ.png';
 set key; set border; set grid; set multiplot;
 set style line  1 lt  1 lw 3.0 pt  1 ps 1.5;
 set style line  2 lt  2 lw 3.0 pt  2 ps 1.5;
 set style line  3 lt  3 lw 3.0 pt  3 ps 1.5;
 set title "surveyEF";
 set xlabel "ETA";
 set autoscale x;
 set ylabel "ROTATIONS";
 set autoscale y;
 plot '.\FIGURES\surveyEF.mdt' using 1:5 title "R_1" with lines linestyle 1 , \
      '.\FIGURES\surveyEF.mdt' using 1:6 title "R_2" with lines linestyle 2 , \
      '.\FIGURES\surveyEF.mdt' using 1:7 title "R_3" with lines linestyle 3 ;
 set nomultiplot;
 set output;