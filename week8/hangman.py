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
        self.remain = self.word.copy()
        self.guessed = [0] * len(self.word)
        self.games = 0
        self.missed = 0

    def already_guessed(self, idx, char):
        return self.guessed[idx] == char

    def ask_char(self):
        hidden = [char if char != 0 else '*' for char in self.guessed]
        msg = 'Enter a letter in word {} >'.format(
            ' '.join(hidden)
        )
        return input(msg)

    def all_guessed(self):
        return 0 not in self.guessed

    def run(self):
        char = self.ask_char()

        if char not in self.word:
            print('{} is not in the word'.format(char))
            self.missed += 1
            return self.run()

        if char not in self.remain:
            print('{} is already in the word'.format(char))
            return self.run()

        idx = self.remain.index(char)

        if not self.already_guessed(idx, char):
            self.guessed[idx] = char
            self.remain[idx] = 0
        else:
            print('{} is already in the word'.format(char))

        if not self.all_guessed():
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

        return self.end_game()

    def end_game(self):
        print('Hangman end game!')

    def want_play_again(self):
        play_again = input(
            'Do you want to guess another word? Enter y or n > '
        )
        if play_again == 'y':
            return True
        elif play_again == 'n':
            return False
        return self.want_play_again()

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
