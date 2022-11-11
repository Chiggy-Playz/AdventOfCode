# https://adventofcode.com/2015/day/5

with open("Inputs/day5.txt") as f:
    strings = list(map(lambda s: s.strip() ,f.readlines()))

nice = 0
disallowed = {"ab", "cd", "pq", "xy"}

for string in strings:

    vowel_in_string = [char for char in string if char in "aeiou"]
    if len(vowel_in_string) < 3:
        continue
    
    if not [ char for char in set(string) if char * 2 in string]:
        continue

    if any([True for substring in disallowed if substring in string]):
        continue

    nice += 1

print(nice)

# Part 2

nice = 0
for string in strings:
    
    for index, char in enumerate(string[:-1]):
        letters = char + string[index+1]
        if letters in string.replace(letters, "..", 1):
            break
    else:
        continue

    for index, char in enumerate(string[:-2]):
        if char == string[index+2]:
            break
    else:
        continue

    nice += 1

print(nice)