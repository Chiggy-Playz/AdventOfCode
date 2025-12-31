from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def parser(lines: InputType):
    ranges = []
    available = []
    ranges_mode = True
    for line in lines:
        if line == "":
            ranges_mode = False
            continue
        if ranges_mode:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
        else:
            available.append(int(line))
    return ranges, available


def part1(lines: InputType):
    ranges, available = parser(lines)

    ranges.sort()

    merged = [ranges[0]]

    for current in ranges[1:]:
        last = merged[-1]

        if current[0] <= last[-1]:
            merged[-1] = (last[0], max(current[1], last[1]))
        else:
            merged.append(current)

    result = 0
    for available in available:
        for range_start, range_end in merged:
            if range_start <= available <= range_end:
                result += 1
                break
            if available < range_start:
                break

    return result


def part2(lines: InputType):
    ranges, _ = parser(lines)

    ranges.sort()

    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]

        if current[0] <= last[-1]:
            merged[-1] = (last[0], max(current[1], last[1]))
        else:
            merged.append(current)

    result = 0
    for current in merged:
        result += current[1] - current[0] + 1

    return result


def main(lines: InputType):
    with timeit("Part 1"):
        p1 = part1(lines)
    print(p1)
    with timeit("Part 2"):
        p2 = part2(lines)
    print(p2)


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
