function [x, y, curvature, tang_x, tang_y, norm_x, norm_y] = get_curvatures_tangents_normals(crv, tt, arrow_flag, print_flag)

% create the NURBS representation of the 1st and 2nd derivatives
[dcrv, dcrv2] = nrbderiv(crv);

% evaluate the 1st and 2nd derivatives of the NURBS curve at each of the test points
[p1, dp, d2p] = nrbdeval(crv, dcrv, dcrv2, tt);

% evaluate the (x,y,z) coordinates of the NURBS curve at each of the test points
p = nrbeval(crv,tt);
x = p(1,:);
y = p(2,:);
z = p(3,:);

% normalize the tangent vectors along the NURBS curve
p2 = vecnorm(dp);
p2_d2p = vecnorm(d2p);

% calculate the normal vectors along the NURBS curve
p2_perp = zeros(size(p2));
p2_perp(1,:) = -p2(2,:);
p2_perp(2,:) = p2(1,:);
p2_perp(3,:) = p2(3,:);


if arrow_flag  % if the user requests the tangent and normal vectors to be plotted...
    % plot the tangent vectors along the NURBS curve
    plot(p1(1,:),p1(2,:),'ro');
    h = quiver(p1(1,:), p1(2,:), p2(1,:), p2(2,:), 0);
    set(h,'Color','black');
    
    % plot the perpendicular vectors along the NURBS curve
    perp = quiver(p1(1,:), p1(2,:), p2_perp(1,:), p2_perp(2,:), 0);
    set(perp,'Color','green');

    % plot the opposite set of perpendicular vectors along the NURBS curve
    perp_rev = quiver(p1(1,:), p1(2,:), -p2_perp(1,:), -p2_perp(2,:), 0);
    set(perp_rev,'Color','green');
end

% save the x&y components of the tangent and normal vectors
tang_x = p2(1,:);
tang_y = p2(2,:);
norm_x = p2_perp(1,:);
norm_y = p2_perp(2,:);


% plot the second derivative vectors along the NURBS curve
% g = quiver(p1(1,:), p1(2,:), p2_d2p(1,:), p2_d2p(2,:), 0);
% set(g,'Color','red');

% curvature = mag( dp x d2p ) / (mag( dp ))^3
%    ref: http://en.wikipedia.org/wiki/NURBS#Curvature
numerator = vecmag( veccross(dp, d2p) );
denominator = (vecmag(dp) ).^3;
curvature = numerator ./ denominator;
radius_of_curvature = 1.0./curvature;

if print_flag  % if the user requests the results to be printed to the screen
    fprintf('%8s %8s %8s %8s %8s %8s %8s %8s \n', 'eta', 'x', 'y', 'k2', 'tang_x', 'tang_y', 'norm_x', 'norm_y');
    fprintf('%8s %8s %8s %8s %8s %8s %8s %8s \n', '-------', '-------', '-------', '-------', '-------', '-------', '-------', '-------');
    for i=1:1:length(x)
        fprintf('%8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f \n', tt(i), x(i), y(i), curvature(i), tang_x(i), tang_y(i), norm_x(i), norm_y(i))
    end
    fprintf('\n')
end