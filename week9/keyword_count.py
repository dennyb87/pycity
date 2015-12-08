#!/usr/bin/env python3
"""Count the occurrences of each keyword 
Write a program that reads in a Python source code file and counts the
occurrence of each keyword in the file.
Your program should prompt the user to enter the Python source code
filename. 
"""
import os
from counter import Counter

keywords = """
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
"""

if __name__ == "__main__":
    filename = input('Enter filename: ')
    keywords = keywords.split()
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            data = f.read().split()
            C = Counter(data, keywords)
            matched = C.collection
            f.closed
            for item in matched.items():
                print('Keyword "{}" occur {} times'.format(
                    item[0], item[1]
                ))
    else:
        print('File "{}" does not exist!'.format(filename))
