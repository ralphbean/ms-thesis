#!/usr/bin/python

import unittest
import linalg

from random import random
from math import tanh

class TestLinalg(unittest.TestCase):
    # TODO -- actually do all these tests by hand.
    def setUp(self):
        self.verbose = True 
        self.As = [[
            [ 1, 1, 1, 3 ],
            [ 2, 3, 7, 0 ],
            [ 1, 3, -2, 17 ]
        ],[
            [ 9,3,4,7],
            [ 4,3,4,8],
            [ 1,1,1,3]
        ],[
            [2, 1, -1, 8],
            [-3,-1,2,-11],
            [-2,1,2,-3]
        ],[
            [2, 4, 5, 47],
            [3, 10, 11, 104],
            [3, 2, 4, 37]
        ],[
            [1,2,4],
            [2,4,9]
        ], [[2,2,2,0,0],
            [-1,2,0,0,2],
            [2,1,-1,-1,1],
            [0,2,0,2,-1]
        ], [[2,0,1,1,2],
            [2,0,1,1,1],
            [0,1,-1,-1,1],
            [-1,1,2,-1,1]
        ]]

    def test_det(self):
        expected = [-33, -13, -19, 36, 0, -12, 12]
        for i in range(len(self.As)):
            M = [row[:-1] for row in self.As[i]]
            self.assertTrue(linalg.det(M) == expected[i])

    def test_elim(self):
        for i in range(len(self.As)):
            a = linalg.gaussianElim(self.As[i])
            self.assertTrue(linalg.is_upper_triangular(a))

    def test_inconsistent(self):
        expected = [False, False, False, False, True, False, True]
        for i in range(len(self.As)):
            a = linalg.gaussianElim(self.As[i])
            self.assertTrue(linalg.inconsistent(a) == expected[i])

    def test_freevars(self):
        expected = [[],[],[],[2],[1],[],[3]]
        for i in range(len(self.As)):
            a = linalg.gaussianElim(self.As[i])
            free = linalg.determineFreeVariables(a)
            self.assertTrue(free == expected[i])

    def test_backsolve(self):
        expected = [
                {   0: 1.0000000000000036,
                    1: 3.9999999999999991,
                    2: -2.0000000000000004},
                {   0: -0.20000000000000007,
                    1: 3.9999999999999991,
                    2: -0.79999999999999905},
                {0: 2.0, 1: 3.0, 2: -0.99999999999999989},
                {0: 5.9999999999999964, 1: 7.5, 2: 1},
                {0: 2.0, 1: 1},
                {
                    0: -0.55555555555555547,
                    1: 0.72222222222222221,
                    2: -0.16666666666666674,
                    3: -1.2222222222222221}
                ]
        for i in range(len(self.As)):
            a = linalg.gaussianElim(self.As[i])
            if not linalg.inconsistent(a):
                free = linalg.determineFreeVariables(a)
                assignments = {}
                for var in free:
                    assignments[var] = 1
                sol = linalg.backsolve(a, assignments)
                if sol != expected[i]:
                    print "Failure expected on matrix", i
                    for row in self.As[i]:
                        print row
                    print "Inconsistent:", linalg.inconsistent(self.As[i])
                self.assertTrue(sol == expected[i])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLinalg))
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

