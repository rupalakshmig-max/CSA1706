N = 4

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)]:
            return False

        if col + (row - i) < N and board[i][col + (row - i)]:
            return False

    return True

def solve(board, row):
    if row == N:
        print_board(board)
        print()
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

board = [[0] * N for _ in range(N)]
solve(board, 0)
