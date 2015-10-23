#!/usr/bin/python

'''
Write a program that prompts the user to enter an integer.
If the number is a multiple of 5, print HiFive.
If the number is divisible by 2, print HiEven.

>>> hi_feven(5)
'HiFive\\n'
'''

def hi_feven(number):
    
    msg = "HiFive\n" if number % 5 == 0 else ""
    msg += "HiEven\n" if number % 2 == 0 else ""

    return msg


if __name__ == "__main__":

    import doctest
    doctest.testmod()

    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(hi_feven(number))