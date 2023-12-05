from input_manager import get_input
import re
from collections import defaultdict
from typing import Generator

input = get_input(__file__, lines=False)
part1 = True

raw_initial_seeds, *raw_categories = input.split("\n\n")
initial_seeds = [int(num) for num in re.findall(r"\d+", raw_initial_seeds)]

categories: dict[str, list[list[int]]] = {}

for raw_category in raw_categories:
    raw_category_name, *category_ranges = raw_category.split("\n")
    category_name = raw_category_name.split(" ")[0]
    categories[category_name] = [
        [int(num) for num in re.findall(r"\d+", line)] for line in category_ranges
    ]


def get_seeds(initial_seeds: list[int], part1: bool) -> Generator[int, None, None]:
    if part1:
        for seed in initial_seeds:
            yield seed
    else:
        for seed_start, count in zip(initial_seeds[::2], initial_seeds[1::2]):
            for seed in range(seed_start, seed_start + count):
                yield seed


processed: dict[str, dict[int, int]] = defaultdict(dict)
seed_to_location: dict[int, int] = {}

for seed in get_seeds(initial_seeds, part1):
    previous_category_destination = seed
    for category, category_ranges in categories.items():
        if (category in processed) and previous_category_destination in processed[
            category
        ]:
            previous_category_destination = processed[category][
                previous_category_destination
            ]
            continue

        processed[category][
            previous_category_destination
        ] = previous_category_destination

        for dest_start, source_start, delta in category_ranges:
            if (previous_category_destination >= (source_start + delta)) or (
                previous_category_destination < source_start
            ):
                continue
            dest = dest_start - source_start + previous_category_destination
            processed[category][previous_category_destination] = dest
            previous_category_destination = dest
            break

    seed_to_location[seed] = previous_category_destination

print(min(seed_to_location.values()))
