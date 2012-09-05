%%% CHOOSE THE SPAR REGIONS THAT WILL BE CALCULATED %%%
toggle_straightBiplane = 1;
toggle_jointTrans = 1;
toggle_monoOutboard = 1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if root_joint_flag
    toggle_root = 1;
    toggle_rootTrans = 1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fprintf('\n')

% write external shape scaling factors to DYMORE-formatted file
fid_shape = fopen([output_path 'shapes.dat'], 'wt');
fprintf(fid_shape, '@SHAPE_DEFINITION {\n');


if root_joint_flag
    % root region %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if toggle_root
        disp('*** ROOT REGION ***')
        start_station = 1;
        end_station = rt_beg_station;

        % write external shape scaling factors for this region to DYMORE-formatted file
        fprintf(fid_shape, ' @SHAPE_NAME {shape_root} {\n');
        fprintf(fid_shape, ' @SHAPE_TYPE {CURVE}\n');
        fprintf(fid_shape, ' @COORDINATE_TYPE {ETA_COORDINATE}\n');

        fprintf(1, '%8s %8s %8s %8s \n', 'station', 'eta', 'cs_ht', 'k2')
    fprintf(1, '%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------')
        for i=start_station:end_station
            [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(root, [x1_to_eta(root,x1(i))], 0, 0);
            fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(root, x1(i)), cs_heights(i), curvature)

            fprintf(fid_shape, ' @ETA_COORDINATE {%6.4f} {\n', x1_to_eta(root, x1(i)));
            fprintf(fid_shape, ' @CURVE_NAME {CurveSquare}\n');
            fprintf(fid_shape, ' @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));
            fprintf(fid_shape, ' @ORIGIN {0.0, 0.0, 0.0}\n');
            fprintf(fid_shape, ' }\n');
        end
        fprintf(1, '\n')

        fprintf(fid_shape, ' }\n\n');
    end


    % root transition region %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if toggle_rootTrans
        disp('*** ROOT TRANSITION REGION ***')
        start_station = rt_beg_station;
        end_station = rt_end_station;

        % write external shape scaling factors for this region to DYMORE-formatted file
        fprintf(fid_shape, ' @SHAPE_NAME {shape_rootTrans} {\n');
        fprintf(fid_shape, ' @SHAPE_TYPE {CURVE}\n');
        fprintf(fid_shape, ' @COORDINATE_TYPE {ETA_COORDINATE}\n');

        % write curve mesh parameters to DYMORE-formatted file
        fid = fopen([output_path 'BC_rootTrans_upper_mesh.dat'], 'wt');
        fid2 = fopen([output_path 'BG_rootTrans_lower_mesh.dat'], 'wt');
        fprintf(fid, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
        fprintf(fid2, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
        fprintf(fid, ' @CURVE_MESH_PARAMETERS_NAME {meshBC} {\n');
        fprintf(fid2, ' @CURVE_MESH_PARAMETERS_NAME {meshBG} {\n');
        fprintf(fid, ' @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
        fprintf(fid2, ' @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
        fprintf(fid, ' @ORDER_OF_ELEMENTS {3}\n');
        fprintf(fid2, ' @ORDER_OF_ELEMENTS {3}\n');

        fprintf(1, '%8s %8s %8s %8s \n', 'station', 'eta', 'cs_ht', 'k2')
        fprintf(1, '%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------')
        for i=start_station:end_station
            fprintf(fid_shape, ' @ETA_COORDINATE {%6.4f} {\n', x1_to_eta(rootTrans_upper, x1(i)));
            fprintf(fid_shape, ' @CURVE_NAME {CurveSquare}\n');

            [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(rootTrans_upper, [x1_to_eta(rootTrans_upper,x1(i))], 0, 0);
            fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(rootTrans_upper, x1(i)), cs_heights(i), curvature)

            fprintf(fid_shape, ' @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));

            fprintf(fid, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_upper, x1(i)));
            fprintf(fid2, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_lower, x1(i)));

            % if i == start_station
            %     fprintf(1, '%8d %8.4f %8.4f \n', i, x1_to_eta(rootTrans_upper, x1(i)), cs_heights(i))

            %     fprintf(fid_shape, ' @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));

            %     fprintf(fid, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_upper, x1(i)));
            %     fprintf(fid2, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_lower, x1(i)));
            % else
            %     fprintf(1, '%8d %8.4f %8.4f \n', i, x1_to_eta(rootTrans_upper, x1(i)), cs_heights(i))

            %     fprintf(fid_shape, ' @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));

            %     fprintf(fid, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_upper, x1(i)));
            %     fprintf(fid2, ' @ETA_COORDINATE {%6.4f}\n', x1_to_eta(rootTrans_lower, x1(i)));
            % end

            fprintf(fid_shape, ' @ORIGIN {0.0, 0.0, 0.0}\n');
            fprintf(fid_shape, ' }\n');

        end
        fprintf(1, '\n')

        fprintf(fid_shape, ' }\n\n');

        fprintf(fid, ' @COMMENTS {models the upper root transition region with %2d cubic beam elements}\n', end_station-start_station);
        fprintf(fid2, ' @COMMENTS {models the lower root transition region with %2d cubic beam elements}\n', end_station-start_station);
        fprintf(fid, ' }\n');
        fprintf(fid2, ' }\n');
        fprintf(fid, '}\n');
        fprintf(fid2, '}\n');
        fclose(fid);
        fclose(fid2);
    end
end


% straight biplane region %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if toggle_straightBiplane
    disp('*** STRAIGHT BIPLANE REGION ***')
    if root_joint_flag
        start_station = rt_end_station;
    else
        start_station = 1;
    end
    end_station = jt_beg_station;

    % write external shape scaling factors for this region to DYMORE-formatted file
    fprintf(fid_shape, '  @SHAPE_NAME {shape_straightBiplane} {\n');
    fprintf(fid_shape, '    @SHAPE_TYPE {CURVE}\n');
    fprintf(fid_shape, '    @COORDINATE_TYPE {ETA_COORDINATE}\n');

    % write curve mesh parameters to DYMORE-formatted file
    fid = fopen([output_path 'CD_straightBiplane_upper_mesh.dat'], 'wt');
    fid2 = fopen([output_path 'GH_straightBiplane_lower_mesh.dat'], 'wt');
    fprintf(fid, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
    fprintf(fid2, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
    fprintf(fid, '  @CURVE_MESH_PARAMETERS_NAME {meshCD} {\n');
    fprintf(fid2, '  @CURVE_MESH_PARAMETERS_NAME {meshGH} {\n');
    fprintf(fid, '    @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
    fprintf(fid2, '    @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
    fprintf(fid, '    @ORDER_OF_ELEMENTS {3}\n');
    fprintf(fid2, '    @ORDER_OF_ELEMENTS {3}\n');

    fprintf(1, '%8s %8s %8s %8s \n', 'station', 'eta', 'cs_ht', 'k2')
    fprintf(1, '%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------')
    for i=start_station:end_station
        fprintf(fid_shape, '    @ETA_COORDINATE {%6.4f} {\n', x1_to_eta(straightBiplane_upper, x1(i)));
        fprintf(fid_shape, '      @CURVE_NAME {CurveSquare}\n');
        fprintf(fid_shape, '      @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));
        fprintf(fid_shape, '      @ORIGIN {0.0, 0.0, 0.0}\n');
        fprintf(fid_shape, '    }\n');

        [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(straightBiplane_upper, [x1_to_eta(straightBiplane_upper,x1(i))], 0, 0);
        fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(straightBiplane_upper, x1(i)), cs_heights(i), curvature)

        fprintf(fid, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(straightBiplane_upper, x1(i)));
        fprintf(fid2, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(straightBiplane_lower, x1(i)));
    end
    fprintf(1, '\n')

    fprintf(fid_shape, '  }\n\n');

    fprintf(fid, '    @COMMENTS {models the upper straight biplane region with %2d cubic beam elements}\n', end_station-start_station);
    fprintf(fid2, '    @COMMENTS {models the lower straight biplane region with %2d cubic beam elements}\n', end_station-start_station);
    fprintf(fid, '  }\n');
    fprintf(fid2, '  }\n');
    fprintf(fid, '}\n');
    fprintf(fid2, '}\n');
    fclose(fid);
    fclose(fid2);
end


% joint transition region %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if toggle_jointTrans
    disp('*** JOINT TRANSITION REGION ***')
    start_station = jt_beg_station;
    end_station = jt_end_station;

    % write external shape scaling factors for this region to DYMORE-formatted file
    fprintf(fid_shape, '  @SHAPE_NAME {shape_jointTrans} {\n');
    fprintf(fid_shape, '    @SHAPE_TYPE {CURVE}\n');
    fprintf(fid_shape, '    @COORDINATE_TYPE {ETA_COORDINATE}\n');

    % write curve mesh parameters to DYMORE-formatted file
    fid = fopen([output_path 'DE_jointTrans_upper_mesh.dat'], 'wt');
    fid2 = fopen([output_path 'HE_jointTrans_lower_mesh.dat'], 'wt');
    fprintf(fid, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
    fprintf(fid2, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
    fprintf(fid, '  @CURVE_MESH_PARAMETERS_NAME {meshDE} {\n');
    fprintf(fid2, '  @CURVE_MESH_PARAMETERS_NAME {meshHE} {\n');
    fprintf(fid, '    @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
    fprintf(fid2, '    @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
    fprintf(fid, '    @ORDER_OF_ELEMENTS {3}\n');
    fprintf(fid2, '    @ORDER_OF_ELEMENTS {3}\n');

    fprintf(1, '%8s %8s %8s %8s \n', 'station', 'eta', 'cs_ht', 'k2')
    fprintf(1, '%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------')
    for i=start_station:end_station
        fprintf(fid_shape, '    @ETA_COORDINATE {%6.4f} {\n', x1_to_eta(jointTrans_upper, x1(i)));
        fprintf(fid_shape, '      @CURVE_NAME {CurveSquare}\n');

        if i == end_station
            fprintf(fid_shape, '      @SCALING_FACTOR {0.0, 1.672, %5.3f}\n', cs_heights(i));

            [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(jointTrans_upper, [x1_to_eta(jointTrans_upper,x1(i))], 0, 0);
            fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(jointTrans_upper, x1(i)), cs_heights(i), curvature)

            fprintf(fid, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(jointTrans_upper, x1(i)));
            fprintf(fid2, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(jointTrans_lower, x1(i)));
        else
            fprintf(fid_shape, '      @SCALING_FACTOR {0.0, 1.586, %5.3f}\n', cs_heights(i));

            [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(jointTrans_upper, [x1_to_eta(jointTrans_upper,x1(i))], 0, 0);
            fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(jointTrans_upper, x1(i)), cs_heights(i), curvature)

            fprintf(fid, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(jointTrans_upper, x1(i)));
            fprintf(fid2, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(jointTrans_lower, x1(i)));
        end

        fprintf(fid_shape, '      @ORIGIN {0.0, 0.0, 0.0}\n');
        fprintf(fid_shape, '    }\n');
    end
    fprintf(1, '\n')

    fprintf(fid_shape, '  }\n\n');

    fprintf(fid, '    @COMMENTS {models the upper joint transition region with %2d cubic beam elements}\n', end_station-start_station);
    fprintf(fid2, '    @COMMENTS {models the lower joint transition region with %2d cubic beam elements}\n', end_station-start_station);
    fprintf(fid, '  }\n');
    fprintf(fid2, '  }\n');
    fprintf(fid, '}\n');
    fprintf(fid2, '}\n');
    fclose(fid);
    fclose(fid2);
end


% outboard monoplane region %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if toggle_monoOutboard
    disp('*** OUTBOARD MONOPLANE REGION ***')
    start_station = jt_end_station;
    end_station = 24;

    % write external shape scaling factors for this region to DYMORE-formatted file
    fprintf(fid_shape, '  @SHAPE_NAME {shape_monoOutboard} {\n');
    fprintf(fid_shape, '    @SHAPE_TYPE {CURVE}\n');
    fprintf(fid_shape, '    @COORDINATE_TYPE {ETA_COORDINATE}\n');

    % write curve mesh parameters to DYMORE-formatted file
    fid = fopen([output_path 'EF_monoOutboard_mesh.dat'], 'wt');
    fprintf(fid, '@CURVE_MESH_PARAMETERS_DEFINITION {\n');
    fprintf(fid, '  @CURVE_MESH_PARAMETERS_NAME {meshEF} {\n');
    fprintf(fid, '    @NUMBER_OF_ELEMENTS {%2d}\n', end_station-start_station);
    fprintf(fid, '    @ORDER_OF_ELEMENTS {3}\n');

    fprintf(1, '%8s %8s %8s %8s \n', 'station', 'eta', 'cs_ht', 'k2')
    fprintf(1, '%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------')
    for i=start_station:end_station
        [x_stn, y_stn, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(monoOutboard, [x1_to_eta(monoOutboard,x1(i))], 0, 0);
        fprintf(1, '%8d %8.4f %8.4f %8.4f \n', i, x1_to_eta(monoOutboard, x1(i)), cs_heights(i), curvature)

        fprintf(fid, '    @ETA_COORDINATE {%6.4f}\n', x1_to_eta(monoOutboard, x1(i)));

        fprintf(fid_shape, '    @ETA_COORDINATE {%6.4f} {\n', x1_to_eta(monoOutboard, x1(i)));
        fprintf(fid_shape, '      @CURVE_NAME {CurveSquare}\n');
        fprintf(fid_shape, '      @SCALING_FACTOR {0.0, 1.672, %5.3f}\n', cs_heights(i));
        fprintf(fid_shape, '      @ORIGIN {0.0, 0.0, 0.0}\n');
        fprintf(fid_shape, '    }\n');
    end
    fprintf(1, '\n')

    fprintf(fid_shape, '  }\n\n');

    fprintf(fid, '    @COMMENTS {models the monoplane outboard region with %2d cubic beam elements}\n', end_station-start_station);
    fprintf(fid, '  }\n');
    fprintf(fid, '}\n');
    fclose(fid);
end

fprintf(fid_shape, '}\n');
fclose(fid_shape);