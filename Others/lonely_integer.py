# https://www.hackerrank.com/challenges/lonely-integer/problem
def lonelyinteger(a):
  tally = []
  for num in a:
    if num not in tally:
      tally.append(num)
    else:
      tally.remove(num)
  return tally[0]
  