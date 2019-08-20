# https://www.hackerrank.com/challenges/migratory-birds/problem
def migratoryBirds(arr):
  tally = {}
  cur_biggest = arr[0]
  for bird in arr:
      if bird in tally:
          tally[bird] += 1
      elif bird not in tally:
          tally[bird] = 1
      if (tally[bird] > tally[cur_biggest]) or (tally[bird] == tally[cur_biggest] and bird < cur_biggest):
        cur_biggest = bird
  return cur_biggest