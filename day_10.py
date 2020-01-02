# Part 1
def build_grid():
  grid = []
  for line in open('inputs/input10.txt'):
    row = []
    for c in line.rstrip('\n'):
      row.append(c)
    grid.append(row)
  return grid

def run_for_astroids(grid):
  max_visible = 0
  pair = ()
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == '#':
        count = count_visible(i, j, grid)
        print("X:", j, "Y:", i, "X:", count)
        if count > max_visible:
          max_visible = count
          pair = (j, i)
  return max_visible, pair

def count_visible(i, j, grid):
  count = 0
  count += check_column(i, j, grid)
  count += check_left(i, j, grid)
  count += check_right(i, j, grid)
  return count

def check_column(y, x, grid):
  top_flag = 0
  bottom_flag = 0
  for row in range(len(grid)):
    if row < y and grid[row][x] == '#':
      top_flag = 1
    elif row > y and grid[row][x] == '#':
      bottom_flag = 1
  return top_flag + bottom_flag

def check_left(y, x, grid):
  column = x-1
  astroids = []
  while column >= 0:
    new_astroids = []
    for row in range(len(grid)):
      if grid[row][column] == '#' and draw_line(x, y, column, row, astroids):
        new_astroids.append((column, row))
    astroids += new_astroids
    column -= 1
  return len(astroids)

def check_right(y, x, grid):
  column = x+1
  astroids = []
  while column < len(grid[0]):
    new_astroids = []
    for row in range(len(grid)):
      if grid[row][column] == '#' and draw_line(x, y, column, row, astroids):
        new_astroids.append((column, row))
    astroids += new_astroids
    column += 1
  return len(astroids)

def draw_line(x1, y1, x2, y2, current_astroids):
  m = (y2 - y1) / (x2 - x1)
  b = (-m*x1) + y1
  for roid in current_astroids:
    y = m*roid[0] + b
    if roid[1] == y:
      return False
  return True
# all in first row to some extra list
# for every astroid that is visible list check if it blocks the current one
# if it is visible add it to my sub list
# at the end of the iteration, add the sublist to the main visible list

print(run_for_astroids(build_grid()))

#329
