#!/usr/bin/python
import pylab
from math import log

def frange(start, stop, step):
        return [ start + float(i)*step for i in range((stop-start+step)/step)]
T = frange(0.01,1,0.01)
X = [1.0/(ele) for ele in T]
pylab.subplot(2,1,1)
pylab.title('1/x')
pylab.plot(T,X)
pylab.subplot(2,1,2)
pylab.title('log(1/x)')
pylab.plot(T,[log(ele) for ele in X])
pylab.show()

