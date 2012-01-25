#!/usr/bin/python
from bpnn import NN
import math
import random
import sys
import time
import shelve
import pylab
import matplotlib

def d_prod(u, v):
    return sum([u[i] * v[i] for i in range(len(u))])

def matr_mult(A, x):
    val = [d_prod(A[r], x) for r in range(len(A))]
    return val

def f_logistic(x):
    return [4*x*(1-x)]
def f_logistic_root(x):
    return [math.sqrt(4*x*(1-x))]
def f_cubic(x):
    return [6.5*x*x*(1-x)]
def f_quartic(x):
    return [8.82*x*x*x*(1-x)]
def f(x):
    # TODO -- try logistic root
    return f_cubic(x)

def generate_pattern(n_test_cases):
    pat = []
    for i in range(n_test_cases):
        val = random.random()
        #val = float(i)/float(n_test_cases) * 1.1 - 0.05 
        val = float(i)/float(n_test_cases) * 0.8 + 0.1
        pat.append([[val,1], [f(val)[0]]])
    return pat

def collect_data(f, t):
    iterations = xrange(200)
    warmups    = xrange(200)
    x = random.random()
    for i in warmups:
        x = f(x)[0]
    X = [[x],[x]]
    for i in iterations:
        X[0].append( f(X[0][-1])[0] )
        X[1].append( X[1][-1] )
        X[0].append( X[0][-1] )
        X[1].append( X[0][-1] )
    return X

def indiv_cobweb(f, t, X):
    pylab.plot(t, [f(ele) for ele in t])
    pylab.plot(t, t)
    pylab.plot(X[1], X[0], 'b-')
    pylab.axis([0,1,0,1])

def indiv_orbits(f, t, X):
    pylab.plot(range(len(X[0])), X[0], 'b-')

def indiv_psd(f, t, X):
    matplotlib.pyplot.psd(X[0], 2048)

def all_diagrams(f1, f2):
    T = 200
    t = range(T)
    t = [float(ele)/float(T) for ele in t]

    x1 = collect_data(f1, t)
    x2 = collect_data(f2, t)

    pylab.figure()
    pylab.subplot(2,1,1)
    pylab.title('Cobweb diagram of iterated map learned by the network.')
    indiv_cobweb(f1, t, x1)
    pylab.subplot(2,1,2)
    pylab.title('Cobweb diagram of the cubic map.  mu=6.5')
    indiv_cobweb(f2, t, x2)

    pylab.figure()
    pylab.subplot(2,1,1)
    pylab.title('State over time of the trained network.')
    indiv_orbits(f1, t, x1)
    pylab.subplot(2,1,2)
    pylab.title('State over time of the cubic map. mu=6.5')
    indiv_orbits(f2, t, x2)
    
    pylab.figure()
    pylab.subplot(2,1,1)
    indiv_psd(f1, t, x1)
    pylab.subplot(2,1,2)
    indiv_psd(f2, t, x2)

    pylab.show()

def find_a_network():
    # TODO notes from thesis update
    #
    #  Look at and implement the quasi-random initialization stuff
    #    from pga's paper.
    #
    #  Try training networks on other chaotic functions
    #    In particular try mu * ( x * (1 - x) )^(1/2) 
    #    pga -- it looks like the function that my network learned
    #
    #  Try finding chaotic autonomous RNNs using my GA.
    #
    
    K = 80 
    pat = generate_pattern(200)
    network1 = NN(2, K, 1)
    d = shelve.open('shelved.networks.db')
    key = str(int(time.time()))
    d[key] = network1
    d.close()
    print "Shelved pre-training under the key", key

    network1.train(pat, True, 0.010)
    print "Done training."

    d = shelve.open('shelved.networks.db')
    key = str(int(time.time()))
    d[key] = network1
    d.close()
    print "Shelved post-training under the key", key

    all_diagrams(lambda x : network1.update([x,1]),f)

def load_a_network(id):
    d = shelve.open('shelved.networks.db')
    network = d[id]
    d.close()
    all_diagrams(lambda x : network.update([x,1]), f)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print "displaying", sys.argv[1]
        load_a_network(sys.argv[1])
    else:
        print "Finding a new network."
        find_a_network()


