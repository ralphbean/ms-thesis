#!/usr/bin/python

import sys, shelve
sys.path.append("/home/ralph/thesis/pga/chaos_control_ga")

from fourier import ifft as idct

import maps, metrics, misc
from random import random
from math import cos, sin


for r in misc.arange(0,2,0.5):
    for theta in misc.arange(0,2*3.14, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        x,y = [ele.real for ele in idct([x,y])]
        print x,y


