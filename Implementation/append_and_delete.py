# https://www.hackerrank.com/challenges/append-and-delete/problem
def appendAndDelete(s,t,k):
  # calc letters to delete
  to_delete = 0
  for idx,char in enumerate(s):
    if (idx > len(t) - 1) or (not char == t[idx]):
      to_delete = len(s) - idx
      break
  # calc letters to add
  to_add = len(t) - (len(s) - to_delete)
  # determine whether possible in number of moves
  base_opps = to_delete + to_add
  if base_opps > k:
    return 'No'
  elif base_opps == k:
    return 'Yes'
  elif base_opps < k:
    if to_add % 2 == 0:
      return 'Yes'
    else:
      return 'No'
      