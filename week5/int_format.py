#!/usr/bin/env python3

'''
Write a function with the following header to format
the integer with the specified width.
defformat(number,width):
The function returns a string for the number with
prefix 0 s. The size of the string is the width.
For example, format(34, 4) returns "0034" and
format(34, 5) returns "00034" . If the number is longer
than the width, the function returns the string
representation for the number.
For example, format(34, 1) returns "34".
3 of 4
Write a test program that prompts the user to enter
a number and its width and displays a string
returned from invoking format(number, width).
Here is a sample run:
Enteraninteger:453
Enterthewidth:6
Theformattednumberis000453
'''

def format(n, width):
    ZERO = "0"
    number = list(str(n))
    num_len = len(number)
    diff = width - num_len
    if diff > 0:
        number.insert(0, ZERO * diff)
    return "".join(number)

if __name__ == "__main__":
    
    number = int(input("Enter an integer: "))
    width = int(input("Enter the width: "))
    formatted = format(number, width)
    msg = "The formatted number is {}".format(formatted)
    print(msg)
