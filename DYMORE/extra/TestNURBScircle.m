% this is a test script that plots a circle as a NURBS curve,
% then calculates the curvature and radius of curvature at
% nine test points around the circle
%
% the curvature and radius of curvature should be constant
% and equal to 1.0 for every point (because this is a unit circle)
%
% Author: Perry Johnson
% Date:   March 27, 2012

clear all;
% close all;
clc;

addpath '.\nurbs-1.3.6\inst' -BEGIN;

% weights
w = [1.0 sqrt(2)/2 1.0 sqrt(2)/2 1.0 sqrt(2)/2 1.0 sqrt(2)/2 1.0];

% control points
% ref: http://en.wikipedia.org/wiki/Non-uniform_rational_B-spline#Example:_a_circle
cntrl = [w(1)*1.0  w(2)*1.0  w(3)*0.0  w(4)*-1.0  w(5)*-1.0  w(6)*-1.0  w(7)* 0.0  w(8)* 1.0 w(9)*1.0;
         w(1)*0.0  w(2)*1.0  w(3)*1.0  w(4)* 1.0  w(5)* 0.0  w(6)*-1.0  w(7)*-1.0  w(8)*-1.0 w(9)*0.0;
         w(1)*0.0  w(2)*0.0  w(3)*0.0  w(4)* 0.0  w(5)* 0.0  w(6)* 0.0  w(7)* 0.0  w(8)* 0.0 w(9)*0.0;
         w(1)      w(2)      w(3)      w(4)       w(5)       w(6)       w(7)       w(8)      w(9)    ];
     
% knot sequence
knots = [0 0 0 pi/2 pi/2 pi pi 3*pi/2 3*pi/2 2*pi 2*pi 2*pi];

% make a 2D NURBS curve
crv = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(crv, 50);
hold on;
title('NURBS circle');

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
%   ref: 
numerator = vecmag( veccross(dp, d2p) );
denominator = (vecmag(dp) ).^3;
curvature = numerator ./ denominator
radius_of_curvature = 1.0./curvature  % radius of curvature is the inverse of the curvature
