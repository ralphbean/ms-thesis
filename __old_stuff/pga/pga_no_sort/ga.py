#!/usr/bin/python
from time import time
from random import random, randint
import shelve, sys, gc

import crossover as cvr
import mutation  as mut
import metrics   as mtr
import selection as sel


# A constant:
first = False
num_trials = 3
max_gens = 3000



# Print things to stdout and log things that need logging
def IO_update(ID, generation, pop, max_gens):
    print "\rL:", mtr.fitness(pop[0]), "a:", pop[0]['amplitude'],
    print "%", 100.0 * float(generation)/(max_gens-1),
    print " First:", first,
    sys.stdout.flush()
    # Print stuff to stdout:
#    print ID
#    print "generation: ", generation

  #  print "  best:", mtr.fitness(pop[0]), "a:", pop[0]['amplitude']
  #  print "  secn:", mtr.fitness(pop[1]), "a:", pop[1]['amplitude']
  #  print "  wrst:", mtr.fitness(pop[-1]), "a:", pop[-1]['amplitude']

    # Log stuff to file with shelve
    d = shelve.open("dat/" + str(ID) + "." + str(generation) + ".pop" )
    d['pop'] = pop
    d.close()


def initialize_pop():
    # Some initialization constants:
    lower_size = 2
    upper_size = 50
    num = 100

    pop = []
    for j in range(num):
        print "\rInitializing Population             %", 100*float(j)/(num-1),
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
        print "  ga.py <comparator> <crossover> <mutation> <selection>"
        sys.exit(1)

    cmp_fnc   = mtr.fn_list[int(sys.argv[1])]
    c_over_op = cvr.fn_list[int(sys.argv[2])]
    select_op = sel.fn_list[int(sys.argv[4])]

    return cmp_fnc, c_over_op, select_op


def do_experiment(cmp_fnc, c_over_op, select_op, trial, force=False):
    ID = str(cmp_fnc)+"."+str(c_over_op)+"."+str(select_op)+"."+str(trial)

    cmp_fnc   = mtr.fn_list[cmp_fnc]
    c_over_op = cvr.fn_list[c_over_op]
    select_op = sel.fn_list[select_op]

    print "ID:", ID,
    print str(cmp_fnc)[10:-15],str(c_over_op)[10:-15],str(select_op)[10:-15]

    pop = None
    generation = 0
    while ( generation < max_gens ):
        # First check to see if this experiment is already done...
        d = shelve.open("dat/"+ID+"." + str(generation) + ".pop")
        if 'pop' in d:
            prog = 100.0 * float(generation)/(max_gens-1)
            print "\rAlready computed.  Skipping ahead.  %",prog," f:",first,
            sys.stdout.flush()            # Update our percentage ticker.

            generation = generation + 1   # Advance the generation counter.
            pop = d['pop']                # Load that population into memory.
            d.close()
            continue
        d.close()

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
    print "  Done."

def combinations():
    combins = []
    for i in range(len(mtr.fn_list)):
        for j in range(len(cvr.fn_list)):
            for k in range(len(sel.fn_list)):
                for l in range(num_trials):
                    combins.append([i,j,k,l])
    if first:
        combins = combins[:len(combins)/2]
    else:
        combins = combins[len(combins)/2:]
    print "Total number of combinations: ", len(combins)
    return combins

if __name__ == '__main__':
    times = []
    combins = combinations()
    for i in range(len(combins)):
        cmp_fnc, c_over_op, select_op, trial = combins[i]
        start = time()

        results = do_experiment(cmp_fnc, c_over_op, select_op, trial)

        times.append(time() - start)
        print "Trial:", times[-1]/(60**2), "(h).",
        avg = sum(times)/(60**2 * len(times))
        print "Average:", avg, "(h). GC:", gc.get_count()
        p_done = 100*float(i+1)/(len(combins))
        h_elap = sum(times)/(60**2)
        print "%",p_done,"done with entire experiment.", h_elap, "(h) elapsed."
        h_left = h_elap*(100-p_done)/p_done
        print "Expect to be done in", h_left, "(h)."
        print

    # Get the function pointers from the arg list
    #cmp_fnc, c_over_op, select_op = handle_args()
    #do_experiment(cmp_fnc, c_over_op, select_op, 0)
