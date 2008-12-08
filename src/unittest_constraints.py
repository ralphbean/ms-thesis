#!/usr/bin/python

import unittest
import constraints

class TestConstraints(unittest.TestCase):
    def testPrintConstraints(self):
        system = { 'n' : 2,
                'eqns' : [
                    { 'data'  :
                        {'type'  : 'operator',
                         'value' : '='},
                      'left'  : { 'data' : 
                                    { 'type' : 'parameter',
                                      'value' : '1' }},
                      'right' : { 
                          'data' : {'type'  : 'operator',
                         'value' : '+'},
                                  'left' : { 'data' : 
                                      {'type' : 'constant',
                                          'value' : '1'}
                                      },
                                  'right': { 'data' : 
                                      {'type' : 'constant',
                                          'value' : '2'}
                                      }}}]}
        print constraints.constraints_to_string(system)

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

