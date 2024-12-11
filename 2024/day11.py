from functools import cache
import sys
from typing import TypeAlias

from utils.functools import ints
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]

sys.setrecursionlimit(10**4)


def solver(stones: list[int], blinks: int):
    @cache
    def blink(num: int, count: int):
        if not count:
            return 1

        if num == 0:
            return blink(1, count - 1)
        s = str(num)
        if len(s) % 2 == 0:
            return blink(int(s[: len(s) // 2]), count - 1) + blink(int(s[len(s) // 2 :]), count - 1)

        return blink(num * 2024, count - 1)

    return sum([blink(num, blinks) for num in stones])


def main(lines: InputType):
    stones = ints(lines[0])
    with timeit("Part 1"):
        print(solver(stones, 25))

    with timeit("Part 2"):
        print(solver(stones, 75))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
    """
    224529
    Part 1 took 1.47 ms
    266820198587914
    Part 2 took 55.19 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 50.67 ms
    """
