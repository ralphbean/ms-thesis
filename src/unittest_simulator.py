#!/usr/bin/python

from simulator import measure_lyapunov
from simulator import logistic_example_system

from random import random
from math import tanh

# Little test stub which yields values consistent with those in the literature.
def test_logistic_lyapunov():
    some_test_values = [1, 1.9, 1.999, 2, 2.001, 2.1, 3,
                        3.236067977, 3.5699456720,
                        3.56994571869, 3.828427125,
                        3.9, 4]
    for i in some_test_values:
        logistic_example_system['consts'][0] = i
        print "",i, measure_lyapunov(logistic_example_system, 2000, 4000, 1)

# Another test routine to investigate various simple ANNs
def test_ANN_lyapunov():
    some_test_values = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    network = { 'n': 1,
            'consts' : [1, 1],
            'eqns' :
              [ lambda vars, consts : tanh(vars[0]*consts[0] + consts[1]) ] }

    for n in range(1,10):
        network = { 'n' : n,
            'consts' : [random() for i in range(n**2 + n)],
            'eqns' : [ lambda v, c : 
                tanh(sum([v[j]+c[i*n+j] for j in range(n)])) 
                + c[-i] for i in range(n)] }
        print "n =", n, ":",
        lyap = measure_lyapunov(network, 0, 3, 1)
        assert(lyap < 0)   # By way of Bean's Grand Nonexistence Theorem (!)
        print lyap

def test():
    print "logistic test:"
    test_logistic_lyapunov()
    print "ANN test:"
    test_ANN_lyapunov()

test()

