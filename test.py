import os
from random import choice


class Game:
    def __init__(self) -> None:
        self.game = 1
        self.player_1 = Player(image='x', is_auto=True)
        self.player_2 = Player(image='o', is_auto=True)
        self.field = Field()

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
        turn = 0

        while self.game:
            self.field.draw()
            if turn > 8:
                print('игра окончена - ничья')
                self.game == 0
                break
            elif turn % 2:
                self.player_2.make_turn(self.field)
            else:
                self.player_1.make_turn(self.field)
            turn += 1

            winner = self.get_winner()
            if winner:
                self.field.draw()
                print(f'{winner} победил')
                self.game = 0
        self.restart()

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
    def __init__(self) -> None:
        self.cells = [i for i in range(1, 10)]
        self.empty_cells = []

    def draw(self):
        os.system('cls')
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])

    def get_empty_cells(self):
        for cell in self.cells:
            if not isinstance(cell, int):
                continue
            self.empty_cells.append(cell)


class App:
    def __init__(self) -> None:
        self.game = Game()
        self.game.run()


class Cell:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(self, is_auto=False, image=None) -> None:
        self.is_auto = is_auto
        self.image = image

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
            random_idx = choice(empty_cells)
            field.cells[random_idx] = self.image


App()
