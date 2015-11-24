#!/usr/bin/env python3
"""Check Password

Some Web sites impose certain rules for passwords. Write a function that
checks whether a string is a valid password. Suppose the password rules
are as follows:
A password must have at least eight characters.
A password must consist of only letters and digits.
A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays
valid password if the rules are followed or invalid password otherwise.
"""
import string


def is_digit(char):
    return str(char) in string.digits


def is_alphanumeric(s):
    alphanumeric = string.ascii_letters + string.digits
    for char in s:
        if char not in alphanumeric:
            return False
    return True


def digits_in_str(s):
    count = 0
    for char in s:
        if is_digit(char):
            count += 1
    return count


def password_validator(password):
    pwd = str(password)
    check_digits = digits_in_str(pwd) >= 2
    return is_alphanumeric(pwd) and check_digits and len(pwd) >= 8


if __name__ == "__main__":
    user_password = input('Enter your password: ')
    msg = 'Your password is {}'
    valid_password = password_validator(user_password)
    if valid_password:
        msg = msg.format('valid.')
    else:
        msg = msg.format('invalid.')
    print(msg)


