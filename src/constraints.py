
from random import random, randint
from math import sqrt, tanh
import inputs
import linalg
import simulator


# constraint.py is a module that deals with systems of contraints and inputs
#  and can instantiate satisfactory systems

# Determines the number of free variables.  Randomly assigns them.  Finally
#  backpropagates the values to the dependent variables and returns the
#  resulting system.
#
# Raises an exception if the set of contraints is unsatisfiable!
def instantiate( constraints, input, num_copies=1 ):
    A = [row for row in constraints]    # Make a copy.

    if linalg.inconsistent(A):
        raise Exception, "Unsatisfiable."

    # http://en.wikipedia.org/wiki/Gaussian_elimination
    A = linalg.gaussianElim(A)

    free_vars = linalg.determineFreeVariables(A)

    networks = [] # List to return
    for i in range(num_copies):
        assignments = {}
        for var in free_vars:
            assignments[var] = random()*20 - 10

        solution = linalg.backsolve(A, assignments)

        # If there are N elements of the solution, that amounts to
        #  sqrt(N) neurons with N connection weights between them all.
        n = int(sqrt(len(solution)))
        network = {
                'n' : n + 2,
                'consts' : [val for val in solution.values()],
                'eqns' : 
                    inputs.input_as_lambdas(input) +
                    [ lambda v, c : tanh(sum([v[j+2] + c[i*n + j]
                        for j in range(n)])) for i in range(n)]
                }
        networks.append(network)
    return networks 

# n is the size of the neural net
def build_random_constraints(n):
    return [[r_val() for j in range(n**2 + 1)] for i in range(n**2)]
def r_val():
    return randint(0,1)*(random()*20-10)
