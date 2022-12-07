input = open("day6/input.txt").read()                       # read input
for size in [4,14]:                                         # window size: 4 (part1) and 14 (part2)
  for i in range(0, len(input)-size):                       # move window of <size> over string
    window = input[i:i+size]                                # get characters in window
    c = [window.count(window[j]) for j in range(0,size)]    # count all occurances of all characters in window
    if( c.count(1) == size ):                               # when the list contains all 1's the characters are unique
      print(i+size)
      break
