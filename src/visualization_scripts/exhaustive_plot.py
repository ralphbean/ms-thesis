#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, metrics, misc
from random import random

# Python Image Library
from PIL import Image

start, stop, step = [float(ele) for ele in sys.argv[1:]]

res = misc.arange(start, stop, step)
l = len(res)
print len(res), "is len(res). ", len(res)**2, "is len(res)**2."
n = Image.new('RGB', (len(res), len(res) ))
d = shelve.open("vals-" + str(l) + "x" + str(l) + ".shelf")
if 'vals' in d:
    vals = d['vals']
    print "Awesome!  Skipping calc."
else:
    vals = [ [0 for j in range(len(res))] for i in range(len(res)) ]
    for i in range(len(res)):
        done = 100 * i / float(len(res))
        print "\rDone:  %%%f.  i=%i of %i." % (done, i, len(res)),
        sys.stdout.flush()

        for j in range(len(res)):
            x, y = res[i], res[j]

            input = [[x,y],[0,0]]
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
    d['vals'] = vals
    d.close()
    print "Done calcing.. building image now."

top = max(max(vals))
for i in range(len(res)):
    for j in range(len(res)):
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
name = "exhaustive-" + str(l) + "x" + str(l) + "." + \
        str(start) + ".to." + str(stop) + \
        ".step_is." + str(step) + ".jpg"
n.rotate(90).save(name)

