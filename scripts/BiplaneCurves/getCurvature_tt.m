function [tt, x, y, curvature] = getCurvature_tt(crv, tt)

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

% plot the tangent vectors along the NURBS curve
plot(p1(1,:),p1(2,:),'ro');
h = quiver(p1(1,:), p1(2,:), p2(1,:), p2(2,:), 0);
set(h,'Color','black');

% plot the perpendicular vectors along the NURBS curve
p2_perp = zeros(size(p2));
p2_perp(1,:) = -p2(2,:);
p2_perp(2,:) = p2(1,:);
p2_perp(3,:) = p2(3,:);
perp = quiver(p1(1,:), p1(2,:), p2_perp(1,:), p2_perp(2,:), 0);
set(perp,'Color','green');
perp_rev = quiver(p1(1,:), p1(2,:), -p2_perp(1,:), -p2_perp(2,:), 0);
set(perp_rev,'Color','green');

% plot the second derivative vectors along the NURBS curve
% g = quiver(p1(1,:), p1(2,:), p2_d2p(1,:), p2_d2p(2,:), 0);
% set(g,'Color','red');

% curvature = mag( dp x d2p ) / (mag( dp ))^3
numerator = vecmag( veccross(dp, d2p) );
denominator = (vecmag(dp) ).^3;
curvature = numerator ./ denominator;
radius_of_curvature = 1.0./curvature;

% print results to the screen
fprintf('%8s %8s %8s %8s \n', 'eta', 'x', 'y', 'k2');
fprintf('%8s %8s %8s %8s \n', '-------', '-------', '-------', '-------');
for i=1:1:length(x)
    fprintf('%8.4f %8.4f %8.4f %8.4f \n', tt(i), x(i), y(i), curvature(i))
end