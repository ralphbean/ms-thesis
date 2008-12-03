#!/usr/bin/python
from random import random
from math import sqrt, fabs, log

# The simulator module contains a few functions for simulating arbitrary
#  *discrete* dynamical systems and approximating their lyapunov spectrums.

# Systems are represented as python dictionaries.  The one-dimensional logistic
#  map will be used here as an example.
logistic_example_system = {
        # The number of variables in the system
        'n' : 1,

        # A list of the values of constants (referenced elsewhere by index)
        'consts' : [4],

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
    print x
    return [system['eqns'][i](x, system['consts']) for i in range(system['n'])]


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
        warmup_iterations=5,
        measurement_iterations=5,
        trials=1):

    total = 0
    for i in range(trials):
        print i

        # Randmoly generate a n-dimensional initial seed
        x = [random() for j in range(system['n'])]

        for j in range(warmup_iterations):
            x = iterate(system, x)

        for j in range(measurement_iterations):
            # TODO -- instead of picking a random point.. pick one based on
            #  an orthonormalization of the system (re:  Chaos and Time-Series
            #  Analysis by J.C. Sprott


            # Now we begin measuring.
            # First, generate a random point that is a distance of d0 from x
            d0 = 0.0000000001
            y = [random() for k in range(system['n'])]

            ymag = sqrt(sum([ele**2 for ele in y]))         # Get the size of y
            y = [d0 * ele / ymag for ele in y]              # Scale y
            y = [y[k] + x[k] for k in range(system['n'])]   # Translate y to x

            # Sanity check:  # TODO -- we can remove this...
            d1 = sqrt(sum([(x[k]-y[k])**2 for k in range(system['n'])]))
            print "sanity check: ", d0, d1
            epsilon = 1e-6
            assert( fabs(d0-d1) < epsilon )


            # Okay -- actually iterate the two values.
            x = iterate(system, x)
            y = iterate(system, y)
            d1 = sqrt(sum([(x[k]-y[k])**2 for k in range(system['n'])]))
            total = total + log( fabs( d1/d0 ) )

            # TODO -- readjust the orbit so it is d0 away in the direction of d1

    print total
    print total/measurement_iterations
    return total / measurement_iterations 

# Little test stub
def test_lyapunov():
    spectrum = measure_lyapunov(logistic_example_system, 200, 2000, 1)
    print "Finished:"
    print spectrum

# Call the test stub
test_lyapunov()

