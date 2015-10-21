#!/usr/bin/python

'''
Write a program that prompts the user to enter an integer.
If the number is a multiple of 5, print HiFive.
If the number is divisible by 2, print HiEven.
'''

user_string = input("Enter an integer: ")

number = int(user_string)

msg = "HiFive\n" if number % 5 == 0 else ""
msg += "HiEven\n" if number % 2 == 0 else ""

print(msg)