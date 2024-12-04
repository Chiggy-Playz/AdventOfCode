def traverseInAllDir(matrix: list[list[str]]):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            # Filter condition
            if col != "X":
                continue

            # Traversing in all diagnols
            # Top right, top left, bottom right, bottom left, right, left, up, down
            dirs = [(-1, 1), (-1, -1), (1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in dirs:
                # Calculate new dir pos
                dy, dx = map(sum, zip((i, j), dir))
                while 0 <= dy < len(matrix) and 0 <= dx < len(matrix):
                    # Computation and check
                    
                    # Add dir again
                    dy, dx = map(sum, zip((dy, dx), dir))