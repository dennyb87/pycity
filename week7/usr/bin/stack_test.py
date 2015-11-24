#!/usr/bin/env python3
import unittest
from stack import Stack


class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack([1,2,3])

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), False)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), self.stack[-1], )
        self.assertEqual(len(self.stack), 3)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(len(self.stack), 2)

    def test_get_size(self):
        self.assertEqual(self.stack.get_size(), len(self.stack))

if __name__ == "__main__":
    unittest.main()
