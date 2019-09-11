# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
def catAndMouse(x, y, z):
  catADist = abs(z - x)
  catBDist = abs(z - y)
  if catADist == catBDist:
    return "Mouse C"
  elif catBDist > catADist:
    return "Cat A"
  elif catADist > catBDist:
    return "Cat B"