#!/usr/bin/env python3
import unittest
from duplicates import eliminate_duplicates


class DuplicatesTest(unittest.TestCase):

    def setUp(self):
        self.L1 = [n for n in range(10)]
        self.L2 = self.L1 * 2

    def test_get_suit(self):
        self.assertEqual(eliminate_duplicates(self.L2), self.L1)


if __name__ == "__main__":
    unittest.main()
