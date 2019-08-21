# Hired.com
# takes a binary tree in the form of an array and works out which side is greater
# returns "" in cases where sides are equal or the provided array is empty
def solution(arr):
  if len(arr) > 1:
    # remove the root
    updated_arr = arr[1:]
    # set the current level of tree
    cur_level = 1
    # initialize left and right score
    left = 0
    right = 0
    # main logic loop
    while len(updated_arr):
      # handles the first level where the cur_level to nodes relationship is different
      if cur_level == 1:
        left += updated_arr[0]
        updated_arr = updated_arr[1:]
        if len(updated_arr):
          right += updated_arr[0]
          updated_arr = updated_arr[1:]
        cur_level += 1
      # handles all subsequent levels
      else:
        # handle left-hand-side update
        for _ in range(2**cur_level // 2):
          if len(updated_arr):
            if updated_arr[0] > 0:
              left += updated_arr[0]
            updated_arr = updated_arr[1:]
          else:
            break
        # handle right-hand-side update
        for _ in range (2**cur_level // 2):
          if len(updated_arr):
            if updated_arr[0] > 0:
              right += updated_arr[0]
            updated_arr = updated_arr[1:]
          else:
            break
    # compare each side and return the correct result
    if left > right:
      return "Left"
    elif left < right:
      return "Right"
    elif left == right:
      return ""
  else:
    return ""
