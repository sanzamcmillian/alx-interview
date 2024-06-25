#!/usr/bin/python3
"""The Pascal's Triangle"""


def pascal_triangle(n):
    """function to generate the pascal's triangle
       Arg:
           n(int): number of rows of the triangle
    """
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return (triangle)
