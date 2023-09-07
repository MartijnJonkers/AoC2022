import math
for part in [1,2]:
  input  = [monkey.split("\n") for monkey in open("day11/input.txt").read().split("\n\n")]
  monkeys = [ {                                                                         
    "items": list(map(int, input[m][1].replace(",", "").split()[2:])),                  # line 1: get initial worry levels
    "oper" : input[m][2].replace("old", "{old}")[19:],                                  # line 2: operation
    "test" : int(input[m][3][21:]),                                                     # line 3: modulo test number
    "result" : [
      int(input[m][5][30:]),                                                            # line 5: where to go when false
      int(input[m][4][29:]),                                                            # line 4: where to go when true
    ]
  } for m in range(0, len(input)) ]
  inspections = [0 for i in range(0, len(monkeys))]                                     # prepare inspections counter

  LCM = math.lcm(*[m["test"] for m in monkeys])                                         # find Least Common Multiple (LCM)

  for round in range(0,20 if part == 1 else 10000):                                     # rounds
    for m in range(0, len(monkeys)):                                                    # monkey index
      for i in range(0, len(monkeys[m]["items"])):                                      # item index
        inspections[m] += 1                                                             # count inspections
        new = eval(monkeys[m]["oper"].format(old = monkeys[m]["items"][i]))             # perform operation
        if part == 1: new = int(new/3)                                                  # part 1: divide by 3
        if part == 2: new %= LCM                                                        # part 2: mod of LCM
        nm = monkeys[m]["result"][ (new % monkeys[m]["test"]) == 0 ]                    # determine next monkey
        monkeys[nm]["items"].append(new)                                                # move item
      monkeys[m]["items"] = []                                                          # all items handled

  inspections.sort(reverse=True)
  print( inspections[0] * inspections[1] )
