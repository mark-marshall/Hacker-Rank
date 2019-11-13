# https://www.hackerrank.com/challenges/reduced-string/problem
def superReducedString(s):
  # initialize string, idx, and complete check
  newString = ''
  cur_idx = 0
  complete = True
  # loop through the chars
  while cur_idx < len(s):
    # check if its the last char
    if cur_idx == len(s)-1:
      newString += s[cur_idx]
      break
    # check if adjacent letter is the same
    elif s[cur_idx] == s[cur_idx+1]:
      cur_idx += 2
      # change complete to false
      complete = False
    # otherwise add the char and increment
    else:
      newString += s[cur_idx]
      cur_idx += 1
  # check if all operation are complete
  if complete == True:
    if len(newString):
      # return string if it not empty
      return newString
    else:
      # otherwise return Empty String
      return 'Empty String'
  # otherwise do the operation again
  else:
    return superReducedString(newString)
