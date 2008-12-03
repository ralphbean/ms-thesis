#!/usr/bin/python

# The simulator module contains a few functions for simulating arbitrary
#  *discrete* dynamical systems and approximating their lyapunov spectrums.

# Systems are represented as python dictionaries.  The one-dimensional logistic
#  map will be used here as an example.
logistic_example_system = {
        # The number of variables in the system
        'n' : 1,

        # A list of the values of constants (referenced elsewhere by index)
        'consts' : (4),

        # A python list of lambda expressions.  Every lambda expression 
        #  takes two parameters, a list of constant values and a list of
        #  variable values
        'eqns' :
          ( lambda vars, consts : consts(0) * vars(0) * (1 - vars(0)) )

          }

