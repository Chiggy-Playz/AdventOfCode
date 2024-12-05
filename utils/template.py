from typing import TypeVar

from utils.input_manager import get_input
from utils.timing import timeit
from timeit import timeit as benchmark

InputType = TypeVar("InputType", str, list[str])


def part1(lines: InputType):
    pass


def part2(lines: InputType):
    pass


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=True)
    main(lines)

    # Benchmark:
    # print(benchmark(lambda: main(lines)))