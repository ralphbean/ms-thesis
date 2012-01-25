% chaos.m

x = 0.22345; y = 0.6789;

for i = 1:100000
  [x,y] = squeezer(x,y);
end;

for i = 1:100000
  [x,y] = squeezer(x,y);
  printf( "%10.7f %10.7f\n" , x, y );
end;
