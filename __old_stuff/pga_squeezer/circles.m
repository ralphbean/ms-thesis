% make a few circles

R = 10;    % number of radii
N = 10000; % number of points on a circle
pi2 = 2*pi;

for r = 1:R
	for a = 1:N
		theta = (a/N) * pi2;
		[u,v] = squeezer(  (r/R) * cos(theta), (r/R) * sin(theta) ) ;
		[u,v] = squeezer( u, v );
		[u,v] = squeezer( u, v );
		printf( "%9.5f %9.5f\n",  u, v );
		% printf( "%9.5f %9.5f\n",  (r/R) * cos(theta), (r/R) * sin(theta) );
	end;
	printf("\n");
end;
