#!/usr/bin/env python3
"""Check SSN

Write a program that prompts the user to enter a Social Security number
in the format ddd­dd­dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.
"""
import string


def is_numeric(s):
    for char in s:
        if not is_digit(char):
            return False
    return True


def matrix_to_str(matrix):
    return ''.join(matrix)


def is_digit(char):
    return str(char) in string.digits


def matrix_len_check(matrix, length):
    return len(matrix) == length


def substring_len_check(matrix):
    sub1, sub2, sub3 = matrix
    return len(sub1) == 3 and len(sub2) == 2 and len(sub3) == 4


def ssn_validator(ssn):
    matrix = str(ssn).split('-')

    if not matrix_len_check(matrix, 3):
        return False

    if not substring_len_check(matrix):
        return False

    codestring = matrix_to_str(matrix)
    onlydigits = is_numeric(codestring)

    return onlydigits


if __name__ == "__main__":

    user_ssn = input('Enter your Social Security Number: ')
    msg = 'Your SSN {} is {}'
    valid_ssn = ssn_validator(user_ssn)
    if valid_ssn:
        msg = msg.format(user_ssn, 'valid.')
    else:
        msg = msg.format(user_ssn, 'invalid.')
    print(msg)


