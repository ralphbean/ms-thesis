#!/usr/bin/python

import sys
from time import sleep
if ( len(sys.argv) == 1 ):
    print "trial ID is required."
    sys.exit()
# Takes time to load:
import pylab

def load_fitnesses(ID):
    F = open("../dat/" + str(ID) +".fit", "r")
    lines = F.readlines()
    # Chew carriage return
    lines = [line[:-1] for line in lines]
    toks = [line.split(",") for line in lines]
    fits = [[float(ele) for ele in tok] for tok in toks]
    return fits





trial_ID = sys.argv[1]
while( True ):
    try:
        fits = load_fitnesses(trial_ID)
        pylab.hold(True)
        #for i in range(len(fits)):
            #pylab.plot([i for j in range(len(fits[i]))],
            #           [float(val) for val in fits[i]],
            #           'b.')
        for i in range(len(fits[0])):
            pylab.plot([j for j in range(len(fits))],
                   [fits[j][i] for j in range(len(fits))],
                   'b-')
        pylab.hold(False)
        pylab.show()
        pylab.cla()
    except IOError:
        print "Waiting on", sys.argv[1], "to appear."
        sleep(10)


