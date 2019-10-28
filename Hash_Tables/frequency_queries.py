# https://www.hackerrank.com/challenges/frequency-queries/problem
def freqQuery(queries):
  data = {}
  freqs = {}
  ans = []
  for query in queries:
    # first query type appends new numbers
    # populate the data table
    if query[0] == 1:
      if query[1] in data:
        data[query[1]] += 1
      else:
        data[query[1]] = 1
      # populate the frequency table   
      if data[query[1]]-1 > 0 and data[query[1]]-1 in freqs:
        freqs[data[query[1]]-1].remove(query[1])
      if data[query[1]] in freqs:
        freqs[data[query[1]]].append(query[1])
      else:
        freqs[data[query[1]]] = [query[1]]
    # second query type removes a number if it exists
    elif query[0] == 2:
      # populate the data table   
      if query[1] in data and data[query[1]] > 0: 
        data[query[1]] -= 1
        # populate the frequency table
        freqs[data[query[1]]+1].remove(query[1])
        if data[query[1]] in freqs:
          freqs[data[query[1]]].append(query[1])
        else:
          freqs[data[query[1]]] = [query[1]]
    # third query type checks whether a frequency exists
    elif query[0] == 3:
      # lookup the value in the frequency table    
      if query[1] in freqs and len(freqs[query[1]]) > 0:
        ans.append(1)
      else:
        ans.append(0)
  return ans
