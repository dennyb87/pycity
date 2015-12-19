#!/usr/bin/env python3
import unittest
from hi_fiven import hi_fiven


class ChineseZodiacTest(unittest.TestCase):

    def test_hi_fiven(self):
        self.assertEqual(hi_fiven(5), 'HiFive\n')
        self.assertEqual(hi_fiven(6), 'HiEven\n')
        self.assertEqual(hi_fiven(10), 'HiFive\nHiEven\n')

if __name__ == "__main__":
    unittest.main()
