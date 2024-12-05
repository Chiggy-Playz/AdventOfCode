from utils.input_manager import get_input
from utils.timing import timeit


def part1(lines: str):
    rules_raw, updates = lines.split("\n\n")
    rules: dict[int, list[int]] = {}
    inv_rules: dict[int, list[int]] = {}
    for rule in rules_raw.splitlines():
        k, v = int(rule.split("|")[0]), int(rule.split("|")[1])
        rules[k] = rules.get(k, []) + [v]
        inv_rules[v] = inv_rules.get(v, []) + [k]

    updates = [list(map(int, line.split(","))) for line in updates.splitlines()]
    safe = 0
    for update in updates:
        for i, num in enumerate(update):
            if set(update[:i]).intersection(set(rules.get(num, []))):
                break
        else:
            safe += update[len(update) // 2]

    return safe


def part2(lines: str):
    rules_raw, updates = lines.split("\n\n")
    rules: dict[int, list[int]] = {}
    inv_rules: dict[int, list[int]] = {}
    for rule in rules_raw.splitlines():
        k, v = int(rule.split("|")[0]), int(rule.split("|")[1])
        rules[k] = rules.get(k, []) + [v]
        inv_rules[v] = inv_rules.get(v, []) + [k]

    updates = [list(map(int, line.split(","))) for line in updates.splitlines()]
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
                if update[i] in rules.get(update[j], []) or update[j] in inv_rules.get(update[i], []):
                    update[i], update[j] = update[j], update[i]

        incorrect += update[len(update) // 2]

    return incorrect


if __name__ == "__main__":
    lines = get_input(testing=False, lines=False)
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))
