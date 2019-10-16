# https://www.hackerrank.com/challenges/fair-rations/problem
def fairRations(B):
  loaves = 0
  for i in reversed(range(len(B))):
    if not (B[i] % 2 == 0):
      if i == 0:
        return 'NO'
      elif i > 0:
        loaves += 1
        B[i] = B[i] + 1
        if i-1 >= 0:
          loaves += 1
          B[i-1] = B[i-1] + 1
  return loaves
