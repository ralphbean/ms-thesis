#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, misc
from random import random

if len(sys.argv) != 3:
    print "Invalid number of arguments."
    print "./pop_bifurcation.py <ID> <size>"
    sys.exit(0)

ID = sys.argv[1]
size = sys.argv[2]

# The hero!
o = shelve.open("../dat/"+ID+"/"+ID+".2999.pop")['pop'][0]
if size == 'local':
    step = 0.000000001
    start = o['amplitude'] - step*1000
    stop = o['amplitude'] + step*1000
elif size == 'global':
    start = 0
    step = 0.00001
    stop = 0.03
else:
    raise ValueError, "wtf!"
input = o['org']

for amplitude in misc.arange(start, stop+step, step):
    for trials in range(4):
        x = [random(), random()]

        for i in range(300):
            x = maps.network(x)
            x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )

        for i in range(300):
            x = maps.network(x)
            x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
            print amplitude, x[0]

