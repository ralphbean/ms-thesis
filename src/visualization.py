#!/usr/bin/python

import sys
from time import sleep
from math import sqrt
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


def load_freevar_count(ID):
    F = open("../dat/" + str(ID) + ".fre", "r")
    lines = F.readlines()
    lines = [line[:-1] for line in lines]
    toks = [line.split(",") for line in lines]
    frees = [[float(ele) for ele in tok] for tok in toks]
    frees = frees[-1]
    return range(len(frees)), frees
def load_diversity(trial_ID):
    F = open("../dat/" + str(trial_ID) + ".div", "r")
    lines = [line[:-1] for line in F.readlines()]
    toks = [line.split(",") for line in lines]
    divs = [[float(ele) for ele in tok] for tok in toks]
    return divs

def fitness_over_time(trial_ID):
    fits = load_fitnesses(trial_ID)
    pylab.hold(True)
    lf = len(fits)
    lfi = len(fits[0])
    lfi2 = lfi/2
    indices = [j for j in range(len(fits))]
    means = [sum(fits[i])/float(lfi) for i in range(lf)]
    s_dev = [sqrt(sum([(fits[i][j]-means[i])**2 for j in range(lfi)])/(lfi-1)) 
                                  for i in range(lf)]
    # Plot all:
    pylab.plot( [j for j in range(len(fits))], fits, 'b.')
    pylab.plot(indices, means, 'r-')
    pylab.plot(indices, [means[i]-s_dev[i] for i in range(lf)], 'g-')
    pylab.plot(indices, [means[i]+s_dev[i] for i in range(lf)], 'g-')
    pylab.hold(False)
    pylab.title('Population fitnesses.')
    pylab.show()
    pylab.cla()

    divs = load_diversity(trial_ID)
    pylab.plot([j for j in range(len(divs))], [e[0] for e in divs], 'r-')
    pylab.title('Constraint diversity')
    pylab.show()
    pylab.cla()
    pylab.plot([j for j in range(len(divs))], [e[1] for e in divs], 'r-')
    pylab.title('Input diversity')
    pylab.show()
    pylab.cla()

def free_vars_count(trial_ID):
    possible, counts = load_freevar_count(trial_ID)
    pylab.plot(possible, counts, 'b-')
    pylab.show()
    pylab.cla()

trial_ID = sys.argv[1]
while( True ):
    try:
       #free_vars_count(trial_ID)
       fitness_over_time(trial_ID)
    except IOError:
        print "Waiting on", sys.argv[1], "to appear."
        sleep(10)
