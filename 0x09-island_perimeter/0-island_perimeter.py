#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check the four neighboring cells
                up = row - 1
                down = row + 1
                left = col - 1
                right = col + 1

                # Initialize edge count
                edges = 0

                # Check up
                if up < 0 or grid[up][col] == 0:
                    edges += 1

                # Check down
                if down >= rows or grid[down][col] == 0:
                    edges += 1

                # Check left
                if left < 0 or grid[row][left] == 0:
                    edges += 1

                # Check right
                if right >= cols or grid[row][right] == 0:
                    edges += 1

                perimeter += edges

    return perimeter
