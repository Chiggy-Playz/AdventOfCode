from input_manager import get_input

input = get_input(__file__)

m = 0
for row in range(len(input)):
    for col in range(len(input[0])):
        # Only keep edge points
        if not (
            (row == 0)
            or (col == 0)
            or (row == (len(input) - 1))
            or (col == (len(input[0]) - 1))
        ):
            continue

        # List of tuples of tuples?, contains current position and direction
        # ( (x, y), (dx, dy) )

        beams: list[tuple[tuple[int, int], tuple[int, int]]] = [
            # ((-1, 0), (1, 0)),
        ]

        # If corner, add 2 starting beams
        starting_point = (col, row)
        if starting_point in (
            (0, 0),
            (len(input[0]) - 1, 0),
            (len(input[0]) - 1, len(input) - 1),
            (0, len(input) - 1),
        ):
            dx1 = 1 if col == 0 else -1
            dx2 = 0

            dy1 = 1 if row == 0 else -1
            dy2 = 0

            beams.append((starting_point, (dx1, dy1)))
            beams.append((starting_point, (dx2, dy2)))
        else:
            dx = 0 if col not in (0, len(input[0]) - 1) else (1 if col == 0 else -1)
            dy = 0 if row not in (0, len(input)-1) else (1 if row == 0 else -1)
            beams.append((starting_point, (dx, dy)))

        energized: set[tuple[int, int]] = {starting_point}
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

        m = max(m, len(energized))

print(m)