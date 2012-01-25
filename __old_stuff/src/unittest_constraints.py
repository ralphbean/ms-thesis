#!/usr/bin/python

import unittest
import simulator
import constraints
import inputs
from random import randint

class TestConstraints(unittest.TestCase):
    def testInstantiate(self):
        # TODO -- come up with a real test here (or series of tests.
        n = 2**2
        A = [[randint(-1,2) for j in range(n+1)] for i in range(n)]
        input = inputs.build_random_input()

        networks = constraints.instantiate(A, input)
        lyaps = [simulator.measure_lyapunov(network) for network in networks]


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConstraints))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

