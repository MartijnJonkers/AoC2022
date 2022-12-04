import os
import sys

def load(file="input.txt", rights="r"):
  return open(os.path.join(sys.path[0], file), rights)

def loadlines(file="input.txt", rights="r", strip = True):
  return [(line.strip() if strip else line) for line in load(file, rights).readlines()]

def result(p1 = "", p2 = ""):
  if( len(str(p1)) > 0 ):
    print("part 1 =", p1)
  if( len(str(p2)) > 0 ):
    print("part 2 =", p2)