# https://adventofcode.com/2015/day/2

with open("Inputs/day2.txt") as f:
    dimensions = [tuple(int(number) for number in line.split("x")) for line in f.readlines()]

total_area = 0
total_ribbon = 0

for (l, b, h) in dimensions:

    lb = l * b
    bh = b * h
    lh = l * h
    
    area_needed = 2 * (lb + bh + lh)
    slack = min(lb, bh, lh)
    
    total_area += area_needed + slack

    ribbon_length = 2 * sum(sorted((l,b,h))[:2])
    bow_length = l*b*h

    total_ribbon += ribbon_length + bow_length

print(total_area)
print(total_ribbon)