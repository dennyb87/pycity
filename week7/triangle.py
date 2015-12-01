#!/usr/bin/env python3
"""Triangle
Design a class named Triangle that extends the GeometricObject class.
The Triangle class contains:

- Three float data fields named side1, side2, and side3 to denote the
  three sides of the triangle.

- A constructor that creates a triangle with the specified side1, side2,
  and side3 with default values 1.0.

- The accessor methods for all three data fields.

- A method named getArea() that returns the area of this triangle.

- A method named getPerimeter() that returns the perimeter of this
  triangle.

- A method named __str__() that returns a string description for the
  triangle.

Implement the Triangle
class. Write a test program that prompts the user to enter the three
sides of the triangle, a color, and 1 or 0 to indicate whether the
triangle is filled. The program should create a Triangle object with
these sides and set the color and filled properties using the input.
The program should display the triangle’s area, perimeter, color, and
True or False to indicate whether the triangle is filled or not.
"""
import math
from GeometricObject import GeometricObject


class Triangle(GeometricObject):

    def __init__(self, side1=1.0, side2=1.0, side3=1.0, *args):
        super().__init__(*args);
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def get_area(self):
        p = self.get_perimeter() / 2
        area = math.sqrt(
            p *
            (p - self.__side1) *
            (p - self.__side2) *
            (p - self.__side3)
        )
        return area

    def __str__(self):
        info = "Triangle: side1 = {} side2 = {} side3 = {}".format(
            self.__side1, self.__side2, self.__side3
        )
        return info

if __name__ == "__main__":
    side1 = float(input('Enter side1: '))
    side2 = float(input('Enter side2: '))
    side3 = float(input('Enter side3: '))
    color = input('Enter color: ')
    filled = int(input('Enter filled: '))

    triangle = Triangle()

    msg = "Triangle:\n area:{}\n perimeter:{}\n color:{}\n isFilled:{}"\
        .format(
        triangle.get_area(),
        triangle.get_perimeter(),
        triangle.get_color(),
        triangle.is_filled()
    )
    print(msg)
