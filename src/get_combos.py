#!/usr/bin/python
import sys
import metrics as mtr
import crossover as cvr
import selection as sel
from ga import num_trials


def combinations(first):
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
    return combins

if __name__ == '__main__':
    #first = False
    #if len(sys.argv) != 2:
    #    print "Usage:   ./ga.py <first=True|False>"
    #    sys.exit(1)
    #if sys.argv[1] == 'False':
    #    first = False
    #else:
    #    first = True

    combins = combinations(True) + combinations(False)
    #combins = combinations(False)

    for combin in combins:
        print ".".join([str(ele) for ele in combin])

