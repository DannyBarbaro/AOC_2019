# Part 1
orbits = {}
for line in open('inputs/input6.txt'):
  planets = line.rstrip('\n').split(')')
  if planets[0] in orbits.keys():
    orbits[planets[0]].add(planets[1])
  else:
    orbits[planets[0]] = set({planets[1]})

queue = [('COM',0)]
touched = set({})
checksum = 0
while len(queue) != 0:
  cursor = queue.pop(0)
  touched.add(cursor[0])
  checksum += cursor[1]
  if cursor[0] in orbits.keys():
    for planet in orbits[cursor[0]]:
      queue.append((planet, cursor[1]+1))

print(checksum)

# Part2
def path_to_com(loc, tree):
  path = []
  cursor = loc
  while True:
    if cursor == 'COM':
      return path
    path.append(cursor)
    cursor = tree[cursor]

parent_tree = {}
for line in open('inputs/input6.txt'):
  planets = line.rstrip('\n').split(')')
  if planets[1] in parent_tree.keys():
    parent_tree[planets[1]].add(planets[0])
  else:
    parent_tree[planets[1]] = planets[0]

me_path = path_to_com('YOU', parent_tree)
me_path.reverse()
santa_path = path_to_com('SAN', parent_tree)
santa_path.reverse()
count = 0
while me_path[count] == santa_path[count]:
  count += 1

print(len(me_path) - count + len(santa_path) - count - 2)
