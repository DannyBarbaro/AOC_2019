def oppcode_1(position_1, position_2, position_result, data):
  data[position_result] = data[position_1] + data[position_2]
  return data

def oppcode_2(position_1, position_2, position_result, data):
  data[position_result] = data[position_1] * data[position_2]
  return data

# Part 1
ints = []
with open('inputs/input2.txt') as f:
  ints = [int(numeric_string) for numeric_string in f.readline().split(',')]
index = 0
while ints[index] != 99:
  if ints[index] == 1:
    ints = oppcode_1(ints[index+1], ints[index+2], ints[index+3], ints)
  elif ints[index] == 2:
    ints = oppcode_2(ints[index+1], ints[index+2], ints[index+3], ints)
  index += 4
print(ints[0])

# Part 2
for i in range(100):
  for j in range(100):
    ints = []
    with open('inputs/input2.txt') as f:
      ints = [int(numeric_string) for numeric_string in f.readline().split(',')]
    ints[1] = i
    ints[2] = j
    index = 0
    while ints[index] != 99:
      if ints[index] == 1:
        ints = oppcode_1(ints[index+1], ints[index+2], ints[index+3], ints)
      elif ints[index] == 2:
        ints = oppcode_2(ints[index+1], ints[index+2], ints[index+3], ints)
      index += 4
    if ints[0] == 19690720:
      print("Noun: ", i, " Verb: ", j)