%%%% GLOBAL CONSTANTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
R = 91.9;       % span, [m]
c_max = 7.628;  % maximum chord of Sandia (monoplane) blade, [m]

% plot the location of the monoplane spar stations as dashed vertical lines
x1 = [0.0 0.2 2.3 4.4 6.5 9.0 12.2 13.9 15.5 17.1 19.8 22.5 25.2 33.4 41.5 49.6 57.8 64.3 65.9 70.8 74.0 82.2 87.0 91.9];
x3 = [-30 30];
for j=1:length(x1)
    plot([x1(j) x1(j)], x3, 'c:');
    if j == 1
        hold on;
    end
end