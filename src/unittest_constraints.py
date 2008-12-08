#!/usr/bin/python

import unittest
import constraints

class TestConstraints(unittest.TestCase):
    def testSatisfactory(self):
        print "TODO -- write test case"
        self.assertFalse( 0==0)
    def testInstantiate(self):
        print "TODO -- write test case"
        self.assertFalse(0==0)
    def testSimplify(self):
        print "TODO -- write test case"
        self.assertFalse(0==0)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConstraints)))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

