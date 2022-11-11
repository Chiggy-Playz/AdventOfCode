# https://adventofcode.com/2015/day/3

with open("Inputs/day3.txt") as f:
    instructions = f.read()

current_position = [0, 0]
delivered_points = {tuple(current_position)}

for char in instructions:
    if char == "^":
        current_position[1] += 1
    elif char == "v":
        current_position[1] -= 1
    elif char == ">":
        current_position[0] += 1
    else: # <
        current_position[0] -= 1
    
    delivered_points.add(tuple(current_position))

print(len(delivered_points))

# Part 2

santas_current_position = [0, 0]
robo_santas_current_position = [0, 0]
delivered_points = {tuple(santas_current_position)}

for index, char in enumerate(instructions):
    
    position = santas_current_position if index % 2 == 0 else robo_santas_current_position

    if char == "^":
        position[1] += 1
    elif char == "v":
        position[1] -= 1
    elif char == ">":
        position[0] += 1
    else: # <
        position[0] -= 1
    
    delivered_points.add(tuple(position))

print(len(delivered_points))