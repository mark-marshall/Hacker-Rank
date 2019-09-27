# https://www.hackerrank.com/challenges/mars-exploration/problem

# Python
def marsExploration(s):
  changed_char_counter = 0
  sos = 'SOS'
  cur_idx = 0
  for char in s:
    if not char.upper() == sos[cur_idx]:
      changed_char_counter += 1
    if cur_idx == (len(sos) - 1):
      cur_idx = 0
    elif cur_idx < (len(sos) - 1):
      cur_idx += 1
  return changed_char_counter

# JavaScript
const marsExploration = s => {
  const sos = 'SOS'
  let changed_char_counter = 0
  let cur_idx = 0
  const sArr = s.split('')
  sArr.forEach(char => {
    if(char.toUpperCase() !== sos[cur_idx]){
      changed_char_counter += 1
    }
    if(cur_idx === (sos.length - 1)){
      cur_idx = 0
    }
    else if(cur_idx < (sos.length - 1)){
      cur_idx += 1
    }
  })
  return changed_char_counter
}
