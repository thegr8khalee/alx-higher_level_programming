#!/usr/bin/python3
"""
N-Queens Problem Solver

This program solves the N-Queens problem and prints all possible solutions.
"""

import sys

def is_safe(board, row, col, N):
    # Check the column on this row
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N):
    if row == N:
        print_solution(board, N)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N)
            board[row][col] = 0

def print_solution(board, N):
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append((i, j))
    print(solution)

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Check if the argument is a valid positive integer
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(sys.argv[1])
    
    # Ensure N is at least 4 for meaningful solutions
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the chessboard
    chessboard = [[0 for _ in range(N)] for _ in range(N)]
    
    # Solve and print N-Queens solutions
    solve_nqueens_util(chessboard, 0, N)
