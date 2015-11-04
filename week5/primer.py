#!/usr/bin/env python3

'''
In the course, the program PrimeNumberFunction.py
provides the isPrime(number) function for testing
whether a number is prime. Use this function to
find the number of prime numbers less than 10,000.
'''

# Check whether number is prime 
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

def primeInRange(start, end):
    prime = []
    for number in range(start, end):
        if isPrime(number):
            prime.append(number)

    return prime

if __name__ == "__main__":

    import doctest
    doctest.testmod(raise_on_error=True)

    result = len(primeInRange(2, 10000))
    msg = "The number of prime numbers less than 10,000 is {}"\
        .format(result)
    print(msg)
