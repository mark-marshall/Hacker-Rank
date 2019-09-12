# https://www.hackerrank.com/challenges/picking-numbers/problem
def pickingNumbers(a):
    hashy = {}
    cur_largest = 0
    # create the keys for the table
    for num in a:
        if not f"{num} -" in hashy:
        hashy[f"{num} -"] = []
        hashy[f"{num} +"] = []
    # populate the table
    for num in a:
        hashy[f"{num} -"].append(num)
        hashy[f"{num} +"].append(num)
        if (f"{num + 1} -") in hashy:
            hashy[f"{num + 1} -"].append(num)
        if (f"{num - 1} +") in hashy:
            hashy[f"{num - 1} +"].append(num)
    # find the largest superset
    for superset in hashy:
        size = len(hashy[superset])
        if size > cur_largest:
            cur_largest = size
    return cur_largest
