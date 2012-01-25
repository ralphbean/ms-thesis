#!/usr/bin/python

import ga
import pylab
from random import random
import sys
from load_special_input import load_special_input

if len(sys.argv) != 4:
    print "Invalid number of arguments."
    print "./amplitude_bifurcation.py start stop step"
    sys.exit(0)

start, stop, step = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

input = load_special_input()

for amplitude in pylab.arange(start, stop+step, step):

    for trials in range(5):
        # TODO - Try fixing the seed.
        x = [random(), random()]

        for i in range(200):
            x = ga.network(x)
            x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
            x[1] = x[1] + ( amplitude * input[1][i % len(input[1])] )

        for i in range(200):
            x = ga.network(x)
            x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
            x[1] = x[1] + ( amplitude * input[1][i % len(input[1])] )
            print amplitude, x[0]

