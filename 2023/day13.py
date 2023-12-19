from input_manager import get_input
import numpy as np

input = get_input(__file__, lines=False)

reflections = input.split("\n\n")


def part1():
    s = 0

    for reflection in reflections:
        arr = np.array([list(i) for i in reflection.splitlines()])
        row, cols = arr.shape

        reflection_found = False

        for col in range(0, cols - 1):
            j = 0
            matched = 0
            impossible = False
            while True:
                if all(arr[:, col - j] == arr[:, col + 1 + j]):
                    matched += 1
                    j += 1

                    # Reached left or right of the list
                    if j > col or ((col + 1 + j) == cols):
                        break
                else:
                    if matched != 0:
                        impossible = True
                    break
            if impossible:
                continue

            if matched == 0:
                continue
            s += col + 1
            reflection_found = True
            break

        if reflection_found:
            continue

        # Checking row wise first ig
        for row in range(0, len(arr) - 1):
            j = 0
            matched = 0
            row_impossible = False
            while True:
                if all(arr[row - j] == arr[row + 1 + j]):
                    matched += 1
                    j += 1
                    # Reached top of the list
                    if j > row or ((row + 1 + j) == len(arr)):
                        break
                else:
                    if matched != 0:
                        row_impossible = True
                    break
            if row_impossible:
                continue

            if matched == 0:
                continue

            s += 100 * (row + 1)
            break

        # Now decide which has more reflections:

    return s


def part2():
    s = 0

    for reflection in reflections:
        arr = np.array([list(i) for i in reflection.splitlines()])
        row, cols = arr.shape

        reflection_found = False

        for col in range(0, cols - 1):
            j = 0
            matched = 0
            impossible = False
            smudged = False
            while True:
                check_arr = arr[:, col - j] == arr[:, col + 1 + j]
                if all(check_arr):
                    matched += 1
                    j += 1

                    # Reached left or right of the list
                    if j > col or ((col + 1 + j) == cols):
                        break
                else:
                    # Check for smudges, fix, and restart
                    if (not smudged) and (np.count_nonzero(check_arr == False) == 1):
                        smudged = True
                        matched += 1
                        j += 1

                        # Reached left or right of the list
                        if j > col or ((col + 1 + j) == cols):
                            break
                        continue

                    if matched != 0:
                        impossible = True
                    break
            if impossible or (matched == 0) or not smudged:
                continue
            s += col + 1
            reflection_found = True
            break
        
        if reflection_found:
            continue

        # Checking row wise first ig
        for row in range(0, len(arr) - 1):
            j = 0
            matched = 0
            row_impossible = False
            smudged = False

            while True:
                check_arr = arr[row - j] == arr[row + 1 + j]
                if all(check_arr):
                    matched += 1
                    j += 1
                    # Reached top of the list
                    if j > row or ((row + 1 + j) == len(arr)):
                        break
                else:
                    # Check for smudges, fix, and restart
                    if not smudged and (np.count_nonzero(check_arr == False) == 1):
                        smudged = True
                        matched += 1
                        j += 1
                        # Reached top of the list
                        if j > row or ((row + 1 + j) == len(arr)):
                            break
                        
                        continue

                    if matched != 0:
                        row_impossible = True
                    break

            if row_impossible or (matched == 0) or not smudged:
                continue

            s += 100 * (row + 1)
            reflection_found = True
            break
    return s

print(part1())
print(part2())
