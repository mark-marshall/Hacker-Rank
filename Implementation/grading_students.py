# https://www.hackerrank.com/challenges/grading/problem
import math
import os
import random
import re
import sys

def get_multiple(grade):
    cur = grade
    while (cur % 5) != 0:
      cur += 1
    return (cur - grade, cur)

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade >= 38:
            ans = get_multiple(grade)
            if ans[0] < 3:
                new_grades.append(ans[1])
                continue
        new_grades.append(grade)
    return new_grades
    