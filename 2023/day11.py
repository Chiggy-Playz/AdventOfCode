from input_manager import get_input
import numpy as np
import itertools
from collections import defaultdict

input = get_input(__file__)
row_length = len(input[0])
col_length = len(input)

empty_rows = [i for i in range(row_length) if len(set(input[i])) == 1]

arr = np.array([list(i) for i in input])

empty_cols = []
for i in range(row_length):
    if len(set(arr[:, i])) == 1:
        empty_cols.append(i)

def solution(k):
    global arr

    galaxies = list(zip(np.argwhere(arr == "#").T[1], np.argwhere(arr == "#").T[0]))
    s = 0
    for (x1, y1), (x2, y2) in itertools.combinations(galaxies, 2):
        dx = 0
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for col in empty_cols:
            if min_x < col < max_x:
                dx += k
        dy = 0
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for row in empty_rows:
            if min_y < row < max_y:
                dy += k
        s += abs(max_x - min_x) + dx + abs(max_y - min_y) + dy 

    return s

print(solution(1))
print(solution(1000000-1))
