#!/usr/bin/env python3
import unittest
from rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle()

    def test_get_area(self):
        area = self.rect.width * self.rect.height
        self.assertEqual(self.rect.get_area(), area)

    def test_get_perimeter(self):
        perimeter = (self.rect.width + self.rect.height) * 2
        self.assertEqual(self.rect.get_perimeter(), perimeter)

if __name__ == "__main__":
    unittest.main()


