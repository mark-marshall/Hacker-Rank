# https://www.hackerrank.com/challenges/chocolate-feast/problem
def chocolateFeast(n, c, m):
  init = n // c
  money = n - init * c
  count = init
  wrappers = init
  while wrappers >= m:
    count += 1
    wrappers -= m
    wrappers += 1
  return count
  