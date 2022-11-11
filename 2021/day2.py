with open("Inputs/2.txt", "r") as f:
    inputs = f.readlines()

x = y = aim = 0
for c in inputs:
    direction, mag = c.strip().split()
    if direction == "forward":
        x += int(mag)
        y += aim*int(mag)
    if direction == "down":
        aim += int(mag)
    if direction == "up":
        aim -= int(mag)
print(x,y,x*y)