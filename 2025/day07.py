from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def part1(lines: InputType):
    N = len(lines[0])
    source = lines[0].index("S")
    beams = {source}
    split_count = 0
    for line in lines[2:]:
        for idx, char in enumerate(line):
            if char != "^":
                continue

            if idx in beams:
                split_count += 1
                beams.remove(idx)
                if 0 <= (idx - 1):
                    beams.add(idx - 1)
                if (idx - 1) < N:
                    beams.add(idx + 1)

    return split_count


def part2(lines: InputType):
    N = len(lines[0])
    beams = {i: 0 for i in range(N)}
    source = lines[0].index("S")
    beams[source] = 1
    for line in lines[2:]:
        for idx, char in enumerate(line):
            if char != "^":
                continue

            if beams.get(idx):
                beam_count = beams[idx]
                beams[idx] -= beam_count
                if 0 <= (idx - 1):
                    beams[idx - 1] += beam_count
                if (idx - 1) < N:
                    beams[idx + 1] += beam_count

    return sum(beams.values())


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
