#!/usr/bin/python

import unittest
from unittest_linalg import TestLinalg
from unittest_simulator import TestSimulator
from unittest_constraints import TestConstraints
from unittest_inputs import TestInputs

def suite():    
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimulator))
    suite.addTest(unittest.makeSuite(TestLinalg))
    suite.addTest(unittest.makeSuite(TestInputs))
    suite.addTest(unittest.makeSuite(TestConstraints))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

