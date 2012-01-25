

mu = 5.5; % This value is not specified in the paper...


% Generate figure 1 from the paper.
for b = 7:0.05:26
    a = 5;
    %b = 25;
    W = [-a, a; -b, b];

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
        printf( "%10.7f %10.7f\n" , b, x(1,1) );
    end;
end;



