# https://adventofcode.com/2015/day/6

with open("Inputs/day6.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

# (y, x)
lights = [[False for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    instruction_start, end = instruction.split(" through ")
    end = tuple(map(lambda x: int(x), end.split(",")))
    instruction, start = instruction_start.rsplit(" ", 1)
    start = tuple(map(lambda x: int(x), start.split(",")))

    for y in range(start[1], end[1]+1):
        for x in range(start[0], end[0] + 1):
            if instruction == "toggle":
                lights[y][x] = not lights[y][x]
            elif instruction == "turn on":
                lights[y][x] = True
            else: # Turn off
                lights[y][x] = False

lights_on = 0
for y in lights:
    lights_on += sum(y)

print(lights_on)

# part 2

lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    instruction_start, end = instruction.split(" through ")
    end = tuple(map(lambda x: int(x), end.split(",")))
    instruction, start = instruction_start.rsplit(" ", 1)
    start = tuple(map(lambda x: int(x), start.split(",")))

    for y in range(start[1], end[1]+1):
        for x in range(start[0], end[0] + 1):
            if instruction == "toggle":
                lights[y][x] += 2
            elif instruction == "turn on":
                lights[y][x] += 1
            else: # Turn off
                if lights[y][x]:
                    lights[y][x] -= 1

brightness = 0
for y in lights:
    brightness += sum(y)

print(brightness)