#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# if __name__ == "__main__":
#     matrix = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]

#     rotate_2d_matrix(matrix)
#     print(matrix)
