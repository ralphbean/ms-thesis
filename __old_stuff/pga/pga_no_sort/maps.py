#!/usr/bin/python
from math import cos, sin, atan2, sqrt

# Some constants:
e = 2.71828183
mu = 5.5
a = 5
b = 25
W = [[ -a, a], [-b, b]]

def sigmoid( x, mu ):
    return [( 1 + e**(-mu * ele))**-1 for ele in x]

def logistic( X, mu):
    Y = [X[0], X[1]]
    Y[0] = Y[0] * ( 1.0 - Y[0]) * mu
    Y[1] = Y[1] * ( 1.0 - Y[1]) * mu
    return Y

def squeezer( X, a ):
    x = X[0]
    y = X[1]
    u = x
    v = y/2.0 + (sqrt(1-x**2))/2.0

    r = sqrt(v**2 + u**2)
    theta = 2 * atan2(u,v)
    u = a * r * cos(theta)
    v =     r * sin(theta)

    Y = [u, v]
    return Y

def network( x ):
    return sigmoid( [-a * x[0] + a * x[1], -b * x[0] + b * x[1] ], mu )

