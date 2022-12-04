import re

with open("Inputs/4.txt") as f:
    pairs = f.readlines()

collisions = 0
PART_2 = False
for pair in pairs:
    start1, stop1, start2, stop2 = (int(num) for num in re.findall(r"\d+", pair))
    if start1 <= start2:
        if stop2 <= stop1:
            collisions += 1
            continue
    if start2 <= start1:
        if stop1 <= stop2:
            collisions += 1
            continue
    # Part 2
    if (
        (start2 <= start1 <= stop2)
        or (start2 <= stop1 <= stop2)
        or (start1 <= start2 <= stop1)
        or (start1 <= stop2 <= stop1)
    ) and PART_2:
        collisions += 1
print(collisions)
