# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
def sherlockAndAnagrams(s):
  sets = {}
  matched = 0
  # populate the dictionary
  for idx,char in enumerate(list(s)):
    # handle the char by itself
    if char not in sets:
      sets[char] = [idx]
    elif char in sets:
      # increment matched with number of matching pairs   
      matched += len(sets[char])
      sets[char].append(idx)
    # initalize cur_pos and cur_chain
    cur_pos = idx + 1
    cur_chain = char
    # handle char with all tails
    while cur_pos < len(s):
      cur_chain += list(s)[cur_pos]
      cur_sorted_chain = ''.join(sorted(cur_chain))
      if cur_sorted_chain not in sets:
        sets[cur_sorted_chain] = [idx]
      elif cur_sorted_chain in sets:
        # increment matched with number of matching pairs   
        matched += len(sets[cur_sorted_chain])
        sets[cur_sorted_chain].append(idx)
      cur_pos += 1  
  # return the number of matches
  return matched
