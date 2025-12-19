from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def part1(lines: InputType):
    instructions = [(s[0], int(s[1:])) for s in lines]
    result = 0
    current = 50
    for dirn, count in instructions:
        current = (current + (1 if dirn == "R" else -1) * count) % 100
        if current == 0:
            result += 1
    return result


def part2(lines: InputType):
    instructions = [(s[0], int(s[1:])) for s in lines]

    result = 0
    current = 50
    for dirn, count in instructions:
        if count >= 100:
            result += count // 100
            count = count % 100

        new = current + (1 if dirn == "R" else -1) * count
        if current != 0 and (new <= 0 or 100 <= new):
            result += 1

        current = new % 100

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
    """
    Part 1 took 853.60 µs
    1105
    Part 2 took 1.13 ms
    6599

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 1.66 ms
    """
