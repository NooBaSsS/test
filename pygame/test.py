import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
screen.fill(BG_COLOR)

# Создание игровой доски
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Рисование сетки
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Рисование фигур на доске
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, 2)

# Проверка победителя
def check_winner():
    # Проверка строк
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]

    # Проверка столбцов
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None

# Отрисовка доски
def draw_board():
    draw_grid()
    draw_figures()

# Очистка доски и экрана
def reset_game():
    screen.fill(BG_COLOR)
    draw_board()
    pygame.display.update()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''

# Основной игровой цикл
def main():
    draw_board()
    running = True
    currentPlayer = 'X'
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = currentPlayer
                    if currentPlayer == 'X':
                        currentPlayer = 'O'
                    else:
                        currentPlayer = 'X'
                    draw_board()
                    winner = check_winner()
                    if winner:
                        game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

        pygame.display.update()

if __name__ == "__main__":
    main()
