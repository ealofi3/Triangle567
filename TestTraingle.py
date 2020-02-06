# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 should be Scalene')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(7, 8, 7), 'Isoceles', '7,8,7 should be Isoceles')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(4, 5, 15), 'NotATriangle', '4,5,15 should be NotAtaqngle')

    def testNotVaildA(self):
        self.assertEqual(classifyTriangle(201, 202, 300), 'InvalidInput', '201,202,300 are InvalidInput')

    def testNotVaildB(self):
        self.assertEqual(classifyTriangle(-1, -3, -7), 'InvalidInput', '-1,-3,-7 are InvalidInput')

    def testNotVaildC(self):
        self.assertEqual(classifyTriangle(2.25, 6, 7), 'InvalidInput', '2.25,6,7 are InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

