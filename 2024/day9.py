from typing import TypeAlias

from utils.functools import ints
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = str


def part1(s: InputType):
    digits = ints(s, greedy=False)
    blocks, free = digits[0::2], digits[1::2]
    i, j, k = len(blocks) - 1, 0, 0

    # block id, times it occurs
    out: list[tuple[int, int]] = []
    while k <= i:
        # First append k
        out.append((k, blocks[k]))

        # Now we fuck around with i and j
        while free[j] and i > k:
            if free[j] <= blocks[i]:
                out.append((i, free[j]))
                blocks[i] -= free[j]
                # Completely used up
                free[j] = 0
                if not blocks[i]:
                    i -= 1
            else:
                out.append((i, blocks[i]))
                free[j] -= blocks[i]
                blocks[i] = 0
                i -= 1

        j += 1
        k += 1

    result = 0
    i = 0
    for block, freq in out:
        for pos in range(i, i + freq):
            result += block * pos
        i += freq

    return result


def part2(s: InputType):
    digits = ints(s, greedy=False)

    out: list[tuple[int, int]] = []
    for index, digit in enumerate(digits):
        if index % 2 == 0:
            out.append((index // 2, digit))
        else:
            out.append((-1, digit))

    i = len(out) - 1
    while i > 0:
        block, freq = out[i]
        if block == -1:
            i -= 1
            continue

        for j in range(1, i):
            free_block, free_freq = out[j]
            if free_block != -1:
                continue
            if freq <= free_freq:
                out[i] = (-1, out[i][1])
                out.insert(j, (block, freq))
                free_freq -= freq
                if not free_freq:
                    del out[j + 1]
                else:
                    out[j + 1] = (-1, free_freq)
                break
        else:
            i -= 1

    result = 0
    i = 0
    for block, freq in out:
        if block != -1:
            for pos in range(i, i + freq):
                result += block * pos
        i += freq

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
    6299243228569
    Part 1 took 7.92 ms
    6326952672104
    Part 2 took 1.98 s

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 2.04 s
    """
