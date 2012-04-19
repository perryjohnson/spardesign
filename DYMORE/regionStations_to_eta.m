% clc

% spanwise locations of spar stations
% x1 = [0.0 0.2 2.3 4.4 6.5 9.0 12.2 13.9 15.5 17.1 19.8 22.5 25.2 33.4 41.5 49.6 57.8 64.3 65.9 70.8 74.0 82.2 87.0 91.9];

% total cross-section heights of each spar station of the monoplane spar
% (the first 6 stations include the top and bottom root buildup heights, in addition to the shear web heights)
% cs_heights = [5.392 5.375 5.089 4.791 4.455 4.101 3.680 3.480 3.285 3.089 2.882 2.696 2.498 2.077 1.672 1.360 1.138 0.954 0.910 0.832 0.796 0.707 0.651 0.508];

fprintf('\n')

% root (stations 1-2)
disp('*** ROOT REGION ***')
start_station = 1;
end_station = rt_beg_station;
fprintf('%8s %8s %8s \n', 'station', 'eta', 'cs_ht')
fprintf('%8s %8s %8s \n', '-------', '-------', '-------')
for i=start_station:end_station
    fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(root, x1(i)), cs_heights(i))
end
fprintf('\n')

% root transition region (stations 2-4)
disp('*** ROOT TRANSITION REGION ***')
start_station = rt_beg_station;
end_station = rt_end_station;
fprintf('%8s %8s %8s \n', 'station', 'eta', 'cs_ht')
fprintf('%8s %8s %8s \n', '-------', '-------', '-------')
for i=start_station:end_station
    if i == start_station
        fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(rootTrans_upper, x1(i)), cs_heights(i))
    else
        fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(rootTrans_upper, x1(i)), cs_heights(i)/2.0)
    end
end
fprintf('\n')

% straight biplane region (stations 4-9)
disp('*** STRAIGHT BIPLANE REGION ***')
start_station = rt_end_station;
end_station = jt_beg_station;
fprintf('%8s %8s %8s \n', 'station', 'eta', 'cs_ht')
fprintf('%8s %8s %8s \n', '-------', '-------', '-------')
for i=start_station:end_station
    fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(straightBiplane_upper, x1(i)), cs_heights(i)/2.0)
end
fprintf('\n')

% joint transition region (stations 9-11)
disp('*** JOINT TRANSITION REGION ***')
start_station = jt_beg_station;
end_station = jt_end_station;
fprintf('%8s %8s %8s \n', 'station', 'eta', 'cs_ht')
fprintf('%8s %8s %8s \n', '-------', '-------', '-------')
for i=start_station:end_station
    if i == end_station
        fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(jointTrans_upper, x1(i)), cs_heights(i))
    else
        fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(jointTrans_upper, x1(i)), cs_heights(i)/2.0)
    end
end
fprintf('\n')

% outboard monoplane region (stations 11-24)
disp('*** OUTBOARD MONOPLANE REGION ***')
start_station = jt_end_station;
end_station = 24;
fprintf('%8s %8s %8s \n', 'station', 'eta', 'cs_ht')
fprintf('%8s %8s %8s \n', '-------', '-------', '-------')
for i=start_station:end_station
    fprintf('%8d %8.3f %8.3f \n', i, x1_to_eta(monoOutboard, x1(i)), cs_heights(i))
end
fprintf('\n')