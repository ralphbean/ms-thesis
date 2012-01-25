#!/usr/bin/python

import unittest
import constraints

class TestConstraints(unittest.TestCase):
    def setUp(self):
        self.system = { 'n' : 2,
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
        self.input = {  'x0'  : 0,
                        'dx'  : 1,
                        'eqn' :
                    { 'data'  :
                        {'type'  : 'operator',
                         'value' : '*'},
                      'left'  : { 'data' : 
                                    { 'type' : 'parameter',
                                      'value' : '1' }},
                      'right' : { 
                          'data' : {'type'  : 'operator',
                         'value' : '+'},
                                  'left' : { 'data' : 
                                      {'type' : 'constant',
                                          'value' : '3'}
                                      },
                                  'right': { 'data' : 
                                      {'type' : 'constant',
                                          'value' : '2'}
                                      }}}}

    def testPrintConstraints(self):
        s = constraints.constraints_to_string(self.system)
        self.assertTrue(s == "n:2\n(a_{1}=(1+2))")

    def testPrintInput(self):
        s = constraints.input_to_string(self.input)
        self.assertTrue(s == "x0:0\ndx:1\n(a_{1}*(3+2))")

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

