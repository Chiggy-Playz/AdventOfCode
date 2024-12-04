from utils.input_manager import get_input
import re
import math

input = get_input(__file__)

instructions, *raw_points = input

points: dict[str, list[str]] = {}
for raw_point in raw_points[1:]:
    match = re.findall(r"([0-9A-Z]+)", raw_point)
    assert match
    points[match[0]] = [match[1], match[2]]


def part1():
    count = 0
    i = 0
    current_point = "AAA"

    while current_point != "ZZZ":
        instruction = instructions[i]
        next_point = points[current_point]
        if instruction == "L":
            current_point = next_point[0]
        else:
            current_point = next_point[1]
        count += 1
        i += 1
        if len(instructions) == i:
            i = 0

    return count


def part2():
    current_points = [point for point in points.keys() if point.endswith("A")]
    a = []
    for point in current_points:
        count = 0
        i = 0

        while not point.endswith("Z"):
            instruction = instructions[i]
            next_point = points[point]
            point = next_point[0 if instruction == "L" else 1]
            count += 1
            i += 1
            if len(instructions) == i:
                i = 0
        a.append(count)

    return math.lcm(*a)


print(part1())
print(part2())
