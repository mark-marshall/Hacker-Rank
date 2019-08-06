# https://www.hackerrank.com/challenges/staircase/problem
import math
import os
import random
import re
import sys

def staircase(n):
  cur_stairs = 1
  for _ in range(n):
    spaces = (n - cur_stairs)
    print(" " * spaces + "#" * cur_stairs)
    cur_stairs += 1
