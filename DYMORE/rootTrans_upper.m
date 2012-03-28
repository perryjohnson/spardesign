% this script plots the upper root transition of the biplane blade as a NURBS curve,
% then calculates the curvature and radius of curvature at several test points along the curve
%
% the curvature should be smallest near the middle of the curve
% (and the radius of curvature should be largest near the middle of the curve)
%
% Author: Perry Johnson
% Date:   March 27, 2012

clear all;
% close all;
clc;

addpath '.\nurbs-1.3.6\inst' -BEGIN;

% weights
w = [1.0 0.7 0.3 1.0];

% control points
cntrl = [w(1)*9.0  w(2)*13.9  w(3)*13.9    w(4)*17.1;      % upper root transition
         w(1)*0.0  w(2)* 0.0  w(3)* 3.815  w(4)* 3.815;
         w(1)*0.0  w(2)* 0.0  w(3)* 0.0    w(4)* 0.0;
         w(1)      w(2)       w(3)         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
crv = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(crv, 50);
hold on;
title('upper root transition');

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.-');

% make 9 test points along the NURBS curve, spread between eta=0.0 and eta=1.0
% tt = linspace(0.0,1.0,9);

% make 5 test points along the NURBS curve, at each of the beam element end nodes
tt = [0.0 0.395062 0.604938 0.802469 1.0];

% make 13 test points along the NURBS curve, at each of the cubic beam element nodes
% elem1 = linspace(0.0, 0.395062, 4);
% elem2 = linspace(0.395062, 0.604938, 4);
% elem3 = linspace(0.604938, 0.802469, 4);
% elem4 = linspace(0.802465, 1.0, 4);
% tt = horzcat(elem1, elem2(2:end), elem3(2:end), elem4(2:end));

% create the NURBS representation of the 1st and 2nd derivatives
[dcrv, dcrv2] = nrbderiv(crv);

% evaluate the 1st and 2nd derivatives of the NURBS curve at each of the test points
[p1, dp, d2p] = nrbdeval(crv, dcrv, dcrv2, tt);

% normalize the tangent vectors along the NURBS curve
p2 = vecnorm(dp);
p2_d2p = vecnorm(d2p);

% plot the tangent vectors along the NURBS curve
plot(p1(1,:),p1(2,:),'ro');
h = quiver(p1(1,:), p1(2,:), p2(1,:), p2(2,:), 0);
set(h,'Color','black');
% plot the second derivative vectors along the NURBS curve
% g = quiver(p1(1,:), p1(2,:), p2_d2p(1,:), p2_d2p(2,:), 0);
% set(g,'Color','red');
hold off;

% curvature = mag( dp x d2p ) / (mag( dp ))^3
numerator = vecmag( veccross(dp, d2p) );
denominator = (vecmag(dp) ).^3;
curvature = numerator ./ denominator
radius_of_curvature = 1.0./curvature