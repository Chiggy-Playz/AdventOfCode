with open("Inputs/6.txt") as f:
    stream = f.read()

previous = []
PART2 = True
if not PART2:
    distinct_char = 4
else:
    distinct_char = 14

for index, char in enumerate(stream):
    pass
    previous.append(char)
    if len(previous) < distinct_char:
        continue

    if len(set(previous[-distinct_char:])) == distinct_char:
        print(index+1)
        break

    previous.pop(0)
