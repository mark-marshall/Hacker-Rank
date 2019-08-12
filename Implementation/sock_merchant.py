# https://www.hackerrank.com/challenges/sock-merchant/problem
import math
def sockMerchant(n, ar):
  socks = {}
  pairs = 0
  for sock in ar:
    if sock in socks:
      socks[sock] += 1
    elif sock not in socks:
      socks[sock] = 1
  for tally in socks:
    pairs += math.floor(socks[tally] / 2)
  return pairs
