#!/usr/bin/env python3
"""Count occurrences of numbers
Write a program that reads an unspecified number of integers and finds
the ones that have the most occurrences.
For example, if you enter 2 3 40 3 5 4 –3 3 3 2 0 , the number 3 occurs
most often. Enter all numbers in one line. If not one but several
numbers have the most occurrences, all of them should be reported.
For example, since 9 and 3 appear twice in the list 9 30 3 9 3 2 4
both occurrences should be reported.
"""
from counter import Counter


if __name__ == "__main__":
    numbers = input('Enter random numbers separated by whitespaces: ')
    lst = numbers.split(' ')
    C = Counter(lst)
    for item in C.duplicates().items():
        print('Item "{}" occur {} times'.format(item[0], item[1]))
