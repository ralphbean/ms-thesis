#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, metrics, misc
from random import random

# Python Image Library
from PIL import Image

start1, stop1, step1, start2, stop2, step2, input_len = \
        [float(ele) for ele in sys.argv[1:]]
input_len = int(input_len)
res1 = misc.arange(start1, stop1, step1)
res2 = misc.arange(start2, stop2, step2)
l1 = len(res1)
l2 = len(res2)

print l1, "by", l2, "is", l1*l2

name = "exhaustive-(" + str(input_len) + \
        ").dim." + str(l1) + "x" + str(l2) + "." + \
        str(start1) + ".to." + str(stop1) + \
        ".step_is." + str(step1) + ".and." + \
        str(start2) + ".to." + str(stop2) + ".step_is." + str(step2)

print name + ".*"

n = Image.new('RGB', (l1,l2))
vals = [ [0 for j in range(l2)] for i in range(l1) ]

d = shelve.open(name+".dat")
if not 'vals' in d:
    for i in range(l1):
        done = 100 * i / float(l1)
        print "\rDone:  %%%f.  i=%i of %i." % (done, i, l1),
        sys.stdout.flush()

        for j in range(l2):
            x, y = res1[i], res2[j]

            input = [0 for k in range(input_len)]
            input[0], input[1] = x, y
            input = [input,[0,0]]

            amplitude = 1
            lyaps = [metrics._lyapunov( input,
                                    maps.network,
                                    [random(), random()],
                                    amplitude)
                                        for k in range(1)]

            if sum(lyaps)/float(len(lyaps)) > 0:
                vals[i][j] = 0
            else:
                vals[i][j] = -1 * sum(lyaps)/float(len(lyaps))
    # Save it
    d['vals'] = vals
else:
    print "Skipping all and loading from file."
    vals = d['vals']
d.close()
print "Done calcing.. building image now."

top = max(max(vals))
for i in range(l1):
    for j in range(l2):
        val = vals[i][j]
        if val == 0:
            R, G, B = 0, 0, 0
        else:
            val = val / top
            R = int((val * 52 ) + 204) # From 204 to 256
            G = int((val * 148) + 56 ) # From 56 to 204
            B = 0
        n.putpixel( (i,j), (R,G,B))
print "Done!"
n.rotate(90).show()
n.rotate(90).save(name + ".jpg")

