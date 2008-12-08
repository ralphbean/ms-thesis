#!/usr/bin/python

# constraint.py is a module that deals with systems of contraints and inputs
#  and can instantiate satisfactory systems


# Takes a tree as a dictionary and prints its nodes inorder
def tree_to_inorder_string(root):
    retval = ""
    if ( root.__contains__('left') ):
        retval = retval + tree_to_inorder_string(root['left'])
    retval = retval + root['data']
    if ( root.__contains__('right') ):
        retval = retval + tree_to_inorder_string(root['right'])
    return retval

# Takes the dictionary structure of a set of contraints and prints them in
#  human-readable form
def constraints_to_string( constraints ):
    n = constraints['n']
    retval = "Constraints.   n =" + n
    for c in constraints:
        retval = retval + "\n" + tree_to_inorder_string(c)
    return retval

# Takes the dictionary structure of a system input and prints it in
#  human-readable form
def input_to_string( input ):
    print "TODO"

# Returns true if a system satisfies the given set of constraints and associated
#  input
def satisfactory( system, constraints, input ):
    return false

# Determines the number of free variables.  Randomly assigns them.  Finally
#  backpropagates the values to the dependent variables and returns the
#  resulting system.
#
# Raises an exception if the set of contraints is unsatisfiable!
def instantiate( constraints, input ):
    constraints = simplify(constraints)
    return {}

# Eliminates redundancy and reorganizes a set of contraints to be... simpler.
def simplify( constraints ):
    return constraints
