#!/usr/bin/env python3
import unittest
from score import scorer, get_grade


class ScorerTest(unittest.TestCase):

    def setUp(self):
        self.scores = scorer([40, 55, 70, 58])

    def test_scorer(self):
        self.assertEqual(self.scores, ['C', 'B', 'A', 'B'])

    def test_get_grade(self):
        self.assertEqual(get_grade(40), 'C')
        self.assertEqual(get_grade(55), 'B')

if __name__ == "__main__":
    unittest.main()
