# https://www.hackerrank.com/challenges/save-the-prisoner/problem
def saveThePrisoner(n, m, s):
  if (s + (m - 1)) <= n:
    return s + (m - 1)
  else:
    remainder = (m % n) - 1
    if remainder > 0:
      if s + remainder > n:
        return remainder - (n - s)
      return s + remainder
    elif remainder == 0:
      return s
    elif remainder == -1:
      if s - 1 > 0:
        return s - 1
      return n
