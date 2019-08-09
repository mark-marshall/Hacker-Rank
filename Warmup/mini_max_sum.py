# https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    ascending = sorted(arr)
    decending = sorted(arr, reverse=True)
    min = 0
    max = 0
    for idx in range (4):
        min += ascending[idx]
        max += decending[idx]
    print(f"{min} {max}")
    