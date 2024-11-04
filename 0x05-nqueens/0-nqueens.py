#!/usr/bin/python3
"""N Queens Problem Solver"""
import sys


def print_board(board, n):
    """Print the board with queens' positions"""
    b = []

    for i in range(n):
        b.append([i, board[i]])
    print(b)


def is_position_safe(board, row, col):
    """Check if the position is safe for the queen"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """Recursively find all safe positions for queens"""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if is_position_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1, n)


def create_board(size):
    """Create an empty board"""
    return [-1] * size


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = create_board(n)
solve_nqueens(board, 0, n)
