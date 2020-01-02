# Part 1
data = [int(line.rstrip('\n')) for line in open('inputs/input1.txt')]
fuel = 0
for mass in data:
  fuel += int(mass/3.0)-2
print(fuel)

# Part 2
data = [int(line.rstrip('\n')) for line in open('inputs/input1.txt')]
fuel = 0
for mass in data:
  current_fuel = int(mass/3.0)-2
  fuel += current_fuel
  while current_fuel > 0:
    current_fuel = int(current_fuel/3.0)-2
    if current_fuel > 0:
      fuel += current_fuel
print(fuel)
