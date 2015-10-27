#!/usr/bin/python

'''
This program first prompts the user to enter a year
as an int value and checks if it is a leap year.

>>> is_leap_year(2000)
True
'''

def is_leap_year(year):

    return True if year%4 == 0 and year%100 != 0 or year%400 == 0 else False


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    user_input = input("Enter an year: ")
    year = int(user_input)
    print(is_leap_year(year))
