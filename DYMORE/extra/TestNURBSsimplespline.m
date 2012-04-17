% this is a test script that plots a simple cubic spline as a NURBS curve, then
% calculates the curvature and radius of curvature at nine test points along the curve
%
% the curvature and radius of curvature should be be symmetrical about the midpoint
% the midpoint curvature should be zero, and the midpoint radius of curvature should be infinity
%
% Author: Perry Johnson
% Date:   March 27, 2012

clear all;
% close all;
clc;

addpath '.\nurbs-1.3.6\inst' -BEGIN;

% weights
w = [1.0 1.0 1.0 1.0];

% control points
cntrl = [w(1)*0.0  w(2)*10.0  w(3)*10.0    w(4)*20.0;        % simple cubic spline
         w(1)*0.0  w(2)* 0.0  w(3)* 4.0    w(4)* 4.0;
         w(1)*0.0  w(2)* 0.0  w(3)* 0.0    w(4)* 0.0;
         w(1)      w(2)       w(3)         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
crv = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(crv, 50);
hold on;
title('NURBS simple cubic spline');

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.-');

% make 9 test points along the NURBS curve, spread between eta=0.0 and eta=1.0
tt = linspace(0.0,1.0,9);

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