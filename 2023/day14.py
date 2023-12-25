from input_manager import get_input
from time import monotonic

def solution(part1: bool) -> int:
    input = get_input(__file__)

    rows, cols = len(input), len(input[0])
    dish = [list(i) for i in input]

    cycles = 1000000000 if not part1 else 1
    seen = []

    for cycle in range(cycles):
        for dir in ("NWSE"):

            if dir in "NS":
                outers = cols
                inners = rows
            elif dir in "EW":
                outers = rows
                inners = cols
            else:
                raise Exception()

            # Reverse the array
            if dir == "S":
                dish = dish[::-1]
            if dir == "E":
                dish = [l[::-1] for l in dish]

            for outer in range(outers):
                for inner in range(inners):
                    row = inner if dir in "NS" else outer
                    col = inner if dir not in "NS" else outer
                    current = dish[row][col]

                    if current != "O":
                        continue

                    axis = row if dir in "NS" else col
                    sign = -1
                    limit = (rows if dir in "NS" else col) - 1

                    i = 1
                    while 0 <= (axis + (sign * i)) <= limit:
                        above = (
                            dish[row + (sign * i)][col]
                            if dir in "NS"
                            else dish[row][col + (sign * i)]
                        )

                        # If above is # or O, then we cant move up
                        if above in "#O":
                            break

                        # Swap
                        if dir in "NS":
                            (
                                dish[row + (sign * i)][col],
                                dish[(row + (sign * i)) - sign][col],
                            ) = (
                                dish[(row + (sign * i)) - sign][col],
                                dish[row + (sign * i)][col],
                            )
                        else:
                            (
                                dish[row][col + (sign * i)],
                                dish[row][(col + (sign * i)) - sign],
                            ) = (
                                dish[row][(col + (sign * i)) - sign],
                                dish[row][col + (sign * i)],
                            )
                        i += 1
            
            # Reverse the array
            if dir == "S":
                dish = dish[::-1]
            if dir == "E":
                dish = [l[::-1] for l in dish]

            if part1:
                break
    
        stringDish = "\n".join("".join(l) for l in dish)

        if stringDish in seen:
            seenIndex = seen.index(stringDish)
            loopIndex = ((cycles - seenIndex) % (len(seen) - seenIndex)) - 1
            dish = [list(l) for l in seen[seenIndex:][loopIndex].split("\n")]
            break
        else:
            seen.append(stringDish)

    s = 0

    # Loop
    for col in range(cols):
        for row in range(rows):
            if dish[row][col] != "O":
                continue
            s += rows - row


    return s

start = monotonic()
print(solution(True))
print(solution(False))
print(monotonic() - start)