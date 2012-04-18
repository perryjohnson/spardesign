%%%% GLOBAL CONSTANTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
R = 91.9;       % span, [m]
c_max = 7.628;  % maximum chord of Sandia (monoplane) blade, [m]

% spanwise locations of spar stations
x1 = [0.0 0.2 2.3 4.4 6.5 9.0 12.2 13.9 15.5 17.1 19.8 22.5 25.2 33.4 41.5 49.6 57.8 64.3 65.9 70.8 74.0 82.2 87.0 91.9];

% plot the location of the monoplane spar stations as dashed vertical lines
x3 = [-18 18];
for j=1:length(x1)
    plot([x1(j) x1(j)], x3, 'c:');
    if j == 1
        hold on;
    end
end

% total cross-section heights of each spar station
% (the first 6 stations include the top and bottom root buildup heights, in addition to the shear web heights)
cs_heights = [5.392 5.375 5.089 4.791 4.455 4.101 3.680 3.480 3.285 3.089 2.882 2.696 2.498 2.077 1.672 1.360 1.138 0.954 0.910 0.832 0.796 0.707 0.651 0.508];