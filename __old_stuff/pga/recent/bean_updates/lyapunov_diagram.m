% Examine the follow range of parameter values.
a_start      = 0.4; a_stop    = 1;   a_step  = 0.001;

f = @param_squeezer;    n = 2;
%f = @(S,A) A*S*(1-S);   n = 1;  % The logistic map

for a = a_start:a_step:a_stop
    l = lyapunov(f, a, n);
    printf( "%10.7f %10.7f\n", a, l);
end

