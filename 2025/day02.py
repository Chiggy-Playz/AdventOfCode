from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = str


def part1(lines: InputType):
    ranges = list(map(lambda s: tuple(map(int, s.split("-"))), lines.split(",")))
    invalid = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)
            if len(s) % 2:
                continue

            if s[: len(s) // 2] == s[len(s) // 2 :]:
                invalid += num

    return invalid


def part2(lines: InputType):
    ranges = list(map(lambda s: tuple(map(int, s.split("-"))), lines.split(",")))
    invalid = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)
            left = 1
            while left <= len(s) // 2:
                for i in range(2, (len(s) // left) + 1):
                    if s[:left] != s[(i - 1) * left : i * left]:
                        break
                else:
                    if not len(s) % left:
                        invalid += num
                        left += 1
                        break
                left += 1

    return invalid


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False, lines=False)
    main(lines)
    benchmark(main, lines)
