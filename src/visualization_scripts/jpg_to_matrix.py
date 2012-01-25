#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

import maps, metrics, misc
from random import random
from math import tanh

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

print "Working with", name + ".*"

n = Image.open(name + ".jpg")
outfile = open(name + ".image", "w")

print
for i in range(l1):
    if i % 30 == 0:
        print "\r", i,",",100*float(i)/l1,
        sys.stdout.flush()
    for j in range(l2):
        x,y = res1[i], res2[j]
        r,g,b = n.getpixel((j,l1 - i - 1))
        #r,g,b = [255-k for k in [r,g,b]]
        avg = (r+g+b)/3.0
        avg = 255 - avg
        #if not avg == 255:
        #    avg = avg / 5.0
        if not avg < 250:
            avg = 255
        else:
            avg = avg / 100
        outfile.write("%f, %f, %i\n" %(y,x,avg))
        #outfile.write("%f,%f,%i,%i,%i" % (x,y,r,g,b))
    #outfile.write("\n")
print " Done."
outfile.close()

