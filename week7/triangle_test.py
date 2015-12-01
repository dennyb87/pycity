#!/usr/bin/env python3
import unittest
import math
from triangle import Triangle


class TriangleTest(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle()

    def test_get_side1(self):
        self.assertEqual(
            self.triangle.get_side1(),
            self.triangle._Triangle__side1
        )

    def test_get_side2(self):
        self.assertEqual(
            self.triangle.get_side2(),
            self.triangle._Triangle__side2
        )

    def test_get_side3(self):
        self.assertEqual(
            self.triangle.get_side3(),
            self.triangle._Triangle__side3
        )

    def test_get_perimeter(self):
        self.assertEqual(
            self.triangle.get_perimeter(),
            self.triangle._Triangle__side1 +
            self.triangle._Triangle__side2 +
            self.triangle._Triangle__side3
        )

    def test_get_area(self):
        p = self.triangle.get_perimeter() / 2
        area = math.sqrt(
            p *
            (p - self.triangle._Triangle__side1) *
            (p - self.triangle._Triangle__side2) *
            (p - self.triangle._Triangle__side3)
        )
        self.assertEqual(
            self.triangle.get_area(),
            area
        )

if __name__ == "__main__":
    unittest.main()
