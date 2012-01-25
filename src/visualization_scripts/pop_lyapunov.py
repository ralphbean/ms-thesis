#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, metrics, misc
from random import random

if len(sys.argv) != 3:
    print "Invalid number of arguments."
    print "./pop_lyapunov.py <ID> <size>"
    sys.exit(0)
ID = sys.argv[1]
size = sys.argv[2]

#The hero!
o = shelve.open("../dat/"+ID+"/"+ID+".2999.pop")['pop'][0]
if size == 'local':
    step = 0.000000001
    # Increase back up to 1000
    start = o['amplitude'] - step*1000
    stop = o['amplitude'] + step*1000
elif size == 'global':
    start = 0
    step = 0.000001
    stop = 0.03
else:
    raise ValueError, "wtf!"
input = o['org']

for amplitude in misc.arange(start, stop+step, step):
    lyaps = [metrics._lyapunov( input,
                                maps.network,
                                [random(), random()],
                                amplitude)
                                    for i in range(10)]
    print amplitude, sum(lyaps)/float(len(lyaps))

