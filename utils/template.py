from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def part1(lines: InputType):
    pass


def part2(lines: InputType):
    pass


def main(lines: InputType):
    with timeit("Part 1"):
        p1 = part1(lines)
    print(p1)
    with timeit("Part 2"):
        p2 = part2(lines)
    print(p2)


if __name__ == "__main__":
    lines = get_input(testing=True)
    main(lines)
    benchmark(main, lines)
