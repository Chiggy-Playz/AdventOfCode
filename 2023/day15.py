from common.input_manager import get_input
from collections import defaultdict

input = get_input(__file__, lines=False).strip()

def hash(string):
    temp = 0
    for char in string:
        temp += ord(char)
        temp *= 17
        temp %= 256
    return temp

def part1():
    s = 0
    for string in input.split(","):
        s += hash(string)
    return s

def part2():
    boxes: dict[int, list] = defaultdict(list)

    for instruction in input.split(","):
        if "=" in instruction:
            label, new_power = instruction.split("=")
            box_number = hash(label)
            # Check if in box
            for lens in boxes[box_number]:
                if lens[0] == label:
                    lens[1] = new_power
                    break
            else:
                boxes[box_number].append([label, new_power])
        else:
            label = instruction.split("-")[0]
            box_number = hash(label)

            # Check if in box
            for index, lens in enumerate(boxes[box_number]):
                if lens[0] == label:
                    boxes[box_number].pop(index)
                    break
    
    s = 0
    for box_number, box in boxes.items():
        
        # Multiply box number
        for idx, lens in enumerate(box):
            temp = (box_number+1)
            temp *= (idx+1)
            temp *= int(lens[1])
            s += temp

    return s

print(part1())
print(part2())
