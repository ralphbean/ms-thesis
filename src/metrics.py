
from math import sqrt, log, tanh
from random import random

from maps import network


# Some constants:
epsilon = 0.000000001
warmups = 100
measure = 200
d0 = 0.0000000001

def tan_combo_metric(f, a):
    return tanh(f) + tanh(10*(a-0.12))
def plus_metric(f, a):
    return f + a
def divi_metric(f, a):
    return f / (a + 0.00001)
def piecewise_metric(f, a):
    if f >= 0:
        return f + a
    else:
        return a

# Strings of the inverse function to plot iso-fitness curves.
def inverse_tan_combo_metric_string(step):
    return "t,atanh( -tanh( 10 * (t-0.12) ) + " + str(step) + ")"
    #return "atanh( -tanh( 10 * (x-0.12) ) + " + str(step) + ")"

def inverse_plus_metric_string(step):
    return "t,(-t + " + str(step)
    #return "-x + " + str(step)
def inverse_divi_metric_string(step):
    return "t,(t + 0.00001)*" + str(step)
    #return "(x + 0.00001)*" + str(step)
def inverse_piecewise_metric_string(step):
    if step > 0:
        return "t, " + str(step)
    else:
        return str(0.3 * -1 * step / 2.0) + ", -2.0 * t / 0.3"

    return "t," + str(step) + ", " + str(step) + ",-t"
    #return "-x + " + str(step)   # TODO -- fix this.

fn_list = [tan_combo_metric, divi_metric, plus_metric, piecewise_metric]

# Returns a function pointer
def get_inverse_string(ID):
    cmp_i = int(ID[0])
    d = {   tan_combo_metric : inverse_tan_combo_metric_string,
            plus_metric : inverse_plus_metric_string,
            divi_metric : inverse_divi_metric_string,
            piecewise_metric : inverse_piecewise_metric_string }
    return d[fn_list[cmp_i]]

def comparator(o1, o2, func):
    f1, f2 = fitness(o1), fitness(o2)
    return cmp( func(f1, o1['amplitude']), func(f2, o2['amplitude']) )

def _lyapunov( input, system, seed, amplitude ):
    x = seed
    total = 0
    for i in range(warmups):
        x = system(x)
        x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )

    # First, generate a random point that is a distance of d0 from x
    y = [random() for k in range(len(x))]

    for i in range(measure):
        y = [y[k] - x[k] for k in range(len(x)) ]
        try:
            s = sum([ele**2 for ele in y])
            ymag = sqrt(s)
        except OverflowError:
            break
        if ( ymag == 0 ):
            ymag = ymag + epsilon
        y = [d0 * ele / ymag for ele in y]
        y = [y[k] + x[k] for k in range(len(x)) ]

        x = system( x )
        x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
        y = system( y )
        y[0] = y[0] + ( amplitude * input[0][i % len(input[0])] )

        d1 = sqrt(sum([(x[k]-y[k])**2 for k in range(len(x))]))

        total = total + (d1/d0)

    total = total / float(measure)
    if not total:
        total = epsilon
    return log(total)

def fitness( o ):
    '''Approximate the lyapunov exponent'''

    if 'fitness' in o:
        return o['fitness']

    trials = 50
    lyaps = [_lyapunov(o['org'], network, [random(), random()],o['amplitude'])
                          for i in range( trials )]
    mean = sum(lyaps)/float(len(lyaps))

    # Variance is now *really* the standard deviation
    variance = sqrt(sum([(lyap - mean)**2 for lyap in lyaps])/float(len(lyaps)))

    o['fitness']  = mean #+ variance
    o['variance'] = variance

    return o['fitness']

