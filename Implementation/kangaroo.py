# https://www.hackerrank.com/challenges/kangaroo/problem
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # check to see if slower/same-speed moving kangaroo starts behind
    if (x1 > x2 and v1 >= v2) or (x1 < x2 and v1 <= v2):
        return 'NO'
    else:
        roo_1_cur = x1
        roo_2_cur = x2
        # increment kangaroo positions with respective hops until an end condition is met
        while True:
            if (roo_1_cur > roo_2_cur and v1 > v2) or (roo_1_cur < roo_2_cur and v1 < v2):
                return 'NO'
            elif roo_1_cur == roo_2_cur:
                return 'YES'
            else:
                roo_1_cur += v1
                roo_2_cur += v2
