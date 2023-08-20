#!/usr/bin/python3
"""_summary_
"""


def transpose_matrix(matrix, n):
    """_summary_

    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """_summary_

    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """_summary_

    """
    n = len(matrix)
    # print(n)

    """sample matrix
    1 2 3
    4 5 6
    7 8 9
    """

    # When you transpose matrix you grt this
    """
    1 4 7
    2 5 8
    3 6 9
    """

    transpose_matrix(matrix, n)

    # When you reverse matrix you get this
    """
    7 4 1
    8 5 2
    9 6 3
    """
    reverse_matrix(matrix)

    return matrix
