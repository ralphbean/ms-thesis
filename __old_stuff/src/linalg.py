#!/usr/bin/python
from math import fabs

epsilon = 10**-12
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
        # Find pivot in column j, starting in row i:
        maxi = i
        for k in range(i+1, m):
            if fabs(A[k][j]) > fabs(A[maxi][j]):
                maxi = k

        if not A[maxi][j] == 0:
            # Swap rows i and maxi but do not change the value of i
            swp = A[i]
            A[i] = A[maxi]
            A[maxi] = swp

            # Divide each entry in row i by A[i][j]
            a_ij = float(A[i][j])
            A[i] = [col/a_ij for col in A[i]]

            # Now A[i,j] will have the value 1.
            assert(A[i][j] == 1)

            for u in range(i+1, m):
                # subtract A[u,j] * row i from row u
                A[u] = [A[u][c] - (A[u][j]*A[i][c]) for c in range(len(A[u]))]
                for k in range(len(A[u])):
                    if ( A[u][k] != 0 and 
                            A[u][k] < epsilon and 
                            A[u][k] > -epsilon ):
                        A[u][k] = 0

                # Now A[u,j] will be 0,
                #  since A[u,j] - A[i,j] * A[u,j] = A[u,j] - 1 * A[u,j] = 0
                assert(A[u][j] == 0)

            i = i + 1
        j = j + 1
    return A

def is_upper_triangular(A):
    ret = True 
    for i in range(0, len(A)):
        for j in range(0, i-1):
            if A[i][j] != 0:
                ret = ret and False 
    return ret


# This function assumes A is already in row-echelon form and returns a list
#  of the indices of the free variables.
def determineFreeVariables(A):
    # Strip off the column vector
    V = [row[-1] for row in A]
    A = [row[:-1] for row in A]

    m = len(A)
    n = len(A[0])

    if not m == n:
        raise "A is not square.  Fine in general.. but not for this program."
    free = []
    for i in range(n):
        if A[i][i] == 0:
            free = free + [i]
    return free

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


# Backsolve returns a vector of length n containing assignments for
#  every variable in the system described by A.
# Assignments is a dictionary (potentially empty) mapping free variable indices
#  to some random values
def backsolve(A, assignments):
    V = [row[-1] for row in A]
    A = [row[:-1] for row in A]
    solution = {}
    for i in range(len(A)-1,-1,-1):
        if i in assignments.keys():
            solution[i] = assignments[i]
        else:
            sum = 0
            for j in range(i,len(A[i])):
                if j == i:
                    assert A[i][j] == 1
                    continue # Assume the diagonal is 1
                sum = sum + (A[i][j] * solution[j])
            solution[i] = V[i] - sum
    assert(len(solution.keys()) == len(A))
    return solution

