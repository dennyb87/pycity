#!/usr/bin/env python3
"""Remove text
Write a program that removes all the occurrences of a specified string
from a text file. Your program should prompt the user to enter a
filename and a string to be removed.
Here is a sample run:

Enter a filename: test.txt
Enter the string to be removed: morning
Done
"""
import os

if __name__ == "__main__":
    filename = input('Enter a filename: ')
    target = input('Enter the string to be removed: ')
    if os.path.isfile(filename):
        data = ''
        with open(filename, 'r') as f:
            data += f.read().replace(target, '')
            f.closed
        with open(filename, 'w') as f:
            f.write(data)
            f.closed
            print('Done')
    else:
        print('File "{}" does not exist!'.format(filename))
