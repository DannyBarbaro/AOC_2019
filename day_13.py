datastream_out = []
pixels = {}
ballX = 0
paddleX = 0
def print_board():
  global paddleX, ballX
  for y in range(20): #for y in range(yMax+1):
    s = ""
    for x in range(38): #for x in range(xMax+1):
      if (x,y) in pixels.keys():
        if pixels[(x,y)] == 0:
          s += " "
        elif pixels[(x,y)] == 1:
          s += "🟥"
        elif pixels[(x,y)] == 2:
          s += "◼️"
        elif pixels[(x,y)] == 3:
          s += "_"
          paddleX = x
        elif pixels[(x,y)] == 4:
          s += "🔵"
          ballX = x
    print(s)

def get_value(val, mode, data, relative):
  if mode == 0:
    return data[val] if val in data.keys() else 0
  elif mode == 1:
    return val
  elif mode == 2:
    return data[val+relative] if val+relative in data.keys() else 0

def oppcode_1(val_1, mode_1, val_2, mode_2, result, mode_3, data, relative):
  r = get_value(val_1, mode_1, data, relative) + get_value(val_2, mode_2, data, relative)
  if mode_3 == 0:
    data[result] = r
  else:
    data[result+relative] = r
  return data

def oppcode_2(val_1, mode_1, val_2, mode_2, result, mode_3, data, relative):
  r = get_value(val_1, mode_1, data, relative) * get_value(val_2, mode_2, data, relative)
  if mode_3 == 0:
    data[result] = r
  else:
    data[result+relative] = r
  return data

import sys
def oppcode_3(val, mode, data, relative):
  print_board()
  stick = 0
  if ballX < paddleX:
    stick = -1
  elif ballX > paddleX:
    stick = 1

  if mode == 0:
    data[val] = stick
  else:
    data[val+relative] = stick
  return data

def oppcode_4(val, mode, data, relative):
  datastream_out.append(get_value(val, mode, data, relative))
  if len(datastream_out) == 3:
    if datastream_out[0] == -1:
      print("Score: ", datastream_out[2])
    else:
      pixels[(datastream_out[0], datastream_out[1])] = datastream_out[2]
    datastream_out.clear()

def oppcode_5(val_1, mode_1, data, relative):
  return True if get_value(val_1, mode_1, data, relative) != 0 else False

def oppcode_6(val_1, mode_1, data, relative):
  return True if get_value(val_1, mode_1, data, relative) == 0 else False

def oppcode_7(val_1, mode_1, val_2, mode_2, val_3, mode_3, data, relative):
  num = 1 if get_value(val_1, mode_1, data, relative) < get_value(val_2, mode_2, data, relative) else 0
  if mode_3 == 0:
    data[val_3] = num
  else:
    data[val_3+relative] = num
  return data

def oppcode_8(val_1, mode_1, val_2, mode_2, val_3, mode_3, data, relative):
  num = 1 if get_value(val_1, mode_1, data, relative) == get_value(val_2, mode_2, data, relative) else 0
  if mode_3 == 0:
    data[val_3] = num
  else:
    data[val_3+relative] = num
  return data

def oppcode_9(val_1, mode_1, data, relative):
  return relative + get_value(val_1, mode_1, data, relative)

ints = {}
relative_base = 0
with open('inputs/input13.txt') as f:
  count = 0
  for numeric_string in f.readline().split(','):
    ints[count] = int(numeric_string)
    count += 1
index = 0
while ints[index] != 99:
  code = ints[index]
  op = code % 100
  mode_1 = int(str(code % 1000 - code % 100)[0])
  mode_2 = int(str(code % 10000 - code % 1000)[0])
  mode_3 = int(str(code % 100000 - code % 10000)[0])
  if op == 1:
    ints = oppcode_1(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], mode_3, ints, relative_base)
    index += 4
  elif op == 2:
    ints = oppcode_2(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], mode_3, ints, relative_base)
    index += 4
  elif op == 3:
    ints = oppcode_3(ints[index+1], mode_1, ints, relative_base)
    index += 2
  elif op == 4:
    oppcode_4(ints[index+1], mode_1, ints, relative_base)
    index += 2
  elif op == 5:
    if oppcode_5(ints[index+1], mode_1, ints, relative_base):
      index = get_value(ints[index+2], mode_2, ints, relative_base)
    else:
      index += 3
  elif op == 6:
    if oppcode_6(ints[index+1], mode_1, ints, relative_base):
      index = get_value(ints[index+2], mode_2, ints, relative_base)
    else:
      index += 3
  elif op == 7:
    ints = oppcode_7(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], mode_3, ints, relative_base)
    index += 4
  elif op == 8:
    ints = oppcode_8(ints[index+1], mode_1, ints[index+2], mode_2, ints[index+3], mode_3, ints, relative_base)
    index += 4
  elif op == 9:
    relative_base = oppcode_9(ints[index+1], mode_1, ints, relative_base)
    index += 2

# xMax = 0
# for pixel in pixels.keys():
#   xMax= max(pixel[0], xMax)
# yMax = 0
# for pixel in pixels.keys():
#   yMax = max(pixel[1], yMax)
