  for a = 1:628
  	[x,y] = squeezer(cos(a/100),sin(a/100));
  	printf( "%10.7f %10.7f\n" , x, y );
  end
