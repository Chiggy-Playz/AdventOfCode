from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import InputType


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
    benchmark(main, lines)
