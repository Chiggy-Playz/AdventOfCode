from pprint import pprint

with open("Inputs/5.txt") as f:
    lines = f.readlines()

coordinates = [
    tuple(tuple(map(lambda x: int(x), cord.split(","))) for cord in both_cords.strip().split(" -> "))
    for both_cords in lines
]

# Only horizontal or vertical vents
# coordinates = list(filter(lambda x: (x[0][0] == x[1][0]) or (x[0][1] == x[1][1]), coordinates))

max_x = max(x[0] for c in coordinates for x in c)
max_y = max(x[1] for c in coordinates for x in c)

system = []

for y in range(max_y + 1):
    row = list()
    for x in range(max_x + 1):
        row.append(0)
    system.append(row)

for ((x1, y1), (x2, y2)) in coordinates:

    if x1 == x2:  # Move vertically

        if y2 > y1:  # Move top to bottom

            for i in range(y1, y2 + 1):

                system[i][x1] += 1
        else:  # Move bottom to top

            for i in range(y2, y1 + 1):

                system[i][x1] += 1

    elif y1 == y2:  # Move horizontally

        if x2 > x1:  # Move right to left

            for i in range(x1, x2 + 1):

                system[y1][i] += 1

        else:  # Move left to right

            for i in range(x2, x1 + 1):
                system[y1][i] += 1
    else:  # Diagnol
        
        sgn_x = -1 if (x2 < x1) else 1 # -1
        sgn_y = -1 if (y2 < y1) else 1 # +1

        for i in range(0, abs(x2-x1)+1): # 0, 1, 2
            system[y1+(i*sgn_y)][x1+(i*sgn_x)] += 1
            

# pprint(system)
danger_zones = 0
for row in system:
    for col in row:
        if col > 1:
            danger_zones += 1
print(danger_zones)
