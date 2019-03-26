# -*- coding: utf-8 -*-
"""
@author: Yuan Zhang
SSW567 HW02a
---
Original info:

Updated Jan 21, 2018
Primary goal of this file: to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# The following page has a nice description of the framework
# https://docs.python.org/3/library/unittest.html


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5, 4, 4), 'Isosceles',
                         '5,4,4 is a Isosceles triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 4, 6), 'Scalene',
                         '5,4,6 is a Scalene triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(2, 1, 5), 'NotATriangle',
                         '2,1,5 is Not A Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
