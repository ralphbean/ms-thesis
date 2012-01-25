#!/usr/bin/python
from time import time
from random import random, randint
import shelve, sys, gc, os

import crossover as cvr
import mutation  as mut
import metrics   as mtr
import selection as sel


# A constant:
num_trials = 4
max_gens = 3500



# Print things to stdout and log things that need logging
def IO_update(ID, generation, pop, max_gens):
    # Print update to stdout:
    print "\rL: %f  a: %f      (%%%i done.)" \
            % ( mtr.fitness(pop[0]), pop[0]['amplitude'],
                    100.0 * float(generation)/(max_gens-1)),
    sys.stdout.flush()

    # Log stuff to file with shelve
    d = shelve.open("dat/" + str(ID) + "/" +
                    str(ID) + "." + str(generation) + ".pop" )
    d['pop'] = pop
    d.close()


def initialize_pop():
    # Some initialization constants:
    lower_size = 2
    upper_size = 50
    num = 100

    pop = []
    for j in range(num):
        print "\rInitializing Population        %%%i" % (100*float(j)/(num-1)),
        sys.stdout.flush()
        org = { 'org':
           [[random()*2-1 for i in range(randint(lower_size, upper_size))],
            [0,0,0]],
           'amplitude' : random() * 0.1 + 0.05 }
        org['fitness'] = mtr.fitness(org)
        pop.append(org)
    print "  Done."
    return pop

def handle_args():
    if len(sys.argv) != 5:
        print "Usage:"
        print "  ga.py <comparator> <crossover> <selection> <trial>"
        print "Got:"
        print "  " + " ".join(sys.argv)
        sys.exit(1)

    cmp_fnc   = int(sys.argv[1])
    c_over_op = int(sys.argv[2])
    select_op = int(sys.argv[3])
    trial     = int(sys.argv[4])

    return cmp_fnc, c_over_op, select_op, trial

def already_computed(ID, gen, silent=False):
    pop = None
    d = shelve.open("dat/"+ID+"/"+ID+"."+str(gen) + ".pop")
    if 'pop' in d:
        prog = 100.0 * float(gen)/(max_gens-1)
        if not silent:
            print "\rAlready computed; skipping ahead.  (%%%i)" % prog,
            sys.stdout.flush()        # Update our percentage ticker.
        pop = d['pop']                # Load that population into memory.
    d.close()
    return pop

def combo_to_ID(cmp_fnc, c_over_op, select_op, trial):
    return str(cmp_fnc)+"."+str(c_over_op)+"."+str(select_op)+"."+str(trial)

def do_experiment(cmp_fnc, c_over_op, select_op, trial, force=False):
    ID = combo_to_ID(cmp_fnc, c_over_op, select_op, trial)

    cmp_fnc   = mtr.fn_list[cmp_fnc]
    c_over_op = cvr.fn_list[c_over_op]
    select_op = sel.fn_list[select_op]

    print "ID:", ID,
    print str(cmp_fnc)[10:-15],str(c_over_op)[10:-15],str(select_op)[10:-15]

    pop = already_computed(ID, max_gens-1)
    if pop:
        return

    pop = None
    generation = 0
    while ( generation < max_gens ):
        tmp = already_computed(ID, generation)
        if tmp:
            # Iteratively load saved generations up to where we stopped before
            pop, generation = tmp, generation + 1
            continue

        # Initialize our population if we haven't already
        if not pop:
            pop = initialize_pop()

        # Otherwise we need to compute!
        pop.sort(lambda x,y : mtr.comparator(x,y, cmp_fnc) )  # Eval and sort
        IO_update(ID, generation, pop, max_gens)              # Spit out status
        pop = select_op(pop, c_over_op, cmp_fnc)              # Breed
        generation = generation + 1                           # Tick

        # Forcibly revaluate the fitness of the hero.
        try:
            del pop[0]['fitness']
        except KeyError:
            pass

if __name__ == '__main__':
    # Get the function pointers from the arg list
    cmp_fnc, c_over_op, select_op, trial = handle_args()

    # Do and time the experiment
    t1 = time()
    do_experiment(cmp_fnc, c_over_op, select_op, trial)
    t2 = time()

    # Report back so we can better estimate.
    print
    #print "Experiment took", str((t2-t1)/(60.0*60.0)), "hours."
    print

