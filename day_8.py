# Part 1
# 25 pixels wide and 6 pixels tall = 150 pixels per layer
# data = []
# with open('inputs/input8.txt') as f:
#   data = f.readline()
# layer_count = 0
# min_zero = -1
# zero_count = 0
# one_count = 0
# two_count = 0
# output = 0
# for p in data:
#   pixel = int(p)
#   if layer_count == 150:
#     layer_count = 0
#     if zero_count < min_zero or min_zero == -1:
#       output = one_count * two_count
#       min_zero = zero_count
#     zero_count = 0
#     one_count = 0
#     two_count = 0
#   if pixel == 0:
#     zero_count += 1
#   elif pixel == 1:
#     one_count += 1
#   elif pixel == 2:
#     two_count += 1
#   layer_count+=1

# Part 2
data = []
with open('inputs/input8.txt') as f:
  data = f.readline()
layers = []
for _ in range(int(len(data)/150)):
  layers.append([None] * 150)

count = 0
layer_count = 0
for p in data:
  pixel = int(p)
  layers[layer_count][count] = pixel
  count += 1
  if count == 150:
    layer_count += 1
    count = 0

output = [None] * 150
for layer in layers:
  for i in range(len(layer)):
    if output[i] == None and layer[i] != 2:
      output[i] = layer[i]

print(output)