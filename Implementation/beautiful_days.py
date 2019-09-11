# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
def beautifulDays(i, j, k):
  beautiful_days = 0
  for day in range (i,j + 1):
    rev_day = int(str(day)[::-1])
    if (day - rev_day) % k == 0:
      beautiful_days += 1
  return beautiful_days
  