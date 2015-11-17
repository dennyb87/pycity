#!/usr/bin/env python3
"""Reverse

Write a function that reverses a string. The header of the function is:
def reverse(s):
Write a test program that prompts the user to enter a string, invokes
the reverse function, and displays the reversed string.
"""


def reverse(s):
    rev = ''
    for char in s:
        rev = char + rev
    return rev


if __name__ == "__main__":
    user_string = input('Enter your string: ')
    rev = reverse(user_string)
    msg = 'The reversed string is "{}"'.format(rev)
    print(msg)
