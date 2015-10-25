#!/usr/bin/python

'''
Body Mass Index (BMI) is a measure of health on weight.
It can be calculated by taking your weight in kilograms
and dividing by the square of your height in meters.

>>> bmi_calculator(65, 1.65)
'Normal'
'''

def bmi_calculator(weight, height):

    BMI = weight / height**2

    TABLE = (
        ((29.9), "Obese"),
        ((24.9), "Overweight"),
        ((18.5), "Normal"),
        ((0), "Underweight"),
        )

    return [ TABLE[TABLE.index(data)][1] for data in TABLE if BMI > data[0] ][0]


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    print bmi_calculator(65, 1.65)    