#!/usr/bin/env python3
import unittest
from anagrams import is_anagram


class AnagramTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "silent"
        self.s2 = "listen"

    def test_is_anagram(self):
        self.assertEqual(is_anagram(self.s1, self.s2), True)


if __name__ == "__main__":
    unittest.main()
