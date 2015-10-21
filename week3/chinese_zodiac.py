#!/usr/bin/python

'''
Now let us write a program to find out the Chinese
Zodiac sign for a given year. The Chinese Zodiac sign
is based on a 12-year cycle, each year being represented
by an animal: rat, ox, tiger, rabbit, dragon, snake,
horse, sheep, monkey, rooster, dog, and pig, in this cycle.
'''

zodiac = (
    "monkey",
    "rooster",
    "dog",
    "pig",
    "rat",
    "ox",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "sheep"
    )

user_string = input("Enter an year: ")
sign = zodiac[int(user_string) % 12]

print("Your sign is {} !".format(sign))