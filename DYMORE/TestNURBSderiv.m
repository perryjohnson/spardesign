% clear all;
% close all;
% clc;

addpath 'C:\Program Files (x86)\MATLAB\R2007b\nurbs-1.3.6\inst' -BEGIN;

crv = nrbtestcrv;
nrbplot(crv,48);
title('First derivatives along a test curve.');

tt = linspace(0.0,1.0,9);

dcrv = nrbderiv(crv);

[p1, dp] = nrbdeval(crv,dcrv,tt);

p2 = vecnorm(dp);

hold on;
plot(p1(1,:),p1(2,:),'ro');
h = quiver(p1(1,:),p1(2,:),p2(1,:),p2(2,:),0);
set(h,'Color','black');
hold off;