import pygame
import sys
import copy

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (124, 252, 0)

# Pygame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess - User vs AI")

# Load images
PIECES = {}
def load_images():
    pieces = ['wp','wr','wn','wb','wq','wk','bp','br','bn','bb','bq','bk']
    for piece in pieces:
        PIECES[piece] = pygame.transform.scale(pygame.image.load(f"assets/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))

# Board setup
def create_board():
    board = [
        ['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp'] * 8,
        [''] * 8,
        [''] * 8,
        [''] * 8,
        [''] * 8,
        ['wp'] * 8,
        ['wr','wn','wb','wq','wk','wb','wn','wr']
    ]
    return board

def draw_board(win, board, selected):
    colors = [WHITE, GREY]
    for row in range(ROWS):
        for col in range(COLS):
            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if selected and (row, col) == selected:
                pygame.draw.rect(win, GREEN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != '':
                win.blit(PIECES[piece], (col*SQUARE_SIZE, row*SQUARE_SIZE))

def get_valid_moves(board, row, col):
    piece = board[row][col]
    moves = []
    if piece == '':
        return moves

    color = piece[0]
    type_ = piece[1]

    directions = {
        'p': [(-1, 0), (-2, 0), (-1, -1), (-1, 1)] if color == 'w' else [(1, 0), (2, 0), (1, -1), (1, 1)],
        'r': [(1,0), (-1,0), (0,1), (0,-1)],
        'b': [(1,1), (1,-1), (-1,1), (-1,-1)],
        'q': [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)],
        'k': [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)],
        'n': [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    }

    if type_ == 'p':
        for dr, dc in directions['p']:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if dc == 0:
                    if board[r][c] == '':
                        if abs(dr) == 2 and ((row == 6 and color == 'w') or (row == 1 and color == 'b')):
                            if board[row + dr//2][col] == '':
                                moves.append((r, c))
                        elif abs(dr) == 1:
                            moves.append((r, c))
                else:
                    if board[r][c] != '' and board[r][c][0] != color:
                        moves.append((r, c))

    elif type_ in ['r','b','q']:
        for dr, dc in directions[type_]:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '':
                    moves.append((r, c))
                elif board[r][c][0] != color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc

    elif type_ == 'k' or type_ == 'n':
        for dr, dc in directions[type_]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '' or board[r][c][0] != color:
                    moves.append((r, c))

    return moves

def evaluate_board(board):
    values = {'p':1,'n':3,'b':3,'r':5,'q':9,'k':0}
    score = 0
    for row in board:
        for piece in row:
            if piece:
                val = values[piece[1]]
                score += val if piece[0]=='w' else -val
    return score

def get_all_moves(board, color):
    moves = []
    for row in range(8):
        for col in range(8):
            if board[row][col].startswith(color):
                piece_moves = get_valid_moves(board, row, col)
                for r, c in piece_moves:
                    temp_board = copy.deepcopy(board)
                    temp_board[r][c] = temp_board[row][col]
                    temp_board[row][col] = ''
                    moves.append((temp_board, (row, col, r, c)))
    return moves

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate_board(board), None

    all_moves = get_all_moves(board, 'b' if maximizing else 'w')

    if maximizing:
        max_eval = float('-inf')
        best_move = None
        for move_board, move in all_moves:
            eval = minimax(move_board, depth-1, alpha, beta, False)[0]
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move_board, move in all_moves:
            eval = minimax(move_board, depth-1, alpha, beta, True)[0]
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def main():
    load_images()
    board = create_board()
    run = True
    selected = None
    valid_moves = []
    player_turn = True

    while run:
        draw_board(WIN, board, selected)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                if selected:
                    if (row, col) in valid_moves:
                        board[row][col] = board[selected[0]][selected[1]]
                        board[selected[0]][selected[1]] = ''
                        player_turn = False
                    selected = None
                    valid_moves = []
                else:
                    if board[row][col].startswith('w'):
                        selected = (row, col)
                        valid_moves = get_valid_moves(board, row, col)

        if not player_turn:
            _, move = minimax(board, 2, float('-inf'), float('inf'), True)
            if move:
                sr, sc, er, ec = move
                board[er][ec] = board[sr][sc]
                board[sr][sc] = ''
            player_turn = True

if __name__ == "__main__":
    main()
