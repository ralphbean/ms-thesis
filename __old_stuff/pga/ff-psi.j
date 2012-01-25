#!/usr/bin/env jconsole
print   =: 1!:2 & 2
mp      =: +/ . *         NB. matrix product.
LF      =: 10 { a.  NB. line feed character
fwrite  =: 1!:2
OUT     =: 4 : ' ( , (": x), "1 LF) fwrite < y ' NB.   data OUT file
tanh  =: 7 & o.

NB. arglist =. >ARGV_z_
NB. ying =. trim 2 { arglist
NB. print 'args', ": seed =. do {:  arglist
NB. psi =: Z %. X  NB.  pseudo inverse

NB.  Data for y = x ( 1 - x )
N =: 35  NB.  number of points
J =: 6 NB. size of the hidden layer NB. need 4 for cubic, 3 for quadratic, 6 for 4th
x =: N %~ i. 1+N  NB.  x steps 0 to 1
Z =: 4*x * (1-x)    NB.  quadratic function
Z =: 4*x*x * (1-x)  NB.  cubic function
Z =: 4*x*x*x * (1-x)  NB.  4th order function
X =: |: 1 ,. x  NB.  append bias to the input


iterate =: 3 : 0
   for_i. i.y do.
     if. i = 0 do. W =: 1 -~ 2 * ? (J,2)$0  NB. random weights
     else.         W =: |: (|: Y) %. |: X   NB. psi weights
	 end.
     Y =: tanh W mp X
     V =: Z %. |: Y
     Actual =: V mp Y
     maxe =: >. / | Z - Actual
     ssqe =: + / 2 ^~ Z - Actual
     print 13j8 ": maxe, ssqe
   end.
)

iterate 10

(,.Z) OUT ',target'
(,.Actual) OUT ',actual'

exit 99 NB. ==================================================
