% this script plots beam reference line(s) of the biplane blade as several NURBS curves,
% then calculates the curvature and radius of curvature at several test points along the curve
%
% Author: Perry Johnson
% Date:   March 28, 2012

clear all;
clc;

addpath '.\nurbs-1.3.6\inst' -BEGIN;


%%%% GLOBAL CONSTANTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
R = 91.9;       % span, [m]
c_max = 7.628;  % maximum chord in monoplane blade (Sandia), [m]

% plot the location of the monoplane spar stations
x1 = [0.0 0.2 2.3 4.4 6.5 9.0 12.2 13.9 15.5 17.1 19.8 22.5 25.2 33.4 41.5 49.6 57.8 64.3 65.9 70.8 74.0 82.2 87.0 91.9];
x3 = [-20 20];
for j=1:length(x1)
    plot([x1(j) x1(j)], x3, 'c:');
    if j == 1
        hold on;
    end
end


%%%% GLOBAL PARAMETERS, NON-DIMENSIONAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r_j__to__R    = 0.5397;  % joint length-to-span ratio
r_jt__to__r_j = 0.3266;  % joint transition length-to-joint length ratio
r_rt__to__r_j = 0.1633;  % root transition length-to-joint length ratio
r_r__to__r_j  = 0.1815;  % root length-to-joint length ratio
g__to__c      = 1.0003;  % gap-to-chord ratio

% template5 presets:
% r_j__to__R    = 0.5397;  % joint length-to-span ratio
% r_jt__to__r_j = 0.3266;  % joint transition length-to-joint length ratio
% r_rt__to__r_j = 0.1633;  % root transition length-to-joint length ratio
% r_r__to__r_j  = 0.1815;  % root length-to-joint length ratio
% g__to__c      = 1.0003;  % gap-to-chord ratio


%%%% GLOBAL PARAMETERS, DIMENSIONAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
g = g__to__c * c_max;        % gap, [m]
r_j = r_j__to__R * R;        % joint length, [m]
r_r = r_r__to__r_j * r_j;    % root length, [m]
r_rt = r_rt__to__r_j * r_j;  % root transition length, [m]
r_jt = r_jt__to__r_j * r_j;  % joint transition length, [m]

% point = [x, y, z, w];
A = [0.0,         0.0,  0.0,   1.0];
B = [r_r,         0.0,  0.0,   1.0];
C = [r_r + r_rt,  0.0,  g/2.0, 1.0];
D = [r_j - r_jt,  0.0,  g/2.0, 1.0];
E = [r_j,         0.0,  0.0,   1.0];
F = [R,           0.0,  0.0,   1.0];
G = [r_r + r_rt,  0.0, -g/2.0, 1.0];
H = [r_j - r_jt,  0.0, -g/2.0, 1.0];



%%%% ROOT REGION (AB) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [A(4) B(4)];

% control points
cntrl = [w(1)*A(1)  w(2)*B(1);
         w(1)*A(3)  w(2)*B(3);
         w(1)*A(2)  w(2)*B(2);
         w(1)       w(2)];

% knot sequence
knots = [0.0 0.0 1.0 1.0];

% make a 2D NURBS curve
root = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(root, 50);

% create plot for the control points
% plot(cntrl(1,:),cntrl(2,:),'m.:');


%%%% ROOT TRANSITION, UPPER (BC) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [B(4) 1.0 1.0 C(4)];

