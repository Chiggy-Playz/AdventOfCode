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

delta = 0
for empty_row in empty_rows:
    arr = np.insert(arr, empty_row + delta, np.array(list("." * row_length)), 0)
    col_length += 1
    delta += 1

delta = 0
for empty_col in empty_cols:
    arr = np.insert(arr, empty_col + delta, np.array(list("." * col_length)), 1)
    delta += 1

galaxies = list(zip(np.argwhere(arr == "#").T[1], np.argwhere(arr == "#").T[0]))
# distances = defaultdict(lambda: float('inf'))
s = 0
for ((x1, y1), (x2, y2)) in itertools.combinations(galaxies, 2):
    s += abs(x2-x1) + abs(y2 - y1)
print(s)
