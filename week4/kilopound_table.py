#!/usr/bin/env python3

'''
Write a program that displays the following table
(note that 1 kilogram is 2.2 pounds):
Kilograms Pounds
1         2.2
3         6.6
...
197       433.4
199       437.8
'''

def kilopound_table():

    POUNDS = 2.2

    print("Kilograms Pounds")

    for n in range(200):
        print("{0:<10}{1:.1f}".format(n, n * POUNDS))


if __name__ == "__main__":

    kilopound_table()
