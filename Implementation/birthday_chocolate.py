# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Python
def birthday(s, d, m):
  ways = 0;
  for idx, num in enumerate(s):
    # add this num plus x nums in front in arr
    # don't add if we've got to the end of the arr
    offset = 0
    tally = num
    while (idx + offset < len(s) - 1) and (not offset + 1 == m):
      offset += 1
      tally += s[idx + offset]
    # check whether the total is equal to the num of days
    if tally == d:
      ways += 1
  # return num of ways
  return ways

# JavaScript
const birthday = (s,d,m) => {
  let ways = 0;
  for(i=0;i<s.length;i++){
    let offset = 0;
    let tally = s[i];
    while((i + offset < s.length - 1) && (offset +1 !== m)){
      offset += 1;
      tally += s[i + offset]
    }
    if(tally === d){
      ways += 1;
    }
  }
  return ways
}
