#!/usr/bin/env python3

'''
Write a program that reads an unspecified number of integers,
determines how many positive and negative values have been
read, and computes the total and average of the input values
(not counting zeros). Your program ends with the input 0.
'''

positive, negative = 0, 0
total, count, average = 0, 0, 0
data = None

while data != 0:
    data = float(input("Enter an integer (0 to exit): "))

    if data < 0:
        negative+=1

    elif data > 0:
        positive+=1

    total+=data

count = sum([positive, negative])

if count > 0:
    average = total / count
    print("The number of positive is {}".format(positive))
    print("The number of negative is {}".format(negative))
    print("The total is {}".format(total))
    print("The average is {}".format(average))

else:
    print("You didn't enter any number")
