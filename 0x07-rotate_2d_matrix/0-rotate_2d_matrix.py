#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate the  matrix in place"""
    n = len(matrix
    )
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
