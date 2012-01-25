
a = 5;
b = 25;
W = [-a, a; -b, b];

mu = 1; % This value is not specified in the paper...


% Generate figure 1 from the paper.
for mu = 1:0.005:6

    % Initial x, y values:
    x = [0.1; 0.9];
    %x = rand(2,1);

    % Iterate the net.
    for k = 1:200
        x = sigmoid(W*x, mu);
    end;

    % Iterate the net.
    for k = 1:200
        x = sigmoid(W*x, mu);
        printf( "%10.7f %10.7f\n" , mu, x(1,1) );
    end;
end;



