# Part 1
def generate_points(path):
  cursor = [0,0]
  points = set({})
  for seg in path:
    if seg[0] == 'R':
      for _ in range(int(seg[1:])):
        cursor[0] += 1
        points.add(tuple(cursor))
    elif seg[0] == 'L':
      for _ in range(int(seg[1:])):
        cursor[0] -= 1
        points.add(tuple(cursor))
    elif seg[0] == 'U':
      for _ in range(int(seg[1:])):
        cursor[1] += 1
        points.add(tuple(cursor))
    elif seg[0] == 'D':
      for _ in range(int(seg[1:])):
        cursor[1] -= 1
        points.add(tuple(cursor))
  return points

wire1 = set({})
wire2 = set({})
with open('inputs/input3.txt') as f:
  wire1 = generate_points(f.readline().split(','))
  wire2 = generate_points(f.readline().split(','))
intersect = wire1.intersection(wire2)

minimum = -1
for coord in intersect:
  val = abs(coord[0]) + abs(coord[1])
  if val < minimum or minimum == -1:
    minimum = val
print(minimum)

# Part 2
def generate_mapping(path):
  cursor = [0,0]
  counter = 0
  points = {}
  for seg in path:
    if seg[0] == 'R':
      for _ in range(int(seg[1:])):
        cursor[0] += 1
        counter += 1
        if tuple(cursor) not in points:
          points[tuple(cursor)] = counter
    elif seg[0] == 'L':
      for _ in range(int(seg[1:])):
        cursor[0] -= 1
        counter += 1
        if tuple(cursor) not in points:
          points[tuple(cursor)] = counter
    elif seg[0] == 'U':
      for _ in range(int(seg[1:])):
        cursor[1] += 1
        counter += 1
        if tuple(cursor) not in points:
          points[tuple(cursor)] = counter
    elif seg[0] == 'D':
      for _ in range(int(seg[1:])):
        cursor[1] -= 1
        counter += 1
        if tuple(cursor) not in points:
          points[tuple(cursor)] = counter
  return points

wire1 = {}
wire2 = {}
with open('inputs/input3.txt') as f:
  wire1 = generate_mapping(f.readline().split(','))
  wire2 = generate_mapping(f.readline().split(','))

intersect = set(wire1.keys()).intersection(set(wire2.keys()))

minimum = -1
for coord in intersect:
  val = wire1[coord] + wire2[coord]
  if val < minimum or minimum == -1:
    minimum = val
print(minimum)