#!/usr/bin/python


# This is recursive
def det(A, modifier=1):
    if ( len(A) == 2 ):
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    #Otherwise.. laplace's formula:
    d = 0
    for i in range(len(A)):
        M = [row[1:] for row in A[:i]+A[i+1:]]
        d = d + (A[i][0] * modifier * det(M, modifier * -1))
    return d

