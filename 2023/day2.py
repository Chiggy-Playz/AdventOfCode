from utils.input_manager import get_input
import re

input = get_input(__file__)

allowed = {"red": 12, "green": 13, "blue": 14}


def part1():
    valid_ids = []
    for line in input:
        game_id_match = re.search(r"(\d*):", line)
        assert game_id_match
        game_id = int(game_id_match.groups()[0])

        sets = line.split(": ")[-1]
        for set in sets.split(";"):
            for cube_group in set.split(", "):
                cube_group_match = re.search(r"(\d*) (blue|red|green)", cube_group)
                assert cube_group_match
                count = cube_group_match.groups()[0]
                color = cube_group_match.groups()[1]
                if int(count) > allowed[color]:
                    break
            else:
                continue
            break
        else:
            valid_ids.append(game_id)
            continue

    return sum(valid_ids)


def part2():
    powers = []
    for line in input:
        game_id_match = re.search(r"(\d*):", line)
        assert game_id_match
        game_id = int(game_id_match.groups()[0])

        sets = line.split(": ")[-1]
        red_max = green_max = blue_max = 0

        for set in sets.split(";"):
            for cube_group in set.split(", "):
                cube_group_match = re.search(r"(\d*) (blue|red|green)", cube_group)
                assert cube_group_match
                count = int(cube_group_match.groups()[0])
                color = cube_group_match.groups()[1]
                match color:
                    case "red":
                        red_max = max(red_max, count)
                    case "green":
                        green_max = max(green_max, count)
                    case "blue":
                        blue_max = max(blue_max, count)

        powers.append(red_max * green_max * blue_max)

    return sum(powers)


print(part1())
print(part2())
