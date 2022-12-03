with open("Inputs/2.txt") as f:
    inputs = f.readlines()

# A, X: Rock
# B, Y: Paper
# C, Z: Scissor

round_points = {m:idx+1 for idx, m in enumerate(("X", "Y", "Z"))}
win_moves = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}
score = 0
for line in inputs:
    opponent, me = line.strip().split(" ")
    score += round_points[me]
    if opponent == {"X":"A", "Y":"B", "Z":"C"}[me]:
        score += 3
    elif win_moves[me] == opponent:
        # Win
        score += 6
    else:
        score += 0
print(score)

# Part 2

# X: Lose
# Y: Draw
# Z: Win

round_points = {"X": 0, "Y": 3, "Z": 6,}
move_points = {m:idx+1 for idx, m in enumerate(("A", "B", "C"))}
win_moves = {
    "A": "B",
    "B": "C",
    "C": "A",
}
score = 0

for line in inputs:
    opponent, end = line.strip().split(" ")
    score += round_points[end]
    if end == "Y":
        score += move_points[opponent]
    elif end == "Z":
        score += move_points[win_moves[opponent]]
    else:
        score += move_points[opponent] - 1 if move_points[opponent] > 1 else 3

print(score)