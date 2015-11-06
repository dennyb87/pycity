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
'''

#Create a matrix of numbers from card number string
def numberToMatrix(number):
    return [ int(char) for char in number ]  

#Get odd place digits
def getOddDigits(number):
    return number[::2]

#Get even place digits
def getEvenDigits(number):
    return number[1::2]

#Return true if the card number isvalid
def isValid(number):
    matrix = numberToMatrix(number)
    odds = getOddDigits(matrix)
    even = getEvenDigits(matrix)
    sumOdds = sumOfDoubleOddPlace(odds)
    sumEven = sumOfEvenPlace(even)
    valid = (sumOdds + sumEven) % 10 == 0
    return valid

#Return sum of odd place digits in number
def sumOfDoubleOddPlace(number):
    total = 0
    for n in number:
        total += getDigit(n)
    return total

#Get result from step 2
def sumOfEvenPlace(number):
    return sum(number)

#Return this number if it is a single digit,otherwise,return
#the sum of the two digits
def getDigit(number):
    number = number * 2
    if number < 10:
        return number
    n = [ int(n) for n in list(str(number)) ]
    return sum(n)

#Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    pass

#Return the number of digits in d
def getSize(d):
    pass

#Return the first k number of digits from number. If the
#number of digits in number is less than k,return number.
def getPrefix(number, k):
    pass

if __name__ == "__main__":

    card_number = input("Enter the card number: ")
    msg = "The entered card number is not valid."
    if isValid(card_number):
        msg = "Your card {} is valid.".format(card_number)
    print(msg)
