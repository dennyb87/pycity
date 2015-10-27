#!/usr/bin/env python3

'''
Body Mass Index (BMI) is a measure of health on weight.
It can be calculated by taking your weight in kilograms
and dividing by the square of your height in meters.

>>> bmi_calculator(65, 1.65)
'Normal'
'''

def bmi_calculator(weight, height):

    bmi = weight / height**2

    OVERWEIGHT, NORMAL, UNDERWEIGHT = 29.9, 24.9, 18.5

    if bmi > OVERWEIGHT:

        return "Obese"

    elif OVERWEIGHT >= bmi > NORMAL:

        return "Overweight"

    elif NORMAL >= bmi > UNDERWEIGHT:

        return "Normal"

    elif bmi <= UNDERWEIGHT:

        return "Underweight"


if __name__ == "__main__":

    import doctest
    doctest.testmod()

    print(bmi_calculator(65, 1.65))
