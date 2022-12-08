with open("Inputs/8.txt") as f:
    raw_grid = f.readlines()

grid = [[int(t) for t in row.strip()] for row in raw_grid]

# Grid is square of side N
N = len(raw_grid)

def on_edge(point: tuple[int, int]):
    edge_length = N-1
    match point:
        case (x, 0):
            return True
        case (0, y): 
            return True
        case (x, y) if edge_length in (x, y):
            return True
        case (x, y):
            return False

# Only interior
visible_trees = 0
highest_scenic_score = 0
PART_2 = True

for y in range(1, N-1):
    for x in range(1, N-1):
        visible = False
        scenic_score = 1
        # x, y
        for direction in ((1,0), (0,1), (-1, 0), (0, -1)):
            point = (x, y)
            tree_seen = 0
            while True:
                tree_seen += 1
                if not on_edge(point):
                    point = tuple(sum(x) for x in zip(point, direction))
                if grid[point[1]][point[0]] >= grid[y][x]:
                    break # Tree hidden in this direction
                if on_edge(point):
                    visible = True
                    break
            scenic_score *= tree_seen
            # Only save cycles if not part 2
            if not PART_2:
                if visible:
                    break
        if visible:
            visible_trees += 1
        highest_scenic_score = max(highest_scenic_score, scenic_score)

print(4*N - 4 + visible_trees)
print(highest_scenic_score)