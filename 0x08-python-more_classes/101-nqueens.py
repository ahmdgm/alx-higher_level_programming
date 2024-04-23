#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
        elif board[i] - i == col - row:
            return False
        elif board[i] + i == col + row:
            return False
    return True


def solve_util(board, row, n, solutions):
    if n == row:
        solutions.append([[i, board[i]] for i in range(len(board))])
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_util(board, row + 1, n, solutions)
            board[row] = -1


def solve(n):
    board = [-1] * n
    solutions = []
    solve_util(board, 0, n, solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(int(sys.argv[1]))
