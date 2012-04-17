function eta = x1_to_eta(crv, x1)

tol = 0.000001;

eta = 0.5;
p = nrbeval(crv, eta);

increment = 0.25;

while abs(p(1) - x1) > tol
    if p(1) > x1
        eta = eta - increment;
    else
        eta = eta + increment;
    end
    p = nrbeval(crv, eta);
    increment = increment/2.0;
end

% fprintf('eta = %10.8f\n', eta);
% fprintf('x1  = %10.8f\n', p(1));
% fprintf('err = %10.8f\n', abs(x1-p(1)));