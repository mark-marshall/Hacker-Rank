# https://www.hackerrank.com/challenges/max-array-sum/problem

def maxSubsetSum(arr):
  cur_max = None
  cur_max_vals = [arr[0]]
  if arr[0] > arr[1]:
    cur_max_vals.append(arr[0])
    cur_max = arr[0]
  else:
    cur_max_vals.append(arr[1])
    cur_max = arr[1]
  for idx,num in enumerate(arr):
    if idx > 1:
      cur_one = num
      cur_two = num + cur_max_vals[len(cur_max_vals)-2]
      if cur_max > cur_one and cur_max > cur_two:
        cur_max_vals.append(cur_max)
      elif cur_one > cur_two:
        cur_max_vals.append(cur_one)
        if cur_one > cur_max:
          cur_max = cur_one
      else:
        cur_max_vals.append(cur_two)
        if cur_two > cur_max:
          cur_max = cur_two
  return cur_max
  