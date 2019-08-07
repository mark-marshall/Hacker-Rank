# https://www.hackerrank.com/challenges/grading/problem
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        to_next = 5 - (grade % 5)
        if grade >= 38 and to_next < 3:
          new_grades.append(grade + to_next)
          continue
        new_grades.append(grade)
    return new_grades
