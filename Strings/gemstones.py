# https://www.hackerrank.com/challenges/gem-stones/problem
def gemstones(arr):
  minerals = set(arr[0])
  for rock in arr[1:]:
    minerals = minerals & set(rock)
  return len(minerals)
  