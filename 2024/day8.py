# from utils.types import InputType
from typing import TypeAlias, TypeVar

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import InputType, Point


def part1(lines: InputType):

    antennas: dict[str, list[Point]] = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] not in ".#":
                antennas[lines[y][x]] = antennas.get(lines[y][x], []) + [(x, y)]

    antinodes = set()

    for _, positions in antennas.items():
        for first in positions:
            for second in positions:
                if first == second:
                    continue

                difference = map(lambda x: x[1] - x[0], zip(first, second))
                nx, ny = map(sum, zip(difference, second))
                if not (0 <= nx < len(lines) and 0 <= ny < len(lines)):
                    continue

                antinodes.add((nx, ny))

    return len(antinodes)


def part2(lines: InputType):
    antennas: dict[str, list[Point]] = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] not in ".#":
                antennas[lines[y][x]] = antennas.get(lines[y][x], []) + [(x, y)]

    antinodes = set()

    for _, positions in antennas.items():
        for first in positions:
            for second in positions:
                if first == second:
                    continue
                antinodes.add(first)
                antinodes.add(second)

                difference = tuple(map(lambda x: x[1] - x[0], zip(first, second)))
                nx, ny = tuple(map(sum, zip(difference, second)))

                while (0 <= nx < len(lines) and 0 <= ny < len(lines)):
                    antinodes.add((nx, ny))
                    nx, ny = tuple(map(sum, zip(difference, (nx, ny))))

    return len(antinodes)


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
