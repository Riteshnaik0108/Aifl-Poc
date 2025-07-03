import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    # Rows, Columns, Diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col from 1 to 3): ").split())
            row -= 1
            col -= 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already taken.")
            else:
                print("Invalid input. Enter row and column between 1 and 3.")
        except ValueError:
            print("Enter valid numbers (e.g. 1 2)")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            break

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are 'X', computer is 'O'")
    print_board(board)

    while True:
        # Player move
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer move
        print("Computer's turn...")
        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
