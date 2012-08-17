clear all;
clc;

addpath '.\nurbs-1.3.6\inst' -BEGIN;

pnts = zeros(4,5,5);
pnts(:,:,1) = [ -100 -100 -100 -100 -100;
    -100  -50 0 50 100;
    0 0 0 0 0;
    1 1 1 1 1];
pnts(:,:,2) = [ -50 -50 -50 -50 -50; % b2,4
    -100 -50 0 50 100;
    0 25 50 100 0;
    1 1 1 1 1];

pnts(:,:,3) = [0 0 0 0 0;
    -100 -50 0 50 100;
    0 25 50 25 0;
    1 1 1 1 1]; 
    
pnts(:,:,4) = [50 50 50 50 50;
    -100 -50 0 50 100;
    0 25 150 25 0;
    1 1 1 1 1];
    
pnts(:,:,5) = [ 100 100 100 100 100;
    -100 -50 0 50 100;
    0 0 0 0 0;
    1 1 1 1 1];

 knots{1} = [0 0 0 1/3 2/3 1 1 1];
 knots{2} = [0 0 0 1/3 2/3 1 1 1];

 srf = nrbmak(pnts,knots);
 nrbplot(srf,[20 20]);hold on;
 title('NURBS surface');
 
 % create plot for the control points
 for i = 1:5
        % U direction
        plot3([pnts(1,1,i) pnts(1,2,i) pnts(1,3,i) pnts(1,4,i) pnts(1,5,i)],[pnts(2,1,i) pnts(2,2,i) pnts(2,3,i) pnts(2,4,i) pnts(2,5,i)],[pnts(3,1,i) pnts(3,2,i) pnts(3,3,i) pnts(3,4,i) pnts(3,5,i)],'b.-');
        % V direction
        plot3([pnts(1,i,1) pnts(1,i,2) pnts(1,i,3) pnts(1,i,4) pnts(1,i,5)],[pnts(2,i,1) pnts(2,i,2) pnts(2,i,3) pnts(2,i,4) pnts(2,i,5)],[pnts(3,i,1) pnts(3,i,2) pnts(3,i,3) pnts(3,i,4) pnts(3,i,5)],'r.-');
 end
 
 axis([-100 100 -100 100 0 200])
 
 hold off;
