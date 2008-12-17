#!/usr/bin/python
from math import fabs

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

def gaussianElim(A):
    m = len(A)
    n = len(A[0])
    i = 0
    j = 0
    while (i < m and j < n ):
        print "A: ",i,j
        for row in A:
            print row
        # Find pivot in column j starting in row i:
        maxi = i
        for k in range(i+1, m):
            if fabs(A[k][j]) > fabs(A[maxi][j]):
                maxi = k
        if not A[maxi][j] == 0:
            # Swap rows i and maxi, but do not change the value of i
            swp = A[i]
            A[i] = A[maxi]
            A[maxi] = swp
            # Divide each entry in row i by A[i][j]
            a_ij = float(A[i][j])
            A[i] = [col/a_ij for col in A[i]]
            # Now A[i,j] will have the value 1.
            assert(A[i][j] == 1)
            for u in range(i+1, m):
                print "A: ",i,j
                for row in A:
                    print row
                # subtract A[u,j] * row i from row u
                A[u] = [A[u][c] - (A[u][j]*A[i][c]) for c in range(len(A[u]))]
                # Now A[u,j] will be 0,
                #  since A[u,j] - A[i,j] * A[u,j] = A[u,j] - 1 * A[u,j] = 0
                assert(A[u][j] == 0)

            i = i + 1
        j = j + 1
    return A


A = [
        [ 9,3,4,7],
        [ 4,3,4,8],
        [ 1,1,1,3]
    ]
B = gaussianElim(A)
C = [row[:-1] for row in B]
V = [row[-1] for row in B]
print "C:"
for row in C:
    print row
print "V:"
for row in V:
    print row
