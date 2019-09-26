# https://www.hackerrank.com/challenges/flatland-space-stations/problem
def flatlandSpaceStations(m, n, c):
  c.sort()
  cur_idx = 0
  max_dist = 0
  # cover the case where m = n for faster returns
  if n == m:
    return 0
  for i in range (m):
    # initialize nearest variable
    nearest = 0
    # cover the case where i only has an upper number
    if i < c[cur_idx]:
      nearest = c[cur_idx] - i
      if nearest > max_dist:
        max_dist = nearest
      continue
    # cover the case where i is larger than the cur_idx + 1 city
    while (cur_idx < len(c) - 1) and (i > c[cur_idx + 1]):
      cur_idx += 1
    # calculate lower and upper values
    lower = abs(i - c[cur_idx])
    nearest = lower
    if (not cur_idx == len(c)-1) and (not i > c[cur_idx + 1]):
      higher = abs(c[cur_idx + 1] - i)
      if higher < lower:
        nearest = higher
    # check whether max_dist needs updating
    if nearest > max_dist:
      max_dist = nearest
  # return
  return max_dist
