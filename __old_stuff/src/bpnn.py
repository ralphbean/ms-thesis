#!/usr/bin/python
# Back-Propagation Neural Networks
# 
# Written in Python.  See http://www.python.org/
# Placed in the public domain.
# Neil Schemenauer <nas@arctrix.com>
#
# Changes:
#    2009-01-30 Fix dsigmoid() to use correct derivative rather than an
#               approximation.  Suggested by Andrew Lionel Blais.
import pylab
import sys
import math
import random
import string

# calculate a random number where:  a <= rand < b
def rand(a, b):
    # TODO -- Use pga's random numbers here.
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function
def dsigmoid(y):
    return 1.0 - math.tanh(y)**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-2.0, 2.0)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError, 'wrong number of inputs'

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError, 'wrong number of target values'

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            # Don't use squared error.  It's railing our tiny errors.
            #error = error + 0.5*(targets[k]-self.ao[k])**2
            error = error + math.fabs(targets[k] - self.ao[k])
        return error


    def test(self, patterns):
        for p in patterns:
            print p[0], '->', self.update(p[0])

    def weights(self):
        print 'Input weights:'
        for i in range(self.ni):
            print self.wi[i]
        print
        print 'Output weights:'
        for j in range(self.nh):
            print self.wo[j]

    def train(self, patterns, plot=False, min_error=0.001, N=0.5, M=0.1):
        print "Training.", plot, min_error
        # N: learning rate
        # M: momentum factor
        error = 1000.0
        pylab.ion()
        lines = None
        plot_error = False 
        errors = []
        iters = -1
        original_patterns = [ele for ele in patterns]
        if plot:
            # Set up our figure
            fig = pylab.figure()
            sbp1 = pylab.subplot(2,1,1)
            dat1 = pylab.plot(
                          range(len(original_patterns)),
                          [self.update(pat[0]) for pat in original_patterns],
                          range(len(original_patterns)),
                          [pat[1] for pat in original_patterns])
            sbp2 = pylab.subplot(2,1,2)
            dat2 = pylab.plot(range(len(errors)), errors)
        while error >= min_error:
            iters = iters + 1
            error = 0
            random.shuffle(patterns)
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            error = error / float(len(patterns))
            errors.append(error)
            if iters % 10 == 0:
                print "\rIters:", iters, "Error  %",error,
                sys.stdout.flush()
                if plot:
                    dat1[0].set_data(range(len(original_patterns)),
                            [self.update(pat[0]) for pat in original_patterns])
                    dat1[1].set_data(range(len(original_patterns)),
                            [pat[1] for pat in original_patterns])
                    sbp2.clear()
                    sbp2.plot(range(len(errors)), errors)
                    win_size = 50
                    if len(errors) > win_size:
                        sbp2.plot(range(len(errors)-win_size, len(errors)),
                                  errors[-win_size:])
                        sbp2.set_xlim(
                                len(errors)-win_size,
                                len(errors))
                        sbp2.set_ylim(
                                min(errors[-win_size:]),
                                max(errors[-win_size:]))


                    pylab.draw()
        pylab.ioff()
        print "Done."


def demo():
    # Teach network XOR function
    pat = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(2, 2, 1)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)


if __name__ == '__main__':
    demo()
