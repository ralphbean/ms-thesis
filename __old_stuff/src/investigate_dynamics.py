#!/usr/bin/python
from bpnn import NN
import math
from math import sin, pi
import random
import sys
import time
import shelve
import pylab
import matplotlib

inf = 1e10000000
ninf = -1e10000000

def frange(start, stop, step):
    return [ start + float(i)*step for i in range(int((stop-start+step)/step))]

def f_quartic(x, mu):
    return mu*x*x*x*(1-x)

def f_cubic(x, mu):
    return mu*x*x*(1-x)

def f_quadratic(x, mu):
    return mu*x*(1-x)

def f(x, mu):
    #return mu*sin(pi*x)
    #return f_quartic(x,mu)
    return f_quadratic(x,mu)


def collect_data(f, t):
    iterations = xrange(150)
    warmups    = xrange(1000)
    x = random.random()
    for i in warmups:
        x = f(x)
    X = [[x],[x]]
    for i in iterations:
        X[0].append( f(X[0][-1]) )
        X[1].append( X[1][-1] )
        X[0].append( X[0][-1] )
        X[1].append( X[0][-1] )
    return X


def indiv_cobweb(f, t, X):
    pylab.plot(t, [f(ele) for ele in t])
    pylab.plot(t, t)
    pylab.plot(X[1], X[0], 'b-')
    pylab.axis([0,1,0,1])

def orbit_diagram(f, t, mu_range):
    # pga -- read linuxjournal..  recent mutt issue.
    # pga -- use gnuplot to control 'dot' size.
    #pylab.ion()
    #pylab.xlabel('mu')
    #pylab.ylabel('w-set')
    for mu in mu_range:
        f_mu = lambda x : f(x, mu)
        x = [ele for ele in collect_data(f_mu, None)[0] 
                if ele != inf and ele != ninf]
        for ele in x:
            print mu, ele

        #pylab.plot([mu for i in range(len(x))], x, 'b.')
        #pylab.draw()
    #pylab.ioff()
    #pylab.show()

if __name__ == '__main__':
    t = frange(0,1,0.05)
    mu_range = frange(2.75,4, 0.001)
    orbit_diagram(f, t, mu_range)
    #pylab.ion()
    #for mu in frange(2,4,0.01):
    #    f_mu = lambda x : f(x, mu)
    #    X = collect_data(f_mu, None)
    #    pylab.cla()
    #    indiv_cobweb(f_mu, t, X)
    #    print mu
    #    pylab.draw()
