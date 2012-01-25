function U = param_squeezer(X, a);
x = X(1);
y = X(2);

% v = y;                 u = x/2 + (sqrt(1-y^2))/2;
u = x;                 v = y/2 + (sqrt(1-x^2))/2;

r = sqrt(v^2+u^2);     theta = 2*atan2(u,v);

u = a * r * cos(theta);    v = r * sin(theta);

U = [u,v];
end;
