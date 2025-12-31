from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


# Check 8 adjacent positions
# [(x, y)]
ADJACENT_DIRECTIONS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def roll_finder(grid: list[list[str]]):
    m = len(grid)
    n = len(grid[0])

    positions = []

    for y in range(m):
        for x in range(n):
            if grid[y][x] != "@":
                continue

            count = 0
            for dx, dy in ADJACENT_DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n) and (0 <= ny < m):
                    if grid[ny][nx] == "@":
                        count += 1
                if count > 3:
                    break

            if count < 4:
                positions.append((x, y))

    return positions


def part1(lines: InputType):
    grid = [list(line) for line in lines]
    positions = roll_finder(grid)
    return len(positions)


def part2(lines: InputType):
    grid = [list(line) for line in lines]
    m = len(grid)
    n = len(grid[0])

    counts = {}
    total = 0

    for y in range(m):
        for x in range(n):
            if grid[y][x] != "@":
                continue
            
            count = 0
            for dx, dy in ADJACENT_DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n) and (0 <= ny < m):
                    if grid[ny][nx] == "@":
                        count += 1

            counts[(x, y)] = count

    while True:
        to_remove = []

        for (x, y), count in counts.items():
            if count <= 3:
                to_remove.append((x, y))
        
        if not to_remove:
            break

        total += len(to_remove)

        for x,y in to_remove:
            counts.pop((x, y))
            for dx, dy in ADJACENT_DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (nx, ny) in counts:
                    counts[nx,ny] -= 1

    return total


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
