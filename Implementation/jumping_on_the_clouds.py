# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
def jumpingOnClouds(c):
  cur_cloud = 0
  num_jumps = 0
  while cur_cloud < (len(c) - 1):
    if (cur_cloud + 2) < len(c) and c[cur_cloud + 2] == 0:
      cur_cloud += 2
    else:
      cur_cloud += 1
    num_jumps += 1
  return num_jumps
  