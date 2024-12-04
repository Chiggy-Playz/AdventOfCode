from utils.input_manager import get_input
import re

input = get_input(__file__)
part1 = True
time, distance = ([int(num) for num in re.findall(r"\d+", line.replace(" ", " " if part1 else ""))] for line in input)

prod = 1
for race_time, race_distance in zip(time, distance):
    ways = 0
    for i in range(race_time + 1):
        if i * (race_time - i) > race_distance:
            ways += 1
    prod *= ways

print(prod)
