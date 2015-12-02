#!/usr/bin/env python3
"""Anagrams
Write a function that checks whether two words are anagrams. 
Two words are anagrams if they contain the same letters.
For example, silent and listen are anagrams.
The header of the function is: 
def isAnagram(s1, s2):

(Hint: Obtain two lists for the two strings.
Sort the lists and check if two lists are identical.) 
"""
from bubble import bubble_sort


def is_anagram(s1, s2):
    s1, s2 = list(s1), list(s2)
    bubble_sort(s1), bubble_sort(s2)
    return s1 == s2


if __name__ == "__main__":
    s1, s2 = input('Enter a string 1: '), input('Enter a string 2: ')
    msg = 'The two string are not anagrams'
    if is_anagram(s1, s2):
        msg = 'The string "{}" is the anagram of "{}"'.format(s1, s2)
    print(msg)

