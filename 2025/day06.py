from operator import add, mul
from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def part1(lines: InputType):
    ops = []
    results = []
    for op in lines[-1].split():
        op = op.strip()
        ops.append(add if op == "+" else mul)
        results.append(0 if op == "+" else 1)

    for line in lines[:-1]:
        line = line.split()
        nums = map(int, line)
        for i, num in enumerate(nums):
            results[i] = ops[i](num, results[i])

    return sum(results)


def part2(lines: InputType):
    nums = [0] * len(lines[0])

    for line in lines[:-1]:
        for i, c in enumerate(line):
            digit = int(c) if c.isdigit() else 0
            nums[i] = nums[i] * 10 + digit

    ops = []
    results = []
    for op in lines[-1].split():
        op = op.strip()
        ops.append(add if op == "+" else mul)
        results.append(0 if op == "+" else 1)

    i = 0
    for num in nums:
        if num == 0:
            i += 1
            continue

        # remove trailing 0 first
        while num % 10 == 0:
            num //= 10

        results[i] = ops[i](num, results[i])

    return sum(results)


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
