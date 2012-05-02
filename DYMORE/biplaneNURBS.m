% this script plots beam reference line(s) of the biplane blade as several NURBS curves,
% then calculates the curvature and radius of curvature at several test points along the curve
%
% Author: Perry Johnson
% Date:   April 16, 2012

clear all;
clc;
addpath '.\nurbs-1.3.6\inst' -BEGIN;  % start the NURBS package for MATLAB
global_constants;  % initialize the global constants for the biplane spar


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% USER-DEFINED PARAMETERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
g__to__c = 1.00;                    % gap-to-chord ratio
jt_end_station = 15;                % spar station for end of joint transition
jt_beg_station = jt_end_station-2;  % spar station for beginning of joint transition
jt_mid = 0.5;                       % midpoint for NURBS control points that define joint transition region
rt_beg_station = 2;                 % spar station for beginning of root transition
rt_end_station = rt_beg_station+2;  % spar station for end of root transition
rt_mid = 0.5;                       % midpoint for NURBS control points that define root transition region
inboard_view = 0;                   % if 1, zoom view on inboard region; if 0, show entire spar
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


derived_parameters;  % calculate the derived parameters for the biplane spar


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
cntrl = [w(1)*B(1)  w(2)*(C(1)-B(1))*rt_mid + B(1)  w(3)*(C(1)-B(1))*rt_mid + B(1)  w(4)*C(1);   % x1-coordinates (or x-coordinates on plot)
         w(1)*B(3)  w(2)* 0.0                       w(3)*g/2.0                      w(4)*C(3);   % x3-coordinates (or y-coordinates on plot)
         w(1)*B(2)  w(2)* 0.0                       w(3)* 0.0                       w(4)*C(2);   % x2-coordinates
         w(1)       w(2)                            w(3)                            w(4)];       % weights
                    % midctrlpt_low              % midctrlpt_high
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
rootTrans_upper = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(rootTrans_upper, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

% [tt, x, y, curvature] = getCurvature(rootTrans_upper);

% write NURBS curve to DYMORE-formatted file
fid = fopen('.\input_files\BC_rootTrans_upper_curve.dat', 'wt');
fprintf(fid, '@CURVE_DEFINITION {\n');
fprintf(fid, '  @CURVE_NAME {curveBC} {\n');
fprintf(fid, '    @IS_DEFINED_IN_FRAME {INERTIAL}\n');
fprintf(fid, '    @POINT_DEFINITION {\n');
fprintf(fid, '      @NUMBER_OF_CONTROL_POINTS {4}\n');
fprintf(fid, '      @DEGREE_OF_CURVE {3}\n');
fprintf(fid, '      @RATIONAL_CURVE_FLAG {YES}\n');
fprintf(fid, '      @END_POINT_0 {pointB}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,2), cntrl(3,2), cntrl(2,2), cntrl(4,2));
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,3), cntrl(3,3), cntrl(2,3), cntrl(4,3));
fprintf(fid, '      @END_POINT_1 {pointC}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @SPLINE {NO}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @TRIAD_DEFINITION {\n');
fprintf(fid, '      @ORIENTATION_DISTRIBUTION_NAME {OriDist}\n');
fprintf(fid, '      @INITIAL_COORDINATE {0}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @CURVE_MESH_PARAMETERS_NAME {meshBC}\n');
fprintf(fid, '    @COMMENTS {a cubic spline from the inboard joint (pointB) to the end of the upper root transition (pointC)}\n');
fprintf(fid, '  }\n');
fprintf(fid, '}\n');
fclose(fid);


%%%% ROOT TRANSITION, LOWER (BG) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [B(4) 1.0 1.0 G(4)];

