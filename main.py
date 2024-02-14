import os


COLS = 3
ROWS = 3


class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.content = '.'


class Field():
    def __init__(self):
        self.game = 1
        self.cols = COLS
        self.rows = ROWS
        self.cells = [
            [Cell(x, y) for x in range(self.cols)] for y in range(self.rows)
        ]

    def draw(self):
        for row in self.cells:
            for cell in row:
                print(cell.content, end='')
            print()

    def turn_x(self):
        os.system('cls')
        print('ход "x"')
        self.draw()
        self.c_x = input('строка: ')
        try:
            self.c_x = int(self.c_x)
        except ValueError:
            print(f'строка должна быть числом от 1 до {ROWS}')
            self.turn_x()

        if self.c_x > ROWS or self.c_x <= 0:
            print(f'строка должна быть числом от 1 до {ROWS}')
            self.turn_x()

        self.c_y = input('ряд: ')
        try:
            self.c_y = int(self.c_y)
        except ValueError:
            print(f'строка должна быть числом от 1 до {COLS}')
            self.turn_x()

        if self.c_y > COLS or self.c_y <= 0:
            print(f'строка должна быть числом от 1 до {COLS}')
            self.turn_x()

        if self.cells[self.c_x - 1][self.c_y - 1].content == '.':
            self.cells[self.c_x - 1][self.c_y - 1].content = 'x'
        else:
            print('клетка должна быть пустой')

    def turn_o(self):
        os.system('cls')
        print('ход "o"')
        self.draw()
        self.c_x = input('строка: ')
        try:
            self.c_x = int(self.c_x)
        except ValueError:
            print(f'строка должна быть числом от 1 до {ROWS}')
            self.turn_o()

        if self.c_x > ROWS or self.c_x <= 0:
            print(f'строка должна быть числом от 1 до {ROWS}')
            self.turn_o()

        self.c_y = input('ряд: ')
        try:
            self.c_y = int(self.c_y)
        except ValueError:
            print(f'строка должна быть числом от 1 до {COLS}')
            self.turn_o()

        if self.c_y > COLS or self.c_y <= 0:
            print(f'строка должна быть числом от 1 до {COLS}')
            self.turn_o()

        if self.cells[self.c_x - 1][self.c_y - 1].content == '.':
            self.cells[self.c_x - 1][self.c_y - 1].content = 'o'
        else:
            print('клетка должна быть пустой')

    def check(self):# TODO: сделать выбор между выходом и перезапуском без окончания
        if self.cells[0][0].content == self.cells[0][1].content == self.cells[0][2].content == 'x':
            print('победил "x"')
            input()
        elif self.cells[1][0].content == self.cells[1][1].content == self.cells[1][2].content == 'x':
            print('победил "x"')
            input()
        elif self.cells[2][0].content == self.cells[2][1].content == self.cells[2][2].content == 'x':
            print('победил "x"')
            input()

        elif self.cells[0][0].content == self.cells[1][0].content == self.cells[2][0].content == 'x':
            print('победил "x"')
            input()
        elif self.cells[0][1].content == self.cells[1][1].content == self.cells[2][1].content == 'x':
            print('победил "x"')
            input()
        elif self.cells[0][2].content == self.cells[1][2].content == self.cells[2][2].content == 'x':
            print('победил "x"')
            input()

        elif self.cells[0][0].content == self.cells[1][1].content == self.cells[2][2].content == 'x':
            print('победил "x"')
            input()
        elif self.cells[0][0].content == self.cells[1][1].content == self.cells[2][2].content == 'x':
            print('победил "x"')
            input()


    def run(self):
        while self.game:
            self.turn_x()
            self.check()
            self.turn_o()
            self.check()


field = Field()
field.run()
