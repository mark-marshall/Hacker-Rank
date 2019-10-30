# https://www.hackerrank.com/challenges/count-triplets-1/problem
def countTriplets(arr, r):
  # initialize sets, tails, and count
  sets = {}
  tails = {}
  count = 0
  # loop over the enumerated arr in reverse order
  for idx,num in enumerate(list(reversed(arr))):
    # check whether next-gen is in sets
    if num * r in sets:
      # check whether next-gen is in tails
      if num * r in tails:
        # increment count when full triplet is found
        count += tails[num*r]
      # populate tails
      if num in tails:
        tails[num] += len(sets[num*r])
      else:
        tails[num] = len(sets[num*r])
    # populate sets
    if num in sets:
      sets[num].append(idx)
    else:
      sets[num] = [idx]
  # return count
  return count
