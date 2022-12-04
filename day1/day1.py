elves = sorted([sum(map(int,x.split("\n"))) for x in open("input.txt", "r").read().strip().split("\n\n")], reverse=True)
print("part 1 = ", elves[0], "\npart 2 = ", sum(elves[0:3]))