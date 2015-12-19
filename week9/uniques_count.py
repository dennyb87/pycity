#!/usr/bin/env python3
"""Display non duplicate words in ascending order  
Write a program that prompts the user to enter a text file, reads words
from the file, and displays all the non duplicate words
in ascending order.
"""
import os
from counter import Counter


if __name__ == "__main__":
    filename = input('Enter filename: ')
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            data = f.read().split()
            C = Counter(data)
            uniques = C.uniques()
            f.closed
            for item in sorted(uniques.items(), reverse=True):
                print('Keyword "{}" occur {} times'.format(
                    item[0], item[1]
                ))
    else:
        print('File "{}" does not exist!'.format(filename))
