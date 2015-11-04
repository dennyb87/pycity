#!/usr/bin/env python3

'''
Write a program that displays the following table
(note that 1 mile is 1.609 kilometres):
Miles Kilometres
1       1.609
2       3.218
...
9       15.481
10      16.090
'''

def is_leap_year(year):

    '''
    Could be imported from the leap_year.py module of week3
    '''

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    return False

def leap_year_table():

    start = 2001
    end = 2100

    for year in range(start, end + 1):

        if year % 10 == 0:
            print()

        if is_leap_year(year):
            print(year, end=" ")


if __name__ == "__main__":

    leap_year_table()
