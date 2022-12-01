with open('Inputs/1.txt') as f:
    inputs = f.read()

elfs = inputs.split("\n\n")
calories = tuple()
for elf in elfs:
    s = 0
    for calory in elf.split("\n"):
        s += int(calory.strip())
    calories = tuple(sorted(calories + (s,), reverse=True))[:3]

# Part 1
print(calories[0])

# Part 2
print(sum(calories))
