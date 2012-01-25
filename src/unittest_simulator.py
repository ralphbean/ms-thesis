#!/usr/bin/python

import unittest
import simulator

from random import random
from math import tanh

class TestSimulator(unittest.TestCase):
    # Little test stub which yields values consistent with those in the 
    #  literature.
    def test_logistic_lyapunov(self):
        some_test_values = [1, 1.9, 1.999, 2, 2.001, 2.1, 3, 3.236067977]
        self.do_log_test_neg(some_test_values)
        some_test_values = [ 3.56994571869 ]
        self.do_log_test_pos(some_test_values)
        some_test_values = [3.828427125 ]
        self.do_log_test_neg(some_test_values)
        some_test_values = [3.9, 4]
        self.do_log_test_pos(some_test_values)

    def do_log_test_neg(self, some_test_values):
        for i in some_test_values:
            simulator.logistic_example_system['consts'][0] = i
            lyap = simulator.measure_lyapunov(
                                    simulator.logistic_example_system,
                                    2000, 4000, 1)
            print "L(f(",i,")) =>", lyap
            self.assertTrue(lyap < 0)
    def do_log_test_pos(self, some_test_values):
        for i in some_test_values:
            simulator.logistic_example_system['consts'][0] = i
            lyap = simulator.measure_lyapunov(
                                    simulator.logistic_example_system,
                                    2000, 4000, 1)
            print "L(f(",i,")) =>", lyap
            self.assertTrue(lyap > 0)

    # Another test routine to investigate various simple ANNs
    def test_ANN_lyapunov(self):
        some_test_values = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        network = { 'n': 1,
            'consts' : [1, 1],
            'eqns' :
              [ lambda vars, consts : tanh(vars[0]*consts[0] + consts[1]) ] }

        for n in range(1,10):
            network = { 'n' : n,
                'consts' : [random() for i in range(n**2 + n)],
                'eqns' : [ lambda v, c : 
                  tanh(sum([v[j]+c[i*n+j] for j in range(n)])) 
                    + c[-i] for i in range(n)] }
            print "n =", n, ":",
            lyap = simulator.measure_lyapunov(network, 0, 3, 1)
            # By way of Bean's Grand Nonexistence Theorem (!)
            self.assertTrue(lyap < 0)
            print lyap


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimulator))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

