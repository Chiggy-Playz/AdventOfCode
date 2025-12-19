from typing import TypeAlias

from utils.functools import ingrid, padd, pdiff, traverse_grid
from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import Point

import sys

sys.setrecursionlimit(1000**3)

InputType: TypeAlias = list[str]


def neighbours(n: int, node: Point, valid_only=True):
    result = []
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new = padd(node, dir)
        if valid_only and not ingrid(n, *new):
            continue
        result.append(padd(node, dir))

    return result

# ASssuming invalid only
def neighboursD(n: int, node: Point):
    result: list[tuple[tuple, bool]] = []
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
        new = padd(node, dir)
        nx, ny = new
        # Max bounds, -1 <= nx ny <= n
        if not (-1 <= nx <= n and -1 <= ny <= n):
            continue

        result.append((new, dir in ((-1, -1), (1, 1), (-1, 1), (1, -1),)))

    return result

def part1(lines: InputType):

    regions: list[tuple[str, set]] = []
    visited: set[Point] = set()

    for x, y, val in traverse_grid(lines):
        points = set()
        queue = [(x, y)]
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            points.add(node)
            for neighbour in neighbours(len(lines), node):
                if lines[neighbour[1]][neighbour[0]] != val:
                    continue
                if neighbour not in visited:
                    queue.append(neighbour)
        if not points:
            continue
        regions.append((val, points))

    total_price = 0
    for region, points in regions:
        area = len(points)
        perimeter = 0
        # To calculate perimeter, we just get all neighbours of all points and check which are not in points already
        for point in points:
            perimeter += len(set(neighbours(len(lines), point, False)).difference(points))

        total_price += area * perimeter

    return total_price


def part2(lines: InputType):
    regions: list[tuple[str, set]] = []
    visited: set[Point] = set()

    for x, y, val in traverse_grid(lines):
        points = set()
        queue = [(x, y)]
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            points.add(node)
            for neighbour in neighbours(len(lines), node):
                if lines[neighbour[1]][neighbour[0]] != val:
                    continue
                if neighbour not in visited:
                    queue.append(neighbour)
        if not points:
            continue
        regions.append((val, points))

    total_price = 0
    for region, points in regions:
        area = len(points)
        perimeter = 0
        perimeter_points = set()
        boundary = set()
        # To calculate perimeter, we just get all neighbours of all points and check which are not in points already
        for point in points:
            idk = set(neighbours(len(lines), point, False)).difference(points)
            if idk:
                perimeter_points = perimeter_points.union(idk)
                boundary.add(point)

        outer_boundary = set()
        for point in boundary:
            for neighbour in neighbours(len(lines), point, False):
                if not ingrid(len(lines), *neighbour) or lines[neighbour[1]][neighbour[0]] != region:
                    outer_boundary.add(neighbour)

        total_peri = 0
        visited = set()
        gah = list(outer_boundary.copy())
        while len(visited) != len(outer_boundary):
            node = gah.pop()
            if node in visited:
                continue

            dir = (0,0)

            def dfs(node):
                nonlocal total_peri, dir
                if node in visited:
                    return
                
                visited.add(node)
                for neighbour, diagnol in neighboursD(len(lines), node):
                    if neighbour not in outer_boundary or neighbour in visited:
                        continue

                    if pdiff(neighbour, node) != dir:
                        total_peri += 1
                        dir = pdiff(neighbour, node)
                    dfs(neighbour)                
            
            dfs(node)
        
        print(total_peri)





        # y: dict[int, list] = {}
        # x: dict[int, list] = {}
        # for point in outer_boundary:
        #     y[point[1]] = y.get(point[1], []) + [point]
        #     x[point[0]] = x.get(point[0], []) + [point]


        # sides = set()
        # total_peri = 0
        # for yy, ps in y.items():
        #     if len(ps) == 1:
        #         total_peri += 1
        #         continue

        #     ps.sort(key=lambda x: x[0])
        #     i = 0
        #     j = 0
        #     while i < len(ps) - 1:
        #         if abs(ps[i][0] - ps[i+1][0]) != 1:
        #             sides.add(tuple(ps[j:i+1]))
        #             j = i+1
        #         i+=1

        #     sides.add(tuple(ps[j:]))
        
        # sx = set()
        # for xx, ps in x.items():
        #     if len(ps) == 1:
        #         total_peri += 1
        #         continue

        #     ps.sort(key=lambda s: s[1])
        #     i = 0
        #     j = 0
        #     while i < len(ps) - 1:
        #         if abs(ps[i][1] - ps[i+1][1]) != 1:
        #             sx.add(tuple(ps[j:i+1]))
        #             j = i+1
        #         i+=1

        #     sx.add(tuple(ps[j:]))

        # # visited2 = set()
        # # sides = 0
        # # queue = [list(outer_boundary)[0]]
        # # while queue:
        # #     node = queue.pop(0)
            
        # #     for neighbour in neighbours(len(lines), node):
        # #         if neighbour in outer_boundary:
                    

        # # print(region, area, total_peri)

        # total_peri = 0
        # for xxx in sx:
        #     if len(xxx) != 1:
        #         total_peri += 1
        #         continue

        #     # It means its one. see if its in any sidesy
        #     for yyy in sides:
        #         if xxx[0] in yyy and xxx != yyy:
        #             break
        #     else:
        #         total_peri += 1
        
        # for yyy in sides:
        #     if len(yyy) != 1:
        #         total_peri += 1
        #         continue

        #     # It means its one. see if its in any sidesy
        #     for xxx in sides:
        #         if yyy[0] in xxx and yyy != xxx:
        #             break
        #     else:
        #         total_peri += 1
            
        total_price += area * total_peri
 
    return total_price

def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=True)
    main(lines)
    benchmark(main, lines)
