#!/usr/bin/env python3
"""Rectangle

Write a test program that creates two Rectangle objects
one with width 4 and height 40 and the other with width
3.5 and height 35.7.
Display the width, height, area, and perimeter of each
rectangle in this order.
"""


class Rectangle:

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

if __name__ == "__main__":
    rect1 = Rectangle(4, 40)
    rect2 = Rectangle(3.5, 35.7)
    for rect in [rect1, rect2]:
        msg = "Rectangle:\n"
        msg += "  width:{}\n".format(rect.width)
        msg += "  height:{}\n".format(rect.height)
        msg += "  area:{}\n".format(rect.get_area())
        msg += "  perimeter:{}\n".format(rect.get_perimeter())
        print(msg, end="\n")


