% this script plots beam reference line(s) of the biplane blade as several NURBS curves,
% then calculates the curvature and radius of curvature at several test points along the curve
%
% Author: Perry Johnson
% Date:   April 16, 2012

clear all;
clc;
addpath '.\nurbs-1.3.6\inst' -BEGIN;  % start the NURBS package for MATLAB
global_constants;  % initialize the global constants for the biplane spar


%%%% USER-DEFINED PARAMETERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
g__to__c = 1.00;  % gap-to-chord ratio
rt_beg = x1(6);   % beginning of root transition
rt_end = x1(10);  % end of root transition
jt_beg = x1(14);  % beginning of joint transition
jt_end = x1(16);  % end of joint transition


%%%% DERIVED PARAMETERS, DIMENSIONAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
g = g__to__c * c_max;    % gap, [m]

% point = [x-coordinate, y-coordinate, z-coordinate, weight];
A = [0.0,    0.0,  0.0,   1.0];
B = [rt_beg, 0.0,  0.0,   1.0];
C = [rt_end, 0.0,  g/2.0, 1.0];
D = [jt_beg, 0.0,  g/2.0, 1.0];
E = [jt_end, 0.0,  0.0,   1.0];
F = [R,      0.0,  0.0,   1.0];
G = [rt_end, 0.0, -g/2.0, 1.0];
H = [jt_beg, 0.0, -g/2.0, 1.0];

r_r = B(1);                  % root length, [m]
r_rt = C(1) - B(1);          % root transition length, [m]
r_j = E(1);                  % joint length, [m]
r_jt = E(1) - D(1);          % joint transition length, [m]

fprintf('span:                    R    = %6.3f m \n', R);
fprintf('joint length:            r_j  = %6.3f m \n', r_j);
fprintf('joint transition length: r_jt = %6.3f m \n', r_jt);
fprintf('root transition length:  r_rt = %6.3f m \n', r_rt);
fprintf('root length:             r_r  = %6.3f m \n', r_r);
fprintf('gap:                     g    = %6.3f m \n', g);
fprintf('maximum chord:           c    = %6.3f m \n', c_max);
fprintf('\n');


%%%% DERIVED PARAMETERS, NON-DIMENSIONAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r_j__to__R    = r_j/R;     % joint length-to-span ratio
r_jt__to__r_j = r_jt/r_j;  % joint transition length-to-joint length ratio
r_rt__to__r_j = r_rt/r_j;  % root transition length-to-joint length ratio
r_r__to__r_j  = r_r/r_j;   % root length-to-joint length ratio

fprintf('joint length-to-span ratio:                    r_j/R    = %5.3f \n', r_j__to__R);
fprintf('joint transition length-to-joint length ratio: r_jt/r_j = %5.3f \n', r_jt__to__r_j);
fprintf('root transition length-to-joint length ratio:  r_rt/r_j = %5.3f \n', r_rt__to__r_j);
fprintf('root length-to-joint length ratio:             r_r/r_j  = %5.3f \n', r_r__to__r_j);
fprintf('gap-to-maximum chord ratio:                    g/c      = %5.3f \n', g__to__c);


%%%% WRITE ENDPOINTS OF EACH REGION TO DYMORE-FORMATTED FILE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fid = fopen('biplane_spar_params.dgp', 'wt');
fprintf(fid, '@DESIGN_PARAMETERS_DEFINITION {\n');
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointA_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', A(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointB_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', B(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointC_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', C(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointD_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', D(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointE_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', E(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointF_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', F(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointG_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', G(1:3));
fprintf(fid, '  @DESIGN_PARAMETER_NAME {#pointH_xyz}  @VECTOR_VALUE {%6.3f, %6.3f, %6.3f}\n', H(1:3));
fprintf(fid, '}\n');
fclose(fid);


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

% [tt, x, y, curvature] = getCurvature(rootTrans_upper);


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

% [tt, x, y, curvature] = getCurvature(rootTrans_lower);


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

% [tt, x, y, curvature] = getCurvature(jointTrans_upper);


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

% [tt, x, y, curvature] = getCurvature(jointTrans_lower);


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