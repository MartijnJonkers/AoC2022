import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

elves = sorted([sum(map(int,x.split("\n"))) for x in aoc.load("input.txt", "r").read().strip().split("\n\n")], reverse=True)
aoc.result(elves[0], sum(elves[0:3]))