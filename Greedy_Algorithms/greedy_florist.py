# https://www.hackerrank.com/challenges/greedy-florist/problem
  c.sort(reverse=True)
  cost = 0
  purchases = {}
  purchasees = 0
  for price in c:
    if purchasees < k:
      purchases[purchasees] = 1
      purchasees += 1
      cost += price
    elif purchasees >= k:
      buyer = min(purchases, key=purchases.get)
      purchases[buyer] += 1
      cost += (purchases[buyer] * price)
  return cost
