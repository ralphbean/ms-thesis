#!/usr/bin/python

# constraint.py is a module that deals with systems of contraints and inputs
#  and can instantiate satisfactory systems

import sys
from math import sqrt, tanh
import linalg
import simulator
from random import random, randint


# Takes a tree as a dictionary and prints its nodes inorder
def tree_to_inorder_string(root):
    retval = ""
    if ( len(root.keys()) > 1 ):
        retval = retval + "("

    if ( root.__contains__('left') ):
        retval = retval + tree_to_inorder_string(root['left'])

    if root['type'] == 'operator':
        retval = retval + root['value']
    elif root['type'] == 'parameter':
        retval = retval + "a_{" + root['value'] + "}"
    elif root['type'] == 'constant':
        retval = retval + root['value']
    else:
        raise ValueError, "Undefined data type in inorder traversal."

    if ( root.__contains__('right') ):
        retval = retval + tree_to_inorder_string(root['right'])
    if ( len(root.keys()) > 1 ):
        retval = retval + ")"

    return retval


# Takes the dictionary structure of a system input and prints it in
#  human-readable form
def input_to_string( input ):
    s = "f(a_{0}) = " + tree_to_inorder_string(input['eqn']) 
    return s

ops = { '^' : (lambda x,y : x**y),
        '*' : (lambda x,y : x * y),
        '/' : (lambda x,y : x / y),
        '+' : (lambda x,y : x + y),
        '-' : (lambda x,y : x - y)}

def function_as_lambda(func):
    if func['type'] == 'operator':
        left = function_as_lambda(func['left'])
        righ = function_as_lambda(func['right'])
        return lambda x : ops[func['value']](left(x),righ(x))
    elif func['type'] == 'parameter':
        return lambda x : float(x)
    elif func['type'] == 'constant':
        return lambda x : float(func['value'])
    else:
        raise "Malformed function."

def input_as_lambdas(input):
    t = lambda v, c : v[0] + input['dx']
    f = lambda v, c : function_as_lambda(input['eqn'])(v[0])
    return [t,f]

def build_random_function():
    choice = randint(0,3)
    node = {}
    if choice == 0:
        node['type'] = 'operator'
        operators = ['^', '*', '/', '+', '-']
        node['value'] = operators[randint(0,4)]
        node['left'] = build_random_function()
        node['right'] = build_random_function()
    elif choice == 1:
        # Only doing 1 dimensional.  So there is only one parameter.
        node['type'] = 'parameter'
        node['value'] = str(0)
    else:
        node['type'] = 'constant'
        node['value'] = str((random()*10)-5)
    return node

def build_random_input():
    input = {}
    input['dx'] = 1 #random()
    input['eqn'] = build_random_function()
    return input

# Determines the number of free variables.  Randomly assigns them.  Finally
#  backpropagates the values to the dependent variables and returns the
#  resulting system.
#
# Raises an exception if the set of contraints is unsatisfiable!
def instantiate( constraints, input, num_copies=1 ):
    A = [row for row in constraints]    # Make a copy.

    if linalg.inconsistent(A):
        raise "Unsatisfiable."

    # http://en.wikipedia.org/wiki/Gaussian_elimination
    #print "Doing gaussian elimination for instantiation."
    A = linalg.gaussianElim(A)

    free_vars = linalg.determineFreeVariables(A)
    #print "Num free vars:", len(free_vars)

    networks = [] # List to return
    for i in range(num_copies):
        assignments = {}
        for var in free_vars:
            assignments[var] = random()

        solution = linalg.backsolve(A, assignments)

        # If there are N elements of the solution, that amounts to
        #  sqrt(N) neurons with N connection weights between them all.
        n = int(sqrt(len(solution)))
        network = {
                'n' : n + 2,
                'consts' : [val for val in solution.values()],
                'eqns' : 
                    input_as_lambdas(input) +
                    [ lambda v, c : tanh(sum([v[j+2] + c[i*n + j]
                        for j in range(n)])) for i in range(n)]
                }
        networks.append(network)
    return networks 

def tests():
    # Come up with a set of test constraints...
    n = 10**2 
    # TODO -- linalg is not done. 
    # TODO -- Do n = 16 with randint(-1,2).  It breaks all the time.
    A = [[(random()*2)-1 for j in range(n+1)] for i in range(n)]
    input = build_random_input()
    print "Input is:", input_to_string(input)

    networks = instantiate(A, input)
    print len(networks)
    for network in networks:
        print "Lyapunov measurement is:", simulator.measure_lyapunov(network)
    while ( True ):
        A = [[(random()*2)-1 for j in range(n+1)] for i in range(n)]
        input = build_random_input()
        networks = instantiate(A, input)
        lyap = simulator.measure_lyapunov(networks[0])
        if lyap > 0:
            print lyap, "lyap.  ", input_to_string(input)


tests()
