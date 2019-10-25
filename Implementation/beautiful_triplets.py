# https://www.hackerrank.com/challenges/beautiful-triplets/problem
def beautifulTriplets(d, arr):
  b_triplets = 0
  for num in arr:
    second = num + d
    third = num + (d * 2)
    if second in arr and third in arr:
      b_triplets += 1
  return b_triplets
  