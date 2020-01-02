# Part 1
# count = 0
# for num in range(359282, 820401):
#   num_str = str(num)
#   previous = -1
#   double_flag = False
#   increasing_flag = True
#   for i in range(len(num_str)):
#     digit = int(num_str[i])
#     if digit == previous:
#       double_flag = True
#     if digit < previous:
#       increasing_flag = False
#     previous = digit
#   if double_flag and increasing_flag:
#     count += 1
# print(count)

# Part 2
count = 0
for num in range(359282, 820401):
  num_str = str(num)
  previous = -1
  streak = 1
  contains_double = False
  is_increasing = True
  for i in range(len(num_str)):
    digit = int(num_str[i])
    if digit == previous:
      streak += 1
    else:
      if streak == 2:
        contains_double = True
      streak = 1
    if digit < previous:
      is_increasing = False
      break
    previous = digit
  if streak == 2:
    contains_double = True
  if contains_double and is_increasing:
    count += 1
print(count)