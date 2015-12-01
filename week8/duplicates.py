#!/usr/bin/env python3
"""
Write a function that returns a new list by eliminating the duplicate
values in the list. Use the following function header: 
def eliminateDuplicates(lst):

Write a test program that reads in a list of integers, invokes the 
function, and displays the result. 
Here is the sample run of the program:

Enter ten numbers: 1 2 3 2 1 6 3 4 5 2 
The distinct numbers are: 1 2 3 6 4 5
"""


def eliminate_duplicates(lst):
    lst = lst.copy()
    lst.sort()
    lenght = len(lst)
    first_item = lst[0]
    idx = 0
    result = [first_item]
    for i in range(lenght):
        current = lst[i]
        if current != result[idx]:
            result.append(current)
            idx += 1
    return result


if __name__ == "__main__":
    user_input = input('Enter ten numbers: ')
    numbers = [ int(n) for n in user_input.split(' ')]
    lst = eliminate_duplicates(numbers)
    msg = 'The distinct numbers are {}'.format(lst)
    print(msg)

