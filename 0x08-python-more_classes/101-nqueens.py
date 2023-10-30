#!/usr/bin/python3
"""
N-Queens Backtracking Algorithm

This program finds and prints all solutions to the N-Queens problem.
The N-Queens problem is to place N queens on an NxN chessboard such that
no two queens attack each other. The solutions are printed in the form of
coordinates (row, column) of queens on the board.
"""

from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    # Check if the argument is a valid positive integer
    if not argv[1].isdigit():
        print("N must be a positive integer")
        exit(1)
    
    n = int(argv[1])
    
    # Ensure N is at least 4 for meaningful solutions
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the answer list
    queens_positions = []
    for i in range(n):
        queens_positions.append([i, None])

    def already_exists(y):
        """Check if a queen already exists in the given y position"""
        for x in range(n):
            if y == queens_positions[x][1]:
                return True
        return False

    def reject(x, y):
        """Determine whether to reject the solution"""
        if already_exists(y):
            return False
        i = 0
        while i < x:
            if abs(queens_positions[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_queens_positions(x):
        """Clear queens' positions from the point of failure onwards"""
        for i in range(x, n):
            queens_positions[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find solutions"""
        for y in range(n):
            clear_queens_positions(x)
            if reject(x, y):
                queens_positions[x][1] = y
                if x == n - 1:  # Solution found, print the coordinates
                    print([(pos[0], pos[1]) for pos in queens_positions])
                else:
                    nqueens(x + 1)  # Move on to the next queen position

    # Start the recursive process with the first queen
    nqueens(0)
