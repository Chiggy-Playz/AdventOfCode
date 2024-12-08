from typing import TypeAlias
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import Point
from utils.functools import ingrid, padd, pdiff, traverse_grid

InputType: TypeAlias = list[str]


def solver(lines: InputType):
    antennas: dict[str, list[Point]] = {}

    for x, y, val in traverse_grid(lines):
        if val not in ".#":
            antennas[val] = antennas.get(val, []) + [(x, y)]

    antinodes1 = set()
    antinodes2 = set()

    for _, positions in antennas.items():
        for first in positions:
            for second in positions:
                if first == second:
                    continue
                antinodes2.add(first)
                antinodes2.add(second)
                p1_solved = False
                difference = pdiff(first, second)
                nx, ny = padd(difference, second)

                while ingrid(len(lines), nx, ny):
                    if not p1_solved:
                        antinodes1.add((nx, ny))
                        p1_solved = True

                    antinodes2.add((nx, ny))
                    nx, ny = padd(difference, (nx, ny))

    return len(antinodes1), len(antinodes2)


def main(lines: InputType):
    with timeit("Both parts"):
        print(solver(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
    """
    (367, 1285)
    Both parts took 1.78 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 1.17 ms
    """
