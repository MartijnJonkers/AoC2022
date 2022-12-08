# original source: https://www.reddit.com/r/adventofcode/comments/zfpnka/comment/izg5emd/?utm_source=reddit&utm_medium=web2x&context=3
p1 = p2 = 0
trees = [list(map(int, chars)) for chars in [list(line.strip()) for line in open("day8/input.txt").readlines()]]    # parse grid
for i, row in enumerate(trees):
  for j, height in enumerate(row):
    score = 1
    isVisible = False
    treelines = [
      row[:j][::-1],
      row[j + 1 :],
      [r[j] for r in trees[:i]][::-1],
      [r[j] for r in trees[i + 1 :]],
    ]

    for treeline in treelines:
      for dist, h in enumerate(treeline, 1):
        if h >= height:
          score *= dist
          break
      else:
        isVisible = True
        score *= max(1, len(treeline))

    p1 += int(isVisible)
    p2 = max(p2, score)

print(f"p1: {p1}, p2: {p2}")


#part2 only, original: https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day08p2.py
grid = [list(map(int, line)) for line in open("day8/input.txt").read().splitlines()]
t = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        L = R = U = D = 0
        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1, len(grid)):
            D += 1
            if grid[x][c] >= k:
                break
        t = max(t, U * D * L * R)
print(t)