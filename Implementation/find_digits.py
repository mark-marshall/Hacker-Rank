# https://www.hackerrank.com/challenges/find-digits/problem
def findDigits(n):
  divisors = 0
  for dig in str(n):
    num = int(dig)
    if not num == 0 and n % num == 0:
      divisors += 1
  return divisors
  