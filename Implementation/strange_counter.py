# https://www.hackerrank.com/challenges/strange-code/problem
def strangeCounter(t):
  ac_t = 1
  cur_val = 3
  cur_max_val = 3
  while not ac_t == t:
    if ac_t < t <= (ac_t + cur_max_val - 1):
      return cur_val - (t - ac_t)
    else:
      ac_t += cur_max_val
      cur_max_val *= 2
      cur_val = cur_max_val
  return cur_val
