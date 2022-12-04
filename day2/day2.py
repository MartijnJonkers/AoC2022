input = open("input.txt").read().strip()

for i in range(2):                              # part 1 and 2
  score = 0
  for them, me in [line.split(' ') for line in input.split('\n')]:
    them  = (ord(them) - ord('A')) % 3          # convert ABC to 012 ints
    if(i == 0):
      me = (ord(me) - ord('X')) % 3             # Part 1 : convert XYZ to 012 ints
    else:
      me = (them + (ord(me) - ord('Y'))) % 3    # Part 2 : convert XYZ to 012, offset from 'them'
    score += me + 1                             # compute score based on played hand
    score += 3 if ( them == me ) else 6 if ( ((me - 1) % 3) == them ) else 0  # 0 loss, 3 draw, 6 win
  print("part", i+1, "=", score)
