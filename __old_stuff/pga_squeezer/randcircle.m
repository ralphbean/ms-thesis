% randcircle.m

for i = 1 : 10000
	x = -1 + 2 * rand(1);
	y = -1 + 2 * rand(1);
	if x^2 + y^2 < 1
		[x,y] = squeezer(x,y);
		printf( "%10.7f %10.7f\n" , x, y );
	end;

end;
