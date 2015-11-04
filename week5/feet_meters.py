#!/usr/bin/env python3

'''
Write a module that contains the following two functions:
#Convertsfromfeettometers
deffootToMeter(foot):
#Convertsfrommeterstofeet
defmeterToFoot(meter):
The formulas for the conversion are:
foot = meter / 0.305
meter = 0.305 * foot
Write a test program that invokes these functions to display
the following tables:
Feet Meters|MetersFeet
1.0 0.305 |20.0 66.574
2.0 0.610 |26.0 81.967
...
9.0 2.745 |60.0 196.721
10.0 3.050 |66.0 213.115

>>> footToMeter(1)
0.305

>>> meterToFoot(0.305)
1.0
'''


def footToMeter(foot):
    return foot * 0.305

def meterToFoot(meter):
    return meter / 0.305


if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    print("Feet Meters | Meters Feet")

    # starting meters value
    meters = 20

    # starting step value
    x, y = 4, 6

    for feet in range(1, 11):

        line = "{:<5.1f}{:.3f}  | {:<7.1f}{:.3f}"\
            .format(
                feet,
                footToMeter(feet),
                meters,
                meterToFoot(meters)
                )
        print(line)
        
        # swap values to alternate the increment of meters
        x, y = y, x
        meters+=x
