#!/usr/bin/env python3
"""Bubble Sort
Write a sort function that uses the bubble­sort algorithm.
The bubble­sort algorithm makes several passes through the list.
On each pass, successive neighboring pairs are compared.
If a pair is in decreasing order, its values are swapped;
otherwise, the values remain unchanged. 
The technique is called a bubble sort or sinking sort because the
smaller values gradually “bubble” their way to the top and the larger
values “sink” to the bottom. 
Write a test program that reads in ten numbers, invokes the function,
and displays the sorted numbers. 
"""


def bubble_sort(lst):

    sorted = False
    len_lst = len(lst)
    while not sorted:
        sorted = True
        for i in range(len_lst - 1):
            a, b = lst[i], lst[i+1]
            if a > b:
                lst[i], lst[i+1] = b, a
                sorted = False

if __name__ == "__main__":
    user_input = input('Enter ten numbers: ')
    lst = user_input.split(' ')
    bubble_sort(lst)
    msg = 'The sorted list is {}'.format(' '.join(lst))
    print(msg)

