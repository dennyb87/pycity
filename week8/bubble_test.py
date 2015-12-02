#!/usr/bin/env python3
import unittest
from random import shuffle
from bubble import bubble_sort


class BubbleTest(unittest.TestCase):

    def setUp(self):
        self.ordered_lst = [n for n in range(10)]
        self.shuffle_lst = self.ordered_lst.copy()
        shuffle(self.shuffle_lst)

    def test_bubble_sort(self):
        bubble_sort(self.shuffle_lst)
        self.assertEqual(self.shuffle_lst, self.ordered_lst)


if __name__ == "__main__":
    unittest.main()
