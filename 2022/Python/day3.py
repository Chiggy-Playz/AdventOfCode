with open("Inputs/3.txt") as f:
    rucksacks = f.readlines()

def intersect(sets: list[set[str]]) -> set[str]:
    first, second = sets.pop(), sets.pop()
    fis = first.intersection(second)
    if not sets:
        return fis
    sets.append(fis)
    return intersect(sets)


priorities = 0
for rucksack in rucksacks:
    first, second = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    common_type = next(iter(intersect([set(first), set(second)])), None)
    if not common_type:
        print("No common types")
        continue
    priorities += ord(common_type) - (38 if common_type.isupper() else 96)

print(priorities)

# Part 2

priorities = 0
for team in [rucksacks[i : i + 3] for i in range(0, len(rucksacks) - 2, 3)]:
    common_type = next(
        iter(intersect([set(elf.strip()) for elf in team])),
        None,
    )
    if not common_type:
        print("No common types")
        continue
    priorities += ord(common_type) - (38 if common_type.isupper() else 96)

print(priorities)
