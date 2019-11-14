# https://www.hackerrank.com/challenges/insertionsort2/problem
def insertionSort2(n, arr):
  for i in range (1,n):
    idx = i
    while not (idx == 0):
      if arr[idx] < arr[idx-1]:
        arr[idx],arr[idx-1] = arr[idx-1],arr[idx]
        idx -= 1
      else:
        break
    print(*arr)
