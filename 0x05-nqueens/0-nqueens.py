#!/usr/bin/python3
"""
    program that solves the N queens problem.
"""


def solve_n_queens(n):
    """
        magic method
    """
    def can_place_queen(row, col):
        """
            Check if a queen can be placed on board[row][col]
        # Check left upper diagonal
        """
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False
        # Check left lower diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j]:
                return False
        return True

    def solve(row):
        """
            checking the row
        """
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if can_place_queen(row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    solve(0)
    return result
