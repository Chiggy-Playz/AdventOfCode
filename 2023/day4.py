from input_manager import get_input
import re
from collections import defaultdict

input = get_input(__file__)


def part1():
    sum = 0
    for line in input:
        line = line.strip()
        numbers = line.split(": ")[1]
        raw_winning, raw_card = numbers.split(" | ")
        win_numbers = set(re.findall(r"(\d+)", raw_winning))
        card_numbers = set(re.findall(r"(\d+)", raw_card))
        count = len(win_numbers.intersection(card_numbers))
        sum += int(2 ** (count - 1))
    return sum


def part2():
    processed: dict[int, int] = {}
    instances = defaultdict(lambda: 0)

    def process(idx: int):
        instances[idx] += 1

        if idx not in processed:
            line = input[idx]
            line = line.strip()
            _, numbers = line.split(": ")
            raw_winning, raw_card = numbers.split(" | ")
            win_numbers = set(re.findall(r"(\d+)", raw_winning))
            card_numbers = set(re.findall(r"(\d+)", raw_card))
            count = len(win_numbers.intersection(card_numbers))
            processed[idx] = count
        else:
            count = processed[idx]

        for i in range(idx + 1, idx + count + 1):
            process(i)

    queue = list(range(len(input)))

    while len(queue) != 0:
        idx = queue.pop(0)
        process(idx)

    return sum(instances.values())


print(part1())
print(part2())
