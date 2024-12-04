from common.input_manager import get_input
from collections import defaultdict

input = get_input(__file__)

input = [list(map(lambda s: int(s), x)) for x in input]

# Apply djikstra's algo while keeping the last 3 points in memory for straight line checking

start = (0, 0)
n = len(input)
goal = (n, n)
visited: set[tuple[int, int]] = set()
MAX_DISTANCE = n * n * 9

distance_from_start: dict[tuple[int, int], int] = {(y, x): MAX_DISTANCE for x in range(n) for y in range(n)}
distance_from_start[start] = 0

prev: dict[tuple[int, int], list] = {(y, x): [] for x in range(n) for y in range(n)}

queue = [(y, x) for x in range(n) for y in range(n)]


def adj_list(point: tuple[int, int]):

    # Point, dist
    y, x = point
    adj: list[tuple[tuple[int, int], int]] = []
    for dy, dx in {(0, -1), (0, 1), (1, 0), (-1, 0)}:
        new: tuple[int, int] = y + dy, x + dx
        if (new[0] < 0) or (new[0] >= n) or (new[1] < 0) or (new[1] >= n):
            continue
        adj.append(
            (
                new,
                input[new[0]][new[1]],
            ),
        )
    return adj

while len(queue) != 0:
    current_point: tuple[int, int] = min(queue, key=lambda x: distance_from_start[x])
    queue.remove(current_point)
    x, y = current_point

    adj = adj_list(current_point)

    for neighbour_point, neighbour_dist in adj:
        if neighbour_point not in queue:
            continue


        # Check if more than 4 blocks in straight line:
        previous_4_path: list[tuple[int, int]] = (prev[current_point] + [current_point])[-4:]

        if len(previous_4_path) == 4:
            # If travelling horizontally, the y stays same
            if len(set([p[0] for p in previous_4_path])) == 1:
                # If neighbour path causes travel in same line, skip this point
                if neighbour_point[0] == previous_4_path[0][0]:
                    continue
            elif len(set([p[1] for p in previous_4_path])) == 1:
                if neighbour_point[1] == previous_4_path[0][1]:
                    continue

        alt = distance_from_start[current_point] + neighbour_dist
        if alt < distance_from_start[neighbour_point]:
            distance_from_start[neighbour_point] = alt
            prev[neighbour_point] = prev[current_point] + [current_point]

    print("Hi")
print(":Yo")
