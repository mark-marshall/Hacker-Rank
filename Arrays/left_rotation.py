# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
def rotLeft(a, d):
    for _ in range (d):
        pivot = a.pop(0)
        a.append(pivot)
    return a
