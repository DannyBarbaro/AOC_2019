#positions = [[-6, 2, -9], [12, -14, -4], [9, 5, -6], [-1, -4, 9]]
positions = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
step = 0
states = set({})
res = ''.join([''.join(str(i)) for i in positions]) 
res += ''.join([''.join(str(i)) for i in velocities]) 
states.add(res)

def calc_vel(iterate, moon, xyz_val):
  if positions[iterate][xyz_val] > positions[moon][xyz_val]:
    velocities[moon][xyz_val] += 1
  elif positions[iterate][xyz_val] < positions[moon][xyz_val]:
    velocities[moon][xyz_val] -= 1

while True:
  for moon in range(len(positions)):
    for iterate in range(len(positions)):
      if moon != iterate:
        for xyz in range(3):
          calc_vel(iterate, moon, xyz)
  for moon in range(len(velocities)):
    positions[moon][0] += velocities[moon][0]
    positions[moon][1] += velocities[moon][1]
    positions[moon][2] += velocities[moon][2]
  
  step += 1
  if step == 1000000: #4600000000
    print(step)
  res = ''.join([''.join(str(i)) for i in positions])
  res += ''.join([''.join(str(i)) for i in velocities])
  if res in states:
    print(step)
    break
  else:
    states.add(res)
  

# energy = 0
# for moon in range(len(positions)):
#   pot = abs(positions[moon][0]) + abs(positions[moon][1]) + abs(positions[moon][2])
#   ken = abs(velocities[moon][0]) + abs(velocities[moon][1]) + abs(velocities[moon][2]) 
#   energy += pot * ken

# print(energy)