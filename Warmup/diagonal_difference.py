# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
  # diagonals = primary_diagonal, secondary_diagonal
  diagonals = ([], [])
  # next_idx = primary_diagonal, secondary_diagonal
  next_idx = (0, n - 1)
  for i in range(n):
    # primary diagonal
    diagonals[0].append(arr[i][next_idx[0]])
    next_idx = (next_idx[0] + 1, next_idx[1])
    # secondary diagonal
    diagonals[1].append(arr[i][next_idx[1]])
    next_idx = (next_idx[0], next_idx[1] - 1)
  return (abs(sum(diagonals[0]) - sum(diagonals[1])))
