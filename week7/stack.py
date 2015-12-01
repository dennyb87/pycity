#!/usr/bin/env python3
"""Stack
In the course, the Stack class is implemented using composition.
Define a new Stack class using inheritance that extends list.
Draw UML diagrams of the new class. Implement it.
Write a test program that prompts the user to enter five strings
and displays them in reverse order.
"""


class Stack(list):

    def is_empty(self):
        return super().__len__() == 0

    def peek(self):
        return super().__getitem__(-1)

    def push(self, item):
        return super().append(item)

    def pop(self):
        return super().pop()

    def get_size(self):
        return super().__len__()

if __name__ == "__main__":
    strings = [input('Enter a string: ') for n in range(5)]
    for s in strings:
        stack = Stack(s)
        stack.reverse()
        print(stack)
