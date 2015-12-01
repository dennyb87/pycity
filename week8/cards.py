#!/usr/bin/env python3
"""Deck of cards
The problem is to write a program that picks four cards randomly from a
deck of 52 cards. All the cards can be represented using a list named
deck, filled with initial values 0 to 51, as follows:

deck = list(range(0, 52))

Card numbers 0 to 12 , 13 to 25 , 26 to 38 , and 39 to 51 represent 13
spades, 13 hearts, 13 diamonds, and 13 clubs, respectively:

cardNumber // 13 determines the suit of the card and 
cardNumber % 13 determines the rank of the card

After shuffling the deck, pick the first four cards from deck.
The program displays the cards from these four card numbers.
"""
from random import shuffle


class Deck(list):

    def __init__(self):
        self += range(0, 52)
        self.CARDS_PER_SUIT = 13
        self.SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    def get_suit(self, cardnumber):
        idx = cardnumber // self.CARDS_PER_SUIT
        return self.SUITS[idx]

    def get_rank(self, cardnumber):
        return (cardnumber % self.CARDS_PER_SUIT) + 1

    def get_card(self, idx):
        cardnumber = self.peek(idx)
        return self.get_rank(cardnumber), self.get_suit(cardnumber)

    def peek(self, idx):
        return self[idx]

    def shuffle(self):
        shuffle(self)

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    for i in range(4):
        print(deck.get_card(i))
