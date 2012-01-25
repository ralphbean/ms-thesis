% chaos.m

for i = -2:0.1:2
  printf( "%10.7f %10.7f\n" , i, tanh(i) );
end;
for i = -2:0.1:2
  printf( "%10.7f %10.7f\n" , i, (1+e^(-i))^-1 );
end;

