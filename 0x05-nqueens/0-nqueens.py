#!/usr/bin/env python3
"""N queens"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col, n):
    """Utility function to solve N Queen problem"""
    list = []
    if col == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    list.append([i, j])
        print(list)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solveNQUtil(board, col + 1, n)
            board[i][col] = 0


def init():
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
    return (n)


def nqueens():
    """N queens problem"""

    n = init()
    board = [[0 for j in range(n)] for i in range(n)]
    solveNQUtil(board, 0, n)


if __name__ == "__main__":
    nqueens()
