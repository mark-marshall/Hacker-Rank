# https://www.hackerrank.com/challenges/between-two-sets/problem
def getTotalX(a, b):
  count = 0
  rules = {}
  for a_num in a:
    if a_num not in rules:
      rules[a_num] = 'a'
  for b_num in b:
    if b_num not in rules:
      rules[b_num] = 'b'
  for i in range(1,max(a+b)+1):
    rules_met = True
    for rule in rules:
      if rules[rule] == 'a':
        if i % rule == 0:
          continue
        else:
          rules_met = False
          break
      elif rules[rule] == 'b':
        if rule % i == 0:
          continue
        else:
          rules_met = False
          break
    if rules_met == False:
      rules_met = True
    else:
      count += 1
  return count
