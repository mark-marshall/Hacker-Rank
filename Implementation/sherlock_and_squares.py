# hackerrank.com/challenges/sherlock-and-squares/problem
def squares(a, b):
  cur = math.ceil(math.sqrt(a))
  count = 0
  while math.pow(cur,2) <= b:
    if math.pow(cur,2) >= a:
      count += 1
    cur += 1
  return count
