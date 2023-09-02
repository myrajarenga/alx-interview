#!/usr/bin/python3

"""
Island Perimeter
"""


def island_perimeter(grid):
    if not grid:
        return 0

    def dfs(x, y):
        # Base cases for the DFS recursion
        if x < 0 or x >= len(grid) or y < 0 or y >= \
                len(grid[0]) or grid[x][y] == 0:
            return 1
        # Count the perimeter if we're at the boundary or next to water

        if grid[x][y] == -1:
            return 0  # Skip visited cells

        grid[x][y] = -1  # Mark the cell as visited
        perimeter = 0

        # Explore adjacent cells
        perimeter += dfs(x - 1, y)  # Up
        perimeter += dfs(x + 1, y)  # Down
        perimeter += dfs(x, y - 1)  # Left
        perimeter += dfs(x, y + 1)  # Right

        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Start DFS from the first land cell you encounter
                return dfs(i, j)

    return 0  # If there's no island in the grid
