def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check column for any Queen
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check the left upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check the right upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"  # Place Queen
            if solve_n_queens(board, row + 1, n):
                return True  # Solution found

            board[row][col] = "."  # Backtrack

    return False

def n_queens_with_first_queen_placed(n):
    # Initialize the board
    board = [["."] * n for _ in range(n)]
    board[0][0] = "Q"  # Place the first Queen at (0,0)

    if not solve_n_queens(board, 1, n):  # Start from the second row
        print("No solution exists")
    else:
        print("Solution found with the first Queen at (0,0):")

if __name__ == "__main__":
    n = 8
    n_queens_with_first_queen_placed(n)
