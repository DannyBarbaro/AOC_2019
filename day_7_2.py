datastream = []
def get_value(val, mode, data):
  return data[val] if mode == 0 else val

def oppcode_1(val_1, mode_1, val_2, mode_2, result, data):
  data[result] = get_value(val_1, mode_1, data) + get_value(val_2, mode_2, data)
  return data

def oppcode_2(val_1, mode_1, val_2, mode_2, result, data):
  data[result] = get_value(val_1, mode_1, data) * get_value(val_2, mode_2, data)
  return data

def oppcode_3(val, data):
  data[val] = datastream.pop(0)
  return data

def oppcode_4(val, mode, data):
  return get_value(val, mode, data)

def oppcode_5(val_1, mode_1, data):
  return True if get_value(val_1, mode_1, data) != 0 else False

def oppcode_6(val_1, mode_1, data):
  return True if get_value(val_1, mode_1, data) == 0 else False

def oppcode_7(val_1, mode_1, val_2, mode_2, val_3, data):
  num = 1 if get_value(val_1, mode_1, data) < get_value(val_2, mode_2, data) else 0
  data[val_3] = num
  return data

def oppcode_8(val_1, mode_1, val_2, mode_2, val_3, data):
  num = 1 if get_value(val_1, mode_1, data) == get_value(val_2, mode_2, data) else 0
  data[val_3] = num
  return data

def run_intcode(ints, index):
  while True:
    code = ints[index]
    op = code % 100
    mode_1 = code % 1000 - code % 100
    mode_2 = code % 10000 - code % 1000
    mode_3 = code % 100000 - code % 10000
    if op == 1:
      ints = oppcode_1(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], ints)
      index += 4
    elif op == 2:
      ints = oppcode_2(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], ints)
      index += 4
    elif op == 3:
      ints = oppcode_3(ints[index+1], ints)
      index += 2
    elif op == 4:
      return [oppcode_4(ints[index+1], mode_1, ints), ints, index+2]
    elif op == 5:
      if oppcode_5(ints[index+1], mode_1, ints):
        index = get_value(ints[index+2], mode_2, ints)
      else:
        index += 3
    elif op == 6:
      if oppcode_6(ints[index+1], mode_1, ints):
        index = get_value(ints[index+2], mode_2, ints)
      else:
        index += 3
    elif op == 7:
      ints = oppcode_7(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], ints)
      index += 4
    elif op == 8:
      ints = oppcode_8(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], ints)
      index += 4
    elif op == 99:
      return

def new_state():
  ints = []
  with open('inputs/input7.txt') as f:
    return [int(numeric_string) for numeric_string in f.readline().split(',')]

def calc_for_perm(combo):
  datastream.clear()
  states = [[],[],[],[],[]]
  for i in range(len(states)):
    states[i] = new_state()
  pointers = [0,0,0,0,0]
  val = 0
  isFirst = True
  running = True
  while running:
    for i in range(len(combo)):
      if isFirst:
        datastream.append(combo[i])
      datastream.append(val)
      output = run_intcode(states[i], pointers[i])
      if output == None:
        running = False
      else:
        val = output[0]
        states[i] = output[1]
        pointers[i] = output[2]
    isFirst = False
  return val

# Part 2
import itertools
import time
perms = list(itertools.permutations([5,6,7,8,9]))
maximum = 0
best = []
for combo in perms:
  combo = list(combo)
  val = calc_for_perm(combo)
  if val > maximum:
    maximum = val
    best = combo


print(maximum)
print(combo)
# expected = 139629729