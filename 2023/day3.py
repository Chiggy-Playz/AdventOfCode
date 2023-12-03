from input_manager import get_input
import re
from collections import defaultdict

input = get_input(__file__)

gear_count = defaultdict(list)


def check_adjacent(row: int, column_start: int, column_end: int) -> bool:
    check_top = row != 0
    check_botttom = row != (len(input) - 1)
    check_left = column_start != 0
    check_right = column_end != (len(input[0]))

    left_value = column_start - int(check_left)
    right_value = column_end + int(check_right)
    top_value = row - int(check_top)
    bottom_value = row + int(check_botttom) + 1

    for x in range(left_value, right_value):
        for y in range(top_value, bottom_value):
            if input[y][x].isdigit():
                continue

            if input[y][x] == ".":
                continue

            if input[y][x] == "*":
                gear_count[(y, x)].append(int(input[row][column_start:column_end]))

            return True
    return False


def solution():
    part1_sum = 0
    part2_sum = 0
    for i, line in enumerate(input):
        for match in re.finditer(r"(\d+)", line):
            col_start, col_end = match.span()
            if check_adjacent(i, col_start, col_end):
                part1_sum += int(match.groups()[0])

    for pos, ratios in gear_count.items():
        if len(ratios) <= 1:
            continue

        product = 1
        for ratio in ratios:
            product *= ratio
        part2_sum += product

    return part1_sum, part2_sum


print(solution())
