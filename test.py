import os

class Game:
    def __init__(self) -> None:
        self.game = 1
        self.player_1 = Player(image='x')
        self.player_2 = Player(image='o')
        self.field = Field()

    def run(self):# счеттик ходов, на 10 выход
        turn = 0
        while self.game:
            self.field.draw()
            if : # нечетный
                self.player_1.make_turn(self.field)
            else:
                self.player_2.make_turn(self.field)
            
            



class Field:
    def __init__(self) -> None:
        self.cells = [i for i in range(1, 10)]

    def draw(self):
        os.system('cls')
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])


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
                    print('номер клетки должен быть целым положительным числом от 1 до 9')
                    continue
                idx = cell_number - 1
                if not isinstance(field.cells[idx], int):
                    print('выберите номер пустой клетки')
                break
        field.cells[cell_number - 1] = self.image


App()
