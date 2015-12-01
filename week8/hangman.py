#!/usr/bin/env python3
"""Hangman
Write a hangman game that randomly generates a word and prompts the user
to guess one letter at a time, as shown in the sample run.
Each letter in the word is displayed as an asterisk.
When the user makes a correct guess, the actual letter is then
displayed.
When the user finishes a word, display the number of misses and ask the
user whether to continue playing. 
"""
from random import shuffle


class Hangman:

    def __init__(self):
        self.words = ["write", "that", "program"]
        shuffle(self.words)
        self.word = list(self.words[0])
        self.remain = list(self.word)
        self.guessed = [0 for char in self.word]
        self.games = 0
        self.missed = 0

    def first_guess(self, char, idx):
        return self.guessed[idx] != char

    def run(self):
        hidden = [char if char != 0 else '*' for char in self.guessed]
        msg = 'Enter a letter in word {} >'.format(
            ' '.join(hidden)
        )
        char = input(msg)
        if char in self.word:
            if char in self.remain:
                idx = self.remain.index(char)
                if self.first_guess(char, idx):
                    self.guessed[idx] = char
                    self.remain[idx] = 0
                else:
                    print('{} is already in the word'.format(char))
            else:
                print('{} is already in the word'.format(char))
        else:
            print('{} is not in the word'.format(char))
            self.missed += 1

        if 0 in self.guessed:
            return self.run()
        else:
            self.games += 1

        print(
            'The word is "{}". You missed {} time'.format(
                ''.join(self.word), self.missed
            )
        )
        if self.want_play_again():
            return self.new_game()

        print('Hangman end game!')


    def want_play_again(self):
        play_again = input(
            'Do you want to guess another word? Enter y or n > '
        )
        return play_again == 'y'


    def reset(self):
        self.__init__()

    def new_game(self):
        if self.games:
            self.reset()
        self.run()

    def play(self):
        self.new_game()

if __name__ == "__main__":
    hangman = Hangman()
    hangman.play()
