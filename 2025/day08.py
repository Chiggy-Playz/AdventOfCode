import heapq
from functools import reduce
from typing import TypeAlias

from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit

InputType: TypeAlias = list[str]


def dist(
    p1: tuple[int, ...],
    p2: tuple[int, ...],
):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n  # Track component count

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            # Union by rank
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            self.num_components -= 1
            return True
        return False


def part1(points, edges):
    uf = UnionFind(len(points))
    CONNECTIONS = 1000
    for _ in range(CONNECTIONS):
        _, p1, p2 = heapq.heappop(edges)
        uf.union(p1, p2)

    circuits = {}
    for i in range(len(points)):
        root = uf.find(i)
        circuits[root] = 1 + circuits.get(root, 0)

    top_3 = heapq.nlargest(3, circuits.items(), key=lambda x: x[1])
    return reduce(lambda x, y: x * y, [c[1] for c in top_3], 1)


def part2(points, edges):
    uf = UnionFind(len(points))
    while uf.num_components > 1:
        _, p1, p2 = heapq.heappop(edges)
        if uf.union(p1, p2):
            if uf.num_components == 1:
                return points[p1][0] * points[p2][0]


def main(lines: InputType):
    with timeit("Data Processing"):
        points = [tuple(int(x) for x in line.split(",")) for line in lines]

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((dist(points[i], points[j]), i, j))
        heapq.heapify(edges)

    with timeit("Part 1"):
        p1 = part1(points, list(edges))
    print(p1)
    with timeit("Part 2"):
        p2 = part2(points, edges)
    print(p2)


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)