% control points
cntrl = [w(1)*B(1)  w(2)*(C(1)-B(1))*0.5 + B(1)  w(3)*(C(1)-B(1))*0.5 + B(1)  w(4)*C(1);
         w(1)*B(3)  w(2)* 0.0                    w(3)*g/2.0                   w(4)*C(3);
         w(1)*B(2)  w(2)* 0.0                    w(3)* 0.0                    w(4)*C(2);
         w(1)       w(2)                         w(3)                         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
rootTrans_upper = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(rootTrans_upper, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

[tt, x, y, curvature] = getCurvature(rootTrans_upper);


%%%% ROOT TRANSITION, LOWER (BG) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [B(4) 1.0 1.0 G(4)];

% control points
cntrl = [w(1)*B(1)  w(2)*(G(1)-B(1))*0.5 + B(1)  w(3)*(G(1)-B(1))*0.5 + B(1)  w(4)*G(1);
         w(1)*B(3)  w(2)* 0.0                    w(3)*-g/2.0                  w(4)*G(3);
         w(1)*B(2)  w(2)* 0.0                    w(3)* 0.0                    w(4)*G(2);
         w(1)       w(2)                         w(3)                         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
rootTrans_lower = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(rootTrans_lower, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

[tt, x, y, curvature] = getCurvature(rootTrans_lower);


%%%% STRAIGHT BIPLANE, UPPER (CD) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [C(4) D(4)];

% control points
cntrl = [w(1)*C(1)  w(2)*D(1);
         w(1)*C(3)  w(2)*D(3);
         w(1)*C(2)  w(2)*D(2);
         w(1)       w(2)];

% knot sequence
knots = [0.0 0.0 1.0 1.0];

% make a 2D NURBS curve
straightBiplane_upper = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(straightBiplane_upper, 50);

% create plot for the control points
% plot(cntrl(1,:),cntrl(2,:),'m.:');


%%%% STRAIGHT BIPLANE, LOWER (GH) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [G(4) H(4)];

% control points
cntrl = [w(1)*G(1)  w(2)*H(1);
         w(1)*G(3)  w(2)*H(3);
         w(1)*G(2)  w(2)*H(2);
         w(1)       w(2)];

% knot sequence
knots = [0.0 0.0 1.0 1.0];

% make a 2D NURBS curve
straightBiplane_lower = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(straightBiplane_lower, 50);

% create plot for the control points
% plot(cntrl(1,:),cntrl(2,:),'m.:');


%%%% JOINT TRANSITION, UPPER (DE) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [D(4) 1.0 1.0 E(4)];

% control points
cntrl = [w(1)*D(1)  w(2)*(E(1)-D(1))*0.5 + D(1)  w(3)*(E(1)-D(1))*0.5 + D(1)  w(4)*E(1);
         w(1)*D(3)  w(2)*g/2.0                   w(3)* 0.0                    w(4)*E(3);
         w(1)*D(2)  w(2)* 0.0                    w(3)* 0.0                    w(4)*E(2);
         w(1)       w(2)                         w(3)                         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
jointTrans_upper = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(jointTrans_upper, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

[tt, x, y, curvature] = getCurvature(jointTrans_upper);


%%%% JOINT TRANSITION, LOWER (HE) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [H(4) 1.0 1.0 E(4)];

% control points
cntrl = [w(1)*H(1)  w(2)*(E(1)-D(1))*0.5 + D(1)  w(3)*(E(1)-D(1))*0.5 + D(1)  w(4)*E(1);
         w(1)*H(3)  w(2)*-g/2.0                  w(3)* 0.0                    w(4)*E(3);
         w(1)*H(2)  w(2)* 0.0                    w(3)* 0.0                    w(4)*E(2);
         w(1)       w(2)                         w(3)                         w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
jointTrans_lower = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(jointTrans_lower, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

[tt, x, y, curvature] = getCurvature(jointTrans_lower);


%%%% OUTBOARD MONOPLANE REGION (EF) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [E(4) F(4)];

% control points
cntrl = [w(1)*E(1)  w(2)*F(1);
         w(1)*E(3)  w(2)*F(3);
         w(1)*E(2)  w(2)*F(2);
         w(1)       w(2)];

% knot sequence
knots = [0.0 0.0 1.0 1.0];

% make a 2D NURBS curve
monoOutboard = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(monoOutboard, 50);

% create plot for the control points
% plot(cntrl(1,:),cntrl(2,:),'m.:');


title('biplane blade, beam reference line(s)');
xlim([-5 100])
% ylim([-20 20])
xlabel('x_1, spanwise direction [m]')
ylabel('x_3, flapwise direction [m]')

hold off;