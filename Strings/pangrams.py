# https://www.hackerrank.com/challenges/pangrams/problem

# Python
def pangrams(s):
    tally = {}
    num_alph = 0
    for char in s.replace(" ",""):
        if char.lower() not in tally:
            tally[char.lower()] = True
            num_alph += 1
    print(tally)
    if num_alph == 26:
        return "pangram"
    else:
        return "not pangram"

# JavaScript
const pangrams = s => {
  const tally = {};
  let num_alph = 0;
  const sArr = s.trim().split("");
  sArr.forEach(char => {
    if((!(char.toLowerCase() in tally)) && (char !== " ")){
      tally[char.toLowerCase()] = true
      num_alph += 1
    }
  })
  console.log(num_alph)
  if(num_alph == 26){
    return "pangram"
  } else {
    return "not pangram"
  }
}
