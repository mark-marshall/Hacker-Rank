# https://www.hackerrank.com/challenges/cavity-map/problem
def cavityMap(grid):
  new_grid = []
  i = 0
  j = 0
  while ((i <= len(grid) -1) and (j <= len(grid) - 1)):
    # check whether we need to append a new array to the grid
    if (i == 0 and j == 0) or ((j == len(grid) -1) and (not i == len(grid) -1)):
      new_grid.append('')
    # check whether this is an outter edge el
    if (i == 0) or (i == len(grid) - 1) or (j == 0) or (j == len(grid) - 1):
      new_grid[i] += grid[i][j]
    # for central els check if its a cavity
    else:
      deepest_neighbour = max([grid[i-1][j],grid[i][j+1], grid[i+1][j],grid[i][j-1]])
      if grid[i][j] > deepest_neighbour:
        new_grid[i] += 'X'
      else:
        new_grid[i] += grid[i][j]
    # increment i and j as needed
    if j == len(grid) - 1:
      i += 1
      j = 0
    else:
      j += 1
  # return grid
  return new_grid
  