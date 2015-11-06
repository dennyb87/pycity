#!/usr/bin/env python3

'''
Write a function that returns the number of days
in a year using the following header:
defnumberOfDaysInAYear(year):
Write a test program that displays the number of
days in the years from 2010 to 2020 .
'''

def isLeapYear(year): 
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def numberOfDaysInAYear(year):
    return 366 if isLeapYear(year) else 365

def numberOfDaysInRange(start, end):
    days = 0
    for y in range(start, end + 1):
        days += numberOfDaysInAYear(y)
    return days

if __name__ == "__main__":

    start, end = 2010, 2020
    msg = "The number of days from {} to {} is {}"\
        .format(start, end, numberOfDaysInRange(start, end))
    print(msg)
