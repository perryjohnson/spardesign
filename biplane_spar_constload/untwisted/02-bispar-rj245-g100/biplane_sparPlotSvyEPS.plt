

 ############
 # Title: [surveyAB]
 ############
 reset
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyABQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyABQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyBCQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyBCQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyBGQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyBGQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyCDQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyCDQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyGHQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyGHQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyDEQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyDEQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyHEQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyHEQrotQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyEFQdisQ.eps';
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
 set terminal postscript portrait enhanced color "Times New Roman" 18;
 set size ratio 0.75;
 set output '.\FIGURES\surveyEFQrotQ.eps';
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