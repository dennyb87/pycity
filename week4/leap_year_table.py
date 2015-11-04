#!/usr/bin/env python3

'''
Write a program that displays, ten per line
all the leap years in the twenty-first century
(from year 2001 to 2100).
The years are separated by exactly one space.

>>> list(leap_year_range(2001, 2010))
[2004, 2008]
'''

def is_leap_year(year):

    '''
    Could be imported from the leap_year.py module of week3
    '''

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    return False

def leap_year_range(start, end):

    '''
    Leap year generator
    '''

    for year in range(start, end + 1):

        if is_leap_year(year):
            yield year


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    count = 1

    for year in leap_year_range(2001, 2100):

        end = "\n" if count % 10 == 0 else " "
        print(year, end=end)

        count+=1
