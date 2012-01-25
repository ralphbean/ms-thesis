function [u,v] = squeezer(x,y);

% v = y;                 u = x/2 + (sqrt(1-y^2))/2;
u = x;                 v = y/2 + (sqrt(1-x^2))/2;

r = sqrt(v^2+u^2);     theta = 2*atan2(u,v);

u = r * cos(theta);    v = r * sin(theta);

end;
