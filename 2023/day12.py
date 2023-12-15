from input_manager import get_input
import re
from itertools import combinations
from time import monotonic
from functools import lru_cache, cache

input = get_input(__file__)
part1 = False


def bruteforce():
    s = 0
    for y, line in enumerate(input):
        springs, nums = line.split()[0], list(
            map(int, re.findall(r"\d+", line.split()[1]))
        )

        # This function will take approximately 2 years for part 2 on my system :)
        # if not part1:
        #     springs = "?".join(springs*5)
        #     nums = nums * 5

        unknown_indexes = [i for i, c in enumerate(springs) if c == "?"]
        ways = 0
        for combo in combinations(unknown_indexes, sum(nums) - springs.count("#")):
            combo_line_list = list(springs)
            for index in combo:
                combo_line_list[index] = "#"
            combo_line = "".join(combo_line_list).replace("?", ".")

            # Now we just validate the combo_line
            target_index = 0
            spring_count = 0
            for char in combo_line:
                if spring_count == 0 and char == ".":
                    continue

                if char == "#":
                    spring_count += 1
                else:
                    # Done counting #'s, now we check.
                    if nums[target_index] != spring_count:
                        break  # Whoops, went overboard
                    spring_count = 0
                    target_index += 1
            else:
                # Didnt parse the last spring
                if spring_count != 0 and nums[target_index] != spring_count:
                    continue
                ways += 1

        s += ways
    return s


# Returns number of ways
@lru_cache(maxsize=None)
def check_spring(spring: str, groups: tuple[int]) -> int:
    if len(spring) == 0:
        return len(groups) == 0

    if len(groups) == 0:
        return not ("#" in spring)

    char = spring[0]
    group = groups[0]
    match char:
        case ".":
            return check_spring(spring[1:], groups)
        case "?":
            period = check_spring("." + spring[1:], groups)
            hash = check_spring("#" + spring[1:], groups)
            return period + hash
        case "#":
            # Check if a group matches
            count = 1
            for char in spring[1:]:
                if char == ".":
                    break
                count += 1

            # If theres not enough to make the first group, return 0 ways
            if count < group:
                return 0

            if spring.startswith(group * "#"):
                # If the whole string comprises of group, return 1
                if len(spring) == group:
                    # If there is a group left and we've already exhausted the list, uh oh
                    return len(groups[1:]) == 0

                # Check what the next character is

                # If its `#`, then that means the group is larger than we need :(, return 0
                if spring[group] == "#":
                    return 0

                # However, if its a ?...
                # Here, things get interesting...
                # We replace the ? with a ., and remove the `group` from `groups` and then do another recursive call
                if spring[group] == "?":
                    return check_spring("." + spring[group + 1 :], groups[1:])

                # If its `.`, then remove it from spring and also remove `group` from `groups`
                if spring[group] == ".":
                    return check_spring(spring[group + 1 :], groups[1:])

            else:
                if "?" in spring[:count]:
                    return check_spring(
                        spring[: spring.find("?")]
                        + "."
                        + spring[spring.find("?") + 1 :],
                        groups,
                    ) + check_spring(
                        spring[: spring.find("?")]
                        + "#"
                        + spring[spring.find("?") + 1 :],
                        groups,
                    )
                else:
                    raise Exception("Wild edge case found")
        case _:
            raise Exception("Dafuq?!")

    raise Exception("Interesting.")


def solution(part1: bool):
    s = 0
    for y, line in enumerate(input):
        springs, nums = line.split()[0], tuple(
            map(int, re.findall(r"\d+", line.split()[1]))
        )

        if not part1:
            springs = "?".join([springs] * 5)
            nums = nums * 5
        s += int(check_spring(springs, nums))
    return s

start = monotonic()
print(solution(True))
print(solution(False))
print(f"{(monotonic() - start) * 1000:.0f}ms")
