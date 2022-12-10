input  = [line.strip().split() for line in open("day9/input.txt").readlines()]
X = 0 # for readability
Y = 1 # for readability
for num in [2,10]:                                                          # numer of knots. 2(part1) and 10(part2)
  knots = [[0,0] for n in range(0,num)]                                      # list of knot locations (0=head)
  result = {f"{knots[-1][X]},{knots[-1][Y]}":1}                              # create result dictionary
  for action, steps in input:                                                  # go over input
    for step in range(1, int(steps) + 1):                                        # move 1 step until numnber of steps
      if action == 'R': knots[0][X] += 1                                           # move head 1 right
      if action == 'L': knots[0][X] -= 1                                           # move head 1 left
      if action == 'D': knots[0][Y] += 1                                           # move head 1 down
      if action == 'U': knots[0][Y] -= 1                                           # move head 1 up
      for i in range(1, len(knots)):                                             # move remaining knots
        if not( ( knots[i-1][X] in range(knots[i][X]-1, knots[i][X]+2) ) and       # is knot in range of knot 1 ahead?
                ( knots[i-1][Y] in range(knots[i][Y]-1, knots[i][Y]+2) ) ):
          knots[i][Y] += max(min(knots[i-1][Y] - knots[i][Y], 1), -1)                # not in range, move knot
          knots[i][X] += max(min(knots[i-1][X] - knots[i][X], 1), -1)
      result[f"{knots[-1][X]},{knots[-1][Y]}"] = 1                               # add currunt location to list (or ovewrite when already present)
  print(len(result))                                                         # print the number locations visited
