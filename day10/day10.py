input  = open("day10/input.txt").readlines()

cycles = []
addx = []
signal = {}
X = 1
for l in range(0,len(input)):
  input[l] = input[l].strip().split()                 # split input

  cycles.append( 2 if input[l][0] == "addx" else 1 )  # convert instruction to cycles
  if(len(input[l]) > 1):
    addx.append(int(input[l][1]))                       # addx: add x
  else:
    addx.append(0)                                      # noop: add 0

  cycle = sum(cycles[:l+1])                           # compute cycle after instruction
  for i in range(len(signal)+1, cycle+1):               # compute signal for each cycle in instruction
    signal[i] = [X,i * X]

  X = sum(addx[:l+1]) + 1                             # X gets updated after the instruction

# part 1: compute sum of 20,60,100,140,140,220 signal cycle
sum = 0
for s in range(20,221,40):
  sum += signal[s][1]
print(sum)

# part 2: sprite position and pixel draw cycle
result = [['   ' for i in range(0,40)] for i in range(0,6)]
for i in range(1, len(signal)+1):
  if ((i-1)%40) in range(signal[i][0]-1, signal[i][0]+2):
    result[int((i-1) / 40)][(i-1) % 40] = '###'
for row in result:
  print("".join(row))