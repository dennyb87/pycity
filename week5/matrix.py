#!/usr/bin/env python3

'''
Write a function that displays an n­by­n matrix
using the following header:
defprintMatrix(n):
Each element is 0 or 1, which is generated randomly.
Write a test program that prompts the user
to enter n and displays an n­by­n matrix.
Here is a sample run:
Entern:3
010
000
111
'''

from random import randint


def squareMatrix(size):
    matrix, sub = [], []
    for n in range(size):
        for n in range(size):
            bit = randint(0, 1)
            sub.append(bit)
        matrix.append(sub)
        sub = []  
    return matrix

def printMatrix(matrix):
    for sub in matrix:
        print("\n")
        for bit in sub:
            print(bit, end="    ")
    print("\n")

if __name__ == "__main__":

    matrix = squareMatrix(5)
    printMatrix(matrix)
