#!/usr/bin/python
from math import sqrt, ceil
import shelve
import sys

def all_equal(strs):
    for str in strs:
        if len(str) != len(strs[0]):
            return False
    return True

def diversity(_strs):
    strs = [s for s in _strs]

    m_len = max([len(s) for s in strs])
    for i in range(len(strs)):
        strs[i] = strs[i] * int(ceil(float(m_len)/len(strs[i])))
        strs[i] = strs[i][:m_len]

    if not all_equal(strs):
        raise "Not all the same size."

    # Now that they're all the same size...
    # Calculate the mean
    mean = [0] * m_len
    for s in strs:
        mean = [mean[i] + s[i] for i in range(m_len)]
    mean = [ele/float(len(strs)) for ele in mean]

    tot = 0
    for s in strs:
        diff = [ (s[i] - mean[i])**2 for i in range(m_len) ]
        tot = tot + sum(diff)/float(m_len)
    tot = tot / float(len(strs))
    return tot


if __name__ == '__main__':

    if sys.argv[3] == 'spread_frame':
        filename = "../dat/" + sys.argv[1] + "." + sys.argv[2] + ".pop"
        pop = shelve.open(filename)['pop']
        for o in pop:
            print o['amplitude'], o['fitness']
    else:
        for i in range(int(sys.argv[2])):
            filename = "../dat/" + sys.argv[1] + "." + str(i) + ".pop"
            d = shelve.open(filename)
            if 'pop' in d:
                pop = d['pop']
                fits = [ o['fitness'] for o in pop ]

                if sys.argv[3] == 'fitness':
                    for o in pop:
                        print i, o['fitness']
                elif sys.argv[3] == 'avg_fitness':
                    print i, sum(fits) / float(len(pop))
                elif sys.argv[3] == 'max_fitness':
                    print i, max(fits)
                elif sys.argv[3] == 'min_fitness':
                    print i, min(fits)
                elif sys.argv[3] == 'spread':
                    for o in pop:
                        print o['amplitude'], o['fitness']

                elif sys.argv[3] == 'variance':
                    for o in pop:
                        print i, o['variance']
                elif sys.argv[3] == 'avg_variance':
                    print i, sum( [ o['variance'] for o in pop ] ) / float(len(pop))

                elif sys.argv[3] == 'diversity':
                    # calculate diversity on first string
                    d1 = diversity( [o['org'][0] for o in pop] )
                    d2 = diversity( [o['org'][1] for o in pop] )
                    print i, sqrt(d1**2 + d2**2)


                elif sys.argv[3] == 'length':
                    for o in pop:
                        print i, len(o['org'][0])
                        print i, len(o['org'][1])
                elif sys.argv[3] == 'avg_length':
                    print i, sum( [ len(o['org'][0]) + len(o['org'][1]) for o in pop ] ) / float(2*len(pop))

                else:
                    pass
