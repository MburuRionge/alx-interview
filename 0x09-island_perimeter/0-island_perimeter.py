#!/usr/bin/python3

"""Function to find perimeter of an island"""

def island_perimeter(grid):
    """Calculates the perimeter of an island in a grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Only process land cells
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check for adjacent land cells and subtract 1 for each shared edge
                if r > 0 and grid[r - 1][c] == 1:  # Land above
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Land below
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Land to the left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Land to the right
                    perimeter -= 1

    return perimeter
