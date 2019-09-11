# https://www.hackerrank.com/challenges/utopian-tree/problem
def utopianTree(n):
  h = 1
  for i in range(n + 1):
    if not i == 0:
      if not i % 2 == 0:
        h *= 2
      elif i % 2 == 0:
        h += 1
  return h
