input = open("day8/input.txt").readlines()
grid = [list(map(int, chars)) for chars in [list(line.strip()) for line in input]]    # parse grid

# part 1, can be seen from outside of grid?
result = [[0 for c in list(line.strip())] for line in input]      # build empty result grid
for y in range( 0, len(grid)):                                    # go over each row
  for dir in [range(0, len(grid[0])), range(len(grid[0])-1,-1,-1)]: # (left to right) and (right to left)
    highest = -1
    for x in dir:                                                     # go over each column in row
      if highest < grid[y][x]:                                          # compare highest tree up to that point with selected tree
        highest = grid[y][x]
        result[y][x] = 1                                                  # tree is visible from outside of grid
for x in range(0, len(grid[0])):                                  # go over each column
  for dir in [range( 0, len(grid)), range(len(grid)-1,-1,-1)]:      # (top to bottom) and (bottom to top)
    highest = -1
    for y in dir:                                                     # go over each row in column
      if highest < grid[y][x]:                                          # compare highest tree up to that point with selected tree
        highest = grid[y][x]
        result[y][x] = 1                                                  # tree is visible from outside of grid
print(sum(sum(result,[])))                                        # add up all 1's in result grid

# part2, how far can we look from a tree?
max_score = 0
for y in range( 0, len(grid)):                                    # go over rows
  for x in range( 0, len(grid[0])):                                 # go over columns
    score = [-1,-1,-1,-1]                                             # up, left, down, right
    for dir in [1,-1]:                                                # forward and backward
      r = 1                                                             # reset range
      while score[2 + dir] == -1:                                       # right (dir=1) and left (dir=-1)
        if x+(r*dir) < 0 or x+(r*dir) >= len(grid[0]):
          score[2 + dir] = r - 1                                          # end of grid
        elif grid[y][x+(r*dir)] >= grid[y][x]:
          score[2 + dir] = r                                              # taller tree
        r += 1
      r = 1                                                             # reset range
      while score[1 + dir] == -1:                                       # down (dir=1) and up (dir=-1)
        if y+(r*dir) < 0 or y+(r*dir) >= len(grid):
          score[1 + dir] = r - 1                                          # end of grid
        elif grid[y+(r*dir)][x] >= grid[y][x]:
          score[1 + dir] = r                                              # taller tree
        r += 1        
    max_score = max(max_score, score[0]*score[1]*score[2]*score[3])     # determine max scenic score
print(max_score)                                                    # max contains highest scenic score