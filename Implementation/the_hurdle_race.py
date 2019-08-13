# https://www.hackerrank.com/challenges/the-hurdle-race/problem
def hurdleRace(k, height):
    calc = max(height) - k
    if calc > 0:
        return calc
    return 0
    