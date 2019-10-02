# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

# Python
def kaprekarNumbers(p, q):
  kaprekarNumbersRes = ''
  for i in range (p,q+1):
    squared = list(str(i * i))
    if len(squared) > 1:
      right = int(''.join(squared[-len(str(i)):]))
      if len(squared) % 2 == 0:
        left = int(''.join(squared[:len(str(i))]))
      else:
        left = int(''.join(squared[:len(str(i))-1]))
      if (right > 0) and ((right + left) == i):
        kaprekarNumbersRes += f" {i}"
    elif int(squared[0]) == i:
      kaprekarNumbersRes += f" {i}"
  if not len(kaprekarNumbersRes):
    print('INVALID RANGE')
  else:
    print(kaprekarNumbersRes.lstrip())
