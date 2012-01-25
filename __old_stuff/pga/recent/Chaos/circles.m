% make a few circles

R = 10;    % number of radii
N = 10000; % number of points on a circle

for theta = 1:N
	for r = 1:R
		[u,v] = squeezer(  (r/R) * cos(theta), (r/R) * sin(theta) ) ;
		printf( "%9.5f %9.5f\n",  u, v );
		% printf( "%9.5f %9.5f\n",  (r/R) * cos(theta), (r/R) * sin(theta) );
	end;
end;
