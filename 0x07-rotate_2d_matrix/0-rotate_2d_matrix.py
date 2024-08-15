#!/usr/bin/python3
"""module to rotate a 2-D matrix"""


def rotate_2d_matrix(matrix):
    """A function to implement 2-D matrix rotation"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        matrix.reverse()