% control points
cntrl = [w(1)*B(1)  w(2)*(G(1)-B(1))*rt_mid + B(1)  w(3)*(G(1)-B(1))*rt_mid + B(1)  w(4)*G(1);
         w(1)*B(3)  w(2)* 0.0                       w(3)*-g/2.0                     w(4)*G(3);
         w(1)*B(2)  w(2)* 0.0                       w(3)* 0.0                       w(4)*G(2);
         w(1)       w(2)                            w(3)                            w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
rootTrans_lower = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(rootTrans_lower, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

% [tt, x, y, curvature] = getCurvature(rootTrans_lower);

% write NURBS curve to DYMORE-formatted file
fid = fopen('.\input_files\BG_rootTrans_lower_curve.dat', 'wt');
fprintf(fid, '@CURVE_DEFINITION {\n');
fprintf(fid, '  @CURVE_NAME {curveBG} {\n');
fprintf(fid, '    @IS_DEFINED_IN_FRAME {INERTIAL}\n');
fprintf(fid, '    @POINT_DEFINITION {\n');
fprintf(fid, '      @NUMBER_OF_CONTROL_POINTS {4}\n');
fprintf(fid, '      @DEGREE_OF_CURVE {3}\n');
fprintf(fid, '      @RATIONAL_CURVE_FLAG {YES}\n');
fprintf(fid, '      @END_POINT_0 {pointB}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,2), cntrl(3,2), cntrl(2,2), cntrl(4,2));
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,3), cntrl(3,3), cntrl(2,3), cntrl(4,3));
fprintf(fid, '      @END_POINT_1 {pointG}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @SPLINE {NO}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @TRIAD_DEFINITION {\n');
fprintf(fid, '      @ORIENTATION_DISTRIBUTION_NAME {OriDist}\n');
fprintf(fid, '      @INITIAL_COORDINATE {0}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @CURVE_MESH_PARAMETERS_NAME {meshBG}\n');
fprintf(fid, '    @COMMENTS {a cubic spline from the inboard joint (pointB) to the end of the lower root transition (pointG)}\n');
fprintf(fid, '  }\n');
fprintf(fid, '}\n');
fclose(fid);


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
cntrl = [w(1)*D(1)  w(2)*(E(1)-D(1))*jt_mid + D(1)  w(3)*(E(1)-D(1))*jt_mid + D(1)  w(4)*E(1);
         w(1)*D(3)  w(2)*g/2.0                      w(3)* 0.0                       w(4)*E(3);
         w(1)*D(2)  w(2)* 0.0                       w(3)* 0.0                       w(4)*E(2);
         w(1)       w(2)                            w(3)                            w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
jointTrans_upper = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(jointTrans_upper, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

% [tt, x, y, curvature] = getCurvature_tt(jointTrans_upper,[0.0, 0.3254, 0.3354, 0.3454, 1.0]);

% write NURBS curve to DYMORE-formatted file
fid = fopen('.\input_files\DE_jointTrans_upper_curve.dat', 'wt');
fprintf(fid, '@CURVE_DEFINITION {\n');
fprintf(fid, '  @CURVE_NAME {curveDE} {\n');
fprintf(fid, '    @IS_DEFINED_IN_FRAME {INERTIAL}\n');
fprintf(fid, '    @POINT_DEFINITION {\n');
fprintf(fid, '      @NUMBER_OF_CONTROL_POINTS {4}\n');
fprintf(fid, '      @DEGREE_OF_CURVE {3}\n');
fprintf(fid, '      @RATIONAL_CURVE_FLAG {YES}\n');
fprintf(fid, '      @END_POINT_0 {pointD}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,2), cntrl(3,2), cntrl(2,2), cntrl(4,2));
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,3), cntrl(3,3), cntrl(2,3), cntrl(4,3));
fprintf(fid, '      @END_POINT_1 {pointE}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @SPLINE {NO}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @TRIAD_DEFINITION {\n');
fprintf(fid, '      @ORIENTATION_DISTRIBUTION_NAME {OriDist}\n');
fprintf(fid, '      @INITIAL_COORDINATE {0}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @CURVE_MESH_PARAMETERS_NAME {meshDE}\n');
fprintf(fid, '    @COMMENTS {a cubic spline from the upper joint transition (pointD) to the outboard joint (pointE)}\n');
fprintf(fid, '  }\n');
fprintf(fid, '}\n');
fclose(fid);


%%%% JOINT TRANSITION, LOWER (HE) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% weights
w = [H(4) 1.0 1.0 E(4)];

% control points
cntrl = [w(1)*H(1)  w(2)*(E(1)-D(1))*jt_mid + D(1)  w(3)*(E(1)-D(1))*jt_mid + D(1)  w(4)*E(1);
         w(1)*H(3)  w(2)*-g/2.0                     w(3)* 0.0                       w(4)*E(3);
         w(1)*H(2)  w(2)* 0.0                       w(3)* 0.0                       w(4)*E(2);
         w(1)       w(2)                            w(3)                            w(4)];
     
% knot sequence
knots = [0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0];

% make a 2D NURBS curve
jointTrans_lower = nrbmak(cntrl,knots);

% plot the NURBS curve
nrbplot(jointTrans_lower, 50);

% create plot for the control points
plot(cntrl(1,:),cntrl(2,:),'m.:');

% [tt, x, y, curvature] = getCurvature(jointTrans_lower);

% write NURBS curve to DYMORE-formatted file
fid = fopen('.\input_files\HE_jointTrans_lower_curve.dat', 'wt');
fprintf(fid, '@CURVE_DEFINITION {\n');
fprintf(fid, '  @CURVE_NAME {curveHE} {\n');
fprintf(fid, '    @IS_DEFINED_IN_FRAME {INERTIAL}\n');
fprintf(fid, '    @POINT_DEFINITION {\n');
fprintf(fid, '      @NUMBER_OF_CONTROL_POINTS {4}\n');
fprintf(fid, '      @DEGREE_OF_CURVE {3}\n');
fprintf(fid, '      @RATIONAL_CURVE_FLAG {YES}\n');
fprintf(fid, '      @END_POINT_0 {pointH}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,2), cntrl(3,2), cntrl(2,2), cntrl(4,2));
fprintf(fid, '      @COORDINATES {%6.3f, %6.3f, %6.3f, %6.3f}\n', cntrl(1,3), cntrl(3,3), cntrl(2,3), cntrl(4,3));
fprintf(fid, '      @END_POINT_1 {pointE}\n');
fprintf(fid, '      @WEIGHT_DEFINITION {1.0}\n');
fprintf(fid, '      @SPLINE {NO}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @TRIAD_DEFINITION {\n');
fprintf(fid, '      @ORIENTATION_DISTRIBUTION_NAME {OriDist}\n');
fprintf(fid, '      @INITIAL_COORDINATE {0}\n');
fprintf(fid, '    }\n');
fprintf(fid, '    @CURVE_MESH_PARAMETERS_NAME {meshHE}\n');
fprintf(fid, '    @COMMENTS {a cubic spline from the lower joint transition (pointH) to the outboard joint (pointE)}\n');
fprintf(fid, '  }\n');
fprintf(fid, '}\n');
fclose(fid);


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


%%%% plot cross-section heights %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fprintf('\n')

for j=1:length(x1)
    s = cs_heights(j)/4;  % half-height scaling factor for biplane cross-sections
    if j <= rt_beg_station
        fprintf('station #%d, root region\n', j)
        plot([x1(j) x1(j)], [cs_heights(j)/2 -cs_heights(j)/2], 'k-');
    elseif rt_beg_station < j && j < rt_end_station
        fprintf('station #%d, root transition region\n', j)
        % upper station
        [x, y, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(rootTrans_upper, [x1_to_eta(rootTrans_upper,x1(j))], 0);
        plot([x(1) x(1)+s*norm_x(1)], [y(1) y(1)+s*norm_y(1)], 'k-')
        plot([x(1) x(1)-s*norm_x(1)], [y(1) y(1)-s*norm_y(1)], 'k-')
        % lower station
        [x, y, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(rootTrans_lower, [x1_to_eta(rootTrans_lower,x1(j))], 0);
        plot([x(1) x(1)+s*norm_x(1)], [y(1) y(1)+s*norm_y(1)], 'k-')
        plot([x(1) x(1)-s*norm_x(1)], [y(1) y(1)-s*norm_y(1)], 'k-')
    elseif rt_end_station <= j && j <= jt_beg_station
        fprintf('station #%d, straight biplane region\n', j)
        plot([x1(j) x1(j)], [s+g/2 -s+g/2], 'k-');
        plot([x1(j) x1(j)], [s-g/2 -s-g/2], 'k-');
    elseif jt_beg_station < j && j < jt_end_station
        fprintf('station #%d, joint transition region\n', j)
        % upper station
        [x, y, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(jointTrans_upper, [x1_to_eta(jointTrans_upper,x1(j))], 0);
        plot([x(1) x(1)+s*norm_x(1)], [y(1) y(1)+s*norm_y(1)], 'k-')
        plot([x(1) x(1)-s*norm_x(1)], [y(1) y(1)-s*norm_y(1)], 'k-')
        % lower station
        [x, y, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(jointTrans_lower, [x1_to_eta(jointTrans_lower,x1(j))], 0);
        plot([x(1) x(1)+s*norm_x(1)], [y(1) y(1)+s*norm_y(1)], 'k-')
        plot([x(1) x(1)-s*norm_x(1)], [y(1) y(1)-s*norm_y(1)], 'k-')
    else
        fprintf('station #%d, outboard monoplane region\n', j)
        plot([x1(j) x1(j)], [cs_heights(j)/2 -cs_heights(j)/2], 'k-');
    end
end

title('biplane spar, one-dimensional reference lines');
if inboard_view
    xlim([x1(rt_beg_station)-1 x1(jt_end_station)+1])
    ylim([-6 6])
else
    xlim([-5 100])
    ylim([-20 20])  
end
xlabel('x_1, spanwise direction [m]')
ylabel('x_3, flapwise direction [m]')


hold off;

% print cross-section heights for each region to the screen
regionStations_to_eta