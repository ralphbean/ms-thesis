#!/home/ralph/j602/bin/jconsole
NB. fetch command line parameters
NB. parameters
N =: 10  NB.  weights matrix size
NB. above got all right
cos    =: 2 & o.
theta =: 0.2  NB.  
P =: 15   NB.  number of patterns
print   =: 1!:2 & 2
mp      =: +/ . *         NB. matrix product.
LF      =: 10 { a.  NB. line feed character
fwrite  =: 1!:2
OUT     =: 4 : ' ( , (": x), "1 LF) fwrite < y ' NB.   data OUT file
NB. ============================================
NB.  Several versions of "poly" function. Last is used.
poly    =: 3 : '(mask =. , <:/~ i.   #y) # , */~   y' NB. no bias
poly    =: 3 : '1,y'  NB.  Try the data plain, for comparison
poly    =: 3 : '(mask =. , <:/~ i. 1+#y) # , */~ 1,y'  NB. better
NB. ============================================
blank =: ' '
maxy  =: ] = (>./)  NB.  show maxima in binary vector
tanh  =: 7 & o.

arglist =. >ARGV_z_
NB. ying =. trim 2 { arglist
print 'args', ": seed =. do {:  arglist
print seed+1
9!:1 seed

W       =: 1 -~ 2 * ? ((N+2) , N) $ 0  NB.  weights matrix
pattern =: 3 : '(,~y)# _1 1' NB. Frequency
pattern =: 3 : '(1,y)# 1 _1' NB. Density
data    =: pattern each < "0 (1 + i.P)
submod  =: 4 : 'y {~ (#y)|x'  NB.  subscript mod pattern length

makeXZ =: 4 : 0 NB. This routine makes the X and Z matrics
   warm_up =. x [ total_reps =. y
   X =: (0,(#poly N#0))$0  NB.  initialize the matrix of inputs
   Z =: (0,P)$0            NB.  initialize the matrix of targets
   for_p.  i.P  do.        NB.  for each pattern
	  target =. 1 -~ 2 * p = i.P  NB. bi-polar target
	  pat =. > p { data
      Xnow =. N$0
	  for_t. i. total_reps do.
         Xnow =. tanh ( 1, (cos p*theta*t) , Xnow)  mp  W
         NB. Xnow =. tanh ( ( t submod pat ) 0 } Xnow)  mp  W
		 if. t >: warm_up do.
		   X =: X, poly Xnow  NB.  append vectors to matrices
		   Z =: Z, target
		 end.
	  end.
   end.
)

100 makeXZ 600
psi =: Z %. X  NB.  pseudo inverse

answ =: maxy "1 raw_output =. X mp psi

yes_ct =. ": yes =. +/(Z>0) -: "1 answ
pct =. (8j3": 100*yes%#answ),'%'
print 'Size of matrix W: ', ": #W
print 'Number of patterns: ', ":P
print 'Theta max: ', ": theta
print 'Correct ', yes_ct,' out of ',(":#answ),pct

NB. Write file 'top2' of 2 largest output activations
(7j3 ": top2 =. 2 {. "1 \:~ "1 raw_output) OUT 'top2'

NB.  Make the confusion matrix
target_actual =: (Z>0) ,. answ
yes_count =: 3 : 0
   ind =. ( (0{y) = i.P ) , ( (1{y) = i.P ) 
   +/ target_actual -: "1 1 ind
)

table =: (<@,)"0 0/~ i.P
print 4j0 ": each yes_count each table

test =: 4 : 0
  NB. Set up a test.
  NB. Start theta at 0.05, increase by dtheta of 0.0005 each time step
  X =: (0,(#poly N#0))$0  NB.  initialize the matrix of inputs
  Xnow =. N$0
  theta =. 0.0  [ dtheta =. x
  for_t. i. y do.
     X =: X, poly Xnow =. tanh ( (1 2 o. theta*t) (0 1) } Xnow)  mp  W
     theta =. theta + dtheta
  end.

  values =: (i.P) #~ "1 answ =: maxy "1 raw_output =. X mp psi
  values OUT 'values'
)
NB. 0.0000065 test 80000
exit 99 NB. ==================================================
