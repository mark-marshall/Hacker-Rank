# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

# Python
def hackerrankInString(s):
  result = 'hackerrank'
  cur_idx = 0
  for char in s:
    if char == result[cur_idx]:
      if cur_idx == len(result) - 1:
        return 'YES'
      cur_idx += 1
  return 'NO'

# JavaScript
const hackerrankInString = s => {
  const result = 'hackerrank';
  let cur_idx = 0;
  let complete = false
  s.split('').forEach(char => {
    if (char === result[cur_idx]){
      if(cur_idx === (result.length - 1)){
        complete = true
      }
      cur_idx += 1
    }
  })
  if(complete){
    return 'YES'
  }
  return 'NO'
}