# https://www.hackerrank.com/challenges/angry-professor/problem
def angryProfessor(k, a):
  arrived = 0
  for arrivals in a:
    if arrivals <= 0:
      arrived += 1
    if arrived == k:
      return 'NO'
  return 'YES'
  