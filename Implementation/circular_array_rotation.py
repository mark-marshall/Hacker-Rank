# https://www.hackerrank.com/challenges/circular-array-rotation/problem
def circularArrayRotation(a, k, queries):
  for _ in range (k):
    mover = a[-1]
    del a[-1]
    a.insert(0,mover)
  return [a[num] for num in queries]
