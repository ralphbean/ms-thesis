#!/usr/bin/python

import unittest
import linalg

from random import random
from math import tanh

class TestInputs(unittest.TestCase):

    # TODO -- write this.
    def setUp(self):
        pass
    def test_deep_copy(self):
        pass

    def test_inorder_string(self):
        pass
    def test_input_to_string(self):
        pass
    def test_function_as_lambda(self):
        pass
    def test_input_as_lambdas(self):
        pass
    def test_build_random_function(self):

        pass
    def test_build_random_input(self):
        pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLinalg))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

