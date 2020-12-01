from random import randrange
from time import sleep


class Map:
    def __init__(self, size: int, symbol: str, enemy: str):
        self.size = size
        self.symbol = symbol[0].upper()
        self.value = 3
        self.enemy = enemy[0].upper()
        self.enemy_value = 1
        self.map = [[0 for _ in range(self.size)]for _ in range(self.size)]

    def begin_map(self, number: int, init_x: int = 0, init_y: int = 0) -> None:
        self.map[init_x][init_y] = self.value

        while number > 0:
            x = randrange(self.size)
            y = randrange(self.size)
            while self.map[x][y] != 0:
                x = randrange(self.size)
                y = randrange(self.size)

            self.map[x][y] = self.enemy_value
            number -= 1

    def map_update(self, posicao: tuple, posicao_atual: tuple) -> bool:
        pos_x = posicao[0]
        pos_y = posicao[1]

        if self.map[pos_x][pos_y] != self.enemy_value:
            self.map[posicao_atual[0]][posicao_atual[1]] = 0
            self.map[pos_x][pos_y] = self.value
            return True

        return False

    def draw(self, moved: bool = 1) -> None:
        print('-' * (self.size * 2 - 1))

        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == self.value:
                    print(f'{self.symbol} ', end='')
                elif self.map[i][j] == self.enemy_value:
                    print(f'{self.enemy} ', end='')
                else:
                    print('. ', end='')
            print()

        if not moved:
            print("Não pode ir na direção")

        sleep(1.5)
