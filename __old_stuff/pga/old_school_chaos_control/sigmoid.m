function sig = sigmoid(Z, mu)
sig = (1 + e.^(-mu.*Z)).^-1;

