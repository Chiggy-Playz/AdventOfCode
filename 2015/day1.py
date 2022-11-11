# https://adventofcode.com/2015/day/1

from email.mime import base


with open("Inputs/day1.txt") as f:
    input = f.read()

floor = 0
basement_causing_character = 0

for index, character in enumerate(input):
    floor += 1 if character == "(" else -1
    if basement_causing_character == 0 and floor == -1:
        basement_causing_character = index + 1

print(floor)
print(basement_causing_character)
