from input_manager import get_input

input = get_input(__file__)

# List of tuples of tuples?, contains current position and direction
# ( (x, y), (dx, dy) )
beams: list[tuple[tuple[int, int], tuple[int, int]]] = [
    ((-1, 0), (1, 0)),
]

energized: set[tuple[int, int]] = {(0, 0)}
states: set[tuple[tuple[int, int], tuple[int, int]]] = set()

while len(beams) != 0:
    beam = beams.pop(0)
    (x, y), (dx, dy) = beam

    while True:
        # Check if we've seen this state before, in which case the beam already energized the points
        if ((x, y), (dx, dy)) in states:
            break

        new_x, new_y = (x + dx, y + dy)

        # Check if we run into a wall
        # Stop if we do and move into the next
        if (
            (new_x < 0)
            or (new_y < 0)
            or (new_x >= len(input[0]))
            or (new_y >= len(input))
        ):
            break

        energized.add((new_x, new_y))
        next_tile = input[new_y][new_x]

        states.add(((x, y), (dx, dy)))

        match next_tile:
            case ".":
                # Empty space, just move beam ahead
                x, y = new_x, new_y
                continue
            case "\\":
                # There's 4 cases for this one :)
                x, y = new_x, new_y

                # If we're moving horizontally,
                if dx != 0:
                    # We're moving right
                    if dx == 1:
                        dx, dy = 0, 1
                    # We're moving left
                    else:
                        dx, dy = 0, -1
                else:
                    # We're moving down
                    if dy == 1:
                        dx, dy = 1, 0
                    # We're moving up
                    else:
                        dx, dy = -1, 0
                continue
            case "/":
                # Another 4 cases ugh :)
                x, y = new_x, new_y

                # If we're moving horizontally,
                if dx != 0:
                    # We're moving right
                    if dx == 1:
                        dx, dy = 0, -1
                    # We're moving left
                    else:
                        dx, dy = 0, 1
                else:
                    # We're moving down
                    if dy == 1:
                        dx, dy = -1, 0
                    # We're moving up
                    else:
                        dx, dy = 1, 0
                continue
            case "|":
                # Check which end we hit
                # This means we hit it in the side, split into two
                if dx != 0:
                    beams.append(((new_x, new_y), (0, -1)))
                    beams.append(((new_x, new_y), (0, 1)))
                    break
                # Else just pass through as if it was empty space
                else:
                    x, y = new_x, new_y
            case "-":
                # Check which end we hit
                # This means we hit it in the side, split into two
                if dy != 0:
                    beams.append(((new_x, new_y), (-1, 0)))
                    beams.append(((new_x, new_y), (1, 0)))
                    break
                # Else just pass through as if it was empty space
                else:
                    x, y = new_x, new_y

print(len(energized))
