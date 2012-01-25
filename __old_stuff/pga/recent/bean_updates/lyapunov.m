function l = lyapunov(fun, a, n);
% fun is the map to measure.
% a is a parameter vector
% n is the dimension of the state space

warmup  = 200;
measure = 200;

epsilon = 0.0000000000001;
d0      = 0.000000001;
total   = 0;
x = rand(n, 1);
y = rand(n, 1) + x;


for i = 1:warmup,
    y = reorient(x, y, d0, epsilon);
    x = fun(x, a);
    y = fun(y, a);
end

for i = 1:measure,
    y = reorient(x, y, d0, epsilon);
    x = fun(x, a);
    y = fun(y, a);
    d1 = norm(x-y);
    total = total + log(abs(d1/d0));
end

l = total / measure;
end


