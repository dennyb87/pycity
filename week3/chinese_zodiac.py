#!/usr/bin/python

'''
Now let us write a program to find out the Chinese
Zodiac sign for a given year. The Chinese Zodiac sign
is based on a 12-year cycle, each year being represented
by an animal: rat, ox, tiger, rabbit, dragon, snake,
horse, sheep, monkey, rooster, dog, and pig, in this cycle.

>>> chinese_zodiac(2000)
'dragon'
'''

def chinese_zodiac(year):

    zodiac =  (
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

    return zodiac[year % 12]


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    user_input = input("Enter an year: ")
    year = int(user_input)
    print(chinese_zodiac(year))
