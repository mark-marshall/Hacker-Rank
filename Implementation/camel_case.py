# https://www.hackerrank.com/challenges/camelcase/problem
def camelcase(s):
  count = 1;
  for char in s:
    if char == char.upper():
      count += 1
  return count
  