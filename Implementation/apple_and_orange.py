# https://www.hackerrank.com/challenges/apple-and-orange/problem
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # initialize fruit counts
    apple_count = 0
    orange_count = 0
    # combine apple and orange arrays
    fruits = [('apple', distance) for distance in apples] + [('orange', distance) for distance in oranges]
    # loop over the combined array
    for fruit in fruits:
        if fruit[0] == 'apple':
            start = a
        elif fruit[0] == 'orange':
            start = b
        fruit_landing = start + fruit[1]
        if s <= fruit_landing <= t:
            if fruit[0] == 'apple':
                apple_count += 1
            elif fruit[0] == 'orange':
                orange_count += 1
    # print final counts
    print(apple_count)
    print(orange_count)
