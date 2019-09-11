# https://www.hackerrank.com/challenges/extra-long-factorials/problem
def extraLongFactorials(n):
  def calculateFactorials(n):
    if n == 0:
      return 1
    return n * calculateFactorials(n-1)
  print(calculateFactorials(n))
  