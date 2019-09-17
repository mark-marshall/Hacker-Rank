# https://www.hackerrank.com/challenges/minimum-distances/problem
def minimumDistances(a):
    # initialize shortest distance variable and negative return
    shortest_dist = -1
    tally = {}
    for idx,num in enumerate(a):
        if num not in tally:
            # populate tally key
            tally[num] = [idx]
        elif num in tally:
            # calculate distance to last instance of the element
            to_last = idx - tally[num][-1]
            # check whether this distance is the shortest
            if (shortest_dist == -1) or (to_last < shortest_dist):
                shortest_dist = to_last
            # append the index of the element to the end of the list
            tally[num].append(idx)
    return shortest_dist
