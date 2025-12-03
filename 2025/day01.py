from utils.input_manager import get_input

input = get_input(__file__)

instructions = [(s[0], int(s[1:])) for s in input]

# P1
result = 0
current = 50
for dirn, count in instructions:
    current = (current + (1 if dirn == "R" else -1) * count) % 100
    if current == 0:
        result += 1

print(result)

# P2
result = 0
current = 50
for dirn, count in instructions:
    if count >= 100:
        result += count // 100
        count = count % 100

    new = current + (1 if dirn == "R" else -1) * count
    if current != 0 and (new <= 0 or 100 <= new):
        result += 1

    current = new % 100

print(result)
