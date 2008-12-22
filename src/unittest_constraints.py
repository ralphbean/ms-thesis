#!/usr/bin/python

import unittest
import constraints

class TestConstraints(unittest.TestCase):
    def setUp(self):
        self.constraints = [
                [
                    [ 0, 0, 0, 1 ],
                    [ 0, 2, 3, 0 ],
                    [ 1, 0, 1, 0 ],
                    [ 2, 2, 3, 4 ]
                ],
                [ 1, 2, 3, 4 ]
                ]
        self.system = 
        self.input = {
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

    def testPrintInput(self):
        s = constraints.input_to_string(self.input)
        print s
        self.assertTrue(s == "dx:1\n(a_{1}*(3+2))")

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

