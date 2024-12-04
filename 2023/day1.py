from common.input_manager import get_input

input = get_input(__file__)


def part1():
    nums = []
    for line in input:
        num = 0
        for char in line:
            if char.isdigit():
                num += 10 * int(char)
                break

        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char.isdigit():
                num += int(char)
                break

        nums.append(num)
    return sum(nums)


def part2():
    num_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    nums = []
    for line in input:
        num = 0
        for i in range(0, len(line)):
            char = line[i]
            if char.isdigit():
                num += 10 * int(char)
                break

            for key, value in num_map.items():
                if line[i:].startswith(key):
                    num += 10 * value
                    break
            else:
                continue
            break

        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char.isdigit():
                num += int(char)
                break
            for key, value in num_map.items():
                if line[:i+1].endswith(key):
                    num += value
                    break
            else:
                continue
            break

        nums.append(num)
    return sum(nums)


print(part1())
print(part2())
