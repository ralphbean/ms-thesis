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
        if not A[i][j] == 0:
            # Divide each entry in row i by A[i][j]
            a_ij = float(A[i][j])
            A[i] = [col/a_ij for col in A[i]]

            # Now A[i,j] will have the value 1.
            assert(A[i][j] == 1)

            for u in range(i+1, m):
                # subtract A[u,j] * row i from row u
                A[u] = [A[u][c] - (A[u][j]*A[i][c]) for c in range(len(A[u]))]

                # Now A[u,j] will be 0,
                #  since A[u,j] - A[i,j] * A[u,j] = A[u,j] - 1 * A[u,j] = 0
                assert(A[u][j] == 0)

            i = i + 1
        j = j + 1
    return A

# This function assumes A is already in row-echelon form
def numberOfFreeVariables(A):
    # Strip off the column vector
    V = [row[-1] for row in A]
    A = [row[:-1] for row in A]

    m = len(A)
    n = len(A[0])

    if not m == n:
        raise "A is not square.  Fine in general.. but not for this program."

    count = 0
    for i in range(n):
        if A[i][i] == 0:
            count = count + 1

    return count

def inconsistent(A):
    for row in A:
        possible = True
        for ele in row[:-1]:
            if not ele == 0:
                possible = False
        if possible:
            if not row[-1] == 0:
                return True
    return False


def backsolve(A, assignments):
    raise "Unimplemented."

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
        n = numberOfFreeVariables(A)
        print "n: ", n
someTests()
