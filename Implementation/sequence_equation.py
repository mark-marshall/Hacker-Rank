# https://www.hackerrank.com/challenges/permutation-equation/problem

# Python
def permutationEquation(p):
  y = []
  for x in range(1,len(p) + 1):
    ph = (p.index(x) + 1)
    y.append(p.index(ph) + 1)
  return y

# JavaScript
const permutationEquation = p =>{
  const y = []
  for(i=1;i<p.length + 1;i++){
    const ph = p.indexOf(i) + 1;
    y.push(p.indexOf(ph) + 1);
  }
  return y
}
