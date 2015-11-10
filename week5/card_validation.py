#!/usr/bin/env python3

'''
Write a program that prompts the user to enter
a credit card number as an integer.
Display whether the number is valid or invalid.

1. Double every second digit from right to left.
If doubling of a digit results in a two­digit number,
add up the two digits to get a single­digit number

2. Now add all single­digit numbers from Step 1.
4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

3. Add all digits in the odd places from right to
left in the card number.
6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

4. Sum the results from Steps 2 and 3.
37 + 38 = 75

5. If the result from Step 4 is divisible by 10
the card number is valid; otherwise, it is invalid.
For example, the number 4388576018402626 is invalid
but the number 4388576018410707 is valid.

Credit card numbers follow certain patterns:
It must have between 13 and 16 digits
and the number must start with:

4  for Visa cards 
5  for MasterCard credit cards 
37 for American Express cards 
6  for Discover cards 
'''

def numberToMatrix(number):
    '''Create a matrix of numbers from card number string'''
    return [ int(char) for char in number ]  

def getOddDigits(number):
    '''Get odd place digits'''
    return number[::2]

def getEvenDigits(number):
    '''Get even place digits'''
    return number[1::2]

def isValid(number):
    '''Return true if the card number isvalid'''
    matrix = numberToMatrix(number)
    odds = getOddDigits(matrix)
    even = getEvenDigits(matrix)
    sumOdds = sumOfDoubleOddPlace(odds)
    sumEven = sumOfEvenPlace(even)
    validNumber = (sumOdds + sumEven) % 10 == 0
    validLen = lenValidator(number)
    validPrefix = prefixValidator(number)
    return validNumber and validLen and validPrefix

def sumOfDoubleOddPlace(number):
    '''Return sum of odd place digits in number'''
    return sum([ getDigit(n) for n in number ])

def sumOfEvenPlace(number):
    '''Get result from step 2'''
    return sum(number)

def getDigit(number):
    '''
    Return this number if it is a single digit, otherwise,
    return the sum of the two digits
    '''
    number = number * 2
    if number < 10:
        return number
    n = [ int(n) for n in list(str(number)) ]
    return sum(n)

def lenValidator(number):
    '''Return True if number has between 13 and 16 digits'''
    return 13 <= len(number) <= 16

def prefixValidator(number):
    '''Return True if a prefix is matched'''
    PREFIXES = [4, 5, 37, 6]
    for prefix in PREFIXES:
        if prefixMatched(number, prefix):
            return True
    return False

def prefixMatched(number, d):
    '''Return true if the digit d is a prefix for number'''
    return d == getPrefix(number, getSize(d))

def getSize(d):
    '''Return the number of digits in d'''
    return len(str(d))

def getPrefix(number, k):
    '''
    Return the first k number of digits from number. If the
    number of digits in number is less than k,return number.
    '''
    return int(number[:k])

if __name__ == "__main__":

    card_number = input("Enter the card number: ")
    msg = "The entered card number is not valid."
    if isValid(card_number):
        msg = "Your card {} is valid.".format(card_number)
    print(msg)
