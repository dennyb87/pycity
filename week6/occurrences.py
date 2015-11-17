#!/usr/bin/env python3
"""Occurrences

Write a function that finds the number of occurrences of a specified
character in a string using the following header:
def count(s,ch):

The str class has the count method. Implement your method without using
the count method. For example, count("Welcome", 'e') returns 2.
Write a test program that prompts the user to enter a string followed
by a character and displays the number of occurrences of the character
in the string.
"""


def count(s, target):
    L = []
    for char in s:
        if char == target:
            L.append(1)
    return sum(L)


if __name__ == "__main__":
    user_string = input('Enter your string: ')
    user_target = input('Enter your target character: ')
    occurrences = count(user_string, user_target)
    msg = 'The occurrences of "{}" in "{}" are {}'.format(
        user_target,
        user_string,
        occurrences
    )
    print(msg)
