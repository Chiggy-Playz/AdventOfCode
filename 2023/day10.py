from input_manager import get_input
import math
input = get_input(__file__)

# Pipe: [ ends (x, y) ]
pipe_ends = {
    "|": ((0, -1), (0, +1)),  # Up and Down
    "-": ((-1, 0), (+1, 0)),  # Left and Right
    "L": ((0, -1), (+1, 0)),  # Up and Right
    "J": ((0, -1), (-1, 0)),  # Up and Left
    "7": ((0, +1), (-1, 0)),  # Down and Left
    "F": ((0, +1), (+1, 0)),  # Down and Right,
    "S": ((0, -1), (+1, 0), (0, +1), (-1, 0)),  # Up right down left
}


def part1() -> list[tuple[int, int]]:
    for y, row in enumerate(input):
        for x, pipe in enumerate(row):
            if pipe != "S":
                continue
            # I could figure out what S is but im running short on time :)
            input[y] = input[y].replace("S", "-")
            loop = [(x, y)]
            current_pipe = pipe

            # Current pipe's x and y
            cx, cy = (x, y)
            # A pipe found, try to find loop
            while True:
                next_pipe = None
                for delta_x, delta_y in pipe_ends[current_pipe]:
                    try:
                        new_x, new_y = cx + delta_x, cy + delta_y

                        # Prevent wrapping around
                        if (new_y < 0) or (new_x < 0):
                            raise IndexError()

                        # If the new point is where we are coming from, skip
                        if (len(loop) > 1) and (new_x, new_y) == loop[-2]:
                            continue

                        # Check if we're back at the starting position
                        if (new_x, new_y) == (x, y):
                            loop.append((new_x, new_y))
                            next_pipe = None
                            break

                        # Check if neighbour pipe exists
                        next_pipe = input[new_y][new_x]

                        if next_pipe == ".":
                            next_pipe = None
                            continue

                        # Check  if the neighbour pipe actually connects
                        if (cx, cy) not in [
                            (new_x + dx, new_y + dy) for dx, dy in pipe_ends[next_pipe]
                        ]:
                            next_pipe = None
                            continue

                        # This means the pipes connects, add to loop and continue searching from this pipe
                        loop.append((new_x, new_y))
                        cx, cy = new_x, new_y
                        current_pipe = next_pipe
                        break
                    except IndexError:
                        continue

                # A pipe was found in the loop, keep on looking
                if next_pipe != None:
                    continue
                break
            # Loop finished
            # There has to be at least 4 pipes for a closed loop
            if (len(loop) > 3) and (loop[0] == loop[-1]):
                return loop[:-1]
    raise Exception("Oops")


def part2(loop: list[tuple[int, int]]):
    min_x = min_y = float("inf")
    max_x = max_y = 0
    for x, y in loop:
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    inside = 0

    for y in range(int(min_y), max_y+1):
        for x in range(int(min_x), max_x+1):
            
            if (x,y) in loop:
                continue
            
            # Go towards the right edge
            interior = "|LJ"
            exterior = "|F7"

            in_count = 0
            ex_count = 0
            for i in range(x+1, max_x+1):
                if (i, y) not in loop:
                    continue
                if input[y][i] in interior:
                    in_count += 1
                if input[y][i] in exterior:
                    ex_count += 1

            inside += ( (in_count % 2) == 1 ) and ( (  ex_count % 2  ) == 1 )
    return inside


loop = part1()
print(math.ceil((len(loop) - 1) / 2))
print(part2(loop))


