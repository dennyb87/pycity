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

def mileskm_table():

    KM = 1.609

    print("Miles Kilometres")

    for n in range(11):
        print("{0:<8}{1:.3f}".format(n, n * KM))


if __name__ == "__main__":

    mileskm_table()
