import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Functions to draw the grid lines
def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                          int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

# Check for win
def check_winner(bd, player):
    # Check rows
    for row in bd:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all([bd[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Check diagonals
    if all([bd[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([bd[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Check for draw
def is_full(bd):
    for row in bd:
        if '' in row:
            return False
    return True

# Minimax algorithm with alpha-beta pruning
def minimax(bd, depth, is_maximizing, alpha, beta):
    if check_winner(bd, 'X'):
        return 1
    elif check_winner(bd, 'O'):
        return -1
    elif is_full(bd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if bd[i][j] == '':
                    bd[i][j] = 'X'
                    eval = minimax(bd, depth + 1, False, alpha, beta)
                    bd[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if bd[i][j] == '':
                    bd[i][j] = 'O'
                    eval = minimax(bd, depth + 1, True, alpha, beta)
                    bd[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Determine best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == '':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def main():
    draw_lines()
    player_turn = True
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if player_turn:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)

                    if board[clicked_row][clicked_col] == '':
                        board[clicked_row][clicked_col] = 'O'
                        if check_winner(board, 'O'):
                            game_over = True
                        player_turn = False
                        draw_figures()

        if not player_turn and not game_over:
            pygame.time.wait(500)
            move = best_move()
            if move:
                board[move[0]][move[1]] = 'X'
                if check_winner(board, 'X'):
                    game_over = True
                player_turn = True
                draw_figures()

        pygame.display.update()

main()