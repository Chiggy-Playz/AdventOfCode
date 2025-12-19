from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = str


def part1(text: InputType):
    ranges = [tuple(map(int, pair.split("-"))) for pair in text.split(",")]
    result = 0

    for left, right in ranges:
        ls = str(left)
        rs = str(right)

        ln = len(ls)
        rn = len(rs)

        # To handle cases like different digit count in ranges, like 88 (2) - 1234 (4)
        for n in range(ln, rn + 1):
            if (n % 2 != 0) or (n < 2):
                continue
            d = n // 2
            start = 10 ** (d - 1)
            end = 10**d

            for i in range(start, end):
                num = i * end + i
                if left <= num <= right:
                    result += num

                if right < num:
                    break

    return result


def part2(text: InputType):
    ranges = [tuple(map(int, pair.split("-"))) for pair in text.split(",")]
    result = 0
    seen = set()
    for left, right in ranges:
        ls = str(left)
        rs = str(right)

        ln = len(ls)
        rn = len(rs)

        for n in range(ln, rn + 1):
            # factorization:
            for factor in range(1, n):
                if n % factor != 0:
                    # not factor
                    continue

                k = n // factor
                start = 10 ** (factor - 1)
                end = 10**factor

                for i in range(start, end):
                    num = i
                    for _ in range(k - 1):
                        num *= 10**factor
                        num += i

                    if left <= num <= right and num not in seen:
                        seen.add(num)
                        result += num

                    if right < num:
                        break
    return result


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False, lines=False)
    main(lines)
    benchmark(main, lines)
    """
    18700015741
    Part 1 took 9.74 ms
    20077272987
    Part 2 took 24.38 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 32.99 ms
    """