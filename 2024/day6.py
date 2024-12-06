from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import InputType

dirs = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}


def part1(lines: InputType):

    # First we find source
    for i, line in enumerate(lines):
        if "^" in line:
            current = (line.index("^"), i)
    # x, y
    dir = (0, -1)
    visited = set([current])
    while True:
        dx, dy = map(sum, zip(current, dir))

        if not ((0 <= dx < len(lines)) and (0 <= dy < len(lines))):
            break

        if lines[dy][dx] != "#":
            visited.add((dx, dy))
            current = dx, dy
            continue

        # Found a block in front, turn.
        dir = dirs[dir]

    return len(visited)


def part2(lines: InputType):
    # First we find source
    for i, line in enumerate(lines):
        if "^" in line:
            source = (line.index("^"), i)
    # x, y
    # current = source
    # dir = (0, -1)
    # obstacles = set()
    # while True:
    #     dx, dy = map(sum, zip(current, dir))

    #     if not ((0 <= dx < len(lines)) and (0 <= dy < len(lines))):
    #         break

    #     if lines[dy][dx] != "#":
    #         obstacles.add((dx, dy))
    #         current = dx, dy
    #         continue

    #     # Found a block in front, turn.
    #     dir = dirs[dir]
        
    # Bruteforce
    p2 = 0
    for y in range(len(lines)):
        for x in range(len(lines)):
            if lines[y][x] in "#^":
                continue
            dir = (0, -1)
            current = source
            visited: dict[tuple[int, int], list[tuple[int, int]]] = {}
            while True:
                dx, dy = map(sum, zip(current, dir))

                if not ((0 <= dx < len(lines)) and (0 <= dy < len(lines))):
                    break

                if (dx, dy) != (x, y) and lines[dy][dx] != "#":
                    if current in visited:
                        if dir in visited[current]:
                            p2 += 1
                            break
                    visited[current] = visited.get(current, []) + [dir]
                    current = (dx, dy)
                    continue

                # Found block
                dir = dirs[dir]

    return p2


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
