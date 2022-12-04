import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

from parse import parse
input = [parse("{:d}-{:d},{:d}-{:d}", line.strip()) for line in aoc.load("input.txt").readlines()]
part1, part2 = 0,0
for v in input:
  part1 += 1 if ( ((v[0] <= v[2]) and (v[1] >= v[3])) or ((v[2] <= v[0]) and (v[3] >= v[1])) ) else 0
  part2 += 1 if ( ((v[1] >= v[2]) and (v[0] <= v[3])) ) else 0
aoc.result( part1, part2 )