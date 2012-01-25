function y = frac(x);
	y = x - floor(x);
end;

function [x,y] = lps_pt(n,A,B);
	x = frac(n*A)*2-1;
	y = frac(n*B)*2-1;
end;

function circle(x,y,r,n);
	dtheta = pi*2/n;
	for i = 1 : n
		theta = i * dtheta;
		u = r*cos(theta)+x;
		v = r*sin(theta)+y;
		[u,v] = squeezer( u,v );
		[u,v] = squeezer( u,v );
		[u,v] = squeezer( u,v );
		[u,v] = squeezer( u,v );
		[u,v] = squeezer( u,v );
		printf( "%8.4f %8.4f\n", u,v );
	end;
	printf("\n");
end;
A = 1;
for i = 1:15
	A = (3*A^2 - A^3 + 1)/(3*A - 1);
end;
B = A^2;

N = 100;
R = 0.03;
M = 450;
for n = 1: M
	[x,y] = lps_pt(n,A,B);
	if x^2 + y^2 + R >= 1; continue; end;
	% printf( "%8.4f %8.4f\n", x, y );
	circle( x, y, R, N );
end;
