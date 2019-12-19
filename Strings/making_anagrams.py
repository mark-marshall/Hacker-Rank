# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

# Python
def makeAnagram(a, b):
  dels = 0
  tally = {}
  for char in a:
    if char in tally:
      tally[char] += 1
    else:
      tally[char] = 1
  for char in b:
    if (char not in tally) or (tally[char] == 0):
      dels += 1
    else:
      tally[char] -= 1
  for char in tally:
    if tally[char] > 0:
      dels += tally[char]
  return dels

# JavaScript
const makeAnagram = (a,b) => {
    let dels = 0
    const tally = {}
    a.forEach(char => {
        char in tally ?
        tally[char] += 1 :
        tally[char] = 1
    })
    b.forEach(char => {
        (!(char in tally)) || (tally[char] === 0) ?
        dels += 1 :
        tally[char] -= 1
    })
    for(let key in tally){
        tally[char] > 0 ?
        dels += tally[char]
    }
    return dels
}
