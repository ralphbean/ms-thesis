#!/usr/bin/python

# constraint.py is a module that deals with systems of contraints and inputs
#  and can instantiate satisfactory systems

# Takes the dictionary structure of a set of contraints and prints them in
#  human-readable form
def print_constraints( constraints ):
    print "TODO"

# Takes the dictionary structure of a system input and prints it in
#  human-readable form
def print_input( input ):
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
