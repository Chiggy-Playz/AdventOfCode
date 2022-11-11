from typing import List, Tuple
from pprint import pprint

with open("Inputs/9.txt") as f:
    points = [[int(point.strip()) for point in line.strip()] for line in f.readlines()]

# X, Y
checked: List[Tuple[int, int]] = []
low_points: List[Tuple[int, int]] = []
# pprint(points)


def location(point):

    if point in {(0, 0), (len(points[0])-1, 0), (0, len(points)-1), (len(points[0])-1, len(points)-1)}:
        return "corner"
    elif (point[0] in {0, len(points[0])-1}) or (point[1] in {0, len(points)-1}):
        return "edge"
    else:
        return "none"


def get_right(point):
    return (point[0] + 1, point[1])

def get_left(point):
    return (point[0]-1, point[1])

def get_up(point):
    return (point[0], point[1] - 1)

def get_down(point):
    return (point[0], point[1] + 1)


def check(point: Tuple[int, int], where: str):
    points_to_check: List[Tuple[int, int]] = []

    if "r" in where:
        points_to_check.append(get_right(point))
    if "l" in where:
        points_to_check.append(get_left(point))    
    if "u" in where:
        points_to_check.append(get_up(point))
    if "d" in where:
        points_to_check.append(get_down(point))
    

    return all((points[py][px] > points[point[1]][point[0]]) for (px,py) in points_to_check)


for row in range(len(points)):
    for column in range(len(points[row])):
        point = (column, row)
        # point is x,y
        res = False

        if location(point) == "corner":

            if point == (0, 0):  # Top left
                res = check(point, "rd")
            elif point == (len(points[row])-1, 0):  # Top right
                res = check(point, "ld")
            elif point == (0, len(points)-1):  # Bottom left
                res = check(point, "ur")
            else:  # Bottom right
                res = check(point, "ul")

        elif location(point) == "edge":

            if point[1] not in {0, len(points)-1}:
                if point[0] == 0: # left wall
                    res = check(point, "udr")
                else: # right wall
                    res = check(point, "udl")
            if point[0] not in {0, len(points[0])-1}:
                if point[1] == 0: # top wall
                    res = check(point, "rld")
                else:
                    res = check(point, "rlu")
        else:
            res = check(point, "udlr") 

        if res:
            low_points.append(point)

risky_points = [points[y][x]+1 for (x,y) in low_points]
print(low_points)
print([points[y][x] for (x,y) in low_points])
pprint(risky_points)
pprint(sum(risky_points))

print("\n\nPART 2\n\n")

for point in low_points:
    
    ''
