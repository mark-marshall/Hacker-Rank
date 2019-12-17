# https://www.hackerrank.com/challenges/2d-array/problem

# Python
def hourglassSum(arr):
  hourglasses = []
  cur_max = None
  cur_top_row = 0
  cur_idx = 0
  while len(hourglasses) < 16:
    cur_hourglass = arr[cur_top_row][cur_idx:cur_idx+3] + [arr[cur_top_row+1][cur_idx+1]] + arr[cur_top_row+2][cur_idx:cur_idx+3]
    hourglasses.append(cur_hourglass)
    if cur_max == None or sum(cur_hourglass) > cur_max:
      cur_max = sum(cur_hourglass)
    if cur_idx <= 2:
      cur_idx += 1
    else:
      cur_idx = 0
      cur_top_row += 1
  return cur_max

# JavaScript
const hourglassSum = (arr) => {
  const hourglasses = []
  let cur_max = null
  let top_row = 0
  let idx = 0
  while(hourglasses.length < 16){
    cur_hourglass = arr[top_row].slice(idx,idx+3).concat(arr[top_row+1][idx+1]).concat(arr[top_row+2].slice(idx,idx+3))
    hourglasses.push(cur_hourglass)
    cur_val = cur_hourglass.reduce((tot,num) => {return tot+num},0)
    cur_max === NaN || cur_val > cur_max ?
    cur_max = cur_val :
    null
    // navigate grid
    if(idx <= 2){
      idx += 1
    } else {
      idx = 0
      top_row += 1
    }
  }
  return cur_max
}