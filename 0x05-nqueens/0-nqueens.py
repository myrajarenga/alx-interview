#!/usr/bin/python3
"""
N Queens placement on NxN chessboard
"""


import sys


def generate_solutions(row, column):
    """
    Generate solutions for N-Queens problem using backtracking.

    :param row: The current row to place the queen.
    :param column: The size of the chessboard (N).
    :return: A list of valid solutions.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place a queen on the chessboard and filter valid positions.

    :param queen: The row index to place the queen.
    :param column: The size of the chessboard (N).
    :param prev_solution: List of previously placed queens' positions.
    :return: List of valid positions for the next queen placement.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if it's safe to place a queen at position (q, x).

    :param q: The row index to place the queen.
    :param x: The column index to place the queen.
    :param array: List of previously placed queens' positions.
    :return: True if safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initialize the N value from the command-line argument.

    :return: The value of N.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """
    Solve and print N-Queens problem for the given N.
    """
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = [[q, x] for q, x in enumerate(array)]
        print(clean)


if __name__ == '__main__':
    n_queens()
