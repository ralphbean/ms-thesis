#!/usr/bin/python

import unittest
import simulator

from random import random
from math import tanh

class TestSimulator(unittest.TestCase):
    # Little test stub which yields values consistent with those in the 
    #  literature.
    def test_logistic_lyapunov_1(self):
        simulator.logistic_example_system['consts'][0] = 1
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_1_99(self):
        simulator.logistic_example_system['consts'][0] = 1.9
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_1_999(self):
        simulator.logistic_example_system['consts'][0] = 1.999
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_2(self):
        simulator.logistic_example_system['consts'][0] = 2
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_2_001(self):
        simulator.logistic_example_system['consts'][0] = 2.001
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_2_1(self):
        simulator.logistic_example_system['consts'][0] = 2.1
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_3(self):
        simulator.logistic_example_system['consts'][0] = 3
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_3_236(self):
        simulator.logistic_example_system['consts'][0] = 3.236067977
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_3_56994571869(self):
        simulator.logistic_example_system['consts'][0] = 3.56994571869
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap > 0)
    def test_logistic_lyapunov_3_828427125(self):
        simulator.logistic_example_system['consts'][0] = 3.828427125
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap < 0)
    def test_logistic_lyapunov_3_9(self):
        simulator.logistic_example_system['consts'][0] = 3.9
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap > 0)
    def test_logistic_lyapunov_4(self):
        simulator.logistic_example_system['consts'][0] = 4
        lyap = simulator.measure_lyapunov(simulator.logistic_example_system)
        self.assertTrue(lyap > 0)



    def get_test_network(self, n):
        return { 'n' : n,
            'consts' : [random() for i in range(n**2 + n)],
            'eqns' : [ lambda v, c : 
              tanh(sum([v[j]+c[i*n+j] for j in range(n)])) 
                + c[-i] for i in range(n)] }

    def test_ANN_lyapunov_1(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(1))<0)
    def test_ANN_lyapunov_2(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(2))<0)
    def test_ANN_lyapunov_3(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(3))<0)
    def test_ANN_lyapunov_4(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(4))<0)
    def test_ANN_lyapunov_5(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(5))<0)
    def test_ANN_lyapunov_6(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(6))<0)
    def test_ANN_lyapunov_7(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(7))<0)
    def test_ANN_lyapunov_8(self):
        self.assertTrue(simulator.measure_lyapunov(self.get_test_network(8))<0)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimulator))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

