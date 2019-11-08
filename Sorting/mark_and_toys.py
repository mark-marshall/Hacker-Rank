# https://www.hackerrank.com/challenges/mark-and-toys/problem
def maximumToys(prices, k):
  purchases = 0
  cur_tot = 0
  prices.sort()
  for price in prices:
    if price + cur_tot <= k:
      purchases += 1
      cur_tot += price
  return purchases
  