def jumpingOnClouds(c, k):
  c.append(c[0])
  e = 100
  cur_idx = 0
  while cur_idx < (len(c) - k):
    cur_idx += k
    if c[cur_idx] == 1:
      e -= 3
    else:
      e -= 1 
  return e
  