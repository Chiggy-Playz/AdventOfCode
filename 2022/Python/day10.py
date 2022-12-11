with open("Inputs/10.txt") as f:
    ops = f.readlines()

# Cycle: value
graph: dict[int, int] = {}

cycle = 1
x = 1

def output():
    global x, cycle
    print("#" if (cycle-1)%40 in (x-1, x, x+1) else ".", end="")

def incr():
    global cycle
    cycle += 1
    if (cycle-1)%40 == 0:
        print()

for op in ops:
    op = op.strip()
    if op == "noop":
        output()
        incr()
    else:
        to_add = int(op.split(" ")[-1])
        output()
        incr()
        output()
        x += to_add
        incr()

#print(sum([graph[c]*c for c in range(20, 221, 40)]))