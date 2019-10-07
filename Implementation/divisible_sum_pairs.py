# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Python
def divisibleSumPairs(n, k, ar):
  tally = 0;
  for i in range(len(ar)):
    for j in range(i+1,len(ar)):
      if (ar[i]+ar[j]) % k == 0:
        tally += 1
  return tally

# JavaScript
const divisibleSumPairs = (n,k,ar) => {
  let tally = 0;
  let i;
  let j;
  for(i=0; i<ar.length; i++){
    for(j=i+1; j<ar.length; j++){
      if((ar[i] + ar[j]) %k === 0){
        tally += 1
      }
    }
  }
  return tally;
}
