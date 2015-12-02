#!/usr/bin/env python3
import unittest
from hangman import Hangman


class HangmanTest(unittest.TestCase):

    def setUp(self):
        self.hm = Hangman()
        self.hm.word = list("testing")
        self.hm.remain = self.hm.word.copy()
        self.hm.guessed = [0] * len(self.hm.word)
        self.hm.games = 0
        self.hm.missed = 0
        # Testing attributes
        self.idx = 0
        self.char = self.hm.word[self.idx]

    def test_already_guessed(self):
        self.assertEqual(
            self.hm.already_guessed(self.idx, self.char),
            False
        )
        self.hm.guessed[self.idx] = self.char
        self.assertEqual(
            self.hm.already_guessed(self.idx, self.char),
            True
        )

    def test_all_guessed(self):
        self.assertEqual(
            self.hm.all_guessed(),
            not 0 in self.hm.guessed
        )


if __name__ == "__main__":
    unittest.main()
