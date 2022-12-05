import re
with open("Inputs/5.txt") as f:
    inp = f.read()
    crates, operations = inp.split("\n\n")  #lines[:8], lines[10:]
    crates, operations = crates.split("\n")[:-1], operations.split("\n")

print("\n".join(crates))

stacks: dict[int, list[str]] = {}
PART2 = True

for height, row in enumerate(crates):
    for i in range(0, len(row), 4):
        crate = row[i:i + 4].strip("[ ]\n")
        if not crate:
            continue
        stack_number = (i // 4) + 1
        if stack_number in stacks:
            stacks[stack_number].insert(0, crate)
        else:
            stacks[stack_number] = [crate]

for operation in operations:
    count, source, dest = [
        int(num.strip()) for num in re.findall(r'\d+', operation)
    ]
    if not PART2:
        for _ in range(count):
            stacks[dest].append(stacks[source].pop())
    else:
        stacks[dest].extend(stacks[source][-count:])
        stacks[source] = stacks[source][:-count]

print("".join(stacks[i][-1] for i in range(1, len(stacks) + 1) if stacks[i]))
