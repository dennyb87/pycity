#!/usr/bin/env python3

'''
Write a program that randomly generates a lottery of a two-digit number,
prompts the user to enter a two-digit number, and determines whether the
user wins according to the following rule:
- If the user input matches the lottery in exact order, the award is 10,000.
- If the user input matches the lottery, the award is 3,000.
- If one digit in the user input matches a digit in the lottery, the award is
1,000.
'''

from random import randint
from collections import Counter

def lottery(user_numbers):

    lottery_numbers = randint(0, 9), randint(0, 9)
    diff = Counter(lottery_numbers) - Counter(user_numbers)
    guessed = len(lottery_numbers) - len(list(diff.elements()))

    msg = "Lottery numbers: {}\n\nYour numbers: {}\n\nYou "\
        .format(lottery_numbers, user_numbers)

    if guessed == 0:
        msg += "lose!"

    elif guessed == 1:
        msg += "won 1,000 pounds!"

    elif lottery_numbers == user_numbers:
        msg += "won 10,000 pounds!"

    else:
        msg += "won 3,000 pounds!"

    return msg


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    user_string = input("Enter a two-digit number: ")
    user_numbers = (int(user_string[0]), int(user_string[1]))

    print lottery(user_numbers)
