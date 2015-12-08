#!/usr/bin/env python3
"""Process scores in a text file
Suppose that a text file contains an unspecified number of scores.
Write a program that reads the scores from the file and displays their
total and average. Scores are separated by blanks.
Your program should prompt the user to enter a filename.
Here is a sample run:

Enter a filename: scores.txt
There are 70 scores
The total is 800
The average is 33.33
"""
import os

if __name__ == "__main__":
    filename = input('Enter a filename: ')
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            scores = [int(n) for n in f.read().split()]
            total = sum(scores)
            average = total / len(scores)
            f.closed
            print('There are {} scores'.format(len(scores)))
            print('The total is {}'.format(total))
            print('The average is {}'.format(average))
    else:
        print('File "{}" does not exist!'.format(filename))
