% Simulate a chaotic neural network.. Identify a potential period-3 repelling
%  orbit.  Perturb the simulation of the network to stabilize on the otherwise
%  repellant period-3 orbit.
n = 3;
a = 5;  b = 25;  W = [-a, a; -b, b];  % Weight matrix for the network
mu  = 5.5;   % mu value for the sigmoid
alp = 0.5;   % alpha value.. scales amount of perturbation
eps = 0.002; % epsilon.. how close to a period-n orbit do we want/need to be?
turn_off_control = 150;  % How long do we leave the controlling-input on?
num_iters = 400;

x = [0.1; 0.9];  % arbitrarily chosen

% 'Warm up the system'
for k = 1:200
    x = sigmoid(W*x, mu);
end

X = rand(2,n)./eps;
% Search for a close return triplet
for k = 1:num_iters
    for j = 1:(n-1);
        X(:,j) = X(:,j+1);
    end
    X(:,n) = x;
    x = sigmoid(W*x, mu);
    if norm(x - X(:,1)) <= eps, break; end;
end;

% Start again...
x = [0.1; 0.9];  % arbitrarily chosen

% 'Warm up the system' again.
for k = 1:200
    x = sigmoid(W*x, mu);
end

cc = 0; % cc stands for 'control counter'
for k = 1:num_iters
    u(:, k) = [0,0];  % Default padding.

    % Turn on control when rdy
    cc = cc + (norm(x(:,k) - X(:,2)) <= eps && ! cc);
    if cc > 0 && cc < turn_off_control,
        i = mod(cc,n)+1;
        u(:,k)=-sigmoid(W*x(:,k),mu)+sigmoid(W*X(:,i),mu)+alp*x(:,k)-alp*X(:,i);
        cc = cc + 1;
    end;
    x(:, k+1) =  sigmoid( W*x(:, k), mu ) + u(:, k);

    printf( "%10.7f %10.7f\n", k, x(1,k));
end;

