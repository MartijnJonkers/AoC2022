import re
lines = open("input.txt").readlines()

score = 0
for line in lines:
  l = int(len(line)/2)
  match = ord(re.findall("[" + line[0:l] + "]", line[l:l+l])[0])
  score += (match - ord('a')) + 1 if (match >= ord('a')) else ((match - ord('A')) + 27)
print(score)

score = 0
for i in range(0,len(lines), 3):
  match1 = re.findall("[" + lines[i].strip() + "]", lines[i+1].strip() )
  match2 = ord(re.findall("[" + "".join(match1) + "]", lines[i+2].strip())[0])
  score += (match2 - ord('a')) + 1 if (match2 >= ord('a')) else ((match2 - ord('A')) + 27)
print(score)
