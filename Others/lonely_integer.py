# https://www.hackerrank.com/challenges/lonely-integer/problem
def lonelyinteger(a):
  tally = {}
  for num in a:
    if num in tally:
      tally[num] = False
    else:
      tally[num] = True
  return [key for key, value in tally.items() if value == True][0]
  