# https://www.hackerrank.com/challenges/equality-in-a-array/problem

# Python
def equalizeArray(arr):
  tally = {}
  cur_largest = 0
  # loop over nums in the array
  for num in arr:
    # increment dict for the num if it already exists
    if num in tally:
      tally[num] += 1
    # otherwise, add it to the dict and assign 1
    elif num not in tally:
      tally[num] = 1
    # check whether this is now the num with largest count
    if tally[num] > cur_largest:
      cur_largest = tally[num]
  # return array length - count of most occuring num
  return len(arr) - cur_largest

# JavaScript
const equalizeArray = arr => {
  const tally = {}
  let cur_largest = 0
  # loop over nums in the array
  arr.forEach(num => {
    # increment dict for the num if it already exists
    if(num in tally){
      tally[num] += 1
    }
    # otherwise, add it to the dict and assign 1
    else{
      tally[num] = 1
    }
    # check whether this is now the num with largest count
    if(tally[num] > cur_largest){
      cur_largest = tally[num]
    }
  })
  # return array length - count of most occuring num
  return arr.length - cur_largest
}
