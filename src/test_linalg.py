#!/usr/bin/python
from linalg import determineFreeVariables, gaussianElim, inconsistent
from linalg import det, backsolve
from random import random

def someTests():
    As = [[
            [ 1, 1, 1, 3 ],
            [ 2, 3, 7, 0 ],
            [ 1, 3, -2, 17 ]
        ],[
            [ 9,3,4,7],
            [ 4,3,4,8],
            [ 1,1,1,3]
        ],[
            [2, 1, -1, 8],
            [-3,-1,2,-11],
            [-2,1,2,-3]
        ],[
            [2, 4, 5, 47],
            [3, 10, 11, 104],
            [3, 2, 4, 37]
        ],[
            [1,2,4],
            [2,4,9]
        ]]
    for A in As:
        print
        print "Original A"
        for row in A:
            print row
        B = gaussianElim(A)
        C = [row[:-1] for row in B]
        V = [row[-1] for row in B]
        print "C:"
        for row in C:
            print row
        print "V:", V
        print "det(C):", det(C),
        print "Inconsistent?: ", inconsistent(B),
        n = determineFreeVariables(B)
        print "free: ", n
        free = {}
        for free_var in n:
            free[free_var] = random()
            print "Free variable assignment:", free_var,"->",free[free_var]

        print "solution:", backsolve(B, free)

someTests()

