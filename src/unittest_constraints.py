#!/usr/bin/python

import unittest
import constraints

class TestConstraints(unittest.TestCase):
    def testPrintConstraints(self):
        pass
    def testPrintInput(self):
        pass
    def testSatisfactory(self):
        pass
    def testInstantiate(self):
        pass
    def testSimplify(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConstraints))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

