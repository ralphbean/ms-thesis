#!/usr/bin/python
from random import random
from math import sqrt, fabs, log, tanh

# The simulator module contains a few functions for simulating arbitrary
#  *discrete* dynamical systems and approximating their lyapunov spectrums.

# Systems are represented as python dictionaries.  The one-dimensional logistic
#  map will be used here as an example.
logistic_example_system = {
        # The number of variables in the system
        'n' : 1,

        # A list of the values of constants (referenced elsewhere by index)
        'consts' : [3.9],

        # A python list of lambda expressions.  Every lambda expression 
        #  takes two parameters, a list of constant values and a list of
        #  variable values
        'eqns' :
          [ lambda vars, consts : consts[0] * vars[0] * (1 - vars[0]) ]

          }


# The iterate function takes a system and a state vector x.  The change rules
#  encoded in the system dictionary are applied to x and the subsequent image
#  it returned.
def iterate(system, x):
    next = []
    for i in range(system['n']):
        try:
            val = system['eqns'][i](x, system['consts'])
        except StandardError, e:
            val = 0 # Division by zero or (-1)^(1/2)
        next.append(val)
    return next
    #return [system['eqns'][i](x, system['consts']) for i in range(system['n'])]


# The measure_lyapunov function takes a system and returns the largest lyapunov
#  value of the system.
#
#  There are three optional parameters:
#    warmup_iterations describes how many times the system should be iterated
#      before measuring to get the orbit closer to the potentially chaotic 
#      attractor.
#    measurement_iterations describes how many times we should iterate the
#      system while approximating the lyapunov spectrum.
def measure_lyapunov(
        system,
        warmup_iterations=500,
        measurement_iterations=1000,
        trials=8):

    epsilon = 1e-6
    total = 0
    for i in range(trials):
        # Randomly generate a n-dimensional initial seed
        x = [random() for j in range(system['n'])]

        for j in range(warmup_iterations):
            x = iterate(system, x)

        # First, generate a random point that is a distance of d0 from x
        d0 = 0.0000000001
        y = [random() + x[k] for k in range(system['n'])]

        for j in range(measurement_iterations):
            y = [y[k] - x[k] for k in range(system['n'])]  # Translate y from x
            ymag = sqrt(sum([ele**2 for ele in y]))        # Get the size of y
            if ( ymag == 0 ):
                ymag = ymag + epsilon
            y = [d0 * ele / ymag for ele in y]             # Scale y
            y = [y[k] + x[k] for k in range(system['n'])]  # Translate y to x

            # Okay -- actually iterate the two values.
            x = iterate(system, x)
            y = iterate(system, y)
            d1 = sqrt(sum([(x[k]-y[k])**2 for k in range(system['n'])]))
            quotient = fabs( d1/d0 )
            if ( quotient == 0 ):
                quotient = quotient + epsilon
            total = total + log( quotient )
    lyap = total / (measurement_iterations * trials)
    return lyap

