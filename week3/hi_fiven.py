#!/usr/bin/env python3

'''
Write a program that prompts the user to enter an integer.
If the number is a multiple of 5, print HiFive.
If the number is divisible by 2, print HiEven.

>>> hi_fiven(5)
'HiFive\\n'
'''


def hi_fiven(number):
    
    msg = "HiFive\n" if number % 5 == 0 else ""
    msg += "HiEven\n" if number % 2 == 0 else ""

    return msg


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(hi_fiven(number))
