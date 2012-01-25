#!/usr/bin/python

import ga
import pylab
import shelve
from random import random
import sys
from load_special_input import load_special_input

if len(sys.argv) != 4:
    print "Invalid number of arguments."
    print "./amplitude_lyapunov.py start stop step"
    sys.exit(0)

start, stop, step = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

#input = load_special_input()
input = [[1,1,1,1],[0,0,0,0]]

for amplitude in pylab.arange(start, stop+step, step):
    lyaps = [ga.lyapunov(input, ga.network, [random(), random()], amplitude)
                                                for i in range(10)]
    print amplitude, sum(lyaps)/float(len(lyaps))
