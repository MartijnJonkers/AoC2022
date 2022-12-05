import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

import re
input = aoc.loadlines("input.txt")                                # read lines
for part in range(-1,2,2):                                        # both parts (-1 and 1)
  # init crates
  crates = [[],[],[],[],[],[],[],[],[]]                           # init empty crate stacks
  for li in range(0, 8):                                          # iterate over all line indices (li) of start stacks
    for ci in range(1,35,4):                                      # get crate at character index (ci)
      if(len(input[li]) > ci) and (input[li][ci] != ' '):         # any crate present at index?
        crates[int(ci/4)].insert(0,input[li][ci])                 # place crate on bottom of stack

  # go over all moves
  for move in input[10:]:
    n,f,t = list(map(int,re.split('move | from | to ',move)[1:])) # parse line to 3 ints: num, from, to
    crates[t-1] += crates[f-1][-n:][::part]                       # part 1, move in reverse. part 2, move no reverse
    crates[f-1] = crates[f-1][:-n]                                # remove moved crates from old stack

  # create result string
  result = ""
  for i in range(0,9):                                            # combine top crates to a string
    result += str(crates[i][-1:][0])
  print("part", 1 if part < 0 else 2, "=",result)                 # print result