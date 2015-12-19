#!/usr/bin/env python3
"""Replace text
Write a program that replaces text in a file. Your program should prompt
the user to enter a filename, an old string, and a new string.
Here is a sample run:

Enter a filename: test.txt
Enter the old string to be replaced: morning
Enter the new string to replace the old string: afternoon
Done
"""
import os

if __name__ == "__main__":
    filename = input('Enter a filename: ')
    old = input('Enter the old string to be replaced: ')
    new = input('Enter the new string to replace the old string: ')
    if os.path.isfile(filename):
        data = ''
        with open(filename, 'r') as f:
            data += f.read().replace(old, new)
            f.closed
        with open(filename, 'w') as f:
            f.write(data)
            f.closed
            print('Done')
    else:
        print('File "{}" does not exist!'.format(filename))
