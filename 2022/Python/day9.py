from cmath import phase
with open("Inputs/9.txt") as f:
    ops = f.readlines()

directions = {
    "R": 1+0j,
    "U": 1j,
    "L": -1+0j,
    "D":-1j,
}

quadrants = {
    0.0: 1+0j,
    0.464: 1+1j,
    1.107: 1+1j,
    1.571: 1j,
    2.034: -1+1j,
    2.678: -1+1j,
    3.142: -1+0j,
    -2.678: -1-1j,
    -2.034: -1-1j,
    -1.571: -1j,
    -1.107: 1-1j,
    -0.464: 1-1j,
    0.785: 1+1j,
    -0.785: 1-1j,
    2.356: -1+1j,
    -2.356: -1-1j,
}
ROOT_2 = abs(1+1j)
PART_2 = True

# Head ... tail
rope = [0j] * (10 if PART_2 else 2)
visited = {rope[-1]}

# Part 2
for op in ops:
    dir, count = op[0], int(op.strip().split()[1])
    for _ in range(count):
        rope[0] += directions[dir]
        for i in range(1, len(rope)):
            prev_knot = rope[i-1]
            knot = rope[i]
            # If true, previous knot is still in adjacent points 
            if abs(prev_knot-knot) <= ROOT_2:
                continue
                
            # If not in adjacent points, move knot
            rope[i] += quadrants[round(phase(prev_knot-knot), 3)]
        visited.add(rope[-1])

print(len(visited))