#!/usr/bin/python

from get_combos import combinations
from ga import already_computed
from ga import combo_to_ID
from ga import max_gens
from get_name_of_experiment import get_name_of_experiment
import shelve, os

if __name__ == '__main__':
    n = 20
    combos = [combo_to_ID(i[0], i[1], i[2], i[3])
                  for i in combinations(True) + combinations(False)]


    count, done, done_scored = 0, [], []
    for combo in combos:
        if already_computed(combo, max_gens-1, True):
            done = done + [combo]
            count = count + 1
    
    for i in range(len(done)):
        print "Starting", done[i], "...", i, "of", len(done)
        if not os.system('./compress_dat.sh ' + str(done[i])):
            print "All good"
        else:
            raise "Fuck."


