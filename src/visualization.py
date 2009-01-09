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


def load_freevar_count(ID):
    F = open("../dat/" + str(ID) + ".fre", "r")
    lines = F.readlines()
    lines = [line[:-1] for line in lines]
    toks = [line.split(",") for line in lines]
    frees = [[float(ele) for ele in tok] for tok in toks]
    frees = frees[0]
    return range(len(frees)), frees

def fitness_over_time(trial_ID):
    fits = load_fitnesses(trial_ID)
    pylab.plot([j for j in range(len(fits))], fits, 'b-')
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
       free_vars_count(trial_ID)
       #fitness_over_time(trial_ID)
    except IOError:
        print "Waiting on", sys.argv[1], "to appear."
        sleep(10)
