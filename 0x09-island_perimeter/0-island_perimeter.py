#!/usr/bin/python3

"""Function to find perimeter of an island"""

def island_perimeter(grid):
    """calculates the perimeter of an island in a grid"""
    perimeter = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for r in range(len(grid)):
        for c in range(len(grid[i])):
            index = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
            check = [r if m[0] in range(row) and m[1] in range(col
                for m in index]

            if grid[r][c]:
                perimeter += sum([1 if not n or not grid[m[0]][m[1]] e
                    for n, m in zip(check, index])

    return (perimeter)
