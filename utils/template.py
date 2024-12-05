from utils.input_manager import get_input
from utils.timing import timeit


def part1(lines: list[str]):
    pass


def part2(lines: list[str]):
    pass

def main():
    lines = get_input(testing=True)
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    main()