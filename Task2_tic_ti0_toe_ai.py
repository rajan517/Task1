import random

# Constants
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal 1
        [board[0][2], board[1][1], board[2][0]]  # Diagonal 2
    ]
    return [player, player, player] in win_conditions


def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]


def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -10
    elif check_winner(board, PLAYER_O):
        return 10
    elif not get_empty_positions(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_positions(board):
            board[i][j] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_positions(board):
            board[i][j] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -float('inf')
    move = None
    for i, j in get_empty_positions(board):
        board[i][j] = PLAYER_O
        score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                if board[x][y] == EMPTY:
                    board[x][y] = PLAYER_X
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column numbers between 0 and 2.")

        if check_winner(board, PLAYER_X):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif not get_empty_positions(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI move
        i, j = best_move(board)
        board[i][j] = PLAYER_O
        print(f"AI moves to ({i}, {j})")
        print_board(board)

        if check_winner(board, PLAYER_O):
            print("AI wins!")
            break
        elif not get_empty_positions(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
    