from utils.input_manager import get_input
import re
from collections import defaultdict
from typing import Generator

input = get_input(__file__, lines=False)

raw_initial_seeds, *raw_categories = input.split("\n\n")
initial_seeds = [int(num) for num in re.findall(r"\d+", raw_initial_seeds)]

categories: dict[str, list[list[int]]] = {}

for raw_category in raw_categories:
    raw_category_name, *category_ranges = raw_category.split("\n")
    category_name = raw_category_name.split(" ")[0]
    categories[category_name] = [[int(num) for num in re.findall(r"\d+", line)] for line in category_ranges]


def part1():
    seed_to_location: dict[int, int] = {}

    for seed in initial_seeds:
        previous_category_destination = seed
        for category, category_ranges in categories.items():
            for dest_start, source_start, delta in category_ranges:
                if (previous_category_destination >= (source_start + delta)) or (
                    previous_category_destination < source_start
                ):
                    continue

                previous_category_destination = dest_start - source_start + previous_category_destination
                break
        seed_to_location[seed] = previous_category_destination

    return min(seed_to_location.values())


def part2():
    # ex, seed-to-soil: [ (98, 99, 50, 51), (50, 97, 52, 99) ]
    ranges: dict[str, list[tuple[int, int, int, int]]] = defaultdict(list)
    loc = float("inf")
    for category, category_ranges in categories.items():
        start_min = float("inf")
        start_max = 0
        dest_min = float("inf")
        dest_max = 0
        count = 0
        for dest_start, source_start, delta in category_ranges:
            source_end = source_start + delta - 1
            dest_end = dest_start + delta - 1

            ranges[category].append((source_start, source_end, dest_start, dest_end))

    loc = float("inf")
    for seed_start, seed_count in zip(initial_seeds[::2], initial_seeds[1::2]):
        seed_count -= 1
        seed_end = seed_start + seed_count
        previous_range = (seed_start, seed_end)
        for category, category_ranges in ranges.items():
            start_matched, end_matched = False, False
            old = previous_range
            for source_start, source_end, dest_start, dest_end in category_ranges:
                if (not start_matched) and (source_start <= previous_range[0] <= source_end):
                    delta = previous_range[0] - source_start
                    previous_range = (
                        dest_start + delta,
                        previous_range[1],
                    )
                    start_matched = True
                if (not end_matched) and (source_start <= previous_range[1] <= source_end):
                    delta = previous_range[1] - source_start
                    previous_range = (
                        previous_range[0],
                        (
                            dest_start + delta
                            if ((source_start <= previous_range[0] <= source_end) or previous_range[0] > source_end)
                            else dest_start
                        ),
                    )
                    end_matched = True

        loc = min(loc, previous_range[0], previous_range[1])
    return loc


print(part1())
print(part2())  # doesnt work :)
