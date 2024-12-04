from utils.input_manager import get_input

lines = get_input(__file__)

part1 = 0

# Find all the x's then search in all directions
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col != "X":
            continue

        # We have found X. Continue searching diagnols
        # Top right, top left, bottom right, bottom left, right, left, up, down
        dirs = [(-1, 1), (-1, -1), (1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        soln = "XMAS"
        for dir in dirs:
            s = "X"
            dy, dx = map(sum, zip((i, j), dir))
            while 0 <= dy < len(lines) and 0 <= dx < len(lines):
                news = s + lines[dy][dx]
                if news not in soln:
                    break

                if news == soln:
                    part1 += 1
                    break

                s = news
                # Add dirn again
                dy, dx = map(sum, zip((dy, dx), dir))

print(part1)

part2 = 0
# Find all the a's
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col != "A" or i in (0, len(lines) - 1) or j in (0, len(lines) - 1):
            continue
        # Now simply get the 2 diagnols accross it
        d1 = lines[i - 1][j - 1] + "A" + lines[i + 1][j + 1]
        d2 = lines[i - 1][j + 1] + "A" + lines[i + 1][j - 1]
        if d1 in ("SAM", "MAS") and d2 in ("SAM", "MAS"):
            part2 += 1

print(part2)
