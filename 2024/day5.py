from utils.input_manager import get_input
from utils.timing import timeit


def part1(rules: dict[int, list[int]], updates: list[list[int]]):
    safe = 0
    for update in updates:
        for i, num in enumerate(update):
            if set(update[:i]).intersection(set(rules.get(num, []))):
                break
        else:
            safe += update[len(update) // 2]
    return safe


def part2(rules: dict[int, list[int]], updates: list[list[int]]):
    incorrect = 0
    for update in updates:
        for i, num in enumerate(update):
            if set(update[:i]).intersection(set(rules.get(num, []))):
                break
        else:
            # If its here it means its correct, move on
            continue

        # We have incorrect shit. need to fix.
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                # Find if i and j are already in correct order
                if update[i] in rules.get(update[j], []):
                    update[i], update[j] = update[j], update[i]

        incorrect += update[len(update) // 2]

    return incorrect


def main():
    lines = get_input(testing=False, lines=False)
    rules_raw, updates = lines.split("\n\n")
    rules: dict[int, list[int]] = {}
    for rule in rules_raw.splitlines():
        k, v = int(rule.split("|")[0]), int(rule.split("|")[1])
        rules[k] = rules.get(k, []) + [v]

    updates = [list(map(int, line.split(","))) for line in updates.splitlines()]
    with timeit("Part 1"):
        print(part1(rules, updates))

    with timeit("Part 2"):
        print(part2(rules, updates))


if __name__ == "__main__":
    main()
