# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    cur_tallest = (0,0)
    for candle_height in ar:
        if candle_height > cur_tallest[0]:
            cur_tallest = (candle_height, 1)
        elif candle_height == cur_tallest[0]:
            cur_tallest = (cur_tallest[0], cur_tallest[1] + 1)
    return cur_tallest[1]
