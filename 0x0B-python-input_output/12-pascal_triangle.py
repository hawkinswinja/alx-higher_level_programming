#!/usr/bin/python3
"""pascal_triangle module
   contains a single function that returns the pascal triangle
"""


def pascal_triangle(n):
    """function to create a list representation of pascal triangle"""
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
            continue
        if i == 1:
            triangle.append([1, 1])
            continue
        prev = triangle[i - 1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i] + prev[i - 1])
        row.append(1)
        triangle.append(row)
    return triangle
