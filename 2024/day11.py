from functools import cache
from typing import TypeAlias

from utils.functools import ints
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def solver(stones: list[int], blinks: int):
    @cache
    def blink(num: int, count: int):
        if not count:
            return 1

        if num == 0:
            return blink(1, count - 1)
        s = str(num)
        if len(s) % 2 == 0:
            l = blink(int(s[: len(s) // 2]), count - 1)
            r = blink(int(s[len(s) // 2 :]), count - 1)
            return l + r

        return blink(num * 2024, count - 1)

    return sum([blink(num, 75) for num in stones])


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
    266820198587914
    Part 1 took 54.81 ms
    266820198587914
    Part 2 took 51.75 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 124.53 ms
    """