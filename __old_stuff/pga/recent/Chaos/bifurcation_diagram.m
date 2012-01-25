
% Warmup iteration range:
warmup_start = 1; warmup_stop = 200;

% Plot this many points for each run.
plot_start   = 1; plot_stop   = 200;

% It appears that there are multiple attractors within the unit circle.
%  To increase our chances of hitting all of them, run multiple trials
%  for each value of a.
trials_start = 1; trials_stop = 5;

% Examine the follow range of parameter values.
a_start      = 0.4; a_stop    = 1;   a_step  = 0.0001;

for a = a_start:a_step:a_stop
    for trial = trials_start:trials_stop
        % Pick an seed in the unit circle
        x = -1 + 2 * rand(1);    y = -1 + 2 * rand(1);
        while x^2 + y^2 >= 1
            x = -1 + 2 * rand(1);    y = -1 + 2 * rand(1);
        end

        % Iterate that seed a couple hundred times
        for i = warmup_start:warmup_stop
            [x,y] = param_squeezer(x,y,a);
        end

        % Iterate a few more times and print the a value and one of the state 
        %  vars.  For a particular a-value, to where do points tend?
        for i = plot_start:plot_stop
            [x,y] = param_squeezer(x,y,a);
            % Plot radius over a
            printf( "%10.7f %10.7f\n", a, sqrt(x^2+y^2));
        end;
    end;
end;

