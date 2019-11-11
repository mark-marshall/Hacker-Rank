# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
def minimumAbsoluteDifference(arr):
  # initialise the cur_min variable
  cur_min = ''
  # remove duplicates and sort
  arr.sort()
  # lop through numbers
  for idx,num in enumerate(arr):
    if not (idx == 0 or idx == len(arr)-1):
      # get left and right nums
      pair_left = abs(num - arr[idx-1])
      pair_right = abs(num - arr[idx+1])
      # compare min(pair) to cur_min
      if cur_min == '' or min(pair_left,pair_right) < cur_min:
        cur_min = min([pair_left,pair_right])
  # return ans
  return cur_min
