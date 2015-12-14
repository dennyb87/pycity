#!/usr/bin/env python3
"""Assign grades
Write a program that reads a list of scores and then assigns grades
based on the following scheme: 
The grade is A if score is 7= best – 10. 
The grade is B if score is 7= best – 20. 
The grade is C if score is 7= best – 30. 
The grade is D if score is 7= best – 40. 
The grade is F otherwise. 
 
Here is a simple run:
Enter scores: 40 55 70 58 
Student 0 score is 40 and grade is C 
Student 1 score is 55 and grade is B 
Student 2 score is 70 and grade is A 
"""


def get_grade(points):
    score = 70 - points
    grades = [(40, 'D'), (30, 'C'), (20, 'B'), (10, 'A')]
    result = ''
    for grade in grades:
        if score <= grade[0]:
            result = grade[1]
    return result


def scorer(points):
    results = []
    for point in points:
        results.append(get_grade(point))
    return results


if __name__ == "__main__":
    user_input = input('Enter scores: ')
    points = [int(n) for n in user_input.split(' ')]
    points = [ int(n) for n in user_input.split(' ')]
    scores = scorer(points)
    for n in range(len(points)):
        msg = 'Student {} score is {} and grade is {}'.format(
            n, points[n], scores[n]
        )
        print(msg)
