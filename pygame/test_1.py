import os
import pygame
from random import choice, randint

CELL_BG = (255, 255, 255)
SCREEN_BG = (0, 0, 0)


class Game:
    def __init__(self, screen, is_silent=False) -> None:
        self.game = 1
        self.player_1 = Player(image='x', is_auto=False)
        self.player_2 = Player(image='o', is_auto=False, is_center=True, is_predict=True)
        self.field = Field(screen)
        self.winner = None
        self.is_silent = is_silent
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.cell_size = min((self.screen.get_size())) / 3
        self.shift_x = (screen_width - 3 * self.cell_size) // 2
        self.shift_y = (screen_height - 3 * self.cell_size) // 2

    def get_winner(self) -> str:
        #  горизонтали
        for i in range(0, 7, 3):
            if self.field.cells[i] == self.field.cells[i+1] == self.field.cells[i+2]:
                return self.field.cells[i]
        #  вертикали
        for i in range(3):
            if self.field.cells[i] == self.field.cells[i+3] == self.field.cells[i+6]:
                return self.field.cells[i]
        #  диагонали
        if self.field.cells[0] == self.field.cells[4] == self.field.cells[8]:
            return self.field.cells[0]
        if self.field.cells[2] == self.field.cells[4] == self.field.cells[6]:
            return self.field.cells[2]

        return ''

    def run(self):  # счеттик ходов, на 10 выход
        self.screen.fill((0, 0, 0))
        self.field.draw(self.shift_x, self.shift_y)
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    y -= self.shift_y
                    x -= self.shift_x
                    idx_x = x // self.cell_size
                    idx_y = y // self.cell_size
                    print(idx_x, idx_y)
                    idx = self.field.cols * idx_y + idx_x
                    print(idx)
                    center_x = self.shift_x + self.cell_size // 2 + idx * self.cell_size // 4
                    center_y = self.shift_y + self.cell_size // 2 + idx * self.cell_size // 4
                    font = pygame.font.Font(None, self.cell_size)
                    font_surf = font.render('X', True, (255, 0, 0))
                    self.screen.blit(font_surf, (center_x, center_y))

            '''
            if not self.is_silent:
                self.field.draw()
            if turn > 8:
                if not self.is_silent:
                    print('игра окончена - ничья')
                    self.game == 0
                break
            elif turn % 2:
                self.player_2.make_turn(self.field)
            else:
                self.player_1.make_turn(self.field)
            turn += 1

            self.winner = self.get_winner()
            if self.winner:
                if not self.is_silent:
                    self.field.draw()
                    print(f'{self.winner} победил')
                self.game = 0
            '''
            pygame.display.flip()
        pygame.quit()
        #  self.restart()

    def restart(self):
        print()
        print('начать новую игру?')
        while True:
            choice = input()
            if choice == 'да':
                self.game = 1
                App()
            elif choice == 'нет':
                exit()
            os.system('cls')
            print('введите "да" или "нет"')


class Field:
    def __init__(self, screen) -> None:
        self.cells = [i for i in range(1, 9)]
        self.empty_cells = []
        self.screen = screen
        self.cell_size = min((self.screen.get_size())) // 3
        self.rows = 3
        self.cols = 3
        self.width = 3
        self.heigth = 3

    def draw(self, shift_x, shift_y):
        x0 = 0
        y0 = 0
        for i in self.cells:
            pygame.draw.rect(self.screen,
                             (randint(0, 255), randint(0, 255), randint(0, 255)),
                             pygame.Rect(
                                        (x0 + self.cell_size * i) % 300 + shift_x, (y0 + i // 3) * self.cell_size + shift_y, self.cell_size, self.cell_size
                                        ))

        '''
        os.system('cls')
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])
        '''
    def get_empty_cells(self):
        for cell in self.cells:
            if not isinstance(cell, int):
                continue
            self.empty_cells.append(cell)


class App:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        game = Game(self.screen, is_silent=False)
        game.run()
        '''
        self.stat = [0, 0, 0]  # x o ничья
        for i in range(1000):
            self.game = Game(is_silent=True)
            self.game.run()

            if self.game.winner == 'x':
                self.stat[0] += 1
            elif self.game.winner == 'o':
                self.stat[1] += 1
            else:
                self.stat[2] += 1
        print(*self.stat)
        '''

class Player:
    def __init__(self, is_auto=False, image=None, is_center=False, is_predict=False) -> None:
        self.is_auto = is_auto
        self.image = image
        self.is_center = is_center
        self.is_predict = is_predict

    def make_turn(self, field):
        if not self.is_auto:
            while True:
                try:
                    cell_number = int(input(f'номер клетки для хода {self.image}: '))
                except ValueError:
                    print('номер клетки должен быть целым положительным числом')
                    continue
                if cell_number > 9 or cell_number < 1:
                    print('номер клетки должен быть целым числом от 1 до 9')
                    continue
                idx = cell_number - 1
                if not isinstance(field.cells[idx], int):
                    print('выберите номер пустой клетки')
                break
            field.cells[cell_number - 1] = self.image

        else:
            empty_cells = []
            for i in range(9):
                if not isinstance(field.cells[i], int):
                    continue
                empty_cells.append(i)
            if self.is_center and 4 in empty_cells:
                field.cells[4] = self.image
                return
            if self.is_predict:
                for idx in empty_cells:
                    '''
                    сделать ход
                    проверить победу
                    если победа - закончить функцию
                    если не побуда - отменить ход и взять след. индекс
                    '''
                    field.cells[idx] = self.image
                    if Game.get_winner() == '':
                        field.cells[idx] = idx + 1
                        continue

            random_idx = choice(empty_cells)
            field.cells[random_idx] = self.image


app = App()
