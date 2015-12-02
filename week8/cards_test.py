#!/usr/bin/env python3
import unittest
from cards import Deck


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_get_suit(self):
        self.assertEqual(self.deck.get_suit(0), 'Spades')
        self.assertEqual(self.deck.get_suit(13), 'Hearts')
        self.assertEqual(self.deck.get_suit(26), 'Diamonds')
        self.assertEqual(self.deck.get_suit(39), 'Clubs')

    def test_get_rank(self):
        self.assertEqual(self.deck.get_rank(0), 1)
        self.assertEqual(self.deck.get_rank(13), 1)
        self.assertEqual(self.deck.get_rank(26), 1)
        self.assertEqual(self.deck.get_rank(39), 1)

    def test_get_card(self):
        i = 0
        cardnumber = self.deck[i]
        card = (
            self.deck.get_rank(cardnumber),
            self.deck.get_suit(cardnumber)
        )
        self.assertEqual(self.deck.get_card(i), card)

    def test_teek(self):
        self.assertEqual(self.deck.peek(0), self.deck[0])

    def test_shuffle(self):
        shuffled_deck = Deck()
        shuffled_deck.shuffle()
        self.assertNotEqual(self.deck, shuffled_deck)

if __name__ == "__main__":
    unittest.main()
