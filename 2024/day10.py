from typing import TypeAlias

from utils.functools import ingrid, ints, lmap, padd, traverse_grid
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import Point

InputType: TypeAlias = list[str]


def neighbours(grid: list[list[int]], node: Point):
    result = []
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if ingrid(len(grid), *padd(node, dir)):
            result.append(padd(node, dir))

    return result


def part1(lines: InputType):

    grid = list(ints(line, greedy=False) for line in lines)
    trailhead_scores: dict[tuple, set] = {}

    trailhead_pos = []
    for x, y, val in traverse_grid(grid):
        if val == 0:
            trailhead_pos.append((x, y))

    for trailhead in trailhead_pos:

        def dfs(node: tuple[int, int], visited: set[Point]):
            if node in visited:
                return

            if grid[node[1]][node[0]] == 9:
                trailhead_scores[trailhead] = trailhead_scores.get(trailhead, set()).union((set([node])))
                return

            visited.add(node)
            for neighbour in neighbours(grid, node):
                if neighbour not in visited and (grid[neighbour[1]][neighbour[0]] - grid[node[1]][node[0]]) == 1:
                    dfs(neighbour, visited)

        dfs(trailhead, set())

    return sum(lmap(len, trailhead_scores.values()))


def part2(lines: InputType):
    grid = list(ints(line, greedy=False) for line in lines)
    trailhead_scores: dict[tuple, list] = {}

    trailhead_pos = []
    for x, y, val in traverse_grid(grid):
        if val == 0:
            trailhead_pos.append((x, y))

    for trailhead in trailhead_pos:

        def dfs(node: tuple[int, int], visited: list[Point]):

            if grid[node[1]][node[0]] == 9:
                trailhead_scores[trailhead] = trailhead_scores.get(trailhead, []) + [node]
                return

            visited.append(node)
            for neighbour in neighbours(grid, node):
                if (grid[neighbour[1]][neighbour[0]] - grid[node[1]][node[0]]) == 1:
                    dfs(neighbour, visited.copy())

        dfs(trailhead, [])

    return sum(lmap(len, trailhead_scores.values()))


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
    """
    629
    Part 1 took 14.30 ms
    1242
    Part 2 took 17.42 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 31.92 ms
    """