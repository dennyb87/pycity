#!/usr/bin/env python3
import unittest
from chinese_zodiac import chinese_zodiac


class ChineseZodiacTest(unittest.TestCase):

    def setUp(self):
        self.zodiac =  (
            "monkey",
            "rooster",
            "dog",
            "pig",
            "rat",
            "ox",
            "tiger",
            "rabbit",
            "dragon",
            "snake",
            "horse",
            "sheep"
            )

    def test_chinese_zodiac(self):
        idx = 0
        for year in range(2004, 2016):
            self.assertEqual(chinese_zodiac(year), self.zodiac[idx])
            idx += 1


if __name__ == "__main__":
    unittest.main()
