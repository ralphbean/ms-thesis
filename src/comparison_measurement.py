#!/usr/bin/python

from get_combos import combinations
from ga import already_computed
from ga import combo_to_ID
from ga import max_gens
from ga import num_trials
from get_name_of_experiment import get_name_of_experiment
import metrics, crossover, selection
import shelve, sys


def combo_score(combo):
    min_amp, num_under = 1, 0
    d = shelve.open("dat/"+combo+"/"+combo+"."+str(max_gens-1)+".pop")
    if not 'pop' in d:
        raise ValueError, "wtf!"
    p = d['pop']
    d.close()

    for org in p:
        if org['fitness'] < 0:
            if org['amplitude'] < min_amp:
                min_amp = org['amplitude']
            num_under = num_under + 1

    score = {'minimal_amplitude' : min_amp,
             'number_under_zero' : num_under,
             'combo' : combo }
    return score


if __name__ == '__main__':
    n = 10
    combos = (combinations(True) + combinations(False))

    count, done, done_scored = 0, [], []
    for combo in combos:
        ID = combo_to_ID(combo[0], combo[1], combo[2], combo[3])
        if already_computed( ID, max_gens-1, True ):
            done = done + [ID]
            count = count + 1
    print "%i of %i (%%%f) are done." % (count, len(combos), 100 * float(count) / len(combos) )

    print "Proceeding to score those already done."
    for combo in done:
        done_scored = done_scored + [combo_score(combo)]

    strs = ["Fitness functions.",
            "Crossover operators.",
            "Selection methods."]
    mods = [metrics, crossover, selection]
    for j in range(len(strs)):
        print
        print strs[j]
        for i in range(len(mods[j].fn_list)):
            print str(mods[j].fn_list[i])[10:-15],
            of_i = [combo for combo in done_scored
                                if combo['combo'][j*2] == str(i)]
            print len(of_i), 
            for k in range(30-len(str(mods[j].fn_list[i])[10:-15])):
                print "",
            amps = [ele['minimal_amplitude'] for ele in of_i]
            print "  min %f" % (min(amps)),
            print "  avg %f" % (sum(amps)/len(amps))

    print
    print "Sorting by minimal amplitude."
    done_scored.sort(lambda x,y :
              cmp(x['minimal_amplitude'], y['minimal_amplitude']))

    print "Top", n, "overall combinations."
    for ele in done_scored[:n]:
        if len(sys.argv) > 1:
            print ele['combo']
        else:
            print "%s: %f : %s" % (ele['combo'], ele['minimal_amplitude'], get_name_of_experiment(ele['combo']))
            #print ele['combo'], ":", ele['minimal_amplitude'], ":", \
            #       get_name_of_experiment(ele['combo'])





