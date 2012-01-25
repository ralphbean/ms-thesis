#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, misc, metrics
from random import random
from math import log

# Natural number.  The larger the more precise.  1 is as low as it goes.
precision = 1

amplitude = 1 # Dummy
ep_stop = float(sys.argv[1])
length = float(sys.argv[2])
ep = length/2.0
while ep > ep_stop:
    # Divide up the half-unit square into boxes of size ep
    num_lengths = int(length/ep)
    not_in, num_in = 1, 1
    xy_pairs = []
    #print length
    #print length/ep
    #print num_lengths
    for i in range(num_lengths):
        for j in range(num_lengths):
            # Center of the box:
            x,y = i*ep + (ep/2.0)-(length/2.0), j*ep + (ep/2.0)-(length/2.0)
            xy_pairs.append( [x,y] )
    ## Sanity checks:
    #xs = [ele[0] for ele in xy_pairs]
    #ys = [ele[1] for ele in xy_pairs]
    #print min(xs),max(xs), min(ys), max(ys), sum(xs)/float(len(xs)), sum(ys)/float(len(ys))
    for pair in xy_pairs:
        x,y = pair
        input = [[x,y],[0,0]]
        lyaps = [metrics._lyapunov( input,
                    maps.network,
                    [random(), random()],
                    amplitude)
                          for count in range(precision)]
        lyap = sum(lyaps)/float(len(lyaps))
        if lyap > 0:
            not_in = not_in + 1
        else:
            num_in = num_in + 1
    print "%f, %f" % (ep, log(num_in)/log(1/ep))
    #ep = ep - 0.0001
    ep = ep / 2

