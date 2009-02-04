from random import random, randint
from math import tanh
import inputs

def build_random_weights(n):
    return [[(random()<0.75*random())*20-10 for j in range(n+1)] for i in range(n)]

def instantiate(weights, input):
    # Turn the weights into a giant row matrix
    consts = []
    for i in range(len(weights)):
        consts = consts + weights[i]
    n = len(weights)

    network = {
            'n' : n + 2,
            'consts' : consts,
            'eqns' : inputs.input_as_lambdas(input) +
            [ lambda v, c : tanh( sum( [ v[j+2] + c[i*(n+1) + j]
                for j in range(n)]) + c[i*(n+1) + n]  ) for i in range(n)]
            }
    # WOW WOW
    # Fixed a major bug here.  The input was *never* driving the network.
    network['eqns'][2] = lambda v, c : tanh(
            sum( [ v[j+2] + c[j] for j in range(n)] ) + v[1] + c[n])

    return network
