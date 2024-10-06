#!/usr/bin/python3
"""Solves the pascal triangle Problem"""


def pascal_triangle(n):
    """ return an empty list if """
    if n <= 0:
        return []

    """INITIALIZE the first row in the triangle"""
    triangle = [[1]]

    """build the triangle row by row"""
    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
