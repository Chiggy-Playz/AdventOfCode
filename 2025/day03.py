from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]

def solver(lines: InputType, N: int):
    result = 0
    for line in lines:
        stack = []
        n = len(line)
        for idx, char in enumerate(line):
            num = int(char)
            # a number which is bigger than last. if pop allowed, then lets pop
            left = n - idx - 1
            while stack and num > stack[-1] and (len(stack) + left >= N):
                stack.pop()
                
            if len(stack) < N:
                stack.append(num)
        joltage = 0
        for i in stack:
            joltage = joltage * 10 + i
        result += joltage

    return result

def part1(lines: InputType):
    return solver(lines, 2)

def part2(lines: InputType):
    return solver(lines, 12)


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
