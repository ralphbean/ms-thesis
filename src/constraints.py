#!/usr/bin/python

# constraint.py is a module that deals with systems of contraints and inputs
#  and can instantiate satisfactory systems

import linalg

# Takes a tree as a dictionary and prints its nodes inorder
def tree_to_inorder_string(root):
    retval = ""
    if ( len(root.keys()) > 1 ):
        retval = retval + "("

    if ( root.__contains__('left') ):
        retval = retval + tree_to_inorder_string(root['left'])

    # This must exist, or we have an invalid tree
    data = root['data']

    # Data can be either a variable, constant, or operator
    if data['type'] == 'operator':
        retval = retval + data['value']
    elif data['type'] == 'parameter':
        retval = retval + "a_{" + data['value'] + "}"
    elif data['type'] == 'constant':
        retval = retval + data['value']
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
    s = "x0:" + str(input['x0']) + "\n"
    s = s + "dx:" + str(input['dx']) + "\n"
    s = s + tree_to_inorder_string(input['eqn'])
    return s

# Determines the number of free variables.  Randomly assigns them.  Finally
#  backpropagates the values to the dependent variables and returns the
#  resulting system.
#
# Raises an exception if the set of contraints is unsatisfiable!
def instantiate( constraints, input ):
    M = constraints[0]
    V = constraints[1]
    if linalg.det(M) == 0:
        raise "Unsatisfiable."
    # TODO -- write this using:
    # http://en.wikipedia.org/wiki/Gaussian_elimination



    return {}

# Eliminates redundancy and reorganizes a set of contraints to be... simpler.
def simplify( constraints ):
    return constraints
