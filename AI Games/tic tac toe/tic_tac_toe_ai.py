import math

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_combos = [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]
    return any(board[i] == board[j] == board[k] == player for i,j,k in win_combos)

def is_draw(board):
    return ' ' not in board

def minimax(board, is_max):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                val = minimax(board, False)
                board[i] = ' '
                best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                val = minimax(board, True)
                board[i] = ' '
                best = min(best, val)
        return best

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main Game
board = [' '] * 9
while True:
    print_board(board)
    user = int(input("Enter position (0-8): "))
    if board[user] != ' ':
        print("Invalid move!")
        continue
    board[user] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break
    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    ai = best_move(board)
    board[ai] = 'O'
    if check_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break
